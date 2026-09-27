#!/usr/bin/env python3
"""
为研究Skill的全文深读分配角色、切分阅读批次（研究Skill · 深读阶段用）。

读取 <skill目录>/references/sources/papers/INDEX.md（acquire_fulltexts.py 生成）与 works.json，
给每篇论文定角色并写回 INDEX.md 的 Role 列，再按页数把论文切成阅读批次，输出 JSON，
每个批次交给一个深读 agent（写卡片的要求见 references/paper-reading-card.md）。

角色规则:
    core       被引前 K 篇、SKILL.md 已提到的、近年（>= --recent）、访谈/回忆录/随笔、--core-ids 指定的 → 全文精读
    supplement 其余有全文的 → 略读（摘要、引言、算法、主定理、实验设置、结论）
    skip       INDEX.md 里已有的 skip 保留（专利、talk 由 acquire_fulltexts.py 按 kind 设定），再加 --skip-ids 指定的（非本人作品等）
批次类型:
    core / supplement  按页数装箱（core ≤110页且≤5篇，supplement ≤220页且≤8篇）
    book               >150页的书、学位论文、长报告，单独一批，按章读
    abstract           没有全文的，30篇一批，只写摘要级卡片

用法:
    python3 plan_reading_batches.py <skill目录> [--round N] [--exclude 上一轮批次.json,...]
                                   [--core-ids ID,..] [--skip-ids ID,..] [--reread ID,..] [--no-abstract] > batches.json
    python3 plan_reading_batches.py <skill目录 或 团队目录> --out-dir <scratch> [--no-abstract] [...]

多轮深读：后续轮次用 --round 2 --exclude round1.json（已分派或已有卡片的论文不再分派），
只分派新找到全文的论文；最后一轮再去掉 --no-abstract，给剩下的写摘要级卡片。
已经读完的轮次不用 --exclude：有全文卡片的论文本来就跳过；--exclude 只给还在读的轮次的计划用。
--exclude 给的文件不存在时警告并忽略。

--out-dir（推荐，省掉手工重定向和 --exclude 清单）:
    计划写到 <out-dir>/batches-<slug>-r<N>.json，正是 team-read.js 默认读的文件名（out-dir = 工作流的 scratch）。
    --round 省略时取「out-dir 里这位成员已有计划的最大轮次」与「已有卡片批次的最大轮次」中较大者 + 1；
    out-dir 里这位成员其他轮次的计划自动当作 --exclude。已存在的同名计划不覆盖（--force 覆盖）。
    第一个参数给团队目录（含 team.json）时，给每位成员各规划一次（--member a,b 只规划这几位）。
    标准输出是每位成员一行摘要；某位成员这一轮没有全文批次时提示：下一轮去掉 --no-abstract（最后一轮）。

--reread ID,..（读卡报 REOCR / WRONG-TEXT、acquire_fulltexts.py --reocr / --drop 处理过之后）:
    这些作品即使已有卡片（如 unreadable）也重新排进批次：有全文的进全文批次，没有的（不带 --no-abstract 时）进摘要批次。
"""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

HEADER = ["#", "ID", "Year", "Title", "Venue", "Cites", "Kind", "Source", "Full text", "Pages", "Role", "Read"]


def norm(t):
    return re.sub(r"[^a-z0-9]+", " ", (t or "").lower()).strip()


def read_rows(index):
    rows, pre, post = [], [], []
    seen_table = False
    for line in index.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
        if len(cells) == len(HEADER) and line.startswith("|"):
            seen_table = True
            if cells[0] == "#" or set(cells[0]) <= {"-"}:
                continue
            rows.append(dict(zip(HEADER, cells)))
        elif not seen_table:
            pre.append(line)
        else:
            post.append(line)
    return rows, pre, post


def write_rows(index, rows, pre, post):
    lines = pre + ["| " + " | ".join(HEADER) + " |", "|" + "|".join(["---"] * len(HEADER)) + "|"]
    lines += ["| " + " | ".join(r[h] for h in HEADER) + " |" for r in rows]
    index.write_text("\n".join(lines + post) + "\n", encoding="utf-8")


def warn(msg):
    print(f"⚠️ {msg}", file=sys.stderr)


def card_round(bid: str) -> int:
    """cards/ 里的批次名 → 轮次：c01 → 1，c2-01 → 2，a3-01 → 3（手工起名的其他批次按 1 算）。"""
    m = re.fullmatch(r"[a-z]+(\d+)-\d+", bid)
    return int(m.group(1)) if m else 1


def plan_files(out_dir: Path, slug: str) -> dict[int, Path]:
    found = {}
    for f in out_dir.glob(f"batches-{slug}-r*.json"):
        m = re.fullmatch(rf"batches-{re.escape(slug)}-r(\d+)\.json", f.name)
        if m:
            found[int(m.group(1))] = f
    return found


