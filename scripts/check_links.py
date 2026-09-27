#!/usr/bin/env python3
"""
校验 Markdown 文档里的相对链接与锚点（Skill / 团队交付前的死链闸门）。

对给定的文件或目录（递归找 *.md）扫描所有 `](目标)` 形式的链接，跳过 http(s)://、mailto: 等带协议的链接：
    文件   目标文件或目录必须存在（相对所在文件解析；以 / 开头的相对 git 仓库根解析）
    锚点   目标是 .md 且带 #锚点 时，锚点必须等于某个标题的 GitHub slug，
           或文档里的 <a id="..."> / <a name="...">；同文件的 (#锚点) 链接同样校验
GitHub slug 规则：小写；去掉除 - 和 _ 以外的标点与符号；空格变 -；中日韩文字保留；
重名标题依次加 -1、-2。代码块、行内代码、HTML 注释和 YAML front matter 里的内容不算链接也不算标题。

默认排除 */private/* 和 */cards/*，--exclude 可再追加（fnmatch 模式，匹配「相对于所给目录」的路径，
前面补 / 后也会再试一次，所以 */private/* 也能命中顶层的 private/）。排除只作用于目录递归，
直接点名的文件总会检查；--no-default-excludes 取消两条默认排除。

研究团队的脚手架（scripts/new_team.py 刚铺好、T1 还没跑）：团队 README 的成员表按约定链到 <成员>/SKILL.md，
而成员的 SKILL.md 由 T1 写。这种链接记为 pending，单列一行、不算坏链。条件全部满足才算：目标文件名是 SKILL.md；
它所在的文件夹存在，并且列在再上一级 team.json 的 members（slug）里；这位成员的 references/research/ 存在但
还没有任何 .md（T1 一开始就写 01–06 调研笔记，所以 T1 开始后仍缺 SKILL.md 就是坏链）。--strict 把 pending 也算坏链。

用法:
    python3 check_links.py <文件或目录>... [--exclude GLOB]... [--no-default-excludes] [--strict]

输出:
    每条坏链一行：<文件>: <链接目标> (missing file|missing anchor)
    每条 pending 一行：· <文件>: <链接目标> (pending: ...)
    最后一行汇总：✅/❌ N files checked, M broken links[ · K pending ...]；有坏链时退出码为 1，路径不存在为 2。
"""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
from fnmatch import fnmatch
from pathlib import Path
from urllib.parse import unquote

DEFAULT_EXCLUDES = ["*/private/*", "*/cards/*"]
MD_SUFFIXES = {".md", ".markdown"}
PENDING = "pending"   # check_file 里 why 以此开头：新铺的团队里还没写的成员 SKILL.md（见文件头）

