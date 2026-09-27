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
                                   [--core-ids ID,..] [--skip-ids ID,..] [--no-abstract] > batches.json

多轮深读：后续轮次用 --round 2 --exclude round1.json（已分派或已有卡片的论文不再分派），
只分派新找到全文的论文；最后一轮再去掉 --no-abstract，给剩下的写摘要级卡片。
"""

import argparse
import json
import re
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


def main():
    ap = argparse.ArgumentParser(description="为全文深读分配角色并切分阅读批次")
    ap.add_argument("skill_dir")
    ap.add_argument("--core-top", type=int, default=25)
    ap.add_argument("--recent", type=int, default=2024)
    ap.add_argument("--core-pages", type=int, default=110)
    ap.add_argument("--supp-pages", type=int, default=220)
    ap.add_argument("--abs-size", type=int, default=30)
    ap.add_argument("--round", type=int, default=1)
    ap.add_argument("--core-ids", default="")
    ap.add_argument("--skip-ids", default="")
    ap.add_argument("--exclude", default="", help="逗号分隔：之前轮次的批次JSON，其中的论文视为已分派")
    ap.add_argument("--no-abstract", action="store_true")
    a = ap.parse_args()

    skill = Path(a.skill_dir)
    papers = skill / "references/sources/papers"
    index = papers / "INDEX.md"
    rows, pre, post = read_rows(index)
    works = {w["id"]: w for w in json.loads((skill / "references/sources/publications/works.json").read_text())["works"]}
    skill_raw = (skill / "SKILL.md").read_text(encoding="utf-8").lower()
    skill_norm = norm(skill_raw)
    txt_files = {p.name.split("-")[0]: p for p in (papers / "txt").glob("*.txt")}
    core_ids = {x for x in a.core_ids.split(",") if x}
    skip_ids = {x for x in a.skip_ids.split(",") if x}

    done, carded = set(), set()  # 已有全文卡片或已分派的论文；已有任何卡片的论文
    for dj in (skill / "references/research/cards").glob("*.digest.json"):
        try:
            cards = json.loads(dj.read_text())
            done |= {d["id"] for d in cards if d.get("read_level") not in ("abstract", "metadata")}
            carded |= {d["id"] for d in cards}
        except (json.JSONDecodeError, KeyError):
            pass
    for f in [x for x in a.exclude.split(",") if x]:
        for b in json.loads(Path(f).read_text())["batches"]:
            if b["mode"] != "abstract":
                done |= {p["id"] for p in b["papers"]}

    def cites(r):
        return int(r["Cites"]) if r["Cites"].isdigit() else 0

    def pages(r):
        return int(r["Pages"]) if r["Pages"].isdigit() else 30

    top = {r["ID"] for r in sorted(rows, key=lambda r: -cites(r))[: a.core_top]}
    for r in rows:
        w = works.get(r["ID"], {})
        if r["ID"] in skip_ids:
            r["Role"] = "skip"
        if r["Role"] == "skip" or r["Read"] not in ("—", ""):
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
        bid = f"{kind[0]}{n:02d}" if a.round == 1 else f"{kind[0]}{a.round}-{n:02d}"
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
               "skip": sum(1 for r in rows if r["Role"] == "skip"),
               "batches": {k: sum(1 for b in batches if b["mode"] == k) for k in ("core", "supplement", "book", "abstract")}}
    print(json.dumps({"summary": summary, "batches": batches}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
