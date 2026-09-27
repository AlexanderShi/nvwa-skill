#!/usr/bin/env python3
"""
为研究Skill的「全文深读」收集开放获取全文（不依赖 OpenAlex / export.arxiv.org）。

读取通用格式的 works.json（Google Scholar 列表 + DBLP/Crossref 补全，见下），为每篇论文依次尝试：
  1. 已知 arXiv ID → arxiv.org/pdf/<id>
  2. arXiv 网页标题检索（arxiv.org/search，标题相似度 ≥ 0.9 且作者姓出现）
  3. DOI → Unpaywall 开放获取位置（只用 OA 链接，不绕过付费墙）
  4. works.json 里给出的候选 PDF 链接（作者主页、机构仓库、DBLP ee）
下载后校验：必须是 PDF，且前两页文本包含标题的大部分关键词，否则丢弃并标 mismatch。
抽取纯文本（扫描版PDF没有文字层、或文字层是字体乱码时，若装了 tesseract 则自动逐页 OCR），维护可提交的 INDEX.md（角色、全文状态、阅读状态；Role/Read 手改会保留）。

用法:
    python3 acquire_fulltexts.py <skill目录> [--works PATH] [--delay SEC] [--only ID,ID] [--recheck]

works.json 格式:
    {"researcher": "...", "works": [{"id": "S001", "title": "...", "authors": "...", "venue": "...",
      "year": 2018, "cites": 239, "doi": "10.1007/...", "arxiv": "1504.04231", "urls": ["https://.../x.pdf"],
      "kind": "journal", "dup_of": null}, ...]}

输出:
    <skill目录>/references/sources/papers/INDEX.md        论文索引（提交）
    <skill目录>/references/sources/papers/*.pdf            全文PDF（git-ignored）
    <skill目录>/references/sources/papers/txt/*.txt       抽取文本（git-ignored）
    <skill目录>/references/sources/papers/abstracts.json  摘要（arXiv/Crossref，提交）

需要的网络: arxiv.org、api.unpaywall.org、api.crossref.org，以及各作者主页/机构仓库
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from difflib import SequenceMatcher
from pathlib import Path

UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) nuwa-skill/acquire_fulltexts (research skill distillation)"}
UNPAYWALL_EMAIL = "nuwa-skill@users.noreply.github.com"
ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([a-z\-]+(?:\.[A-Z]{2})?/\d{7}|\d{4}\.\d{4,5})(?:v\d+)?", re.I)
STOP = {"the", "and", "for", "with", "from", "into", "via", "its", "their", "using", "based", "on", "of", "in", "a", "an", "to"}

INDEX_HEADER = ["#", "ID", "Year", "Title", "Venue", "Cites", "Kind", "Source", "Full text", "Pages", "Role", "Read"]


# ---------- 网络 ----------

def http_get(url: str, timeout: int = 60, tries: int = 3) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < tries - 1:
                time.sleep(10 * (attempt + 1))
                continue
            raise
        except (urllib.error.URLError, TimeoutError):
            if attempt < tries - 1:
                time.sleep(5 * (attempt + 1))
                continue
            raise
    return b""


# ---------- 标题匹配 ----------

def norm_title(t: str) -> str:
    t = html.unescape(re.sub(r"<[^>]+>", " ", t or ""))
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()


def title_ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, norm_title(a), norm_title(b)).ratio()


def key_words(title: str) -> list[str]:
    return [w for w in norm_title(title).split() if len(w) > 3 and w not in STOP]


def title_in_text(title: str, text: str) -> float:
    """前两页文本里出现了标题关键词的比例（校验下载的是不是这篇论文）。"""
    words = key_words(title)
    if not words:
        return 1.0
    body = " " + norm_title(text[:12000]) + " "
    return sum(1 for w in words if f" {w}" in body) / len(words)


# ---------- 来源 ----------

def arxiv_search(title: str, surname: str) -> str | None:
    q = urllib.parse.urlencode({"query": title[:250], "searchtype": "title", "size": 25, "abstracts": "hide"})
    page = http_get(f"https://arxiv.org/search/?{q}").decode("utf-8", "replace")
    best, best_ratio = None, 0.0
    for block in page.split('<li class="arxiv-result">')[1:]:
        m_id = ARXIV_ID_RE.search(block)
        m_t = re.search(r'<p class="title is-5 mathjax">(.*?)</p>', block, re.S)
        m_a = re.search(r'<p class="authors">(.*?)</p>', block, re.S)
        if not (m_id and m_t):
            continue
        authors = norm_title(m_a.group(1)) if m_a else ""
        if surname and norm_title(surname) not in authors:
            continue
        r = title_ratio(title, m_t.group(1))
        if r > best_ratio:
            best, best_ratio = m_id.group(1), r
    return best if best_ratio >= 0.9 else None


def arxiv_abstract(arx: str) -> str:
    try:
        page = http_get(f"https://arxiv.org/abs/{arx}").decode("utf-8", "replace")
    except (urllib.error.URLError, TimeoutError):
        return ""
    m = re.search(r'<blockquote class="abstract[^"]*">(.*?)</blockquote>', page, re.S)
    if not m:
        return ""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(1)))).replace("Abstract:", "").strip()


def unpaywall_pdfs(doi: str) -> list[str]:
    try:
        data = json.loads(http_get(f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={UNPAYWALL_EMAIL}", tries=2))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return []
    urls = []
    for loc in [data.get("best_oa_location") or {}] + list(data.get("oa_locations") or []):
        for k in ("url_for_pdf", "url"):
            u = loc.get(k)
            if u and u not in urls:
                urls.append(u)
    return urls


def crossref_abstract(doi: str) -> str:
    try:
        data = json.loads(http_get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}", tries=2))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return ""
    a = (data.get("message") or {}).get("abstract") or ""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", a))).strip()


# ---------- 全文 ----------

def slug(work: dict) -> str:
    words = norm_title(work.get("title") or "untitled").split()[:8]
    return f"{work['id']}-{work.get('year') or 'nd'}-" + "-".join(words)


COMMON = set("the and of to in is that for we with this are be by on as it an at from or which can if not our then".split())


def stopword_ratio(text: str) -> float:
    """英文常用词占比：正常论文约0.2，字体乱码的文字层 <0.01（非英文论文约0.02-0.04，不会误判）。"""
    words = re.findall(r"[a-z]+", text.lower())
    return sum(1 for w in words if w in COMMON) / len(words) if words else 0.0


def ocr_pages(doc) -> list[str] | None:
    """扫描版PDF（无文字层）：逐页渲染后用 tesseract OCR；没装 tesseract 返回 None。"""
    import shutil
    import tempfile
    if not shutil.which("tesseract"):
        return None
    out = []
    try:
        with tempfile.TemporaryDirectory() as tmp:
            for i in range(len(doc)):
                png = Path(tmp) / f"p{i + 1}.png"
                doc[i].render(scale=300 / 72).to_pil().convert("L").save(png)  # 需要 Pillow
                r = subprocess.run(["tesseract", str(png), "-"], capture_output=True, text=True,
                                   env={**os.environ, "OMP_THREAD_LIMIT": "1"})  # 多线程在小机器上反而极慢
                out.append(r.stdout)
    except (ImportError, OSError, subprocess.SubprocessError):
        return None
    return out


def extract_text(pdf: Path, txt: Path) -> int:
    """返回页数；失败返回 0。文字层几乎为空（扫描件）或是字体乱码时自动 OCR。"""
    try:
        import pypdfium2 as pdfium
        doc = pdfium.PdfDocument(str(pdf))
        pages = [doc[i].get_textpage().get_text_range() for i in range(len(doc))]
        if pages and (sum(len(p.strip()) for p in pages) / len(pages) < 200 or stopword_ratio("".join(pages)) < 0.01):
            ocr = ocr_pages(doc)  # 无文字层，或文字层是字体乱码（Type 3 字体等）
            if ocr and stopword_ratio("".join(ocr)) > stopword_ratio("".join(pages)):
                pages = ocr
        txt.write_text("\n\f\n".join(f"[[page {i + 1}]]\n{p}" for i, p in enumerate(pages)), encoding="utf-8")
        return len(pages)
    except ImportError:
        pass
    except Exception:
        return 0
    try:
        subprocess.run(["pdftotext", "-layout", str(pdf), str(txt)], check=True, capture_output=True)
        return txt.read_text(encoding="utf-8", errors="replace").count("\f") + 1
    except (FileNotFoundError, subprocess.CalledProcessError):
        return 0


def try_pdf(url: str, work: dict, pdf: Path, txt: Path) -> tuple[str, int]:
    """下载并校验。返回 (状态, 页数)：txt / mismatch / notpdf / fail。"""
    try:
        data = http_get(url, timeout=90, tries=2)
    except (urllib.error.URLError, TimeoutError, ValueError):
        return "fail", 0
    if not data.startswith(b"%PDF"):
        return "notpdf", 0
    pdf.write_bytes(data)
    n = extract_text(pdf, txt)
    if not n:
        return "pdf", 0
    if title_in_text(work["title"], txt.read_text(encoding="utf-8", errors="replace")) < 0.6:
        pdf.unlink(missing_ok=True)
        txt.unlink(missing_ok=True)
        return "mismatch", 0
    return "txt", n


# ---------- INDEX ----------

def md(s) -> str:
    return str(s if s is not None else "").replace("|", "\\|").replace("\n", " ").strip()


def read_index(path: Path) -> dict[str, dict]:
    keep = {}
    if not path.exists():
        return keep
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
        if len(cells) == len(INDEX_HEADER) and cells[0] not in ("#",) and not set(cells[0]) <= {"-"}:
            row = dict(zip(INDEX_HEADER, cells))
            keep[row["ID"]] = row
    return keep


def write_index(path: Path, researcher: str, rows: list[dict]) -> None:
    counts = {k: sum(1 for r in rows if r["Full text"] == k) for k in ("txt", "pdf", "no-oa")}
    lines = [
        f"# {researcher} · Full-text index",
        "",
        "> Generated by `scripts/acquire_fulltexts.py` from `../publications/works.json` (Google Scholar profile + DBLP + Crossref).",
        "> Role and Read columns may be edited by hand; re-runs keep them.",
        "> Full text: `txt` = PDF downloaded and text extracted · `pdf` = downloaded, extraction failed · `no-oa` = no open full text found (supply the PDF by hand).",
        "> Source: `arXiv` / `unpaywall` (open-access copy) / `url` (author homepage or repository) / `manual` (supplied by hand).",
        "> Role: `core` (full card) · `contrast` · `supplement` (short card) · `background` (no card) · `skip` (not research: patent, talk, duplicate).",
        "> Read: `—` not read · `abstract` card from abstract only · `skimmed` short card · `carded` full card (see `../../research/07-paper-cards.md`).",
        "> PDFs and extracted text are git-ignored (copyright); only this index is committed.",
        "",
        "| " + " | ".join(INDEX_HEADER) + " |",
        "|" + "|".join(["---"] * len(INDEX_HEADER)) + "|",
    ]
    for i, r in enumerate(rows, 1):
        r["#"] = str(i)
        lines.append("| " + " | ".join(md(r.get(h, "")) for h in INDEX_HEADER) + " |")
    # 书的周边材料（目录、勘误、评论；Venue = "book material"，ID 以 B 开头）不是独立作品，单独计数
    book = [r["ID"] for r in rows if r.get("Venue") == "book material"]
    head = f"{len(rows)} works"
    if book:
        head = f"{len(rows)} rows = {len(rows) - len(book)} works + {len(book)} book-material items ({book[0]}–{book[-1]})"
    lines += ["", f"{head} · txt {counts['txt']} · pdf {counts['pdf']} · no-oa {counts['no-oa']}", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


# ---------- 主流程 ----------

def run(skill_dir: Path, works_path: Path, delay: float, only: set[str], recheck: bool) -> dict:
    data = json.loads(works_path.read_text(encoding="utf-8"))
    researcher = data.get("researcher") or skill_dir.name
    surname = researcher.split()[-1]
    works = [w for w in data.get("works") or [] if w.get("title") and not w.get("dup_of")]
    works.sort(key=lambda w: -(w.get("cites") or 0))

    papers = skill_dir / "references" / "sources" / "papers"
    (papers / "txt").mkdir(parents=True, exist_ok=True)
    index_path = papers / "INDEX.md"
    abs_path = papers / "abstracts.json"
    kept = read_index(index_path)
    abstracts = json.loads(abs_path.read_text(encoding="utf-8")) if abs_path.exists() else {}

    rows = []
    kept_without_file = 0
    for n, w in enumerate(works, 1):
        prev = kept.get(w["id"], {})
        pdf = papers / f"{slug(w)}.pdf"
        txt = papers / "txt" / f"{slug(w)}.txt"
        status, source, pages = "no-oa", prev.get("Source") or "—", prev.get("Pages") or ""
        todo = (not only or w["id"] in only)
        skip_net = (prev.get("Full text") == "no-oa" and not recheck) or w.get("kind") in ("patent", "talk")

        if txt.exists() or pdf.exists():
            if not txt.exists():
                pages = extract_text(pdf, txt) or ""
            elif not pages:
                pages = txt.read_text(encoding="utf-8", errors="replace").count("[[page ") or ""
            status = "txt" if txt.exists() else "pdf"
            if source == "—":  # supplied outside this script (homepage search, report series, by hand)
                urls = " ".join(w.get("urls") or [])
                source = "DAMTP report" if "damtp" in urls else "manual"
        elif todo and not skip_net:
            arx = w.get("arxiv")
            if not arx:
                try:
                    arx = arxiv_search(w["title"], surname)
                except (urllib.error.URLError, TimeoutError) as e:
                    print(f"  ⚠️ arXiv search failed: {w['title'][:60]} ({e})")
                time.sleep(delay)
                if arx:
                    w["arxiv"] = arx
            candidates = []
            if arx:
                candidates.append(("arXiv", f"https://arxiv.org/pdf/{arx}"))
            if w.get("doi"):
                candidates += [("unpaywall", u) for u in unpaywall_pdfs(w["doi"])]
            candidates += [("url", u) for u in (w.get("urls") or []) if u.lower().endswith(".pdf")]
            for src, url in candidates:
                st, np_ = try_pdf(url, w, pdf, txt)
                time.sleep(delay if src == "arXiv" else 0.5)
                if st in ("txt", "pdf"):
                    status, source, pages = st, src, np_ or ""
                    break

        # PDF 与 txt/ 不进 git，新克隆的仓库里没有本地文件：保留已提交的全文状态，不重置为 no-oa
        if status == "no-oa" and prev.get("Full text") in ("txt", "pdf"):
            status, source, pages = prev["Full text"], prev.get("Source") or "—", prev.get("Pages") or ""
            kept_without_file += 1

        if w["id"] not in abstracts and todo and w.get("kind") not in ("patent", "talk"):
            a = arxiv_abstract(w["arxiv"]) if w.get("arxiv") else ""
            if not a and w.get("doi"):
                a = crossref_abstract(w["doi"])
            if a:
                abstracts[w["id"]] = a

        default_role = "skip" if w.get("kind") in ("patent", "talk") else "supplement"
        rows.append({
            "ID": w["id"], "Year": w.get("year") or "—", "Title": w["title"], "Venue": w.get("venue") or "—",
            "Cites": w.get("cites") if w.get("cites") is not None else "—", "Kind": w.get("kind") or "—",
            "Source": source if status in ("txt", "pdf") else "—", "Full text": status, "Pages": pages,
            "Role": prev.get("Role") or default_role, "Read": prev.get("Read") or "—",
        })
        print(f"[{n}/{len(works)}] {w['id']} {status:5} {source:9} {w['title'][:70]}", flush=True)
        if n % 10 == 0:
            write_index(index_path, researcher, rows + [])
            abs_path.write_text(json.dumps(abstracts, ensure_ascii=False, indent=1), encoding="utf-8")

    write_index(index_path, researcher, rows)
    abs_path.write_text(json.dumps(abstracts, ensure_ascii=False, indent=1), encoding="utf-8")
    works_path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")  # 回写新找到的 arXiv ID
    if kept_without_file:
        print(f"  ⚠️ {kept_without_file} rows keep their committed txt/pdf status without a local file "
              f"(PDFs and txt/ are git-ignored; restore them before re-extracting or verifying quotes)")
    return {k: sum(1 for r in rows if r["Full text"] == k) for k in ("txt", "pdf", "no-oa")} | {"total": len(rows)}


def main():
    ap = argparse.ArgumentParser(description="为研究Skill收集开放获取全文并维护论文索引")
    ap.add_argument("skill_dir")
    ap.add_argument("--works", default="")
    ap.add_argument("--delay", type=float, default=3.0, help="arXiv 请求间隔秒数（默认3）")
    ap.add_argument("--only", default="", help="只处理这些ID（逗号分隔）")
    ap.add_argument("--recheck", action="store_true", help="重新检索之前标为 no-oa 的论文")
    args = ap.parse_args()

    skill_dir = Path(args.skill_dir)
    works = Path(args.works) if args.works else skill_dir / "references" / "sources" / "publications" / "works.json"
    if not works.exists():
        print(f"❌ works.json not found: {works}")
        sys.exit(1)
    only = {s.strip() for s in args.only.split(",") if s.strip()}
    c = run(skill_dir, works, args.delay, only, args.recheck)
    print(f"✅ {c['total']} works: txt {c['txt']} · pdf {c['pdf']} · no-oa {c['no-oa']}")
    print(f"   index: {skill_dir / 'references/sources/papers/INDEX.md'}")


if __name__ == "__main__":
    main()
