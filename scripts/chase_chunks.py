#!/usr/bin/env python3
"""
补搜（T3.3）的分块计划：从 INDEX.md 和 works.json 选出还没有开放全文的作品，算好每篇 PDF 的确切目标路径，切成块。
team-chase.js 的 Plan 阶段跑它（以前由 agent 现写 Python 做同样的事）；也可以手工跑，看这一轮要补搜多少。

用法:
    python3 scripts/chase_chunks.py <成员目录> --out <scratch>/chase/<slug>.json --date YYYY-MM-DD
                                    [--chunk-size 20] [--skip-ids S012,S090]

选择规则（与 team-chase.js 一致）:
    选 INDEX.md 里 Full text = no-oa、Role ≠ skip 的作品；排除并按原因计数：dup_of 非空；kind 为 patent / talk；
    kind 为 other 且既没有 DOI 也没有 venue（Scholar 的 other 行多是残片）；书的开放部分（Venue = book material，
    B### 行，由 team-increment.js 处理）；--skip-ids 指定的。
    每篇给出 {"id","year","title","authors","venue","doi","kind","urls","target"}；target 是 acquire_fulltexts.py
    认得的 PDF 路径（papers/<slug>.pdf）。书（kind book）排在最后。
    works.json 里有、INDEX.md 里没有的作品说明 acquire_fulltexts.py 还没在当前的 works.json 上跑过：报问题，不分块。

输出:
    --out 写 JSON 列表（每块一个列表）；标准输出打印一行 JSON 摘要:
    {"chunk_file", "works", "chunks", "books", "next_run", "excluded": [{"reason", "count"}], "problems": [...]}
    next_run = 1 + papers/ 里当天已有的 abstracts-chase-<date>-r<N>-*.json 的最大 N（没有就是 1），
    这一轮的补搜 agent 写 abstracts-chase-<date>-r<next_run>-<块>.json，不会覆盖之前没合并的文件。
    有 problems 时退出码 1。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from acquire_fulltexts import read_index, slug  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="补搜分块计划（T3.3）")
    ap.add_argument("member_dir")
    ap.add_argument("--out", required=True, help="分块 JSON 写到这里（如 <scratch>/chase/<slug>.json）")
    ap.add_argument("--date", required=True, help="补搜日期 YYYY-MM-DD（摘要文件名用）")
    ap.add_argument("--chunk-size", type=int, default=20)
    ap.add_argument("--skip-ids", default="", help="不补搜的作品（逗号分隔）")
    a = ap.parse_args()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", a.date):
        sys.exit("❌ --date must be YYYY-MM-DD")
    sk = Path(a.member_dir)
    papers = sk / "references/sources/papers"
    wj = sk / "references/sources/publications/works.json"
    problems, excluded = [], {}
    if not wj.exists() or not (papers / "INDEX.md").exists():
        problems.append(f"missing {'works.json' if not wj.exists() else 'papers/INDEX.md'}: run team-harvest.js and "
                        f"acquire_fulltexts.py first")
        print(json.dumps({"chunk_file": "", "works": 0, "chunks": 0, "books": 0, "next_run": 1, "excluded": [],
                          "problems": problems}))
        sys.exit(1)
    works = {w["id"]: w for w in json.loads(wj.read_text(encoding="utf-8"))["works"]}
    index = read_index(papers / "INDEX.md")
    skip = {x.strip() for x in a.skip_ids.split(",") if x.strip()}
    unknown = sorted(skip - set(works))
    if unknown:
        problems.append(f"--skip-ids not in works.json: {', '.join(unknown)}")
    missing = [i for i, w in works.items() if not w.get("dup_of") and w.get("title") and i not in index]
    if missing:
        problems.append(f"{len(missing)} works of works.json are not in INDEX.md (e.g. {', '.join(missing[:5])}): "
                        f"acquire_fulltexts.py has not run on the current works.json; run it, then plan again")

    def drop(reason):
        excluded[reason] = excluded.get(reason, 0) + 1

    picked = []
    for wid, w in works.items():
        if w.get("dup_of"):
            drop("duplicate (dup_of set)")
            continue
        row = index.get(wid)
        if not row or row.get("Full text") != "no-oa" or row.get("Role") == "skip":
            continue
        kind = w.get("kind") or ""
        if wid in skip:
            drop("--skip-ids")
        elif kind in ("patent", "talk"):
            drop(f"kind {kind}")
        elif kind == "other" and not w.get("doi") and not w.get("venue"):
            drop("kind other without DOI or venue")
        elif row.get("Venue") == "book material":
            drop("book material (B rows; team-increment.js)")
        else:
            picked.append({"id": wid, "year": w.get("year"), "title": w.get("title"), "authors": w.get("authors"),
                           "venue": w.get("venue"), "doi": w.get("doi"), "kind": kind, "urls": w.get("urls") or [],
                           "target": str((papers / f"{slug(w)}.pdf").resolve())})
    picked.sort(key=lambda x: (x["kind"] == "book", str(x["year"] or 9999), x["id"]))
    size = max(1, a.chunk_size)
    chunks = [] if missing else [picked[i:i + size] for i in range(0, len(picked), size)]
    runs = [int(m.group(1)) for f in papers.glob(f"abstracts-chase-{a.date}-r*-*.json")
            if (m := re.match(rf"abstracts-chase-{re.escape(a.date)}-r(\d+)-", f.name))]
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(chunks, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"chunk_file": str(out.resolve()), "works": 0 if missing else len(picked), "chunks": len(chunks),
                      "books": 0 if missing else sum(1 for x in picked if x["kind"] == "book"),
                      "next_run": max(runs, default=0) + 1,
                      "excluded": [{"reason": k, "count": v} for k, v in sorted(excluded.items())],
                      "problems": problems}, ensure_ascii=False))
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
