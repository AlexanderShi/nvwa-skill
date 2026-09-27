#!/usr/bin/env python3
"""
校验论文卡片里的原文摘录（研究Skill · 全文深读的质量闸门）。

读取 <skill目录>/references/research/cards/*.digest.json 中每篇论文的 quotes，
在对应全文 txt（references/sources/papers/txt/<ID>-*.txt）或 abstracts.json 里查找原文。
比较前统一：Unicode 规范化、连字（ﬁ→fi）、行末连字符断词、引号与破折号、空白。

用法:
    python3 verify_card_quotes.py <skill目录> [--show N]

输出每张卡片的通过/失败数；失败的摘录需要改成原文或去掉引号标为转述。
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "")
    s = re.sub(r"\[\[page \d+\]\]", " ", s)
    s = s.replace("\f", " ")
    s = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", s)          # hyphenation at line end
    s = re.sub(r"[‐-―−]", "-", s)           # dashes/minus
    s = re.sub(r"[‘’‚‛`´]", "'", s)
    s = re.sub(r"[“”„‟]", '"', s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()


def squash(s: str) -> str:
    """更宽松的比较：只保留字母数字（公式抽取常丢空格/符号）。"""
    return re.sub(r"[^a-z0-9]+", "", s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("skill_dir")
    ap.add_argument("--show", type=int, default=20)
    a = ap.parse_args()

    sk = Path(a.skill_dir)
    txt_dir = sk / "references/sources/papers/txt"
    abs_path = sk / "references/sources/papers/abstracts.json"
    abstracts = json.loads(abs_path.read_text(encoding="utf-8")) if abs_path.exists() else {}
    cache: dict[str, tuple[str, str]] = {}

    def source(pid: str) -> tuple[str, str]:
        if pid not in cache:
            files = sorted(txt_dir.glob(f"{pid}-*.txt"))
            text = files[0].read_text(encoding="utf-8", errors="replace") if files else ""
            text += "\n" + (abstracts.get(pid) or "")
            n = norm(text)
            cache[pid] = (n, squash(n))
        return cache[pid]

    total = ok = loose = 0
    failures = []
    for dj in sorted((sk / "references/research/cards").glob("*.digest.json")):
        try:
            cards = json.loads(dj.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"❌ {dj.name}: invalid JSON ({e})")
            continue
        for c in cards:
            for q in c.get("quotes") or []:
                text = q.get("text") if isinstance(q, dict) else str(q)
                if not text:
                    continue
                total += 1
                n, sq = source(c.get("id", ""))
                qn = norm(text).strip("\"' .…")
                parts = [p.strip() for p in re.split(r"\s*(?:\.\.\.|…|\[\.\.\.\])\s*", qn) if len(p.strip()) > 3]
                if parts and all(p in n for p in parts):
                    ok += 1
                elif parts and all(squash(p) in sq for p in parts):
                    loose += 1
                else:
                    failures.append((dj.name, c.get("id"), q.get("page") if isinstance(q, dict) else "", text))

    print(f"quotes: {total} · exact {ok} · match ignoring spacing/symbols {loose} · NOT FOUND {len(failures)}")
    for f in failures[: a.show]:
        print(f"  ✗ {f[0]} {f[1]} p.{f[2]}: {f[3][:160]}")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