FENCE_RE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
ATX_RE = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?(?:[ \t]+#+)?[ \t]*$")
SETEXT_RE = re.compile(r"^ {0,3}(?:=+|-+)[ \t]*$")
# 上一行是这些时，下一行的 === / --- 不构成 setext 标题
NOT_PARAGRAPH_RE = re.compile(r"^(?: {4}|\s*(?:$|#|>|\||<|[-*+][ \t]|\d+[.)][ \t]|[-*_]{3,}\s*$))")
LINK_RE = re.compile(
    r"\]\(\s*(<[^>\n]*>|(?:[^()\s]|\([^()\s]*\))+)"   # 目标：<...> 或允许一层括号
    r"(?:\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?\s*\)"  # 可选 title
)
HTML_ANCHOR_RE = re.compile(r"<[a-zA-Z][\w-]*\b[^>]*?\s(?:id|name)\s*=\s*[\"']([^\"']+)[\"']", re.I)
CODE_SPAN_RE = re.compile(r"(`+)(?!`).*?(?<!`)\1(?!`)")
COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
SCHEME_RE = re.compile(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|//)")


def prose_lines(text: str) -> list[str]:
    """按行返回正文：front matter、围栏代码块、HTML 注释都换成空白（保留行数）。"""
    lines = text.splitlines()
    start = 0
    if lines and lines[0].strip() == "---":
        for j in range(1, len(lines)):
            if lines[j].strip() in ("---", "..."):
                start = j + 1
                break
    out = [""] * start
    fence = None
    for line in lines[start:]:
        if fence:
            s = line.strip()
            if s and set(s) == {fence[0]} and len(s) >= len(fence):
                fence = None
            out.append("")
            continue
        m = FENCE_RE.match(line)
        if m:
            fence = m.group(1)
            out.append("")
        else:
            out.append(line)
    joined = COMMENT_RE.sub(lambda m: re.sub(r"[^\n]", " ", m.group()), "\n".join(out))
    return joined.split("\n")


def heading_texts(lines: list[str]):
    for i, line in enumerate(lines):
        m = ATX_RE.match(line)
        if m:
            yield m.group(2) or ""
        elif SETEXT_RE.match(line) and i > 0 and not NOT_PARAGRAPH_RE.match(lines[i - 1]) \
                and not SETEXT_RE.match(lines[i - 1]):
            yield lines[i - 1]


def slugify(heading: str) -> str:
    """GitHub 风格的标题锚点：先去掉 Markdown/HTML 标记取可见文字，再按 github-slugger 规则。"""
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", heading)          # 图片不进可见文字
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)            # [文字](链接) → 文字
    t = re.sub(r"\[([^\]]*)\]\[[^\]]*\]", r"\1", t)           # [文字][ref] → 文字
    t = re.sub(r"<[^>]+>", "", t)                             # HTML 标签
    t = t.replace("`", "")
    t = re.sub(r"(?<!\w)_+|_+(?!\w)", "", t)                  # _强调_ 的下划线；词内的 snake_case 保留
    t = html.unescape(t).strip().lower()
    t = re.sub(r"[^\w\- ]", "", t)                            # \w 含中日韩文字、数字、_
    return t.replace(" ", "-")


class Checker:
    def __init__(self):
        self.anchor_cache: dict[Path, set[str]] = {}
        self.root_cache: dict[Path, Path] = {}
        self.team_cache: dict[Path, set[str]] = {}

    def team_members(self, team_dir: Path) -> set[str]:
        """team_dir/team.json 里成员的 slug；没有或读不了时为空集。"""
        if team_dir not in self.team_cache:
            slugs: set[str] = set()
            try:
                cfg = json.loads((team_dir / "team.json").read_text(encoding="utf-8"))
                ms = cfg.get("members") if isinstance(cfg, dict) else None
                slugs = {m["slug"] for m in ms or [] if isinstance(m, dict) and isinstance(m.get("slug"), str)}
            except (OSError, UnicodeDecodeError, ValueError):
                pass
            self.team_cache[team_dir] = slugs
        return self.team_cache[team_dir]

    def pending_member(self, target: Path) -> str | None:
        """target 是新铺团队里还没写的成员 SKILL.md（T1 还没开始）时返回成员 slug，否则 None。"""
        target = target.resolve()
        member = target.parent
        if target.name != "SKILL.md" or not member.is_dir():
            return None
        research = member / "references" / "research"
        if not research.is_dir() or any(f.is_file() and f.suffix.lower() in MD_SUFFIXES for f in research.rglob("*")):
            return None
        return member.name if member.name in self.team_members(member.parent) else None

    def anchors(self, path: Path) -> set[str]:
        key = path.resolve()
        if key not in self.anchor_cache:
            lines = prose_lines(path.read_text(encoding="utf-8", errors="replace"))
            found: set[str] = set()
            occurrences: dict[str, int] = {}
            for h in heading_texts(lines):
                base = slug = slugify(h)
                while slug in occurrences:                    # 与 github-slugger 相同的重名处理
                    occurrences[base] += 1
                    slug = f"{base}-{occurrences[base]}"
                occurrences[slug] = 0
                found.add(slug)
            found.update(HTML_ANCHOR_RE.findall("\n".join(lines)))
            self.anchor_cache[key] = found
        return self.anchor_cache[key]

    def repo_root(self, path: Path) -> Path:
        d = path.resolve().parent
        if d not in self.root_cache:
            root = next((p for p in [d, *d.parents] if (p / ".git").exists()), Path.cwd())
            self.root_cache[d] = root
        return self.root_cache[d]

    def check_file(self, f: Path) -> list[tuple[str, str]]:
        bad = []
        for line in prose_lines(f.read_text(encoding="utf-8", errors="replace")):
            for m in LINK_RE.finditer(CODE_SPAN_RE.sub(" ", line)):
                target = m.group(1)
                if target.startswith("<"):
                    target = target[1:-1].strip()
                if not target or SCHEME_RE.match(target):
                    continue
                path_part, _, frag = target.partition("#")
                path_part = path_part.split("?", 1)[0]
                if path_part:
                    base = self.repo_root(f) if path_part.startswith("/") else f.parent
                    cands = dict.fromkeys([unquote(path_part), path_part])
                    resolved = next((base / c.lstrip("/") for c in cands if (base / c.lstrip("/")).exists()), None)
                    if resolved is None:
                        slug = self.pending_member(base / next(iter(cands)).lstrip("/"))
                        bad.append((target, f"{PENDING}: {slug} has no SKILL.md yet; fresh scaffold, T1 writes it"
                                    if slug else "missing file"))
                        continue
                else:
                    resolved = f
                if frag and resolved.is_file() and resolved.suffix.lower() in MD_SUFFIXES:
                    frag = unquote(frag)
                    frag = frag[len("user-content-"):] if frag.startswith("user-content-") else frag
                    known = self.anchors(resolved)
                    if frag not in known and frag.lower() not in known:
                        bad.append((target, "missing anchor"))
        return bad


def collect(paths: list[str], excludes: list[str]) -> list[Path]:
    files: dict[Path, Path] = {}
    for arg in paths:
        p = Path(arg)
        if p.is_file():
            files.setdefault(p.resolve(), p)
        elif p.is_dir():
            for f in sorted(p.rglob("*")):
                if not f.is_file() or f.suffix.lower() not in MD_SUFFIXES:
                    continue
                rel = f.relative_to(p).as_posix()
                if any(fnmatch(rel, g) or fnmatch("/" + rel, g) for g in excludes):
                    continue
                files.setdefault(f.resolve(), f)
        else:
            print(f"❌ no such file or directory: {arg}", file=sys.stderr)
            sys.exit(2)
    return sorted(files.values(), key=lambda f: f.as_posix())


def display(f: Path) -> str:
    rel = os.path.relpath(f.resolve())
    return f.resolve().as_posix() if rel.startswith("..") else Path(rel).as_posix()


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    ap = argparse.ArgumentParser(description="检查 Markdown 相对链接与锚点")
    ap.add_argument("paths", nargs="+", help="Markdown 文件或目录（目录递归 *.md）")
    ap.add_argument("--exclude", action="append", default=[], metavar="GLOB",
                    help="目录递归时排除的 fnmatch 模式，可重复")
    ap.add_argument("--no-default-excludes", action="store_true",
                    help="不使用默认排除 " + " ".join(DEFAULT_EXCLUDES))
    ap.add_argument("--strict", action="store_true",
                    help="新铺团队里还没写的成员 SKILL.md（pending）也算坏链")
    a = ap.parse_args()

    excludes = ([] if a.no_default_excludes else DEFAULT_EXCLUDES) + a.exclude
    files = collect(a.paths, excludes)
    checker = Checker()
    broken = pending = 0
    for f in files:
        for target, why in checker.check_file(f):
            if why.startswith(PENDING) and not a.strict:
                print(f"· {display(f)}: {target} ({why})")
                pending += 1
            else:
                print(f"{display(f)}: {target} ({why})")
                broken += 1
    mark = "❌" if broken else "✅"
    tail = (f" · {pending} pending (member SKILL.md not written yet: T1 writes it; --strict counts these as broken)"
            if pending else "")
    print(f"{mark} {len(files)} files checked, {broken} broken links{tail}")
    sys.exit(1 if broken else 0)


if __name__ == "__main__":
    main()
