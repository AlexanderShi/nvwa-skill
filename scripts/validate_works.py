#!/usr/bin/env python3
"""
校验发表列表 works.json（研究Skill · 全文深读 T3.1 harvest 之后、acquire_fulltexts.py 之前的结构闸门）。

参数可以是 works.json 文件、它所在的 publications/ 目录、Skill 目录（找 references/sources/publications/works.json）
或团队目录（按 team.json 的成员顺序，再补上其他含 works.json 的子目录；还没有 works.json 的成员只提示不报错）。

错误（退出码 1）:
    顶层      必须是 {"works": [...]} 对象
    必需键    每行都有 id title authors venue year cites doi arxiv urls kind dup_of sources（note、head 等多出的键允许）
    id        <字母><至少 3 位数字>，字母见下表；同一文件内不能重复
    dup_of    null，或本文件里另一行的 id（不能指向自己，不能成环）
    year      整数或 null，1450 ≤ year ≤ 今年+1
    cites     非负整数或 null
    doi       null，或 10.<4–9 位数字>/<后缀>（不带 https://doi.org/ 或 doi: 前缀，不含空白）
    arxiv     null，或新式 YYMM.NNNN[vN]（2015 年起 YYMM.NNNNN）/ 旧式 archive[.XX]/YYMMNNN[vN]（不带 arXiv: 前缀）
    urls      列表，每项是不含空白的 http(s):// 链接
    sources   字符串列表
    kind      下表之一（--extra-kinds 可加）
    其他      title 非空字符串；authors 字符串；venue 字符串或 null

警告（不影响退出码，交给人判断）:
    近似重复  标题规范化（去重音、小写、去标点）后相似度 ≥ --title-threshold（默认 0.95）或去掉空格后完全相同，
              却不在同一个 dup_of 组里；相连的行合成一组报一次。更正/勘误（Erratum/Correction/Corrigendum/
              Addendum …）与原文不算。会议版与期刊版、报告与发表版、演讲与论文同名是常见的合法情况，确认后可不理
    同一标识  两行 doi 或 arxiv 相同却不在同一个 dup_of 组里
    无定位    非 dup_of 行 doi、arxiv、urls 全空（acquire_fulltexts.py 只能靠 arXiv 标题检索找全文）
    其他      dup_of 链（A→B→C，应直接指向保留的那一行）；S 行的 sources 里没有 scholar；sources 为空；
              authors 为空；顶层缺 researcher（acquire_fulltexts.py 用它按作者列表找 arXiv）

ID 字母（DFO 团队五份 works.json 实际用到的，product/dfo-team/）:
    S   Google Scholar 行，按 Scholar 引用排序编号
    D   Scholar 上没有、只在 DBLP / Crossref / Semantic Scholar / 机构出版列表等书目库里的作品
    H   只在作者主页或简历上的作品
    R   机构报告系列里对不上 Scholar 行的条目（DFO 里是 DAMTP 报告，其中一份是关于本人的回忆录）
    X   关于本人的外部文献：访谈、口述史
    B   书的开放部分：目录、勘误、增补、书评、前言；team_status.py 只把它计入 Book material 列
    新字母用 --extra-id-letters 加（例如 --extra-id-letters PT）。

kind（同上，实际用到的）:
    journal conference chapter book report preprint thesis patent talk other
    errata review book-toc book-addendum essay interview memoir
    patent / talk 会被 acquire_fulltexts.py 设为 skip；interview / memoir / essay 由 plan_reading_batches.py 设为 core。

用法:
    python3 validate_works.py <works.json|publications目录|Skill目录|团队目录>... [--title-threshold 0.95] [--show N]
                              [--extra-id-letters XY] [--extra-kinds a,b]

示例:
    python3 scripts/validate_works.py product/dfo-team
    python3 scripts/validate_works.py product/dfo-team/michael-powell

输出:
    每个文件一段：首行是条目统计，其后每条错误（❌）/ 警告（⚠️）一行，每类警告最多列 --show 条（默认 10，0 只给数目）。
    最后一行汇总：✅/❌ N files, M works, E errors, W warnings；有错误退出码 1，路径不存在或找不到 works.json 为 2。
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

WORKS_REL = Path("references/sources/publications/works.json")
REQUIRED = ("id", "title", "authors", "venue", "year", "cites", "doi", "arxiv", "urls", "kind", "dup_of", "sources")
ID_LETTERS = {
    "S": "Google Scholar row",
    "D": "bibliographic database only (DBLP, Crossref, ...)",
    "H": "author homepage / CV only",
    "R": "report series item not matched to a Scholar row",
    "X": "external document about the researcher (interview, oral history)",
    "B": "open part of a book (ToC, errata, addendum, review, front matter)",
}
KINDS = {"journal", "conference", "chapter", "book", "report", "preprint", "thesis", "patent", "talk", "other",
         "errata", "review", "book-toc", "book-addendum", "essay", "interview", "memoir"}
MIN_YEAR = 1450
MAX_YEAR = datetime.date.today().year + 1

DOI_RE = re.compile(r"^10\.\d{4,9}/\S+$")
ARXIV_NEW_RE = re.compile(r"^(\d{2})(\d{2})\.(\d{4,5})(?:v\d+)?$")
ARXIV_OLD_RE = re.compile(r"^[a-z]+(?:-[a-z]+)*(?:\.[A-Z]{2})?/\d{2}(\d{2})\d{3}(?:v\d+)?$")
URL_RE = re.compile(r"^https?://\S+$")
CORRECTION_RE = re.compile(r"^(?:erratum|errata|corrigendum|corrigenda|correction|corrections|addendum|comments? on)\b")


# ---------- 找文件 ----------

def find_works(arg: str) -> tuple[list[Path], list[str]] | None:
    """返回 (works.json 列表, 提示行)；路径不存在时 None。"""
    p = Path(arg)
    if p.is_file():
        return [p], []
    if not p.is_dir():
        return None
    for cand in (p / "works.json", p / WORKS_REL):
        if cand.is_file():
            return [cand], []
    found: list[Path] = []
    notes: list[str] = []
    cfg = p / "team.json"
    if cfg.is_file():
        try:
            members = json.loads(cfg.read_text(encoding="utf-8")).get("members") or []
        except (json.JSONDecodeError, AttributeError):
            members = []
            notes.append(f"⚠️ {display(cfg)}: not valid team.json, falling back to */{WORKS_REL.as_posix()}")
        for m in members:
            slug = m.get("slug") if isinstance(m, dict) else None
            if not slug:
                continue
            w = p / slug / WORKS_REL
            if w.is_file():
                found.append(w)
            else:
                notes.append(f"· {slug}: no works.json yet")
    for w in sorted(p.glob(f"*/{WORKS_REL.as_posix()}")):
        if w not in found:
            found.append(w)
    return found, notes


def display(f: Path) -> str:
    rel = os.path.relpath(f.resolve())
    return f.resolve().as_posix() if rel.startswith("..") else Path(rel).as_posix()


# ---------- 标题 ----------

def norm_title(t: str) -> str:
    t = unicodedata.normalize("NFKD", t or "")
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"[^\w]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def similar(a: str, b: str, threshold: float) -> bool:
    if a.replace(" ", "") == b.replace(" ", ""):
        return True
    sm = SequenceMatcher(None, a, b, autojunk=False)
    return sm.real_quick_ratio() >= threshold and sm.quick_ratio() >= threshold and sm.ratio() >= threshold


# ---------- 校验 ----------

class Report:
    def __init__(self, show: int):
        self.show = show
        self.errors: list[str] = []
        self.warnings: dict[str, list[str]] = defaultdict(list)
        self.id_lists: set[str] = set()                   # 只列 id 的类别，打印时并成一行

    def err(self, wid, msg: str):
        self.errors.append(f"{wid}: {msg}" if wid else msg)

    def warn(self, category: str, item: str, ids_only: bool = False):
        self.warnings[category].append(item)
        if ids_only:
            self.id_lists.add(category)

    @property
    def n_warnings(self) -> int:
        return sum(len(v) for v in self.warnings.values())

    def lines(self) -> list[str]:
        out = [f"  ❌ {e}" for e in self.errors]
        for cat, items in self.warnings.items():
            if self.show <= 0:
                out.append(f"  ⚠️ {cat}: {len(items)}")
            elif cat in self.id_lists:
                limit = self.show * 5
                more = len(items) - limit
                out.append(f"  ⚠️ {cat} ({len(items)}): {', '.join(items[:limit])}" + (f", … {more} more" if more > 0 else ""))
            else:
                out += [f"  ⚠️ {cat}: {i}" for i in items[: self.show]]
                if len(items) > self.show:
                    out.append(f"  ⚠️ {cat}: … {len(items) - self.show} more (--show N)")
        return out


def check_arxiv(a: str) -> str | None:
    m = ARXIV_NEW_RE.match(a)
    if m:
        yymm, month, digits = int(m.group(1) + m.group(2)), int(m.group(2)), len(m.group(3))
        if not 1 <= month <= 12 or yymm < 704:
            return f"arxiv {a!r}: YYMM {m.group(1)}{m.group(2)} is not a valid new-style month (0704 onwards)"
        if (yymm >= 1501) != (digits == 5):
            return f"arxiv {a!r}: ids from 1501 on have 5 digits after the dot, earlier ones 4"
        return None
    m = ARXIV_OLD_RE.match(a)
    if m:
        return None if 1 <= int(m.group(1)) <= 12 else f"arxiv {a!r}: month {m.group(1)} out of range"
    hint = " (drop the 'arXiv:' prefix)" if a.lower().startswith("arxiv:") else \
        " (store the id, not the URL)" if "arxiv.org" in a else ""
    return f"arxiv {a!r} is not an arXiv id (YYMM.NNNNN[vN] or archive/YYMMNNN){hint}"


def check_row(w: dict, rep: Report, letters: set[str], kinds: set[str]):
    wid = w.get("id")
    missing = [k for k in REQUIRED if k not in w]
    if missing:
        rep.err(wid if isinstance(wid, str) else None, f"missing keys: {', '.join(missing)}")
    label = wid if isinstance(wid, str) else repr(wid)
    if "id" in w:
        m = re.fullmatch(r"([A-Za-z]+)(\d{3,})", wid) if isinstance(wid, str) else None
        if not m or m.group(1) not in letters:
            rep.err(label, f"id {wid!r} does not match <letter><3+ digits> with letter in {''.join(sorted(letters))}")
    if "title" in w and (not isinstance(w["title"], str) or not w["title"].strip()):
        rep.err(label, "title must be a non-empty string (acquire_fulltexts.py drops rows without one)")
    if "authors" in w:
        if not isinstance(w["authors"], str):
            rep.err(label, f"authors must be a string, got {type(w['authors']).__name__}")
        elif not w["authors"].strip() and not w.get("dup_of"):
            rep.warn("empty authors", label, ids_only=True)
    if "venue" in w and w["venue"] is not None and not isinstance(w["venue"], str):
        rep.err(label, f"venue must be a string or null, got {type(w['venue']).__name__}")
    if "year" in w and w["year"] is not None:
        y = w["year"]
        if type(y) is not int:
            rep.err(label, f"year must be an integer or null, got {y!r}")
        elif not MIN_YEAR <= y <= MAX_YEAR:
            rep.err(label, f"year {y} outside {MIN_YEAR}–{MAX_YEAR}")
    if "cites" in w and w["cites"] is not None and (type(w["cites"]) is not int or w["cites"] < 0):
        rep.err(label, f"cites must be a non-negative integer or null, got {w['cites']!r}")
    if "doi" in w and w["doi"] is not None:
        d = w["doi"]
        if not isinstance(d, str) or not DOI_RE.match(d):
            hint = ""
            if isinstance(d, str) and re.match(r"(?i)^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", d):
                hint = " (drop the https://doi.org/ or doi: prefix)"
            rep.err(label, f"doi {d!r} is not a DOI (10.NNNN/suffix){hint}")
    if "arxiv" in w and w["arxiv"] is not None:
        a = w["arxiv"]
        problem = check_arxiv(a) if isinstance(a, str) else f"arxiv must be a string or null, got {a!r}"
        if problem:
            rep.err(label, problem)
    if "urls" in w:
        u = w["urls"]
        if not isinstance(u, list):
            rep.err(label, f"urls must be a list, got {type(u).__name__}")
        else:
            for x in u:
                if not isinstance(x, str) or not URL_RE.match(x):
                    rep.err(label, f"url {x!r} is not an http(s) link without spaces")
    if "sources" in w:
        s = w["sources"]
        if not isinstance(s, list) or not all(isinstance(x, str) and x for x in s):
            rep.err(label, f"sources must be a list of non-empty strings, got {s!r}")
        elif not s:
            rep.warn("empty sources", label, ids_only=True)
        elif isinstance(wid, str) and wid.startswith("S") and "scholar" not in s:
            rep.warn("S rows without 'scholar' in sources", label, ids_only=True)
    if "kind" in w:
        k = w["kind"]
        if not isinstance(k, str) or k not in kinds:
            rep.err(label, f"kind {k!r} not in: {' '.join(sorted(kinds))} (new kinds: --extra-kinds)")


def validate(path: Path, rep: Report, letters: set[str], kinds: set[str], threshold: float) -> Counter:
    stats: Counter = Counter()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        rep.err(None, f"cannot read JSON: {e}")
        return stats
    if not isinstance(data, dict) or not isinstance(data.get("works"), list):
        rep.err(None, 'top level must be an object {"researcher": ..., "works": [...]}')
        return stats
    if not data.get("researcher"):
        rep.warn("top level", 'no "researcher" (acquire_fulltexts.py falls back to the folder name for arXiv author search)')
    works = data["works"]
    rows = []
    for i, w in enumerate(works):
        if not isinstance(w, dict):
            rep.err(None, f"works[{i}] is not an object")
            continue
        check_row(w, rep, letters, kinds)
        rows.append(w)
    stats["works"] = len(works)

    ids = [w.get("id") for w in rows if isinstance(w.get("id"), str)]
    for wid, n in Counter(ids).items():
        if n > 1:
            rep.err(wid, f"id used {n} times")
    for wid in ids:
        stats["letter " + re.sub(r"\d+$", "", wid)] += 1
    byid = {w["id"]: w for w in rows if isinstance(w.get("id"), str)}

    # dup_of：存在、非自身、无环；链只警告
    root: dict[str, str] = {}
    for wid, w in byid.items():
        d = w.get("dup_of")
        if d is None:
            continue
        stats["dup_of"] += 1
        if not isinstance(d, str) or d not in byid:
            rep.err(wid, f"dup_of {d!r} is not an id in this file")
        elif d == wid:
            rep.err(wid, "dup_of points to itself")
    cycles: set[frozenset] = set()
    for wid in byid:
        seen = [wid]
        cur = wid
        cyclic: frozenset = frozenset()
        while True:
            nxt = byid[cur].get("dup_of")
            if not isinstance(nxt, str) or nxt not in byid or nxt == cur:
                break
            if nxt in seen:
                cyclic = frozenset(seen[seen.index(nxt):])
                if cyclic not in cycles:
                    cycles.add(cyclic)
                    rep.err(nxt, "dup_of cycle: " + " → ".join(seen[seen.index(nxt):] + [nxt]))
                break
            seen.append(nxt)
            cur = nxt
        root[wid] = min(cyclic) if cyclic else cur
        if len(seen) > 2 and not cyclic:
            rep.warn("dup_of chain (point straight at the kept row)", " → ".join(seen))

    # 同一 doi / arxiv 却不在同一 dup_of 组
    for key in ("doi", "arxiv"):
        groups: dict[str, list[str]] = defaultdict(list)
        for wid, w in byid.items():
            v = w.get(key)
            if isinstance(v, str) and v:
                groups[re.sub(r"v\d+$", "", v.lower()) if key == "arxiv" else v.lower()].append(wid)
        for v, members in groups.items():
            if len({root[m] for m in members}) > 1:
                rep.warn(f"same {key}, not linked by dup_of", f"{v}: {', '.join(members)}")

    # 近似重复标题
    items = [(wid, norm_title(w.get("title") if isinstance(w.get("title"), str) else "")) for wid, w in byid.items()]
    items = [(wid, t) for wid, t in items if t]
    parent = {wid: wid for wid, _ in items}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i in range(len(items)):
        a, ta = items[i]
        for j in range(i + 1, len(items)):
            b, tb = items[j]
            if root[a] == root[b]:
                continue
            if bool(CORRECTION_RE.match(ta)) != bool(CORRECTION_RE.match(tb)):
                continue
            if similar(ta, tb, threshold):
                parent[find(a)] = find(b)
    clusters: dict[str, list[str]] = defaultdict(list)
    for wid, _ in items:
        clusters[find(wid)].append(wid)
    for members in clusters.values():
        if len(members) < 2:
            continue

        def tag(x):
            w = byid[x]
            return f"{x} ({w.get('kind')}, {w.get('year') if w.get('year') is not None else '—'})"
        title = byid[members[0]].get("title", "")
        title = title if len(title) <= 70 else title[:69] + "…"
        rep.warn("near-duplicate titles, not linked by dup_of", " ~ ".join(tag(x) for x in members) + f' "{title}"')

    # 无定位
    for wid, w in byid.items():
        if w.get("dup_of"):
            continue
        if not w.get("doi") and not w.get("arxiv") and not w.get("urls"):
            rep.warn("no doi/arxiv/urls (non-dup rows)", wid, ids_only=True)
    return stats


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    ap = argparse.ArgumentParser(description="校验 works.json（必需键、ID、dup_of、年份、DOI、arXiv、近似重复）")
    ap.add_argument("paths", nargs="+", help="works.json、publications 目录、Skill 目录或团队目录")
    ap.add_argument("--title-threshold", type=float, default=0.95, metavar="R",
                    help="近似重复标题的相似度阈值（difflib ratio，默认 0.95）")
    ap.add_argument("--show", type=int, default=10, metavar="N", help="每类警告最多列 N 条（默认 10；0 只给数目）")
    ap.add_argument("--extra-id-letters", default="", metavar="XY", help="额外允许的 ID 字母")
    ap.add_argument("--extra-kinds", default="", metavar="a,b", help="额外允许的 kind，逗号分隔")
    a = ap.parse_args()

    letters = set(ID_LETTERS) | {c for c in a.extra_id_letters.upper() if c.isalpha()}
    kinds = KINDS | {k.strip() for k in a.extra_kinds.split(",") if k.strip()}
    files: list[Path] = []
    for arg in a.paths:
        res = find_works(arg)
        if res is None:
            print(f"❌ no such file or directory: {arg}", file=sys.stderr)
            sys.exit(2)
        found, notes = res
        for n in notes:
            print(n)
        if not found:
            print(f"❌ no works.json under {arg} (expected <skill>/{WORKS_REL.as_posix()})", file=sys.stderr)
            sys.exit(2)
        files += [f for f in found if f.resolve() not in {x.resolve() for x in files}]

    n_err = n_warn = n_works = 0
    for f in files:
        rep = Report(a.show)
        stats = validate(f, rep, letters, kinds, a.title_threshold)
        letters_s = " · ".join(f"{k[7:]} {v}" for k, v in sorted(stats.items()) if k.startswith("letter "))
        mark = "❌" if rep.errors else "✅"
        print(f"{mark} {display(f)}: {stats['works']} works ({letters_s or 'no ids'}), {stats['dup_of']} dup_of, "
              f"{len(rep.errors)} errors, {rep.n_warnings} warnings")
        for line in rep.lines():
            print(line)
        n_err += len(rep.errors)
        n_warn += rep.n_warnings
        n_works += stats["works"]
    mark = "❌" if n_err else "✅"
    print(f"{mark} {len(files)} files, {n_works} works, {n_err} errors, {n_warn} warnings")
    sys.exit(1 if n_err else 0)


if __name__ == "__main__":
    main()
