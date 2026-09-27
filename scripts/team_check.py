#!/usr/bin/env python3
"""
研究团队的交付闸门：把手册第四节、第九节的检查一次跑完（研究团队 · 每一档结束时、交付之前）。

用法:
    python3 scripts/team_check.py product/<team> [--tier auto|base|deep] [--skip-quality] [--member a,b] [--json]

检查（任何一项 ✗ 退出码为 1；— 表示跳过并写明原因）:
  团队
    team.json       能读、字段合法（与 new_team.py 同一套校验）
    links           check_links.py <team> 0 broken
    templates       团队里所有 .md 没有 {{ 和 [TODO
    git             git ls-files <team> 里没有 PDF / PostScript / DjVu / EPUB、txt/，private/ 下只有 README.md
    readme          团队 README 链接每位成员的文件夹（](<slug>/…)）
    roundtable      圆桌 SKILL.md 存在，frontmatter name = team.json 的 roundtable；Team 表有每位成员的 `slug`；
                    座位表里每位成员至少主讲一行；3–6 条 fault line，每条引用至少两位成员
                    （深读档：每条两边都有 [<slug> card <ID> p. N] 卡片引用，引用的 ID 在该成员的卡片里都存在，
                    不剩 "card evidence pending"）
    coverage        深读档：DEEP-READING.md 原样含 team_status.py --coverage 的表，README 原样含 --coverage --short 的表
  每位成员
    skill           SKILL.md 存在；quality_check.py 12/12（--skip-quality 跳过）；## Roundtable Card 的 7 项齐全
    works           深读档：validate_works.py 0 errors；INDEX.md 行数 = 去重后的研究作品数
    cards           深读档：没有未读行（INDEX 的 Read 列）；07 / 08 / 09 / technique-catalog 都在
    quotes          深读档：verify_card_quotes.py NOT FOUND = 0（本地没有 txt/ 时跳过：PDF 和 txt 不进 git，新容器里要先重跑
                    acquire_fulltexts.py）
    ledger          深读档：check_ledger.py 指向 09-evidence-ledger.md 的锚点都能解析

--tier auto（默认）：有任何成员写了卡片（references/research/cards/*.digest.json）就按深读档查，否则按轻量档。
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import team_status as ts  # noqa: E402

CARD_LABELS = ["Lens", "Leads when", "First questions asked", "Default recommendation", "Will push back on",
               "Likely disagreements", "Blind spots"]
BAD_FILES = re.compile(r"\.(pdf|ps|ps\.gz|djvu|epub)$|/txt/|/private/", re.I)
CITE = re.compile(r"\[([a-z0-9][a-z0-9-]*) ([^\]]+)\]")
CARD_ID = re.compile(r"\b[A-Z]\d{3,}\b")


class Report:
    def __init__(self):
        self.rows = []

    def add(self, scope: str, name: str, ok: bool | None, detail: str = ""):
        self.rows.append({"scope": scope, "check": name, "status": "pass" if ok else ("skip" if ok is None else "fail"),
                          "detail": detail})

    @property
    def failed(self) -> list[dict]:
        return [r for r in self.rows if r["status"] == "fail"]


def run(cmd: list[str], cwd: Path | None = None) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, cwd=cwd, timeout=600)
    except (OSError, subprocess.TimeoutExpired) as e:
        return 99, str(e)
    return p.returncode, (p.stdout + p.stderr).strip()


def last_line(out: str) -> str:
    lines = [l for l in out.splitlines() if l.strip()]
    return lines[-1][:200] if lines else ""


def section(text: str, start: str, stop: re.Pattern) -> str:
    i = text.find(start)
    if i < 0:
        return ""
    m = stop.search(text, i + len(start))
    return text[i:m.start() if m else len(text)]


def digest_ids(member_dir: Path) -> set[str]:
    ids = set()
    for dj in (member_dir / "references/research/cards").glob("*.digest.json"):
        try:
            ids |= {str(c.get("id")) for c in json.loads(dj.read_text(encoding="utf-8"))}
        except (ValueError, AttributeError):
            pass
    return ids


def check_roundtable(rep: Report, team: Path, cfg: dict, deep: bool):
    slugs = [m["slug"] for m in cfg["members"]]
    rt = team / cfg["roundtable"] / "SKILL.md"
    if not rt.exists():
        rep.add("team", "roundtable", False, f"{rt} missing (team-layer.js, T2)")
        return
    text = rt.read_text(encoding="utf-8")
    probs = []
    m = re.search(r"^name:\s*(\S+)", text, re.M)
    if not m or m.group(1) != cfg["roundtable"]:
        probs.append(f"frontmatter name is {m.group(1) if m else 'missing'}, team.json says {cfg['roundtable']}")
    team_tab = section(text, "## Team", re.compile(r"^## ", re.M))
    missing = [s for s in slugs if f"`{s}`" not in team_tab]
    if missing:
        probs.append(f"not in the Team table: {', '.join(missing)}")
    seat = section(text, "Step 1 · Seating", re.compile(r"^###? ", re.M))
    leads = []
    for line in seat.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.lstrip().startswith("|") and len(cells) >= 2 and not set(cells[0]) <= set("-: ") \
                and cells[1].lower() not in ("leads", "lead"):
            leads.append(cells[1])
    if not leads:
        probs.append("no seating table found under 'Step 1 · Seating'")
    else:
        idle = [mm["slug"] for mm in cfg["members"]
                if not any((mm.get("surname") or mm["name"].split()[-1]) in l for l in leads)]
        if idle:
            probs.append(f"leads no seating row: {', '.join(idle)}")
    fl = section(text, "Documented fault lines", re.compile(r"^> 🔵|^###? ", re.M))
    items = re.findall(r"^\d+\. \*\*(.+?)\*\*(.*)$", fl, re.M)
    if not 3 <= len(items) <= 6:
        probs.append(f"{len(items)} documented fault lines (3–6 expected)")
    ids = {s: digest_ids(team / s) for s in slugs} if deep else {}
    for title, body in items:
        cites = [(s, t) for s, t in CITE.findall(body) if s in slugs]
        sides = {s for s, _ in cites}
        if deep:
            card_sides = {s for s, t in cites if re.match(r"cards?\b", t)}
            if len(card_sides) < 2:
                probs.append(f"fault line '{title[:50]}': card evidence from {len(card_sides)} member(s), 2 needed")
            miss = sorted({f"{s} {i}" for s, t in cites if re.match(r"cards?\b", t) for i in CARD_ID.findall(t)
                           if i not in ids.get(s, set())})
            if miss:
                probs.append(f"fault line '{title[:50]}': card ids not in the digests: {', '.join(miss[:8])}")
            if "evidence pending" in body:
                probs.append(f"fault line '{title[:50]}': still says 'card evidence pending'")
        elif len(sides) < 2:
            probs.append(f"fault line '{title[:50]}': cites {len(sides)} member(s) as [<slug> …], 2 needed")
    rep.add("team", "roundtable", not probs, "; ".join(probs) or
            f"{len(slugs)} members seated, {len(items)} fault lines with evidence from both sides")


def check_member(rep: Report, team: Path, m: dict, deep: bool, skip_quality: bool, st: dict):
    sk = team / m["slug"]
    skill = sk / "SKILL.md"
    scope = m["slug"]
    if not skill.exists():
        rep.add(scope, "skill", False, "SKILL.md missing (team-base-skills.js, T1)")
        return
    probs = []
    if not skip_quality:
        q = ts.quality(skill)
        if q != "12/12":
            probs.append(f"quality_check.py {q}")
    card = section(skill.read_text(encoding="utf-8"), "## Roundtable Card", re.compile(r"^## ", re.M))
    if not card:
        probs.append("no ## Roundtable Card")
    else:
        lost = [l for l in CARD_LABELS if l.lower() not in card.lower()]
        if lost:
            probs.append(f"Roundtable Card lacks: {', '.join(lost)}")
    rep.add(scope, "skill", not probs, "; ".join(probs) or ("12/12, Roundtable Card complete" if not skip_quality
                                                            else "Roundtable Card complete (quality check skipped)"))
    if not deep:
        return
    wj = sk / "references/sources/publications/works.json"
    if not wj.exists():
        rep.add(scope, "works", False, "publications/works.json missing (team-harvest.js, T3.1)")
    else:
        rc, out = run([sys.executable, str(HERE / "validate_works.py"), str(wj)])
        ok = rc == 0 and st["index_complete"]
        detail = last_line(out)
        if not st["index_complete"]:
            detail += (f"; INDEX.md has {st['indexed']} research rows, works.json {st['works_distinct_research']} distinct "
                       "(rerun acquire_fulltexts.py)" if st["index_exists"] else "; papers/INDEX.md missing (acquire_fulltexts.py)")
        rep.add(scope, "works", ok, detail)
    miss = [n for n, ok in (("07", st["has_07"]), ("08", st["has_08"]), ("09", st["has_09"]),
                            ("technique-catalog", st["has_catalog"])) if not ok]
    rep.add(scope, "cards", not st["unread"] and not miss and st["cards"] > 0,
            f"{st['cards']} cards, {st['unread']} unread INDEX rows" + (f"; missing {', '.join(miss)}" if miss else ""))
    txt = sk / "references/sources/papers/txt"
    have = len(list(txt.glob("*.txt"))) if txt.is_dir() else 0
    if st["full_text"] and not have:
        rep.add(scope, "quotes", None, f"no local txt/ ({st['full_text']} rows have text): run acquire_fulltexts.py first "
                                       "(PDFs and txt/ are git-ignored), then rerun")
    else:
        rc, out = run([sys.executable, str(HERE / "verify_card_quotes.py"), str(sk)])
        head = next((l for l in out.splitlines() if l.startswith("quotes:")), last_line(out))
        extra = f"; only {have} of {st['full_text']} texts on disk" if have < st["full_text"] else ""
        rep.add(scope, "quotes", rc == 0, head + extra)
    rc, out = run([sys.executable, str(HERE / "check_ledger.py"), str(sk)])
    rep.add(scope, "ledger", rc == 0, last_line(out))


def main():
    ap = argparse.ArgumentParser(description="研究团队交付闸门（一次跑完手册第四节的检查）")
    ap.add_argument("team_dir")
    ap.add_argument("--tier", choices=["auto", "base", "deep"], default="auto")
    ap.add_argument("--skip-quality", action="store_true", help="不跑 quality_check.py（更快）")
    ap.add_argument("--member", default="", help="成员级检查只查这几位（逗号分隔 slug）；团队级检查照常")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    team = Path(a.team_dir)
    if not (team / "team.json").exists():
        sys.exit(f"❌ {team}/team.json not found")
    import new_team
    cfg, errs = new_team.load_config(team / "team.json")
    rep = Report()
    rep.add("team", "team.json", not errs, "; ".join(errs) or f"{len(cfg['members'])} members")
    if errs:
        print("\n".join(f"❌ {e}" for e in errs))
        sys.exit(1)
    only = [x for x in a.member.split(",") if x]
    unknown = [x for x in only if x not in {m["slug"] for m in cfg["members"]}]
    if unknown:
        sys.exit(f"❌ --member: not in team.json: {', '.join(unknown)}")
    deep = a.tier == "deep" or (a.tier == "auto" and any(
        any((team / m["slug"] / "references/research/cards").glob("*.digest.json")) for m in cfg["members"]))
    sts = {m["slug"]: ts.member_status(team, m, False) for m in cfg["members"]}

    rc, out = run([sys.executable, str(HERE / "check_links.py"), str(team)])
    rep.add("team", "links", rc == 0, last_line(out))
    hits = []
    for f in sorted(team.rglob("*.md")):
        if "/private/" in f.as_posix() and f.name != "README.md":
            continue
        for n, line in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            if "{{" in line or "[TODO" in line:
                hits.append(f"{f.relative_to(team)}:{n}")
    rep.add("team", "templates", not hits, f"{len(hits)} line(s) with {{{{ or [TODO: {', '.join(hits[:8])}"
            + (" …" if len(hits) > 8 else "") if hits else "no {{ and no [TODO left")
    rc, out = run(["git", "ls-files", "--", "."], cwd=team)
    if rc != 0:
        rep.add("team", "git", None, "not a git checkout")
    else:
        bad = [p for p in out.splitlines() if BAD_FILES.search("/" + p) and not p.endswith("/private/README.md")
               and not p.startswith("private/README.md")]
        rep.add("team", "git", not bad, f"tracked copyrighted or private files: {', '.join(bad[:8])}" if bad
                else "no PDF/PS/DjVu/EPUB, txt/ or private/ files tracked (private/README.md only)")
    readme = team / "README.md"
    rtext = readme.read_text(encoding="utf-8") if readme.exists() else ""
    unlinked = [m["slug"] for m in cfg["members"] if f"]({m['slug']}/" not in rtext]
    rep.add("team", "readme", readme.exists() and not unlinked,
            "README.md missing" if not readme.exists() else
            (f"member rows missing: {', '.join(unlinked)}" if unlinked else "links every member"))
    check_roundtable(rep, team, cfg, deep)
    if deep:
        ordered = [sts[m["slug"]] for m in cfg["members"]]
        dr = team / "DEEP-READING.md"
        full, short = ts.coverage_md(ordered), ts.coverage_short_md(ordered)
        probs = []
        if not dr.exists() or full not in dr.read_text(encoding="utf-8"):
            probs.append("DEEP-READING.md does not contain the table of team_status.py --coverage verbatim")
        flat = "\n".join(l.strip() for l in rtext.splitlines())  # the summary may sit indented inside a bullet
        if short not in flat:
            probs.append("README.md does not contain the table of team_status.py --coverage --short verbatim")
        rep.add("team", "coverage", not probs, "; ".join(probs) or "DEEP-READING.md and README.md match team_status.py")
    for m in cfg["members"]:
        if not only or m["slug"] in only:
            check_member(rep, team, m, deep, a.skip_quality, sts[m["slug"]])

    if a.json:
        print(json.dumps({"team": cfg["team"], "tier": "deep" if deep else "base", "checks": rep.rows,
                          "failed": len(rep.failed)}, ensure_ascii=False, indent=1))
    else:
        mark = {"pass": "✓", "fail": "✗", "skip": "—"}
        print(f"team_check {team} · {'deep' if deep else 'base'} tier")
        for r in rep.rows:
            print(f"  {mark[r['status']]} {r['scope']:<22} {r['check']:<11} {r['detail']}")
        n = len(rep.failed)
        skipped = sum(1 for r in rep.rows if r["status"] == "skip")
        print(f"{'❌' if n else '✅'} {len(rep.rows)} checks: {n} failed, {skipped} skipped")
    sys.exit(1 if rep.failed else 0)


if __name__ == "__main__":
    main()
