#!/usr/bin/env python3
"""
研究团队（多位研究者的研究Skill + 圆桌）的进度与覆盖统计。

读 <团队目录>/team.json（没有时自动找成员目录：含 references/research/ 或 SKILL.md 带 type: research-craft 的子目录），
对每位成员报告流水线走到了哪一步，并输出深读的精确覆盖表（与 DEEP-READING.md / README 诚实边界里的表同格式）。

进度列:
    base      SKILL.md 是否存在 + quality_check.py 结果（如 12/12）
    notes     references/research/01–06 调研笔记有几份
    works     publications/works.json 条目数（Scholar 行 / 去重后的研究作品；书的开放部分 B### 另计）
    index     papers/INDEX.md 的研究作品行数 · 其中有开放全文（txt）的 · 索引是否完整（= 去重后的研究作品数，✓/✗）
    cards     卡片批次文件数 · 卡片数 · 摘录数 · INDEX 里还没读的行（Read 列为 —，不含 skip）
    synth     07 / 08 / 09 / technique-catalog 是否存在
    stage     推断的当前阶段（T0 骨架 → T1 基础Skill → T3.1 发表列表 → T3.2 全文 → T3.5 卡片 → T3.6 汇总；
              汇总后 SKILL.md 超过 --max-words 时注明要跑 T3.7。T3.6 与 T3.7 都写 09，所以不单列「T3.7 已跑」）
    next      下一步该跑什么（团队层：T2 看圆桌里还有没有标 T2 的 TODO；T3.8 看 DEEP-READING.md 的覆盖表是否等于 --coverage）

覆盖表（--coverage）:
    Scholar rows · Distinct works indexed · Open full text · Read in full · Read in part · Abstract only ·
    Metadata only (incl. unreadable) · Skipped · Book material carded · Quotes verified
    B### 行（书的开放部分：目录、勘误、增补、书评、前言）只计入 Book material 列，不计入研究作品各列。

五列摘要（--coverage --short）: 团队 README 诚实边界里的那张小表，每格都由上面的全表相加，不用手算:
    Researcher（team.json 的 surname）· Works indexed · Read in full / in part ·
    Abstract or metadata only (incl. unreadable) = Abstract only + Metadata only · Skipped
    没有 Total 行；README 与 DEEP-READING.md 的数字因此永远一致。

用法:
    python3 team_status.py <团队目录> [--coverage [--short]] [--json] [--no-quality] [--max-words N]

示例:
    python3 scripts/team_status.py product/dfo-team
    python3 scripts/team_status.py product/dfo-team --coverage      # 可直接贴进 DEEP-READING.md 的 Coverage 表
    python3 scripts/team_status.py product/dfo-team --coverage --short   # 可直接贴进团队 README 诚实边界的五列摘要

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


def member_status(team: Path, m: dict, with_quality: bool, max_words: int = 13000) -> dict:
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
    distinct = [w for w in works if not w.get("dup_of")]
    skill_words = len((sk / "SKILL.md").read_text(encoding="utf-8").split()) if (sk / "SKILL.md").exists() else 0
    book_rows = [r for r in rows if r.get("ID", "").startswith("B")]
    active = [r for r in work_rows if r.get("Role") != "skip"]
    read = {k: sum(1 for r in active if r.get("Read") == k) for k in READ_LEVELS}
    st = {
        "slug": m["slug"], "name": m.get("name") or m["slug"], "surname": m.get("surname") or "",
        "skill": (sk / "SKILL.md").exists(),
        "quality": quality(sk / "SKILL.md") if with_quality else "",
        "notes": sum(1 for p in research.glob("0[1-6]-*.md")) if research.is_dir() else 0,
        "scholar_rows": sum(1 for w in works if str(w.get("id", "")).startswith("S")),
        "works": len(works), "works_distinct": len(distinct),
        "works_distinct_research": sum(1 for w in distinct if not str(w.get("id", "")).startswith("B")),
        "book_items": sum(1 for w in distinct if str(w.get("id", "")).startswith("B")),
        "index_exists": (papers / "INDEX.md").exists(), "skill_words": skill_words,
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
    st["index_complete"] = st["index_exists"] and st["indexed"] == st["works_distinct_research"]
    st["over_budget"] = st["has_08"] and skill_words > max_words
    if st["has_08"]:
        stage = f"T3.6 synthesized ({skill_words} words" + (f" > {max_words}: run T3.7)" if st["over_budget"] else ")")
    elif st["cards"]:
        stage = f"T3.5 reading ({st['unread']} rows unread)" if st["unread"] else "T3.5 carded"
    elif st["full_text"] or st["index_exists"]:
        stage = f"T3.2 full texts ({st['full_text']} open)"
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


def team_layer_done(team: Path, cfg: dict) -> bool:
    """T2 做完：圆桌 SKILL.md 存在，且没有标给 T2（team-layer.js）的 [TODO 项。"""
    rt = team / str(cfg.get("roundtable") or "") / "SKILL.md"
    if not cfg.get("roundtable") or not rt.exists():
        return False
    return not re.search(r"\[TODO[^\]]*\(T2\)", rt.read_text(encoding="utf-8"))


def integrated(team: Path, sts: list[dict]) -> bool:
    """T3.8 做完：DEEP-READING.md 里原样有 --coverage 的整张表。"""
    dr = team / "DEEP-READING.md"
    return dr.exists() and coverage_md(sts) in dr.read_text(encoding="utf-8")


def next_step(s: dict, t2: bool, t38: bool) -> str:
    stage = s["stage"]
    if stage.startswith("T0"):
        return "team-base-skills.js (T1)"
    if stage.startswith("T1"):
        return "team-layer.js with all members (T2)" if not t2 else "base tier done; deep tier: team-harvest.js (T3.1)"
    if stage.startswith("T3.1"):
        return "validate_works.py, then acquire_fulltexts.py (T3.2)"
    if stage.startswith("T3.2"):
        return "team-chase.js (T3.3), then plan_reading_batches.py --out-dir <scratch> (T3.4)"
    if s["has_08"]:
        if s["over_budget"]:
            return "team-tighten.js (T3.7)"
        return "done; T4 team-increment.js when new material appears" if t38 else "team-integrate.js with all members (T3.8)"
    if s["unread"]:
        return "plan_reading_batches.py --out-dir <scratch>, then team-read.js (next round)"
    return "team-synthesize.js (T3.6)"


def progress_md(team: str, sts: list[dict], t2: bool = False, t38: bool = False) -> str:
    out = [f"## {team} · progress", "",
           "| Member | Stage | Base skill | Notes 01–06 | Works (Scholar / distinct) | Indexed · txt | Batches · cards · quotes | Unread rows | 07 · 08 · 09 · catalog | Next |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for s in sts:
        base = (s["quality"] or "✓") if s["skill"] else "—"
        works = f"{s['scholar_rows']} / {s['works_distinct_research']}" + (f" + {s['book_items']} book item{'' if s['book_items'] == 1 else 's'}" if s["book_items"] else "")
        idx = f"{s['indexed']} {'✓' if s['index_complete'] else '✗'} · {s['full_text']}" if s["index_exists"] else "— · —"
        out.append(f"| {s['name']} | {s['stage']} | {base} | {s['notes']}/6 | {works} | "
                   f"{idx} | {s['batches']} · {s['cards']} · {s['quotes']} | {s['unread']} | "
                   f"{yn(s['has_07'])} {yn(s['has_08'])} {yn(s['has_09'])} {yn(s['has_catalog'])} | {s['next']} |")
    out += ["", "Indexed ✓ = INDEX.md has one row per distinct research work of works.json (the T3.2 gate); book items (B###) are "
            "listed in INDEX.md too but counted apart. "
            f"Team layer (T2): {'✓' if t2 else '·'} · coverage in DEEP-READING.md matches --coverage (T3.8): {'✓' if t38 else '·'}"]
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


SHORT_COLS = [("Works indexed", lambda s: str(s["indexed"])),
              ("Read in full / in part", lambda s: f"{s['read_full']} / {s['read_part']}"),
              ("Abstract or metadata only (incl. unreadable)", lambda s: str(s["abstract"] + s["metadata"])),
              ("Skipped (not the author's, or not research)", lambda s: str(s["skipped"]))]


def coverage_short_md(sts: list[dict]) -> str:
    """团队 README 的五列摘要：每格由 coverage_md 的全表相加得到（姓用 team.json 的 surname）。"""
    out = ["| Researcher | " + " | ".join(t for t, _ in SHORT_COLS) + " |", "|---" * (len(SHORT_COLS) + 1) + "|"]
    for s in sts:
        out.append(f"| {s['surname'] or s['name']} | " + " | ".join(f(s) for _, f in SHORT_COLS) + " |")
    unread = sum(s["unread"] for s in sts)
    if unread:
        out.append("")
        out.append(f"⚠️ {unread} indexed works have no card yet (Read column empty); the table is not final.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="研究团队进度与深读覆盖统计")
    ap.add_argument("team_dir")
    ap.add_argument("--coverage", action="store_true", help="只输出覆盖表（markdown）")
    ap.add_argument("--short", action="store_true", help="与 --coverage 一起用：团队 README 的五列摘要（由全表相加）")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    ap.add_argument("--no-quality", action="store_true", help="不跑 quality_check.py（更快）")
    ap.add_argument("--max-words", type=int, default=13000, help="汇总后 SKILL.md 超过这个词数就提示跑 T3.7（默认 13000）")
    a = ap.parse_args()
    if a.short and not a.coverage:
        ap.error("--short goes with --coverage")
    team = Path(a.team_dir)
    if not team.is_dir():
        sys.exit(f"❌ 不是目录：{team}")
    cfg, members = load_members(team)
    if not members:
        sys.exit(f"❌ {team} 里没有找到成员（缺 team.json，也没有含 references/research/ 的子目录）")
    sts = [member_status(team, m, not (a.no_quality or a.coverage or a.json), a.max_words) for m in members]
    t2, t38 = team_layer_done(team, cfg), integrated(team, sts)
    for s in sts:
        s["next"] = next_step(s, t2, t38)
    if a.json:
        print(json.dumps({"team": cfg.get("team", team.name), "team_layer_done": t2, "integrated": t38, "members": sts},
                         ensure_ascii=False, indent=1))
    elif a.coverage:
        print(coverage_short_md(sts) if a.short else coverage_md(sts))
    else:
        print(progress_md(cfg.get("title") or cfg.get("team") or team.name, sts, t2, t38))
        print()
        print(coverage_md(sts))


if __name__ == "__main__":
    main()
