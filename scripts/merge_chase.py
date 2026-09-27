#!/usr/bin/env python3
"""
合并「补漏」（chase）工作流的产出：把 papers/abstracts-chase-*.json 里找到的摘要并进
abstracts.json / abstract-sources.json，再重跑 acquire_fulltexts.py 给 chase 放进 papers/ 的全文建索引、抽文本，
报告哪些论文新有了全文（研究Skill · 全文深读 T3.3 之后）。

chase 分块文件格式（每个 agent 一份，JSON 对象，键是作品ID）:
    {"S012": "摘要原文……", "S012__src": "https://出处（落地页 / Crossref / 仓库）", "S034": null, ...}
    值为 "" 或 null 表示没找到，跳过；<id>__src 记摘要出处，只在这条摘要确实被并入时写进 abstract-sources.json。

规则:
    · 已有的摘要从不覆盖（不同文本只计数，不替换），所以重复运行是安全的
    · 坏文件（不是合法 JSON、不是对象）报告并保留，一条也不并
    · 文件里个别坏条目（值不是字符串；ID 不在 works.json / INDEX.md 里）报告并保留整个文件，其余条目照常并入
    · 全部条目都处理干净的分块文件并完后删除
    · 最后（除非 --no-acquire）重跑 scripts/acquire_fulltexts.py <skill目录>，比较 INDEX.md 的 Full text 列与 txt/，
      列出新有全文的ID

用法:
    python3 merge_chase.py <skill目录> [--no-acquire] [--dry-run]

输出:
    合并统计、每个问题一行、新全文的ID；最后一行汇总：✅/❌ …；有坏文件/坏条目或 acquire 失败时退出码为 1，路径不存在为 2。
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHUNK_GLOB = "abstracts-chase-*.json"


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")  # 与 acquire_fulltexts.py 同格式


def index_status(papers: Path) -> dict[str, str]:
    """INDEX.md → {ID: Full text 列}（acquire_fulltexts.py 的 12 列格式）。"""
    out: dict[str, str] = {}
    path = papers / "INDEX.md"
    if not path.exists():
        return out
    header = None
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
        if not cells:
            continue
        if cells[0] == "#":
            header = cells
        elif header and len(cells) == len(header) and not set(cells[0]) <= {"-"}:
            row = dict(zip(header, cells))
            out[row.get("ID", "")] = row.get("Full text", "")
    return out


def txt_ids(papers: Path) -> set[str]:
    return {p.name.split("-")[0] for p in (papers / "txt").glob("*.txt")} if (papers / "txt").is_dir() else set()


def known_ids(skill: Path, papers: Path) -> set[str]:
    ids = set(index_status(papers))
    works = skill / "references" / "sources" / "publications" / "works.json"
    if works.exists():
        try:
            ids |= {str(w.get("id")) for w in json.loads(works.read_text(encoding="utf-8")).get("works") or []
                    if isinstance(w, dict) and w.get("id")}
        except (json.JSONDecodeError, AttributeError):
            pass
    ids.discard("")
    return ids


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skill_dir", help="研究Skill目录（含 references/sources/papers/）")
    ap.add_argument("--no-acquire", action="store_true", help="只合并摘要，不重跑 acquire_fulltexts.py")
    ap.add_argument("--dry-run", action="store_true", help="只报告会合并什么，不写文件、不删分块、不跑 acquire")
    a = ap.parse_args()

    skill = Path(a.skill_dir)
    papers = skill / "references" / "sources" / "papers"
    if not papers.is_dir():
        print(f"❌ no papers folder: {papers}", file=sys.stderr)
        sys.exit(2)
    abs_path, src_path = papers / "abstracts.json", papers / "abstract-sources.json"
    try:
        abstracts = load_json(abs_path, {})
        sources = load_json(src_path, {})
    except json.JSONDecodeError as e:
        print(f"❌ cannot read {abs_path.name} / {src_path.name}: {e} — fix it before merging")
        sys.exit(1)
    if not isinstance(abstracts, dict) or not isinstance(sources, dict):
        print(f"❌ {abs_path.name} / {src_path.name} must be JSON objects {{id: text}} — fix it before merging")
        sys.exit(1)
    known = known_ids(skill, papers)

    chunks = sorted(papers.glob(CHUNK_GLOB))
    added: list[str] = []
    kept_existing: list[str] = []   # 已有摘要、chase 给了不同文本 → 不覆盖
    empty = same = 0
    problems: list[str] = []
    kept_files: list[Path] = []
    merged_files: list[Path] = []
    for f in chunks:
        try:
            data = json.loads(f.read_text(encoding="utf-8-sig"))  # 容忍 BOM（有的编辑器 / 工具会加）
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            problems.append(f"{f.name}: invalid JSON ({e}) — kept")
            kept_files.append(f)
            continue
        if not isinstance(data, dict):
            problems.append(f"{f.name}: not a JSON object ({type(data).__name__}) — kept")
            kept_files.append(f)
            continue
        bad = False
        for key, val in data.items():
            if key.endswith("__src"):
                if key[:-5] not in data:
                    print(f"  · {f.name}: {key} has no abstract in this file (ignored)")
                continue
            if val is None or (isinstance(val, str) and not val.strip()):
                empty += 1
                continue
            if not isinstance(val, str):
                problems.append(f"{f.name}: {key}: abstract is {type(val).__name__}, not a string")
                bad = True
                continue
            if known and key not in known:
                problems.append(f"{f.name}: {key}: id not in works.json / INDEX.md")
                bad = True
                continue
            src = data.get(key + "__src")
            if src is not None and not isinstance(src, str):
                problems.append(f"{f.name}: {key}__src is {type(src).__name__}, not a string")
                bad = True
                continue
            text = val.strip()
            if abstracts.get(key):
                if str(abstracts[key]).strip() == text:
                    same += 1
                else:
                    kept_existing.append(key)
                continue
            abstracts[key] = text
            if src and src.strip():
                sources[key] = src.strip()
            added.append(key)
        (kept_files if bad else merged_files).append(f)
        if bad:
            problems.append(f"{f.name}: kept (fix the entries above and rerun; merging is idempotent)")

    print(f"chunks: {len(chunks)} · merged {len(merged_files)} · kept {len(kept_files)}")
    print(f"abstracts: +{len(added)} new ({len(abstracts)} total) · {len(kept_existing)} not overwritten"
          f" · {same} already identical · {empty} empty")
    if added:
        print("  added: " + ", ".join(added))
    if kept_existing:
        print("  existing abstract kept (chase text differs): " + ", ".join(kept_existing))
    for p in problems:
        print(f"  ✗ {p}")

    if not a.dry_run:
        if added:
            dump_json(abs_path, abstracts)
            if sources or src_path.exists():
                dump_json(src_path, sources)
        for f in merged_files:
            f.unlink()

    acquire_note = "acquisition skipped"
    acquire_failed = False
    if not (a.no_acquire or a.dry_run):
        before_idx, before_txt = index_status(papers), txt_ids(papers)
        cmd = [sys.executable, str(HERE / "acquire_fulltexts.py"), str(skill)]
        print("running: " + " ".join(cmd))
        out = subprocess.run(cmd, capture_output=True, text=True)
        tail = [line for line in out.stdout.strip().splitlines() if line.strip()][-3:]
        for line in tail:
            print("  " + line)
        if out.returncode != 0:
            acquire_failed = True
            print("  ✗ acquire_fulltexts.py exit " + str(out.returncode) + ": " + out.stderr.strip()[-800:])
            acquire_note = "acquisition failed"
        else:
            after_idx, after_txt = index_status(papers), txt_ids(papers)
            new_txt = sorted(i for i in after_txt - before_txt)
            new_idx = sorted(i for i, st in after_idx.items()
                             if st in ("txt", "pdf") and before_idx.get(i) not in ("txt", "pdf"))
            pdf_only = sorted(i for i, st in after_idx.items() if st == "pdf")
            fresh = sorted(set(new_txt) | set(new_idx))
            print("new full texts: " + (", ".join(fresh) if fresh else "none"))
            if pdf_only:
                print("  pdf without extracted text (scan/garbled; see OCR notes): " + ", ".join(pdf_only))
            acquire_note = f"{len(fresh)} new full texts"

    n_bad = len(kept_files) + (1 if acquire_failed else 0)
    mark = "❌" if n_bad else "✅"
    dry = " (dry run, nothing written)" if a.dry_run else ""
    print(f"{mark} {skill}: +{len(added)} abstracts from {len(merged_files)} chunk files, "
          f"{len(kept_files)} kept with problems, {acquire_note}{dry}")
    sys.exit(1 if n_bad else 0)


if __name__ == "__main__":
    main()
