#!/usr/bin/env python3
"""
按论文卡片回填 INDEX.md 的 Read 列（研究Skill · 深读阶段用）。

读 <skill目录>/references/research/cards/*.digest.json 的 read_level：
full → carded · partial → skimmed · abstract → abstract · metadata → metadata · unreadable → unreadable。
同一篇有多张卡片时取读得最深的一张。

用法:
    python3 mark_read_from_cards.py <skill目录>
"""

import json
import re
import sys
from pathlib import Path

RANK = ["—", "unreadable", "metadata", "abstract", "skimmed", "carded"]
MAP = {"full": "carded", "partial": "skimmed", "abstract": "abstract", "metadata": "metadata", "unreadable": "unreadable"}


def main():
    sk = Path(sys.argv[1])
    index = sk / "references/sources/papers/INDEX.md"
    level = {}
    for dj in sorted((sk / "references/research/cards").glob("*.digest.json")):
        for c in json.loads(dj.read_text(encoding="utf-8")):
            new = MAP.get(c.get("read_level", ""), "—")
            if RANK.index(new) >= RANK.index(level.get(c["id"], "—")):
                level[c["id"]] = new
    out, counts = [], {}
    for line in index.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
        if len(cells) == 12 and cells[0] != "#" and not set(cells[0]) <= {"-"}:
            if cells[1] in level:
                cells[11] = level[cells[1]]
                line = "| " + " | ".join(cells) + " |"
            counts[cells[11]] = counts.get(cells[11], 0) + 1
        out.append(line)
    index.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{sk.name}: {counts} · works with cards: {len(level)}")


if __name__ == "__main__":
    main()
