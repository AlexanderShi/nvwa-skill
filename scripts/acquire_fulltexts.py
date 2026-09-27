#!/usr/bin/env python3
"""
为研究Skill的「全文深读」收集开放获取全文（不依赖 OpenAlex / export.arxiv.org）。

读取通用格式的 works.json（Google Scholar 列表 + DBLP/Crossref 补全，见下），为每篇论文依次尝试：
  1. 已知 arXiv ID → arxiv.org/pdf/<id>
  2. arXiv 网页标题检索（arxiv.org/search，标题相似度 ≥ 0.9 且作者姓出现）；
     搜不到时在研究者的 arXiv 论文列表里按相似度 ≥ 0.9 再找（预印本标题常和发表版差一两个词）
  3. DOI → Unpaywall 开放获取位置（只用 OA 链接，不绕过付费墙）
  4. works.json 里给出的候选 PDF 链接（作者主页、机构仓库、DBLP ee）
下载后校验：必须是 PDF，且前两页文本包含标题的大部分关键词，否则丢弃并标 mismatch。
抽取纯文本（扫描版PDF没有文字层、或文字层是字体乱码时，若装了 tesseract 则自动逐页 OCR），维护可提交的 INDEX.md（角色、全文状态、阅读状态；Role/Read 手改会保留）。

用法:
    python3 acquire_fulltexts.py <skill目录> [--works PATH] [--delay SEC] [--only ID,ID] [--recheck] [--ocr-lang LANG]
                                 [--reocr ID,ID] [--drop ID,ID]

读卡 agent 报的两类问题（team-read.js 的 next 会给出现成命令）:
    --reocr ID,..  REOCR：删掉这些作品的 txt，不管乱码检测结果，强制对 PDF 逐页 OCR（用 --ocr-lang），再重建索引行。
    --drop ID,..   WRONG-TEXT：删掉这些作品的 PDF 和 txt，索引行改回 no-oa（之后的运行不再自动下载；要重新找用 --recheck，
                   先把 works.json 里指向错误文件的 url 或 arXiv id 删掉）。
    两者都只处理给出的 ID（相当于同时给了 --only）。之后用 plan_reading_batches.py --reread <ID,..> 把它们重新排进批次。

OCR 与语言:
    文字层几乎为空（扫描件）时逐页 OCR；文字层是拉丁字母却几乎没有英文常用词（字体乱码，常用词占比 < 0.01），
    或非空白字符里控制字符（码位 < 32）占三成以上（Type 3 字体乱码，零星字母会骗过常用词检测）时也 OCR。
    以非拉丁文字为主的文字层（中文、日文、俄文、希腊文……）不按英文常用词判乱码，原样保留。
    --ocr-lang 传给 tesseract -l（如 deu、fra、chi_sim、eng+deu；要先装对应的 tesseract 语言包），
    默认取环境变量 NUWA_OCR_LANG，没有就用 tesseract 自己的默认（eng）。merge_chase.py 重跑本脚本时环境变量照样生效。

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

# 不经本脚本下载、手动放进 papers/ 的全文，按 works.json 里 urls 的关键词标注来源（小写匹配，先匹配先用）。
# 标签按团队配置：<团队目录>/team.json 的可选键 "source_labels"，如 {"gerad.ca": "GERAD Cahier"}（成员目录的上一级
# 就是团队目录）。都不匹配或没有配置时标 "manual"。已有 Source 的行保留原值。
def source_labels(skill_dir: Path) -> dict[str, str]:
    tj = skill_dir.resolve().parent / "team.json"
    try:
        labels = json.loads(tj.read_text(encoding="utf-8")).get("source_labels") or {}
    except (OSError, ValueError):
        return {}
    return {str(k).lower(): str(v) for k, v in labels.items()} if isinstance(labels, dict) else {}

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

def arxiv_results(page: str) -> list[tuple[str, str, str]]:
    """arXiv 检索结果页 → [(arXiv ID, 标题, 作者)]。"""
    out = []
    for block in page.split('<li class="arxiv-result">')[1:]:
        m_id = ARXIV_ID_RE.search(block)
        m_t = re.search(r'<p class="title is-5 mathjax">(.*?)</p>', block, re.S)
        m_a = re.search(r'<p class="authors">(.*?)</p>', block, re.S)
        if m_id and m_t:
            out.append((m_id.group(1), m_t.group(1), norm_title(m_a.group(1)) if m_a else ""))
    return out


def best_arxiv_match(title: str, results: list[tuple[str, str, str]], surname: str = "") -> str | None:
    best, best_ratio = None, 0.0
    for arx, t, authors in results:
        if surname and norm_title(surname) not in authors:
            continue
        r = title_ratio(title, t)
        if r > best_ratio:
            best, best_ratio = arx, r
    return best if best_ratio >= 0.9 else None


def arxiv_search(title: str, surname: str) -> str | None:
    q = urllib.parse.urlencode({"query": title[:250], "searchtype": "title", "size": 25, "abstracts": "hide"})
    page = http_get(f"https://arxiv.org/search/?{q}").decode("utf-8", "replace")
    return best_arxiv_match(title, arxiv_results(page), surname)


def arxiv_author_papers(researcher: str, delay: float, limit: int = 1000) -> list[tuple[str, str, str]]:
    """研究者在 arXiv 上的全部论文（按作者检索）。
    预印本标题常和正式发表版差一两个词，而 arXiv 标题检索要求每个词都出现，一个词不同就搜不到；
    标题检索落空时在这份列表里按相似度匹配。"""
    parts = researcher.split()
    query = f"{parts[-1]}, {parts[0][0]}" if len(parts) > 1 else researcher  # arXiv 推荐的「姓, 名首字母」
    papers = []
    for start in range(0, limit, 200):
        q = urllib.parse.urlencode({"query": query, "searchtype": "author", "size": 200, "abstracts": "hide", "start": start})
        page = arxiv_results(http_get(f"https://arxiv.org/search/?{q}").decode("utf-8", "replace"))
        papers += page
        if len(page) < 200:
            break
        time.sleep(delay)
    return papers


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


OCR_LANG = os.environ.get("NUWA_OCR_LANG", "").strip()  # tesseract -l 的值；main() 里 --ocr-lang 覆盖


def stopword_ratio(text: str) -> float:
    """英文常用词占比：正常论文约0.2，字体乱码的文字层 <0.01（德法等拉丁文字论文约0.02-0.04，不会误判）。"""
    words = re.findall(r"[a-z]+", text.lower())
    return sum(1 for w in words if w in COMMON) / len(words) if words else 0.0


def latin_share(text: str) -> float:
    """字母里拉丁字母（含带重音的）所占比例；没有字母时算 1（按拉丁文字处理，乱码判断照旧）。"""
    import unicodedata
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return 1.0
    latin = sum(1 for c in letters if c.isascii() or unicodedata.name(c, "").startswith("LATIN"))
    return latin / len(letters)


def letter_count(text: str) -> int:
    return sum(1 for c in text if c.isalpha())


def control_share(text: str) -> float:
    """非空白字符里控制字符（码位 < 32）的比例：Type 3 字体乱码的文字层常在 0.4 以上，正常文字层接近 0。"""
    ns = [c for c in text if not c.isspace()]
    return sum(1 for c in ns if ord(c) < 32) / len(ns) if ns else 0.0


def garbled(text: str) -> bool:
    """字体乱码的文字层：拉丁文字却几乎没有英文常用词，或控制字符占三成以上（零星字母会骗过常用词检测）。
    以非拉丁文字为主的正常文字层不按英文常用词判断。"""
    return control_share(text) >= 0.3 or (latin_share(text) >= 0.5 and stopword_ratio(text) < 0.01)


def ocr_pages(doc) -> list[str] | None:
    """扫描版PDF（无文字层）：逐页渲染后用 tesseract OCR（语言 = OCR_LANG）；没装 tesseract 返回 None。"""
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
                r = subprocess.run(["tesseract", str(png), "-"] + (["-l", OCR_LANG] if OCR_LANG else []),
                                   capture_output=True, text=True,
                                   env={**os.environ, "OMP_THREAD_LIMIT": "1"})  # 多线程在小机器上反而极慢
                out.append(r.stdout)
    except (ImportError, OSError, subprocess.SubprocessError):
        return None
    return out


def extract_text(pdf: Path, txt: Path, force_ocr: bool = False) -> int:
    """返回页数；失败返回 0。文字层几乎为空（扫描件）或是字体乱码时自动 OCR；force_ocr（--reocr）时总是 OCR。"""
    try:
        import pypdfium2 as pdfium
        doc = pdfium.PdfDocument(str(pdf))
        pages = [doc[i].get_textpage().get_text_range() for i in range(len(doc))]
        text = "".join(pages)
        if pages and (force_ocr or sum(len(p.strip()) for p in pages) / len(pages) < 200 or garbled(text)):
            ocr = ocr_pages(doc)  # 无文字层，或文字层是字体乱码（Type 3 字体等）
            if force_ocr and ocr is None:
                print(f"  ⚠️ --reocr {pdf.name}: tesseract is not installed (apt-get install tesseract-ocr); kept the text layer")
            if ocr:
                o = "".join(ocr)
                if (force_ocr and o.strip()) or stopword_ratio(o) > stopword_ratio(text) or \
                        (latin_share(o) < 0.5 and letter_count(o) > letter_count(text)):  # 非拉丁文字的扫描件
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


def list_sources(note: str) -> str:
    """works.json 的 source_note 的第一句（括号或句号之前），如 "Google Scholar profile + DBLP + Crossref"。"""
    return re.split(r"\s\(|\.\s", (note or "").strip(), maxsplit=1)[0].strip().rstrip(".")


def write_index(path: Path, researcher: str, rows: list[dict], source_note: str = "") -> None:
    counts = {k: sum(1 for r in rows if r["Full text"] == k) for k in ("txt", "pdf", "no-oa")}
    src = list_sources(source_note)
    lines = [
        f"# {researcher} · Full-text index",
        "",
        f"> Generated by `scripts/acquire_fulltexts.py` from `../publications/works.json`{f' ({src})' if src else ''}.",
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
    def n(k: int, word: str) -> str:
        return f"{k} {word}" + ("" if k == 1 else "s")
    head = n(len(rows), "work")
    if len(book) == 1:
        head = f"{n(len(rows), 'row')} = {n(len(rows) - 1, 'work')} + 1 book-material item ({book[0]})"
    elif book:
        head = f"{n(len(rows), 'row')} = {n(len(rows) - len(book), 'work')} + {len(book)} book-material items ({book[0]}–{book[-1]})"
    lines += ["", f"{head} · txt {counts['txt']} · pdf {counts['pdf']} · no-oa {counts['no-oa']}", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


# ---------- 主流程 ----------

def run(skill_dir: Path, works_path: Path, delay: float, only: set[str], recheck: bool,
        reocr: set[str] = frozenset(), drop: set[str] = frozenset()) -> dict:
    data = json.loads(works_path.read_text(encoding="utf-8"))
    researcher = data.get("researcher") or skill_dir.name
    note = data.get("source_note") or ""
    labels = source_labels(skill_dir)
    known = {w.get("id") for w in data.get("works") or []}
    for i in sorted((reocr | drop) - known):
        print(f"  ⚠️ {i}: not in works.json (--reocr/--drop ignored for it)")
    if reocr & drop:
        print(f"  ⚠️ both --reocr and --drop for {', '.join(sorted(reocr & drop))}: --drop wins")
        reocr = reocr - drop
    surname = researcher.split()[-1]
    works = [w for w in data.get("works") or [] if w.get("title") and not w.get("dup_of")]
    works.sort(key=lambda w: -(w.get("cites") or 0))

    papers = skill_dir / "references" / "sources" / "papers"
    (papers / "txt").mkdir(parents=True, exist_ok=True)
    index_path = papers / "INDEX.md"
    abs_path = papers / "abstracts.json"
    kept = read_index(index_path)
    abstracts = json.loads(abs_path.read_text(encoding="utf-8")) if abs_path.exists() else {}
    author_papers = None  # 按需取一次

    rows = []
    kept_without_file = 0
    for n, w in enumerate(works, 1):
        prev = kept.get(w["id"], {})
        pdf = papers / f"{slug(w)}.pdf"
        txt = papers / "txt" / f"{slug(w)}.txt"
        status, source, pages = "no-oa", prev.get("Source") or "—", prev.get("Pages") or ""
        todo = (not only or w["id"] in only)
        skip_net = (prev.get("Full text") == "no-oa" and not recheck) or w.get("kind") in ("patent", "talk")
        if w["id"] in drop:  # WRONG-TEXT: the file on disk is another work; forget it, do not re-download it now
            for f in (pdf, txt):
                if f.exists():
                    f.unlink()
                    print(f"  --drop {w['id']}: deleted {f.name}")
            if prev.get("Source") in ("arXiv", "url"):
                print(f"  ⚠️ --drop {w['id']}: the wrong file came from its {prev['Source']} candidate; remove that arXiv id / url "
                      f"from works.json before any --recheck, or it will be downloaded again")
            source, pages, skip_net = "—", "", True
        elif w["id"] in reocr:
            if pdf.exists():
                txt.unlink(missing_ok=True)
                pages = extract_text(pdf, txt, force_ocr=True) or ""
                print(f"  --reocr {w['id']}: {pages or 0} pages OCR'd from {pdf.name}")
            else:
                print(f"  ⚠️ --reocr {w['id']}: no PDF on disk ({pdf.name}); restore it first (a plain run re-downloads what it can)")

        if txt.exists() or pdf.exists():
            if not txt.exists():
                pages = extract_text(pdf, txt) or ""
            elif not pages:
                pages = txt.read_text(encoding="utf-8", errors="replace").count("[[page ") or ""
            status = "txt" if txt.exists() else "pdf"
            if source == "—":  # supplied outside this script (homepage search, report series, by hand)
                urls = " ".join(w.get("urls") or []).lower()
                source = next((label for key, label in labels.items() if key in urls), "manual")
        elif todo and not skip_net:
            arx = w.get("arxiv")
            if not arx:
                try:
                    arx = arxiv_search(w["title"], surname)
                except (urllib.error.URLError, TimeoutError) as e:
                    print(f"  ⚠️ arXiv search failed: {w['title'][:60]} ({e})")
                time.sleep(delay)
                if not arx:
                    if author_papers is None:
                        try:
                            author_papers = arxiv_author_papers(researcher, delay)
                        except (urllib.error.URLError, TimeoutError) as e:
                            print(f"  ⚠️ arXiv author listing failed: {researcher} ({e})")
                            author_papers = []
                        time.sleep(delay)
                    arx = best_arxiv_match(w["title"], author_papers)
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
        if status == "no-oa" and prev.get("Full text") in ("txt", "pdf") and w["id"] not in drop:
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
            write_index(index_path, researcher, rows + [], note)
            abs_path.write_text(json.dumps(abstracts, ensure_ascii=False, indent=1), encoding="utf-8")

    write_index(index_path, researcher, rows, note)
    abs_path.write_text(json.dumps(abstracts, ensure_ascii=False, indent=1), encoding="utf-8")
    works_path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")  # 回写新找到的 arXiv ID
    if kept_without_file:
        print(f"  ⚠️ {kept_without_file} rows keep their committed txt/pdf status without a local file "
              f"(PDFs and txt/ are git-ignored; restore them before re-extracting or verifying quotes)")
    return {k: sum(1 for r in rows if r["Full text"] == k) for k in ("txt", "pdf", "no-oa")} | {"total": len(rows)}


def main():
    global OCR_LANG
    ap = argparse.ArgumentParser(description="为研究Skill收集开放获取全文并维护论文索引")
    ap.add_argument("skill_dir")
    ap.add_argument("--works", default="")
    ap.add_argument("--delay", type=float, default=3.0, help="arXiv 请求间隔秒数（默认3）")
    ap.add_argument("--only", default="", help="只处理这些ID（逗号分隔）")
    ap.add_argument("--recheck", action="store_true", help="重新检索之前标为 no-oa 的论文")
    ap.add_argument("--ocr-lang", default=OCR_LANG, metavar="LANG",
                    help="tesseract 的 -l 语言（如 deu、chi_sim、eng+fra；默认取环境变量 NUWA_OCR_LANG，否则 tesseract 默认 eng）")
    ap.add_argument("--reocr", default="", metavar="ID,ID",
                    help="读卡报 REOCR 的作品：删 txt，强制对 PDF 逐页 OCR（只处理这些 ID）")
    ap.add_argument("--drop", default="", metavar="ID,ID",
                    help="读卡报 WRONG-TEXT 的作品：删 PDF 和 txt，索引行改回 no-oa（只处理这些 ID）")
    args = ap.parse_args()
    OCR_LANG = args.ocr_lang.strip()

    skill_dir = Path(args.skill_dir)
    works = Path(args.works) if args.works else skill_dir / "references" / "sources" / "publications" / "works.json"
    if not works.exists():
        print(f"❌ works.json not found: {works}")
        sys.exit(1)
    only = {s.strip() for s in args.only.split(",") if s.strip()}
    reocr = {s.strip() for s in args.reocr.split(",") if s.strip()}
    drop = {s.strip() for s in args.drop.split(",") if s.strip()}
    if (reocr or drop) and not only:
        only = reocr | drop  # no network work for anything else
    c = run(skill_dir, works, args.delay, only, args.recheck, reocr, drop)
    print(f"✅ {c['total']} works: txt {c['txt']} · pdf {c['pdf']} · no-oa {c['no-oa']}")
    print(f"   index: {skill_dir / 'references/sources/papers/INDEX.md'}")


if __name__ == "__main__":
    main()
