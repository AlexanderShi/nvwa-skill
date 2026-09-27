#!/usr/bin/env python3
"""
为研究Skill的「全文深读」准备论文全文（研究Skill · 深读阶段用）。

读取 fetch_publications.py --json 生成的 works.json，为每篇论文找到 arXiv 版本，
下载PDF、抽取纯文本，并维护一份可提交的论文索引 INDEX.md（角色、全文状态、阅读状态），
供深读agent逐篇写「论文卡片」（见 references/paper-reading-card.md）。

用法:
    python3 fetch_fulltexts.py <skill目录> [选项]

选项:
    --works PATH     works.json 路径（默认 <skill目录>/references/sources/publications/works.json）
    --max N          最多处理N篇（按被引降序；默认全部）
    --core K         被引前K篇默认标为 core（默认 20），其余为 supplement；已有INDEX中的角色不覆盖
    --delay SEC      arXiv 请求间隔秒数（默认 3，arXiv API 要求礼貌访问）
    --no-download    只匹配arXiv、更新INDEX，不下载PDF

需要的网络: api.openalex.org（先跑 fetch_publications.py）、export.arxiv.org、arxiv.org

输出:
    <skill目录>/references/sources/papers/INDEX.md    论文索引（提交到git）
    <skill目录>/references/sources/papers/*.pdf        全文PDF（git-ignored）
    <skill目录>/references/sources/papers/txt/*.txt   抽取的纯文本（git-ignored）

注意:
    - 只下载 arXiv 开放获取版本；不在arXiv上的论文在INDEX中标为 no-oa，需要用户自行提供PDF
    - PDF和全文文本不提交（版权），INDEX.md 只含元数据
    - Google Scholar 不提供可编程访问，也禁止抓取；发表列表以 OpenAlex 为准
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher
from pathlib import Path

ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([a-z\-]+(?:\.[A-Z]{2})?/\d{7}|\d{4}\.\d{4,5})(?:v\d+)?", re.I)
ARXIV_DOI_RE = re.compile(r"10\.48550/arxiv\.([0-9]{4}\.[0-9]{4,5})", re.I)
ATOM = {"a": "http://www.w3.org/2005/Atom"}
UA = {"User-Agent": "nuwa-skill/fetch_fulltexts (research skill distillation)"}

INDEX_HEADER = ["#", "Year", "Title", "Venue", "Cites", "arXiv", "Full text", "Role", "Read", "OpenAlex"]


# ---------- 网络（测试时可替换） ----------

def http_get(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < 2:
                time.sleep(5 * (attempt + 1))
                continue
            raise
        except urllib.error.URLError:
            if attempt < 2:
                time.sleep(5 * (attempt + 1))
                continue
            raise
    return b""


# ---------- arXiv 匹配 ----------

def norm_title(t: str) -> str:
    t = re.sub(r"<[^>]+>", " ", t or "")
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def arxiv_from_work(work: dict) -> str | None:
    """从 OpenAlex 记录里直接找 arXiv ID（locations / DOI）。"""
    urls = []
    for loc in [work.get("primary_location") or {}] + list(work.get("locations") or []):
        urls += [loc.get("landing_page_url") or "", loc.get("pdf_url") or ""]
    urls.append((work.get("open_access") or {}).get("oa_url") or "")
    for u in urls:
        m = ARXIV_ID_RE.search(u)
        if m:
            return m.group(1)
    m = ARXIV_DOI_RE.search(work.get("doi") or "")
    return m.group(1) if m else None


def surname_of(author: dict) -> str:
    name = (author.get("display_name") or "").strip()
    return name.split()[-1] if name else ""


def arxiv_search(title: str, surname: str) -> str | None:
    """按标题+作者姓在 arXiv API 搜索，标题相似度 ≥ 0.9 才认。"""
    words = [w for w in norm_title(title).split() if len(w) > 2][:10]
    if not words:
        return None
    q = " AND ".join([f"ti:{w}" for w in words] + ([f"au:{surname}"] if surname else []))
    url = "https://export.arxiv.org/api/query?" + urllib.parse.urlencode({"search_query": q, "max_results": 5})
    root = ET.fromstring(http_get(url))
    target = norm_title(title)
    best, best_ratio = None, 0.0
    for entry in root.findall("a:entry", ATOM):
        t = entry.findtext("a:title", default="", namespaces=ATOM)
        ratio = SequenceMatcher(None, target, norm_title(t)).ratio()
        if ratio > best_ratio:
            m = ARXIV_ID_RE.search(entry.findtext("a:id", default="", namespaces=ATOM))
            best, best_ratio = (m.group(1) if m else None), ratio
    return best if best_ratio >= 0.9 else None


# ---------- 全文 ----------

def slug(work: dict) -> str:
    words = norm_title(work.get("title") or "untitled").split()[:8]
    return f"{work.get('publication_year') or 'nd'}-" + "-".join(words)


def extract_text(pdf: Path, txt: Path) -> bool:
    try:
        import pypdfium2 as pdfium
        doc = pdfium.PdfDocument(str(pdf))
        pages = [doc[i].get_textpage().get_text_range() for i in range(len(doc))]
        txt.write_text("\n\f\n".join(pages), encoding="utf-8")
        return True
    except ImportError:
        pass
    except Exception:
        return False
    try:
        subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True, capture_output=True)
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False


# ---------- INDEX ----------

def md(s) -> str:
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ").strip()


def read_index(path: Path) -> dict[str, dict]:
    """保留已有的 Role / Read 列（按 OpenAlex ID）。"""
    keep = {}
    if not path.exists():
        return keep
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
        if len(cells) == len(INDEX_HEADER) and cells[0] not in ("#", "---") and not set(cells[0]) <= {"-"}:
            row = dict(zip(INDEX_HEADER, cells))
            keep[row["OpenAlex"]] = row
    return keep


def write_index(path: Path, researcher: str, rows: list[dict]) -> None:
    lines = [
        f"# {researcher} · 论文全文索引",
        "",
        "> 由 `scripts/fetch_fulltexts.py` 生成并更新；Role 与 Read 列可手工编辑，重跑时保留。",
        "> Full text: `txt` = 已下载并抽取文本 · `pdf` = 已下载但抽取失败 · `arxiv` = 找到arXiv但未下载 · `no-oa` = 未找到开放全文（需自行提供PDF）",
        "> Role: `core`（深读，写完整论文卡片）· `contrast`（对照）· `supplement`（略读，写简版卡片）· `background`（不单独写卡片）",
        "> Read: `—` 未读 · `skimmed` 略读卡片已写 · `carded` 完整卡片已写（见 `../../research/07-paper-cards.md`）",
        "",
        "| " + " | ".join(INDEX_HEADER) + " |",
        "|" + "|".join(["---"] * len(INDEX_HEADER)) + "|",
    ]
    for i, r in enumerate(rows, 1):
        r["#"] = str(i)
        lines.append("| " + " | ".join(md(r.get(h, "")) for h in INDEX_HEADER) + " |")
    counts = {k: sum(1 for r in rows if r["Full text"] == k) for k in ("txt", "pdf", "arxiv", "no-oa")}
    lines += ["", f"共 {len(rows)} 篇 · txt {counts['txt']} · pdf {counts['pdf']} · arxiv {counts['arxiv']} · no-oa {counts['no-oa']}", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


# ---------- 主流程 ----------

def run(skill_dir: Path, works_path: Path, max_n: int | None, core_k: int, delay: float, download: bool) -> dict:
    data = json.loads(works_path.read_text(encoding="utf-8"))
    author = data.get("author") or {}
    aid = (author.get("id") or "").rstrip("/").split("/")[-1]
    researcher = author.get("display_name") or skill_dir.name
    works = sorted([w for w in data.get("works") or [] if w.get("title")],
                   key=lambda w: w.get("cited_by_count") or 0, reverse=True)
    if max_n:
        works = works[:max_n]

    papers = skill_dir / "references" / "sources" / "papers"
    (papers / "txt").mkdir(parents=True, exist_ok=True)
    index_path = papers / "INDEX.md"
    kept = read_index(index_path)

    rows = []
    for rank, w in enumerate(works):
        wid = (w.get("id") or "").rstrip("/").split("/")[-1]
        prev = kept.get(wid, {})
        arx = prev.get("arXiv") if prev.get("arXiv") not in (None, "", "—") else arxiv_from_work(w)
        if not arx:
            me = next((a for a in w.get("authorships") or []
                       if ((a.get("author") or {}).get("id") or "").endswith(aid)), {})
            try:
                arx = arxiv_search(w["title"], surname_of(me.get("author") or {}))
            except (urllib.error.URLError, ET.ParseError, TimeoutError) as e:
                print(f"  ⚠️ arXiv 搜索失败：{w['title'][:60]}… ({e})")
                arx = None
            time.sleep(delay)

        status = "no-oa"
        if arx:
            status = "arxiv"
            pdf = papers / f"{slug(w)}.pdf"
            txt = papers / "txt" / f"{slug(w)}.txt"
            if download and not pdf.exists():
                try:
                    pdf.write_bytes(http_get(f"https://arxiv.org/pdf/{arx}"))
                    time.sleep(delay)
                except (urllib.error.URLError, TimeoutError) as e:
                    print(f"  ⚠️ 下载失败 {arx}: {e}")
            if pdf.exists():
                status = "txt" if (txt.exists() or extract_text(pdf, txt)) else "pdf"

        venue = ((w.get("primary_location") or {}).get("source") or {}).get("display_name") or "—"
        rows.append({
            "Year": w.get("publication_year") or "—",
            "Title": w.get("title"),
            "Venue": venue,
            "Cites": w.get("cited_by_count") or 0,
            "arXiv": arx or "—",
            "Full text": status,
            "Role": prev.get("Role") or ("core" if rank < core_k else "supplement"),
            "Read": prev.get("Read") or "—",
            "OpenAlex": wid,
        })
        print(f"[{rank + 1}/{len(works)}] {status:6} {w['title'][:70]}")

    write_index(index_path, researcher, rows)
    return {k: sum(1 for r in rows if r["Full text"] == k) for k in ("txt", "pdf", "arxiv", "no-oa")} | {"total": len(rows)}


def main():
    ap = argparse.ArgumentParser(description="为研究Skill下载arXiv全文并维护论文索引")
    ap.add_argument("skill_dir")
    ap.add_argument("--works", default="")
    ap.add_argument("--max", type=int, default=0)
    ap.add_argument("--core", type=int, default=20)
    ap.add_argument("--delay", type=float, default=3.0)
    ap.add_argument("--no-download", action="store_true")
    args = ap.parse_args()

    skill_dir = Path(args.skill_dir)
    works = Path(args.works) if args.works else skill_dir / "references" / "sources" / "publications" / "works.json"
    if not works.exists():
        print(f"❌ 找不到 {works}")
        print(f"   先运行: python3 scripts/fetch_publications.py \"<姓名>\" --json --out {works.parent}")
        sys.exit(1)
    try:
        c = run(skill_dir, works, args.max or None, args.core, args.delay, not args.no_download)
    except urllib.error.URLError as e:
        print(f"❌ 访问 arXiv 失败：{e}（需要允许 export.arxiv.org 与 arxiv.org）")
        sys.exit(2)
    print(f"✅ {c['total']} 篇：全文文本 {c['txt']} · 仅PDF {c['pdf']} · 未下载 {c['arxiv']} · 无开放全文 {c['no-oa']}")
    print(f"   索引：{skill_dir / 'references/sources/papers/INDEX.md'}")


if __name__ == "__main__":
    main()