def plan(skill: Path, a, rnd: int, exclude: list[Path]) -> dict:
    papers = skill / "references/sources/papers"
    index = papers / "INDEX.md"
    rows, pre, post = read_rows(index)
    works = {w["id"]: w for w in json.loads((skill / "references/sources/publications/works.json").read_text())["works"]}
    skill_raw = (skill / "SKILL.md").read_text(encoding="utf-8").lower()
    skill_norm = norm(skill_raw)
    txt_files = {p.name.split("-")[0]: p for p in (papers / "txt").glob("*.txt")}
    core_ids = {x for x in a.core_ids.split(",") if x}
    skip_ids = {x for x in a.skip_ids.split(",") if x}
    reread = {x.strip() for x in a.reread.split(",") if x.strip()}
    unknown = reread - {r["ID"] for r in rows}
    if unknown:
        warn(f"{skill.name}: --reread ids not in INDEX.md: {', '.join(sorted(unknown))}")

    done, carded = set(), set()  # 已有全文卡片或已分派的论文；已有任何卡片的论文
    for dj in (skill / "references/research/cards").glob("*.digest.json"):
        try:
            cards = json.loads(dj.read_text())
            done |= {d["id"] for d in cards if d.get("read_level") not in ("abstract", "metadata")}
            carded |= {d["id"] for d in cards}
        except (json.JSONDecodeError, KeyError):
            pass
    for f in exclude:
        try:
            batches = json.loads(f.read_text())["batches"]
        except FileNotFoundError:
            warn(f"--exclude {f}: file not found, ignored (finished rounds are skipped through their cards anyway)")
            continue
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            warn(f"--exclude {f}: not a batch plan ({e}), ignored")
            continue
        for b in batches:
            if b["mode"] != "abstract":
                done |= {p["id"] for p in b["papers"]}
    done -= reread
    carded -= reread

    def cites(r):
        return int(r["Cites"]) if r["Cites"].isdigit() else 0

    def pages(r):
        return int(r["Pages"]) if r["Pages"].isdigit() else 30

    top = {r["ID"] for r in sorted(rows, key=lambda r: -cites(r))[: a.core_top]}
    for r in rows:
        w = works.get(r["ID"], {})
        if r["ID"] in skip_ids:
            r["Role"] = "skip"
        if r["Role"] == "skip" or (r["Read"] not in ("—", "") and r["ID"] not in reread):
            continue
        mentioned = (w.get("doi") and w["doi"].lower() in skill_raw) or (w.get("arxiv") and w["arxiv"] in skill_raw) \
            or (len(norm(r["Title"])) > 25 and norm(r["Title"]) in skill_norm)
        recent = r["Year"].isdigit() and int(r["Year"]) >= a.recent
        special = w.get("kind") in ("interview", "memoir", "essay") or r["ID"] in core_ids
        r["Role"] = "core" if (r["ID"] in top or mentioned or recent or special) else "supplement"
    write_rows(index, rows, pre, post)

    full = [r for r in rows if r["Full text"] == "txt" and r["Role"] != "skip" and r["ID"] in txt_files and r["ID"] not in done]
    full.sort(key=lambda r: (r["Year"] if r["Year"].isdigit() else "9999", r["ID"]))
    batches = []

    def emit(kind, group):
        n = len([b for b in batches if b["bid"][0] == kind[0]]) + 1
        bid = f"{kind[0]}{n:02d}" if rnd == 1 else f"{kind[0]}{rnd}-{n:02d}"
        batches.append({"bid": bid, "mode": kind, "papers": [{
            "id": r["ID"], "year": r["Year"], "title": r["Title"], "venue": r["Venue"], "role": r["Role"], "pages": pages(r),
            "txt": str(txt_files[r["ID"]]) if r["ID"] in txt_files else None, "doi": works.get(r["ID"], {}).get("doi"),
            "arxiv": works.get(r["ID"], {}).get("arxiv"), "authors": works.get(r["ID"], {}).get("authors"),
            "cites": r["Cites"], "note": works.get(r["ID"], {}).get("note")} for r in group]})

    for role, budget, cap in (("core", a.core_pages, 5), ("supplement", a.supp_pages, 8)):
        group, pg = [], 0
        for r in [r for r in full if r["Role"] == role]:
            if pages(r) > 150:
                emit("book", [r])
                continue
            if group and (pg + pages(r) > budget or len(group) >= cap):
                emit(role, group)
                group, pg = [], 0
            group.append(r)
            pg += pages(r)
        if group:
            emit(role, group)

    rest = [r for r in rows if r["Role"] != "skip" and r["ID"] not in carded
            and not (r["Full text"] == "txt" and r["ID"] in txt_files)]
    rest.sort(key=lambda r: (r["Year"] if r["Year"].isdigit() else "9999", r["ID"]))
    if not a.no_abstract:
        for i in range(0, len(rest), a.abs_size):
            emit("abstract", rest[i:i + a.abs_size])

    summary = {"rows": len(rows), "full_to_read": len(full), "abstract_only": len(rest),
               "skip": sum(1 for r in rows if r["Role"] == "skip"), "round": rnd,
               "batches": {k: sum(1 for b in batches if b["mode"] == k) for k in ("core", "supplement", "book", "abstract")}}
    return {"summary": summary, "batches": batches}


