#!/usr/bin/env python3
"""
拉取研究者的发表全景（研究Skill · Agent 1 用）。
数据来自 OpenAlex 公开API（免费、无需key）。输出发表概况、高被引论文、
研究方向随时间的变化、作者位次变化（一作→末作）、高频合作者和代表作候选，
供Agent 1选代表作、Agent 6画研究轨迹。

用法:
    python3 fetch_publications.py "<研究者姓名>" [选项]

选项:
    --out DIR          输出目录（默认 ./publications）
    --author-id ID     直接指定OpenAlex作者ID（如 A5023888391），跳过同名消歧
    --orcid ORCID      用ORCID定位作者（如 0000-0002-1825-0097）
    --top N            高被引论文取前N篇（默认 25）
    --abstracts N      为前N篇高被引论文导出摘要（默认 10，0=不导出）
    --max-works N      用于统计的论文上限（默认 2000）
    --mailto EMAIL     OpenAlex礼貌池参数（可选，限流更宽松）
    --json             额外保存原始数据 works.json

示例:
    python3 fetch_publications.py "Richard Hamming" --out .claude/skills/hamming-research-craft/references/sources/publications
    python3 fetch_publications.py "Kaiming He" --author-id A5000000000

输出:
    <out>/publications.md   发表全景摘要
    <out>/abstracts.md      代表作候选的摘要（便于精读前筛选）
    <out>/works.json        原始数据（仅 --json）

注意：
    - OpenAlex的作者消歧并不完美，同名/拆分档案常见。脚本会列出候选，
      默认选被引最高的那个；不是本人时用 --author-id 重跑
    - 被引数因数据源不同会和Google Scholar有出入，只作相对比较
    - 这是调研原料，不是结论。代表作最终由调研判断，不由被引数决定
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

API = "https://api.openalex.org"
WORK_FIELDS = ",".join([
    "id", "doi", "title", "publication_year", "publication_date", "type",
    "cited_by_count", "primary_location", "authorships", "primary_topic",
    "open_access", "ids",
])


# ---------- API ----------

def api_get(path: str, params: dict, mailto: str = "") -> dict:
    """GET OpenAlex，429/5xx 指数退避重试3次。"""
    params = {k: v for k, v in params.items() if v not in (None, "")}
    if mailto:
        params["mailto"] = mailto
    api_key = os.environ.get("OPENALEX_API_KEY")
    if api_key:
        params["api_key"] = api_key
    url = f"{API}{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "nuwa-skill/fetch_publications"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return {}
            if e.code in (429, 500, 502, 503) and attempt < 2:
                time.sleep(2 ** (attempt + 1))
                continue
            raise
        except urllib.error.URLError:
            if attempt < 2:
                time.sleep(2 ** (attempt + 1))
                continue
            raise
    return {}


def short_id(openalex_id: str) -> str:
    return (openalex_id or "").rstrip("/").split("/")[-1]


def resolve_author(name: str, author_id: str, orcid: str, mailto: str) -> tuple[dict, list[dict]]:
    """返回 (选中的作者, 候选列表)。"""
    if author_id:
        return api_get(f"/authors/{short_id(author_id)}", {}, mailto), []
    if orcid:
        return api_get(f"/authors/orcid:{orcid}", {}, mailto), []
    res = api_get("/authors", {"search": name, "per-page": 10}, mailto)
    candidates = res.get("results") or []
    if not candidates:
        return {}, []
    chosen = max(candidates, key=lambda a: a.get("cited_by_count") or 0)
    return chosen, candidates


def fetch_works(author_id: str, max_works: int, mailto: str) -> list[dict]:
    """按被引降序分页拉取作者全部论文（cursor分页，每页200）。"""
    works, cursor = [], "*"
    while cursor and len(works) < max_works:
        res = api_get("/works", {
            "filter": f"author.id:{author_id}",
            "sort": "cited_by_count:desc",
            "per-page": 200,
            "cursor": cursor,
            "select": WORK_FIELDS,
        }, mailto)
        batch = res.get("results") or []
        if not batch:
            break
        works.extend(batch)
        cursor = (res.get("meta") or {}).get("next_cursor")
    return works[:max_works]


def fetch_abstracts(work_ids: list[str], mailto: str) -> dict[str, str]:
    """摘要只对少量论文单独拉取（abstract_inverted_index 体积大）。"""
    out = {}
    for wid in work_ids:
        w = api_get(f"/works/{short_id(wid)}", {"select": "id,abstract_inverted_index"}, mailto)
        text = rebuild_abstract(w.get("abstract_inverted_index"))
        if text:
            out[wid] = text
    return out


# ---------- 解析 ----------

def rebuild_abstract(inverted: dict | None) -> str:
    if not inverted:
        return ""
    positions = [(pos, word) for word, poss in inverted.items() for pos in poss]
    return " ".join(word for _, word in sorted(positions))


def venue(work: dict) -> str:
    src = ((work.get("primary_location") or {}).get("source") or {})
    return src.get("display_name") or "—"


def topic(work: dict) -> str:
    return ((work.get("primary_topic") or {}).get("display_name")) or ""


def subfield(work: dict) -> str:
    return (((work.get("primary_topic") or {}).get("subfield") or {}).get("display_name")) or ""


def identifier(work: dict) -> str:
    """优先 DOI，其次 arXiv 链接，最后 OpenAlex ID——保证每篇都可核实。"""
    if work.get("doi"):
        return work["doi"]
    loc = work.get("primary_location") or {}
    landing = loc.get("landing_page_url") or ""
    if "arxiv.org" in landing:
        return landing
    return work.get("id") or "—"


def author_position(work: dict, author_id: str) -> str:
    for a in work.get("authorships") or []:
        if short_id((a.get("author") or {}).get("id")) == author_id:
            n = len(work.get("authorships") or [])
            if n == 1:
                return "solo"
            return a.get("author_position") or "middle"
    return "unknown"


def period_of(year: int, span: int = 5) -> str:
    start = year - year % span
    return f"{start}-{start + span - 1}"


def analyze(author: dict, works: list[dict], recent_years: int = 2) -> dict:
    aid = short_id(author.get("id"))
    this_year = date.today().year

    by_period = defaultdict(lambda: {"n": 0, "pos": Counter(), "topics": Counter(),
                                     "subfields": Counter(), "top": None})
    coauthors = {}
    venues = Counter()

    for w in works:
        year = w.get("publication_year")
        if not year:
            continue
        pos = author_position(w, aid)
        p = by_period[period_of(year)]
        p["n"] += 1
        p["pos"][pos] += 1
        if topic(w):
            p["topics"][topic(w)] += 1
        if subfield(w):
            p["subfields"][subfield(w)] += 1
        if p["top"] is None or (w.get("cited_by_count") or 0) > (p["top"].get("cited_by_count") or 0):
            p["top"] = w
        if venue(w) != "—":
            venues[venue(w)] += 1

        for a in w.get("authorships") or []:
            co = a.get("author") or {}
            cid = short_id(co.get("id"))
            if not cid or cid == aid:
                continue
            c = coauthors.setdefault(cid, {"name": co.get("display_name") or cid, "n": 0,
                                           "first": year, "last": year, "mentee": 0})
            c["n"] += 1
            c["first"] = min(c["first"], year)
            c["last"] = max(c["last"], year)
            # 对方一作 + 本人末作：常见的导师-学生署名模式（仅为推测信号）
            if a.get("author_position") == "first" and pos == "last":
                c["mentee"] += 1

    by_cites = sorted(works, key=lambda w: w.get("cited_by_count") or 0, reverse=True)
    recent = sorted(
        [w for w in works if (w.get("publication_year") or 0) >= this_year - recent_years],
        key=lambda w: (w.get("publication_date") or str(w.get("publication_year") or "")), reverse=True,
    )

    # 代表作候选：高被引前3 + 突破作 + 各时期最高被引（去重）
    candidates, seen = [], set()

    def add(w, reason):
        if w and w.get("id") not in seen:
            seen.add(w.get("id"))
            candidates.append((w, reason))

    for w in by_cites[:3]:
        add(w, "高被引")
    if by_cites:
        cutoff = max(1, len(by_cites) // 10)
        top_decile = by_cites[:cutoff]
        breakout = min(top_decile, key=lambda w: w.get("publication_year") or 9999)
        add(breakout, "突破作（高被引中最早的一篇）")
    for per in sorted(by_period):
        add(by_period[per]["top"], f"{per} 时期最高被引")

    return {
        "periods": dict(sorted(by_period.items())),
        "coauthors": sorted(coauthors.values(), key=lambda c: c["n"], reverse=True),
        "venues": venues,
        "by_cites": by_cites,
        "recent": recent,
        "candidates": candidates,
    }


# ---------- 输出 ----------

def md_escape(text: str) -> str:
    return (text or "").replace("|", "\\|").replace("\n", " ").strip()


def render_candidates(candidates: list[dict], chosen_id: str) -> list[str]:
    lines = ["## 同名候选（请核对是否选对了人）", "",
             "| 选中 | OpenAlex ID | 姓名 | 机构 | 论文数 | 被引 | 主要方向 |",
             "|------|------------|------|------|-------|------|---------|"]
    for a in candidates:
        inst = ", ".join(i.get("display_name", "") for i in (a.get("last_known_institutions") or [])[:2]) or "—"
        topics = ", ".join(t.get("display_name", "") for t in (a.get("topics") or [])[:3]) or "—"
        mark = "✅" if short_id(a.get("id")) == chosen_id else ""
        lines.append(f"| {mark} | `{short_id(a.get('id'))}` | {md_escape(a.get('display_name'))} | "
                     f"{md_escape(inst)} | {a.get('works_count', 0)} | {a.get('cited_by_count') or 0} | {md_escape(topics)} |")
    lines += ["", "> 默认选被引最高的档案。不是本人时，用 `--author-id <ID>` 重跑。"
              "同一人被拆成多个档案也很常见，必要时分别跑再合并。", ""]
    return lines


def render(author: dict, works: list[dict], a: dict, candidates: list[dict], top: int) -> str:
    aid = short_id(author.get("id"))
    stats = author.get("summary_stats") or {}
    inst = ", ".join(i.get("display_name", "") for i in (author.get("last_known_institutions") or [])) or "—"
    today = date.today().isoformat()
    L = [f"# {author.get('display_name')} · 发表全景", "",
         f"> 数据来源：OpenAlex（作者ID `{aid}`），拉取日期 {today}。"
         "被引数与Google Scholar会有出入，只作相对比较。本文件是调研原料，不是结论。", ""]

    if len(candidates) > 1:
        L += render_candidates(candidates, aid)

    L += ["## 概况", "",
          f"- 当前机构：{inst}",
          f"- ORCID：{author.get('orcid') or '—'}",
          f"- 论文数：{author.get('works_count', len(works))}（本次统计 {len(works)} 篇）",
          f"- 总被引：{author.get('cited_by_count', '—')}",
          f"- h-index：{stats.get('h_index', '—')} · i10-index：{stats.get('i10_index', '—')}", ""]

    L += [f"## 高被引论文 Top {top}", "",
          "| # | 年份 | 标题 | Venue | 被引 | 位次 | 标识 |",
          "|---|------|------|-------|------|------|------|"]
    for i, w in enumerate(a["by_cites"][:top], 1):
        L.append(f"| {i} | {w.get('publication_year') or '—'} | {md_escape(w.get('title'))} | "
                 f"{md_escape(venue(w))} | {w.get('cited_by_count') or 0} | "
                 f"{author_position(w, aid)} | {identifier(w)} |")
    L.append("")

    L += ["## 研究轨迹（按5年分段）", "",
          "位次统计：first=一作，last=末作（常为导师/PI），solo=独作。"
          "一作占比下降、末作占比上升，通常意味着从亲手做转向带团队——研究Skill要区分这两个阶段的方法。", "",
          "| 时期 | 论文数 | first / last / solo / middle | 主要方向 | 该时期最高被引 |",
          "|------|-------|-----------------------------|---------|--------------|"]
    for per, p in a["periods"].items():
        pos = p["pos"]
        directions = ", ".join(t for t, _ in (p["subfields"] or p["topics"]).most_common(3)) or "—"
        best = p["top"]
        best_str = f"{md_escape(best.get('title'))}（{best.get('cited_by_count') or 0}）" if best else "—"
        L.append(f"| {per} | {p['n']} | {pos['first']} / {pos['last']} / {pos['solo']} / {pos['middle']} | "
                 f"{md_escape(directions)} | {best_str} |")
    L.append("")

    L += ["## 高频合作者（Top 15）", "",
          "「对方一作×本人末作」次数高，常见于导师-学生关系——**仅为推测信号**，需Agent 4/6核实。", "",
          "| 合作者 | 合作篇数 | 合作年份 | 对方一作×本人末作 |",
          "|-------|---------|---------|-----------------|"]
    for c in a["coauthors"][:15]:
        L.append(f"| {md_escape(c['name'])} | {c['n']} | {c['first']}-{c['last']} | {c['mentee']} |")
    L.append("")

    L += ["## 常投Venue（Top 10）", ""]
    L += [f"- {md_escape(v)}：{n}篇" for v, n in a["venues"].most_common(10)] or ["- —"]
    L.append("")

    L += ["## 最近的论文", ""]
    if a["recent"]:
        for w in a["recent"][:15]:
            L.append(f"- {w.get('publication_date') or w.get('publication_year')} · "
                     f"{md_escape(w.get('title'))} · {md_escape(venue(w))} · {identifier(w)}")
    else:
        L.append("- 近两年无新论文（或数据源尚未收录）——Agent 6 需另行核实最近动态")
    L.append("")

    L += ["## 代表作候选（供Agent 1做代表作解剖）", "",
          "按被引和时期自动挑选，**最终代表作由调研判断**：本人自认最重要的、方向转折点之作，可能不在此列。", ""]
    for w, reason in a["candidates"]:
        L.append(f"- **{md_escape(w.get('title'))}**（{w.get('publication_year') or '—'}，"
                 f"{md_escape(venue(w))}，被引{w.get('cited_by_count') or 0}）— {reason} — {identifier(w)}")
    L.append("")
    return "\n".join(L)


def render_abstracts(author: dict, works: list[dict], abstracts: dict[str, str]) -> str:
    L = [f"# {author.get('display_name')} · 代表作候选摘要", "",
         "> 来自OpenAlex，仅供筛选精读对象。引用前请回到原文核对。", ""]
    for w in works:
        text = abstracts.get(w.get("id"))
        if not text:
            continue
        L += [f"## {w.get('title')}", "",
              f"{w.get('publication_year') or '—'} · {venue(w)} · 被引{w.get('cited_by_count') or 0} · {identifier(w)}", "",
              text, ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description="拉取研究者的发表全景（OpenAlex）")
    ap.add_argument("name", nargs="?", default="", help="研究者姓名（英文名命中率更高）")
    ap.add_argument("--out", default="publications")
    ap.add_argument("--author-id", default="")
    ap.add_argument("--orcid", default="")
    ap.add_argument("--top", type=int, default=25)
    ap.add_argument("--abstracts", type=int, default=10)
    ap.add_argument("--max-works", type=int, default=2000)
    ap.add_argument("--mailto", default="")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if not (args.name or args.author_id or args.orcid):
        ap.print_usage()
        sys.exit(1)

    try:
        author, candidates = resolve_author(args.name, args.author_id, args.orcid, args.mailto)
        if not author:
            print(f"❌ OpenAlex 未找到作者：{args.name or args.author_id or args.orcid}")
            print("   试试英文全名、--orcid，或到 https://openalex.org 手动搜索后用 --author-id 指定")
            sys.exit(1)
        aid = short_id(author.get("id"))
        print(f">>> 作者：{author.get('display_name')}（{aid}），论文数 {author.get('works_count')}")
        if len(candidates) > 1:
            print(f"⚠️ 有 {len(candidates)} 个同名候选，已选被引最高的一个；候选表见 publications.md")

        works = fetch_works(aid, args.max_works, args.mailto)
        print(f">>> 拉取论文 {len(works)} 篇")
        analysis = analyze(author, works)

        abstracts = {}
        if args.abstracts > 0:
            ids = [w.get("id") for w, _ in analysis["candidates"]]
            ids += [w.get("id") for w in analysis["by_cites"] if w.get("id") not in ids]
            abstracts = fetch_abstracts(ids[:args.abstracts], args.mailto)
    except (urllib.error.URLError, TimeoutError) as e:
        print(f"❌ 访问 OpenAlex 失败：{e}")
        print("   检查网络/代理；无法联网时改用 Google Scholar / DBLP / Semantic Scholar 手动整理发表列表")
        sys.exit(2)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    (out / "publications.md").write_text(render(author, works, analysis, candidates, args.top), encoding="utf-8")
    print(f"✅ {out / 'publications.md'}")
    if abstracts:
        ordered = [w for w, _ in analysis["candidates"]] + analysis["by_cites"]
        seen, unique = set(), []
        for w in ordered:
            if w.get("id") not in seen:
                seen.add(w.get("id"))
                unique.append(w)
        (out / "abstracts.md").write_text(render_abstracts(author, unique, abstracts), encoding="utf-8")
        print(f"✅ {out / 'abstracts.md'}（{len(abstracts)} 篇摘要）")
    if args.json:
        (out / "works.json").write_text(json.dumps({"author": author, "works": works}, ensure_ascii=False, indent=1),
                                        encoding="utf-8")
        print(f"✅ {out / 'works.json'}")


if __name__ == "__main__":
    main()
