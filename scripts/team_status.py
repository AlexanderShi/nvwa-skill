#!/usr/bin/env python3
"""
研究团队（多位研究者的研究Skill + 圆桌）的进度与覆盖统计。

读 <团队目录>/team.json（没有时自动找成员目录：含 references/research/ 或 SKILL.md 带 type: research-craft 的子目录），
对每位成员报告流水线走到了哪一步，并输出深读的精确覆盖表（与 DEEP-READING.md / README 诚实边界里的表同格式）。

进度列:
    base      SKILL.md 是否存在 + quality_check.py 结果（如 12/12）
    notes     references/research/01–06 调研笔记有几份
    works     publications/works.json 条目数（Scholar 行 / 去重后）
    index     papers/INDEX.md 行数 · 其中有开放全文（txt）的
    cards     卡片批次文件数 · 卡片数 · 摘录数 · INDEX 里还没读的行（Read 列为 —，不含 skip）
    synth     07 / 08 / 09 / technique-catalog 是否存在
    stage     推断的当前阶段（T1 基础Skill → T3.1 发表列表 → T3.2 全文 → T3.5 卡片 → T3.6 汇总 → T3.7 精简）

覆盖表（--coverage）:
    Scholar rows · Distinct works indexed · Open full text · Read in full · Read in part · Abstract only ·
    Metadata only (incl. unreadable) · Skipped · Book material carded · Quotes verified
    B### 行（书的开放部分：目录、勘误、增补、书评、前言）只计入 Book material 列，不计入研究作品各列。

用法:
    python3 team_status.py <团队目录> [--coverage] [--json] [--no-quality]

示例:
    python3 scripts/team_status.py product/dfo-team
    python3 scripts/team_status.py product/dfo-team --coverage      # 可直接贴进 DEEP-READING.md 的 Coverage 表

输出:
    默认 markdown（进度表；加 --coverage 只输出覆盖表），--json 输出全部字段。
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
READ_LEVELS = ("carded", "skimmed", "abstract", "metadata", "unreadable")


def load_members(team: Path) -> tuple[dict, list[dict]]:
    cfg_path = team / "team.json"
    if cfg_path.exists():
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
        return cfg, cfg.get("members") or []
    members = []
    for d in sorted(p for p in team.iterdir() if p.is_dir()):
        skill = d / "SKILL.md"
        research = (d / "references" / "research").is_dir()
        typed = skill.exists() and re.search(r"^type:\s*research-craft", skill.read_text(encoding="utf-8", errors="replace")[:3000], re.M)
        if research or typed:
            members.append({"slug": d.name, "name": d.name})
    return {"team": team.name}, members


def index_rows(path: Path) -> list[dict]:
    """INDEX.md（acquire_fulltexts.py 的 12 列格式）→ 行字典列表。"""
    rows = []
    if not path.exists():
        return rows
    header = None
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
        if not cells:
            continue
        if cells[0] == "#":
            header = cells
            continue
        if header and len(cells) == len(header) and not set(cells[0]) <= {"-"}:
            rows.append(dict(zip(header, cells)))
    return rows


def quality(skill: Path) -> str:
    if not skill.exists():
        return "—"
    try:
        out = subprocess.run([sys.executable, str(HERE / "quality_check.py"), str(skill)],
                             capture_output=True, text=True, timeout=120).stdout
    except (OSError, subprocess.TimeoutExpired):
        return "?"
    m = re.findall(r"(\d+)\s*/\s*(\d+)\s*通过", out)
    return f"{m[-1][0]}/{m[-1][1]}" if m else "?"


def member_status(team: Path, m: dict, with_quality: bool) -> dict:
    sk = team / m["slug"]
    research = sk / "references" / "research"
    papers = sk / "references" / "sources" / "papers"
    works_path = sk / "references" / "sources" / "publications" / "works.json"
    works = json.loads(works_path.read_text(encoding="utf-8")).get("works", []) if works_path.exists() else []
    rows = index_rows(papers / "INDEX.md")
    digests = sorted((research / "cards").glob("*.digest.json")) if (research / "cards").is_dir() else []
    cards = quotes = 0
    for dj in digests:
        data = json.loads(dj.read_text(encoding="utf-8"))
        cards += len(data)
        quotes += sum(len(c.get("quotes") or []) for c in data)

    work_rows = [r for r in rows if not r.get("ID", "").startswith("B")]
    book_rows = [r for r in rows if r.get("ID", "").startswith("B")]
    active = [r for r in work_rows if r.get("Role") != "skip"]
    read = {k: sum(1 for r in active if r.get("Read") == k) for k in READ_LEVELS}
    st = {
        "slug": m["slug"], "name": m.get("name") or m["slug"],
        "skill": (sk / "SKILL.md").exists(),
        "quality": quality(sk / "SKILL.md") if with_quality else "",
        "notes": sum(1 for p in research.glob("0[1-6]-*.md")) if research.is_dir() else 0,
        "scholar_rows": sum(1 for w in works if str(w.get("id", "")).startswith("S")),
        "works": len(works), "works_distinct": sum(1 for w in works if not w.get("dup_of")),
        "indexed": len(work_rows), "full_text": sum(1 for r in work_rows if r.get("Full text") == "txt"),
        "read_full": read["carded"], "read_part": read["skimmed"], "abstract": read["abstract"],
        "metadata": read["metadata"] + read["unreadable"], "unreadable": read["unreadable"],
        "skipped": sum(1 for r in work_rows if r.get("Role") == "skip"),
        "unread": sum(1 for r in active if r.get("Read") not in READ_LEVELS),
        "book_rows": len(book_rows), "book_carded": sum(1 for r in book_rows if r.get("Read") in ("carded", "skimmed")),
        "batches": len(digests), "cards": cards, "quotes": quotes,
        "has_07": (research / "07-paper-cards.md").exists(), "has_08": (research / "08-deep-reading-synthesis.md").exists(),
        "has_09": (research / "09-evidence-ledger.md").exists(),
        "has_catalog": (sk / "references" / "technique-catalog.md").exists(),
    }
    if st["has_09"]:
        stage = "T3.7 tightened"
    elif st["has_08"]:
        stage = "T3.6 synthesized"
    elif st["cards"]:
        stage = f"T3.5 reading ({st['unread']} rows unread)" if st["unread"] else "T3.5 carded"
    elif st["full_text"]:
        stage = "T3.2 full texts"
    elif st["works"]:
        stage = "T3.1 harvested"
    elif st["skill"]:
        stage = "T1 base skill"
    else:
        stage = "T0 scaffold"
    if not st["skill"] and stage != "T0 scaffold":
        stage += " · ⚠️ no SKILL.md (T1 missing)"
    st["stage"] = stage
    return st


def yn(b: bool) -> str:
    return "✓" if b else "·"


def progress_md(team: str, sts: list[dict]) -> str:
    out = [f"## {team} · progress", "",
           "| Member | Stage | Base skill | Notes 01–06 | Works (Scholar / distinct) | Indexed · txt | Batches · cards · quotes | Unread rows | 07 · 08 · 09 · catalog |",
           "|---|---|---|---|---|---|---|---|---|"]
    for s in sts:
        base = (s["quality"] or "✓") if s["skill"] else "—"
        out.append(f"| {s['name']} | {s['stage']} | {base} | {s['notes']}/6 | {s['scholar_rows']} / {s['works_distinct']} | "
                   f"{s['indexed']} · {s['full_text']} | {s['batches']} · {s['cards']} · {s['quotes']} | {s['unread']} | "
                   f"{yn(s['has_07'])} {yn(s['has_08'])} {yn(s['has_09'])} {yn(s['has_catalog'])} |")
    return "\n".join(out)


COV_COLS = [("scholar_rows", "Scholar rows"), ("indexed", "Distinct works indexed"), ("full_text", "Open full text"),
            ("read_full", "Read in full"), ("read_part", "Read in part"), ("abstract", "Abstract only"),
            ("metadata", "Metadata only (incl. unreadable)"), ("skipped", "Skipped (not the author's / non-research)"),
            ("book_carded", "Book material carded"), ("quotes", "Quotes verified")]


def coverage_md(sts: list[dict]) -> str:
    out = ["| Researcher | " + " | ".join(t for _, t in COV_COLS) + " |", "|---" * (len(COV_COLS) + 1) + "|"]
    for s in sts:
        out.append(f"| {s['name']} | " + " | ".join(str(s[k]) for k, _ in COV_COLS) + " |")
    out.append("| **Total** | " + " | ".join(str(sum(s[k] for s in sts)) for k, _ in COV_COLS) + " |")
    unread = sum(s["unread"] for s in sts)
    if unread:
        out.append("")
        out.append(f"⚠️ {unread} indexed works have no card yet (Read column empty); the table is not final.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="研究团队进度与深读覆盖统计")
    ap.add_argument("team_dir")
    ap.add_argument("--coverage", action="store_true", help="只输出覆盖表（markdown）")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    ap.add_argument("--no-quality", action="store_true", help="不跑 quality_check.py（更快）")
    a = ap.parse_args()
    team = Path(a.team_dir)
    if not team.is_dir():
        sys.exit(f"❌ 不是目录：{team}")
    cfg, members = load_members(team)
    if not members:
        sys.exit(f"❌ {team} 里没有找到成员（缺 team.json，也没有含 references/research/ 的子目录）")
    sts = [member_status(team, m, not (a.no_quality or a.coverage)) for m in members]
    if a.json:
        print(json.dumps({"team": cfg.get("team", team.name), "members": sts}, ensure_ascii=False, indent=1))
    elif a.coverage:
        print(coverage_md(sts))
    else:
        print(progress_md(cfg.get("title") or cfg.get("team") or team.name, sts))
        print()
        print(coverage_md(sts))


if __name__ == "__main__":
    main()