def members_of(target: Path, only: list[str]) -> list[Path]:
    """团队目录（含 team.json）→ 各成员目录；成员目录 → 它自己。"""
    tj = target / "team.json"
    if not tj.exists():
        return [target]
    slugs = [m["slug"] for m in json.loads(tj.read_text(encoding="utf-8")).get("members") or []]
    bad = [s for s in only if s not in slugs]
    if bad:
        sys.exit(f"❌ --member: not in team.json: {', '.join(bad)}")
    return [target / s for s in slugs if not only or s in only]


def main():
    ap = argparse.ArgumentParser(description="为全文深读分配角色并切分阅读批次")
    ap.add_argument("skill_dir", help="成员目录；与 --out-dir 一起用时也可以是团队目录（含 team.json）")
    ap.add_argument("--core-top", type=int, default=25)
    ap.add_argument("--recent", type=int, default=datetime.date.today().year - 2,
                    help="这一年及以后的作品一律精读（core）；默认今年减 2")
    ap.add_argument("--core-pages", type=int, default=110)
    ap.add_argument("--supp-pages", type=int, default=220)
    ap.add_argument("--abs-size", type=int, default=30)
    ap.add_argument("--round", type=int, default=None, help="轮次（默认 1；带 --out-dir 时默认下一轮）")
    ap.add_argument("--core-ids", default="")
    ap.add_argument("--skip-ids", default="")
    ap.add_argument("--reread", default="", help="逗号分隔：即使已有卡片也重新分派的作品（REOCR / WRONG-TEXT 之后）")
    ap.add_argument("--exclude", default="", help="逗号分隔：还在读的轮次的批次JSON，其中的论文视为已分派（文件不存在时警告并忽略）")
    ap.add_argument("--no-abstract", action="store_true")
    ap.add_argument("--out-dir", help="写 <out-dir>/batches-<slug>-r<N>.json（自动排除 out-dir 里其他轮次的计划）")
    ap.add_argument("--member", default="", help="团队目录时只规划这几位（逗号分隔 slug）")
    ap.add_argument("--force", action="store_true", help="--out-dir：覆盖已存在的同名计划")
    a = ap.parse_args()

    target = Path(a.skill_dir)
    exclude = [Path(x) for x in a.exclude.split(",") if x]
    if not a.out_dir:
        if (target / "team.json").exists():
            sys.exit("❌ a team folder needs --out-dir (one plan file per member)")
        res = plan(target, a, a.round or 1, exclude)
        print(json.dumps(res, ensure_ascii=False, indent=1))
        s = res["summary"]
        if a.no_abstract and not s["full_to_read"]:
            warn(f"{target.name}: no full-text batches this round; plan the final round without --no-abstract")
        return

    out = Path(a.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    rc = 0
    for skill in members_of(target, [x for x in a.member.split(",") if x]):
        slug = skill.name
        if not (skill / "references/sources/papers/INDEX.md").exists():
            print(f"{slug}: no papers/INDEX.md yet (run acquire_fulltexts.py first); skipped")
            rc = 1
            continue
        have = plan_files(out, slug)
        cards = [card_round(p.name[:-len(".digest.json")]) for p in (skill / "references/research/cards").glob("*.digest.json")]
        rnd = a.round or max([0, *have, *cards]) + 1
        dest = out / f"batches-{slug}-r{rnd}.json"
        if dest.exists() and not a.force:
            print(f"{slug}: {dest} exists (a plan of round {rnd}, maybe still being read); not replaced (--force replaces it)")
            rc = 1
            continue
        excl = exclude + [f for k, f in sorted(have.items()) if k != rnd]
        res = plan(skill, a, rnd, excl)
        s = res["summary"]
        b = s["batches"]
        nfull = b["core"] + b["supplement"] + b["book"]
        line = (f"{slug}: round {rnd}: {nfull} full-text batch(es) (core {b['core']}, supplement {b['supplement']}, "
                f"book {b['book']}), {b['abstract']} abstract batch(es); {s['full_to_read']} works with text, "
                f"{s['abstract_only']} without")
        if excl:
            line += f"; excluded {len(excl)} other plan(s)"
        if not res["batches"]:
            print(f"{line} — nothing to plan, no file written")
        else:
            dest.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
            print(f"{line} → {dest}")
        if a.no_abstract and not nfull and s["abstract_only"]:
            print(f"  {slug}: no full-text batches left: plan the final round now, without --no-abstract "
                  f"({s['abstract_only']} works go to abstract / metadata batches)")
    sys.exit(rc)


if __name__ == "__main__":
    main()
