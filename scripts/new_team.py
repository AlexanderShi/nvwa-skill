#!/usr/bin/env python3
"""
新建研究团队（多位研究者的研究Skill + 圆桌）：起草 team.json，按模板铺团队目录，或给已有团队加成员。

三种用法:
    1) 起草 team.json（schema 1）
       python3 new_team.py --init <团队slug> --field "..." --members "Name One;Name Two" [--title "..."]
                           [--language English] [--out PATH] [--force]
       成员 slug 由姓名生成（去重音、小写、非字母数字变 -；中文名保留原字），surname 取最后一个词（跳过 Jr./II 等），
       scholar / dblp / orcid / homepage / hint 留空，living=true，student_mode=false，created=今天，
       roundtable=<去掉 -team 的团队slug>-roundtable。默认写到 <--root>/<团队slug>/team.json，已存在不覆盖（--force 覆盖）。
       填好 scholar id 和 hint 后做第 2 步。

    2) 按 team.json 铺团队目录
       python3 new_team.py <team.json> [--root DIR] [--templates DIR] [--force] [--dry-run] [--set NAME=VALUE]...
       --root 默认 <仓库>/product，团队目录 = <--root>/<team.json 的 team>；--templates 默认 <仓库>/references/team-templates。
       生成（与 product/dfo-team/ 相同的布局）:
           <团队>/team.json                                       复制进来
           <团队>/README.md                                       ← team-README.md
           <团队>/DEEP-READING.md                                 ← DEEP-READING.md（标为未开始）
           <团队>/<roundtable>/SKILL.md                           ← roundtable-SKILL.md
           <团队>/<成员>/references/research/                     空目录（.gitkeep）；01–06 调研笔记由 T1 写
           <团队>/<成员>/references/sources/RESOURCES.md          ← member-RESOURCES.md
           <团队>/<成员>/references/sources/{publications,papers,talks,essays,software}/   空目录（.gitkeep）
           <团队>/<成员>/references/sources/private/README.md     ← private-README.md（private/ 其余内容被 git 忽略）
       成员的 SKILL.md 不生成（T1 写）。已存在的文件一律保留，--force 才覆盖；重跑只补缺的部分。

    3) 给已有团队加成员（先把他写进团队目录里的 team.json 的 members）
       python3 new_team.py <team.json> --add-member <slug> [--add-member <slug>]... [--root DIR] [--templates DIR] [--force] [--dry-run]
       只铺这位成员的目录，并把他的一行插进 README.md 的成员表：有 <!-- members:start --> / <!-- members:end -->
       标记时把 {{MEMBER_TABLE}} 格式的一行插在 end 标记前；没有标记时照最后一个链接到成员文件夹的表格行造一行
       （同样的列数，slug / 姓名换成新成员，其余格 [TODO]）插在它后面；都找不到就在文末追加一条 [TODO]。
       圆桌 SKILL.md 和 DEEP-READING.md 不改，只在「下一步」里提醒。

模板占位符（简单字符串替换，{{NAME}}）:
    团队级   {{TEAM_SLUG}} {{TEAM_TITLE}} {{FIELD}} {{LANGUAGE}} {{DATE}}（今天） {{ROUNDTABLE_SLUG}}
             {{MEMBER_TABLE}}（每位成员一行 | [Name](slug/SKILL.md) | lens: [TODO] | 状态 |）
             {{MEMBER_LIST}}（逗号分隔的姓名） {{MEMBER_COUNT}}
    成员级   以上全部，加 {{MEMBER_NAME}} {{MEMBER_SLUG}} {{MEMBER_SURNAME}}
             {{SCHOLAR_URL}}（https://scholar.google.com/citations?user=<id>&hl=en；没有 id 时为 [TODO: …]）
    --set NAME=VALUE 可补充或覆盖。模板里出现未知占位符或落单的 {{ 算错误：列出来，一个文件也不写。
    需要研究才能填的内容在模板里写成 [TODO: …]，`grep -rn "TODO" product/<团队>` 列出所有待办。

输出:
    逐行列出 + 新建 / = 已存在保留 / ! 覆盖 / ~ 更新（加成员时的 README），每个写入的文件后标 [TODO 数；
    检查 git 是否忽略成员的 PDF、papers/txt/ 和 private/；最后打印「下一步」。
    最后一行汇总 ✅/❌；team.json 不合法、模板缺失或占位符有误时退出码 1，什么都不写。

示例:
    python3 scripts/new_team.py --init bo-team --field "Bayesian optimization" --members "Peter Frazier;Roman Garnett"
    python3 scripts/new_team.py product/bo-team/team.json
    python3 scripts/new_team.py product/bo-team/team.json --add-member andreas-krause
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
DEFAULT_ROOT = REPO / "product"
DEFAULT_TEMPLATES = REPO / "references" / "team-templates"

TEAM_TEMPLATES = [("team-README.md", "README.md"), ("DEEP-READING.md", "DEEP-READING.md"),
                  ("roundtable-SKILL.md", "{roundtable}/SKILL.md")]
MEMBER_TEMPLATES = [("member-RESOURCES.md", "references/sources/RESOURCES.md"),
                    ("private-README.md", "references/sources/private/README.md")]
MEMBER_DIRS = ["references/research"] + [f"references/sources/{d}" for d in
                                         ("publications", "papers", "talks", "essays", "software")]
MARK_START, MARK_END = "<!-- members:start -->", "<!-- members:end -->"
IGNORED_PROBES = ["references/sources/papers/x.pdf", "references/sources/papers/txt/x.txt",
                  "references/sources/private/x.md"]
TRACKED_PROBES = ["references/sources/private/README.md"]

PLACEHOLDER_RE = re.compile(r"\{\{\s*([A-Za-z0-9_]+)\s*\}\}")
SAFE_SLUG_RE = re.compile(r"^\w[\w.-]*$")
NAME_SUFFIXES = {"jr", "jr.", "sr", "sr.", "ii", "iii", "iv"}
TRANSLIT = str.maketrans({"ł": "l", "Ł": "L", "ø": "o", "Ø": "O", "đ": "d", "Đ": "D", "ı": "i", "ß": "ss",
                          "æ": "ae", "Æ": "AE", "œ": "oe", "Œ": "OE", "þ": "th", "ð": "d"})


def display(p: Path) -> str:
    rel = os.path.relpath(p.resolve())
    return p.resolve().as_posix() if rel.startswith("..") else Path(rel).as_posix()


def same_path(a: Path, b: Path) -> bool:
    return a.resolve() == b.resolve()


def today() -> str:
    return datetime.date.today().isoformat()


# ---------- --init ----------

def slugify(name: str) -> str:
    words = name.split()
    while len(words) > 1 and words[-1].strip(",").lower() in NAME_SUFFIXES:
        words.pop()
    s = unicodedata.normalize("NFKD", " ".join(words).translate(TRANSLIT))
    s = "".join(c for c in s if not unicodedata.combining(c)).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    if not slug:                                          # 中文等非拉丁姓名：保留原字
        slug = re.sub(r"[^\w]+", "-", unicodedata.normalize("NFKC", name).lower()).strip("-_")
    return slug


def surname_of(name: str) -> str:
    words = [w.strip(",") for w in name.split() if w.strip(",")]
    while len(words) > 1 and words[-1].lower() in NAME_SUFFIXES:
        words.pop()
    return words[-1] if words else name


def default_title(team: str) -> str:
    return " ".join(w.upper() if len(w) <= 3 else w.capitalize() for w in re.split(r"[-_]+", team) if w)


def init_team(a) -> int:
    team = a.init
    if not SAFE_SLUG_RE.match(team) or ".." in team:
        print(f"❌ 团队 slug 只能用字母、数字、- _ .：{team!r}")
        return 1
    names = [n.strip() for n in re.split(r"[;\n]", a.members or "") if n.strip()]
    if not names:
        print('❌ --members 为空（用分号分隔："Name One;Name Two"）')
        return 1
    for n in sorted({n for n in names if names.count(n) > 1}):
        print(f"⚠️ {n!r} 出现了 {names.count(n)} 次（同名的不同研究者要靠 hint 区分，否则删掉重复）")
    base = team[:-5] if team.endswith("-team") and len(team) > 5 else team
    roundtable = f"{base}-roundtable"
    members, used = [], {roundtable}
    for n in names:
        slug = slugify(n) or "member"
        s, k = slug, 2
        while s in used:
            s, k = f"{slug}-{k}", k + 1
        used.add(s)
        members.append({"slug": s, "name": n, "surname": surname_of(n), "living": True, "hint": "",
                        "scholar": "", "dblp": "", "orcid": "", "homepage": "", "chase_hints": [],
                        "student_mode": False})
    cfg = {"schema": 1, "team": team, "title": a.title or default_title(team), "field": a.field,
           "language": a.language, "created": today(), "roundtable": roundtable, "chase_hints": [],
           "members": members}
    out = Path(a.out) if a.out else Path(a.root) / team / "team.json"
    if out.exists() and not a.force:
        print(f"❌ {display(out)} 已存在，未覆盖（--force 覆盖）")
        return 1
    if a.dry_run:
        print(json.dumps(cfg, ensure_ascii=False, indent=1))
        print(f"✅ (dry run) 会写 {display(out)}（{len(members)} 位成员）")
        return 0
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("| slug | name | surname |\n|---|---|---|")
    for m in members:
        print(f"| {m['slug']} | {m['name']} | {m['surname']} |")
    print(f"roundtable: {roundtable}")
    print()
    print("下一步:")
    print(f"  1. 编辑 {display(out)}：每位成员填 scholar（Google Scholar 主页网址 citations?user=<id> 里的 id）、")
    print("     hint（单位、年代、代表作；harvest 与检索靠它区分同名者）、能找到的 dblp / orcid / homepage；")
    print("     核对 slug（会成为文件夹名）、surname、living、student_mode；按需写团队级与个人级 chase_hints（开放仓库线索）。")
    if not 3 <= len(members) <= 6:
        print(f"     注意：现在 {len(members)} 位；3–6 位视角互补、有公开分歧的研究者最合适。")
    root_opt = "" if same_path(Path(a.root), DEFAULT_ROOT) else f" --root {display(Path(a.root))}"
    print(f"  2. python3 {display(HERE / 'new_team.py')} {display(out)}{root_opt}      # 按模板铺团队目录")
    print(f"  3. 然后按 {display(REPO / 'references/research-team-playbook.md')} 往下走"
          f"（T1: {display(HERE / 'workflows/team-base-skills.js')}，启动方式见 {display(HERE / 'workflows/README.md')}）。")
    print(f"✅ wrote {display(out)} ({len(members)} members)")
    return 0


# ---------- team.json ----------

def load_config(path: Path) -> tuple[dict | None, list[str]]:
    try:
        cfg = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as e:
        return None, [f"{display(path)}: 读不了 JSON：{e}"]
    errs = []
    if not isinstance(cfg, dict):
        return None, [f"{display(path)}: 顶层必须是对象"]
    if cfg.get("schema") != 1:
        errs.append(f"schema 必须是 1（现在是 {cfg.get('schema')!r}）")
    for key in ("team", "title", "field", "roundtable"):
        if not isinstance(cfg.get(key), str) or not cfg.get(key).strip():
            errs.append(f"缺 {key}（非空字符串）")
    for key in ("team", "roundtable"):
        v = cfg.get(key)
        if isinstance(v, str) and v and (not SAFE_SLUG_RE.match(v) or ".." in v):
            errs.append(f"{key} {v!r} 不能当文件夹名（只用字母、数字、- _ .）")
    members = cfg.get("members")
    if not isinstance(members, list) or not members:
        errs.append("members 必须是非空列表")
        members = []
    seen = set()
    for i, m in enumerate(members):
        if not isinstance(m, dict):
            errs.append(f"members[{i}] 不是对象")
            continue
        slug, name = m.get("slug"), m.get("name")
        where = f"members[{i}]" + (f" ({slug})" if isinstance(slug, str) else "")
        if not isinstance(slug, str) or not SAFE_SLUG_RE.match(slug) or ".." in slug:
            errs.append(f"{where}: slug {slug!r} 不能当文件夹名")
        elif slug in seen:
            errs.append(f"{where}: slug 重复")
        elif slug == cfg.get("roundtable"):
            errs.append(f"{where}: slug 与 roundtable 同名")
        seen.add(slug)
        if not isinstance(name, str) or not name.strip():
            errs.append(f"{where}: 缺 name")
        for key in ("surname", "hint", "scholar", "dblp", "orcid", "homepage"):
            if key in m and not isinstance(m[key], str):
                errs.append(f"{where}: {key} 必须是字符串")
        for key in ("living", "student_mode"):
            if key in m and not isinstance(m[key], bool):
                errs.append(f"{where}: {key} 必须是 true/false")
        if "chase_hints" in m and not (isinstance(m["chase_hints"], list) and all(isinstance(x, str) for x in m["chase_hints"])):
            errs.append(f"{where}: chase_hints 必须是字符串列表")
    if "chase_hints" in cfg and not (isinstance(cfg["chase_hints"], list) and all(isinstance(x, str) for x in cfg["chase_hints"])):
        errs.append("chase_hints 必须是字符串列表")
    return cfg, [f"{display(path)}: {e}" for e in errs]


# ---------- 模板 ----------

def member_row(team_dir: Path, m: dict) -> str:
    stage = "T1 base skill" if (team_dir / m["slug"] / "SKILL.md").exists() else "T0 scaffold"
    if m.get("student_mode"):
        stage += " · student mode"
    return f"| [{m['name']}]({m['slug']}/SKILL.md) | lens: [TODO] | {stage} |"


def team_values(cfg: dict, team_dir: Path, extra: dict) -> dict:
    ms = cfg["members"]
    v = {"TEAM_SLUG": cfg["team"], "TEAM_TITLE": cfg["title"], "FIELD": cfg["field"],
         "LANGUAGE": cfg.get("language") or "English", "DATE": today(), "ROUNDTABLE_SLUG": cfg["roundtable"],
         "MEMBER_TABLE": "\n".join(member_row(team_dir, m) for m in ms),
         "MEMBER_LIST": ", ".join(m["name"] for m in ms), "MEMBER_COUNT": str(len(ms))}
    v.update(extra)
    return v


def member_values(base: dict, m: dict, extra: dict) -> dict:
    v = dict(base)
    sch = (m.get("scholar") or "").strip()
    v.update({"MEMBER_NAME": m["name"], "MEMBER_SLUG": m["slug"], "MEMBER_SURNAME": m.get("surname") or surname_of(m["name"]),
              "SCHOLAR_URL": f"https://scholar.google.com/citations?user={sch}&hl=en" if sch
              else "[TODO: Google Scholar profile URL]"})
    v.update(extra)
    return v


def template_problems(name: str, text: str, values: dict) -> list[str]:
    probs = []
    for i, line in enumerate(text.splitlines(), 1):
        unknown = [m.group(0) for m in PLACEHOLDER_RE.finditer(line) if m.group(1) not in values]
        stray = PLACEHOLDER_RE.sub("", line).count("{{")
        if unknown:
            probs.append(f"{name}:{i}: 未知占位符 {' '.join(unknown)}")
        if stray:
            probs.append(f"{name}:{i}: 落单的 {{{{（不是 {{{{NAME}}}} 形式）")
    return probs


def fill(text: str, values: dict) -> str:
    return PLACEHOLDER_RE.sub(lambda m: values.get(m.group(1), m.group(0)), text)


# ---------- 计划与执行 ----------

class Plan:
    def __init__(self, team_dir: Path, force: bool):
        self.team_dir, self.force = team_dir, force
        self.actions: list[tuple] = []       # (kind, path, content, label)
        self.errors: list[str] = []
        self.notes: list[str] = []

    def file(self, rel: str, content: str):
        self.actions.append(("file", self.team_dir / rel, content, rel))

    def dirs(self, member: str, rels: list[str]):
        self.actions.append(("dirs", self.team_dir / member, rels, member))

    def update(self, rel: str, content: str, why: str):
        self.actions.append(("update", self.team_dir / rel, content, f"{rel} ({why})"))

    def keep(self, rel: str, why: str):
        self.actions.append(("keep", self.team_dir / rel, None, f"{rel} ({why})"))


def row_like(line: str, nb: dict, m: dict, standard: str) -> str:
    """照着邻居成员的表格行造一行。邻居行是 {{MEMBER_TABLE}} 的格式（3 格、第一格链到 slug/SKILL.md）时直接用标准行；
    否则同样的列数：含邻居 slug 的格换成新 slug 与新姓名（没有全名时换姓），等于邻居姓名的格换成新姓名，其余格 [TODO]。"""
    cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
    if len(cells) == 3 and re.fullmatch(rf"\[[^\]]*\]\(\s*(?:\./)?{re.escape(nb['slug'])}/SKILL\.md\s*\)", cells[0]):
        return standard
    out = []
    for c in cells:
        if nb["slug"] in c:
            c = c.replace(nb["slug"], m["slug"])
            if nb.get("name") and nb["name"] in c:
                c = c.replace(nb["name"], m["name"])
            elif nb.get("surname") and m.get("surname"):
                c = c.replace(nb["surname"], m["surname"])
            out.append(c)
        elif c == nb.get("name"):
            out.append(m["name"])
        else:
            out.append("[TODO]")
    return "| " + " | ".join(out) + " |"


def member_link_re(slug: str) -> re.Pattern:
    """表格里链到成员文件夹的链接：](slug/…) 或 ](./slug/…)。"""
    return re.compile(rf"\]\(\s*(?:\./)?{re.escape(slug)}/")


def listed_in_table(text: str, slug: str) -> bool:
    rx = member_link_re(slug)
    return any(ln.lstrip().startswith("|") and rx.search(ln) for ln in text.split("\n"))


def insert_member_row(text: str, row: str, m: dict, others: list[dict]) -> tuple[str, str]:
    """有 members 标记时把标准行插在 end 标记前；否则照最后一个成员行的格式插在它后面；都没有就在文末追加 [TODO]。"""
    slug = m["slug"]
    lines = text.split("\n")
    if listed_in_table(text, slug) or f"({slug}/) to the member table" in text:
        return text, "already listed"
    if MARK_START in text and MARK_END in text and text.index(MARK_START) < text.index(MARK_END):
        end = next(i for i, ln in enumerate(lines) if MARK_END in ln)
        lines.insert(end, row)
        return "\n".join(lines), "row added before " + MARK_END
    last, nb = None, None
    for i, ln in enumerate(lines):
        if not ln.lstrip().startswith("|"):
            continue
        hit = next((o for o in others if member_link_re(o["slug"]).search(ln)), None)
        if hit:
            last, nb = i, hit
    if last is not None:
        lines.insert(last + 1, row_like(lines[last], nb, m, row))
        return "\n".join(lines), f"row added after {nb['slug']}'s row"
    tail = "" if text.endswith("\n") else "\n"
    return text + f"{tail}\n[TODO: add {m['name']} ({slug}/) to the member table: `{row}`]\n", \
        "no member table found, TODO appended"


def sync_team_json(plan: Plan, src: Path, cfg: dict, adding: list[str]):
    dest = plan.team_dir / "team.json"
    if not dest.exists():
        plan.file("team.json", src.read_text(encoding="utf-8"))
        return
    if dest.resolve() == src.resolve():
        plan.keep("team.json", "就是输入文件")
        return
    try:
        same = json.loads(dest.read_text(encoding="utf-8")) == cfg
    except (OSError, json.JSONDecodeError):
        same = False
    if same:
        plan.keep("team.json", "内容相同")
        return
    if plan.force:
        plan.file("team.json", src.read_text(encoding="utf-8"))
        return
    try:
        have = {m.get("slug") for m in json.loads(dest.read_text(encoding="utf-8")).get("members") or []}
    except (OSError, json.JSONDecodeError, AttributeError):
        have = set()
    missing = [s for s in adding if s not in have]
    if missing:
        plan.errors.append(f"{display(dest)} 里没有成员 {', '.join(missing)}，而且与 {display(src)} 不同："
                           f"把成员写进团队目录里的 team.json 再跑，或 --force 用 {display(src)} 覆盖它")
    else:
        plan.notes.append(f"⚠️ {display(dest)} 与 {display(src)} 不同，保留团队目录里的版本（--force 覆盖）")


def load_templates(tdir: Path, names: list[str], plan: Plan) -> dict:
    out = {}
    for n in names:
        p = tdir / n
        if p.is_file():
            out[n] = p.read_text(encoding="utf-8")
        else:
            plan.errors.append(f"缺模板 {display(p)}")
    return out


def build_plan(a, src: Path, cfg: dict, adding: list[str], extra: dict) -> Plan:
    team_dir = Path(a.root) / cfg["team"]
    plan = Plan(team_dir, a.force)
    slugs = [m["slug"] for m in cfg["members"]]
    if adding:
        if not team_dir.is_dir():
            plan.errors.append(f"团队目录 {display(team_dir)} 不存在：先不带 --add-member 跑一次")
        unknown = [s for s in adding if s not in slugs]
        if unknown:
            plan.errors.append(f"{display(src)} 的 members 里没有 {', '.join(unknown)}（先把他写进 team.json）")
    if src.parent.name != cfg["team"] and src.name == "team.json" and src.parent.parent.resolve() == Path(a.root).resolve():
        plan.notes.append(f"⚠️ {display(src)} 所在文件夹名与 team 字段 {cfg['team']!r} 不同，团队目录按 team 字段建")
    if src.parent.name == cfg["team"] and not same_path(src.parent, team_dir):
        plan.notes.append(f"⚠️ {display(src)} 在团队文件夹 {display(src.parent)} 里，但团队目录会建在 {display(team_dir)}；"
                          f"要铺在原处就加 --root {display(src.parent.parent)}")
    if not adding and not a.force and (team_dir / "README.md").is_file():
        text = (team_dir / "README.md").read_text(encoding="utf-8")
        unlisted = [m["slug"] for m in cfg["members"] if not listed_in_table(text, m["slug"])]
        if unlisted:
            plan.notes.append(f"⚠️ 已有的 README.md 成员表里没有 {', '.join(unlisted)}（重跑不改已存在的文件）："
                              f"用 --add-member {' --add-member '.join(unlisted)} 加行，圆桌 SKILL.md 也要补上")
    sync_team_json(plan, src, cfg, adding)
    tnames = ([] if adding else [t for t, _ in TEAM_TEMPLATES]) + [t for t, _ in MEMBER_TEMPLATES]
    templates = load_templates(Path(a.templates), tnames, plan)
    if plan.errors:
        return plan

    base = team_values(cfg, team_dir, extra)
    for t, _ in TEAM_TEMPLATES:
        if t in templates:
            plan.errors += template_problems(t, templates[t], base)
    probe = member_values(base, cfg["members"][0], extra)
    for t, _ in MEMBER_TEMPLATES:
        plan.errors += template_problems(t, templates[t], probe)
    if plan.errors:
        return plan

    if not adding:
        for t, dest in TEAM_TEMPLATES:
            plan.file(dest.format(roundtable=cfg["roundtable"]), fill(templates[t], base))
    for m in cfg["members"]:
        if adding and m["slug"] not in adding:
            continue
        mv = member_values(base, m, extra)
        plan.dirs(m["slug"], MEMBER_DIRS)
        for t, dest in MEMBER_TEMPLATES:
            plan.file(f"{m['slug']}/{dest}", fill(templates[t], mv))
    if adding:
        readme = team_dir / "README.md"
        if not readme.is_file():
            plan.notes.append(f"⚠️ {display(readme)} 不存在，成员表没有更新")
        else:
            text = readme.read_text(encoding="utf-8")
            hows = []
            for m in cfg["members"]:
                if m["slug"] not in adding:
                    continue
                others = [o for o in cfg["members"] if o["slug"] != m["slug"]]
                text, how = insert_member_row(text, member_row(team_dir, m), m, others)
                if how == "already listed":
                    plan.keep("README.md", f"已有 {m['slug']} 的行")
                else:
                    hows.append(f"{m['slug']}: {how}")
            if hows:
                plan.update("README.md", text, "; ".join(hows))
    return plan


def execute(plan: Plan, dry: bool) -> tuple[dict, int]:
    counts = {"created": 0, "kept": 0, "overwritten": 0, "updated": 0, "dirs": 0}
    todos = 0
    for kind, path, content, label in plan.actions:
        if kind == "dirs":
            new = []
            for rel in content:
                d = path / rel
                if not d.is_dir():
                    new.append(rel)
                if not dry:
                    d.mkdir(parents=True, exist_ok=True)
                    keep = d / ".gitkeep"
                    if not any(d.iterdir()):
                        keep.touch()
            counts["dirs"] += len(new)
            if new:
                groups = ["references/research/"] if "references/research" in new else []
                srcs = [r.rsplit("/", 1)[1] for r in new if r.startswith("references/sources/")]
                if srcs:
                    groups.append("references/sources/{" + ",".join(srcs) + "}/" if len(srcs) > 1
                                  else f"references/sources/{srcs[0]}/")
                print(f"  + {label}/: {', '.join(groups)} (.gitkeep)")
            continue
        if kind == "keep":
            counts["kept"] += 1
            print(f"  = {label}")
            continue
        n_todo = content.count("[TODO")
        tag = f" · {n_todo} TODO" if n_todo else ""
        if kind == "update":
            counts["updated"] += 1
            print(f"  ~ {label}{tag}")
        elif path.exists() and not plan.force:
            counts["kept"] += 1
            print(f"  = {label} (已存在，保留；--force 覆盖)")
            continue
        elif path.exists():
            counts["overwritten"] += 1
            print(f"  ! {label} (覆盖){tag}")
        else:
            counts["created"] += 1
            print(f"  + {label}{tag}")
        todos += n_todo
        if not dry:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    return counts, todos


def git_ignore_check(team_dir: Path, slugs: list[str]) -> tuple[bool, str]:
    """用 git check-ignore 确认 PDF、txt/、private/ 被忽略而 private/README.md 不被忽略。返回 (是否有泄漏, 说明)。"""
    anchor = next((p for p in [team_dir, *team_dir.parents] if p.is_dir()), None)
    if anchor is None:
        return False, "· git: 没检查（目录不存在）"
    try:
        top = subprocess.run(["git", "-C", str(anchor), "rev-parse", "--show-toplevel"],
                             capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.TimeoutExpired):
        return False, "· git: 没检查（没有 git）"
    if top.returncode != 0 or not top.stdout.strip():
        return False, f"· git: 没检查（{display(anchor)} 不在 git 仓库里）；自己确认 PDF、papers/txt/ 和 private/ 不会被提交"
    rel = lambda s, p: os.path.relpath(team_dir / s / p, anchor)
    want_ignored = [rel(s, p) for s in slugs for p in IGNORED_PROBES]
    want_tracked = [rel(s, p) for s in slugs for p in TRACKED_PROBES]
    try:
        out = subprocess.run(["git", "-C", str(anchor), "check-ignore", "--no-index", "--stdin", "-z"],
                             input="\0".join(want_ignored + want_tracked) + "\0",
                             capture_output=True, text=True, timeout=20)
    except (OSError, subprocess.TimeoutExpired):
        return False, "· git: check-ignore 失败，没检查"
    if out.returncode not in (0, 1):
        return False, f"· git: check-ignore 出错（{out.stderr.strip()[:120]}），没检查"
    ignored = set(out.stdout.split("\0"))
    leaks = [p for p in want_ignored if p not in ignored]
    hidden = [p for p in want_tracked if p in ignored]
    if not leaks and not hidden:
        return False, "✅ git: 每位成员的 PDF、papers/txt/ 和 private/（README.md 除外）都被 .gitignore 忽略"
    base = Path(os.path.relpath(team_dir.parent.resolve(), Path(top.stdout.strip()).resolve())).as_posix()
    base = "" if base == "." else base + "/"
    msg = ["❌ git: .gitignore 没覆盖这个团队目录，版权全文或私人材料可能被提交。在仓库根 .gitignore 加上:"]
    msg += [f"     {r}" for r in (f"{base}**/references/sources/papers/*.pdf", f"{base}**/references/sources/papers/txt/",
                                   f"{base}**/references/sources/private/*", f"!{base}**/references/sources/private/README.md")]
    msg += [f"     没被忽略: {p}" for p in leaks[:6]] + [f"     不该被忽略: {p}" for p in hidden[:3]]
    return True, "\n".join(msg)


def next_steps(cfg: dict, team_dir: Path, adding: list[str], leak: bool) -> list[str]:
    t = display(team_dir)
    py = lambda s: f"python3 {display(HERE / s)}"
    wf = display(HERE / "workflows/README.md")
    out = ["下一步:"]
    ms = [m for m in cfg["members"] if not adding or m["slug"] in adding]
    no_sch = [m["slug"] for m in ms if not (m.get("scholar") or "").strip()]
    no_hint = [m["slug"] for m in ms if not (m.get("hint") or "").strip()]
    if no_sch or no_hint:
        out.append("  · 先补 team.json：" + "；".join(x for x in [
            f"没有 scholar id 的 {', '.join(no_sch)}（harvest 需要）" if no_sch else "",
            f"没有 hint 的 {', '.join(no_hint)}（消歧需要）" if no_hint else ""] if x))
    out.append(f'  · grep -rn "TODO" {t}      # 列出所有待补项')
    who = f"成员 {', '.join(adding)} " if adding else "每位成员"
    out.append(f"  · T1 {who}的基础 Skill：{display(HERE / 'workflows/team-base-skills.js')}（启动方式见 {wf}；"
               f"每位成员一个 workflow 并行）；闸门 {py('quality_check.py')} {t}/<成员>/SKILL.md --mode research → 12/12")
    if adding:
        out.append(f"  · 圆桌 {t}/{cfg['roundtable']}/SKILL.md：把新成员加进名单、座次和 Roundtable Card"
                   f"（手改或重跑 {display(HERE / 'workflows/team-layer.js')}）；README 里他那一行的 lens 也要填")
        out.append(f"  · 已做过深读的团队：新成员走 T3（见 playbook），再用 {py('team_status.py')} {t} --coverage 刷新 DEEP-READING.md 的覆盖表")
    else:
        out.append(f"  · T2 团队层：{display(HERE / 'workflows/team-layer.js')}；闸门 {py('check_links.py')} {t}")
    out.append(f"  · 进度：{py('team_status.py')} {t}")
    out.append(f"  · 全流程见 {display(REPO / 'references/research-team-playbook.md')}；每个阶段结束就 commit（容器随时可能被回收）。")
    if leak:
        out.append("  · 先按上面补好 .gitignore 再提交：PDF、papers/txt/ 和 private/（README.md 除外）不能进仓库。")
    else:
        out.append("  · PDF、papers/txt/ 和 private/（README.md 除外）被 .gitignore 忽略：不要 git add -f，版权全文与私人材料不进仓库。")
    return out


def scaffold(a) -> int:
    src = Path(a.team_json)
    if not src.is_file():
        print(f"❌ 找不到 {a.team_json}")
        return 1
    cfg, errs = load_config(src)
    extra = {}
    for kv in a.set or []:
        k, sep, v = kv.partition("=")
        if not sep or not re.fullmatch(r"[A-Za-z0-9_]+", k):
            errs.append(f"--set {kv!r} 应为 NAME=VALUE")
        else:
            extra[k] = v
    if errs:
        for e in errs:
            print(f"❌ {e}")
        print(f"❌ team.json 有 {len(errs)} 处问题，什么都没写")
        return 1
    adding = list(dict.fromkeys(a.add_member or []))
    plan = build_plan(a, src, cfg, adding, extra)
    for n in plan.notes:
        print(n)
    if plan.errors:
        for e in plan.errors:
            print(f"❌ {e}")
        print(f"❌ {len(plan.errors)} 个问题，什么都没写")
        return 1
    print(f"{'(dry run) ' if a.dry_run else ''}{display(plan.team_dir)}/")
    counts, todos = execute(plan, a.dry_run)
    leak, git_msg = git_ignore_check(plan.team_dir, [m["slug"] for m in cfg["members"] if not adding or m["slug"] in adding])
    print(git_msg)
    print()
    for line in next_steps(cfg, plan.team_dir, adding, leak):
        print(line)
    what = f"member {', '.join(adding)}" if adding else f"team {cfg['team']} ({len(cfg['members'])} members)"
    verb = "would scaffold" if a.dry_run else "scaffolded"
    print(f"{'❌' if leak else '✅'} {verb} {what}: created {counts['created']} files + {counts['dirs']} folders, "
          f"updated {counts['updated']}, kept {counts['kept']}, overwritten {counts['overwritten']} · "
          f"{todos} [TODO markers in written files" + (" · .gitignore does not cover it" if leak else ""))
    return 1 if leak else 0


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    ap = argparse.ArgumentParser(description="起草 team.json / 按模板铺研究团队目录 / 给团队加成员")
    ap.add_argument("team_json", nargs="?", help="team.json（铺目录或 --add-member 时）")
    ap.add_argument("--init", metavar="TEAM_SLUG", help="起草 team.json")
    ap.add_argument("--field", help="--init: 领域（写进 team.json 的 field）")
    ap.add_argument("--members", help='--init: 成员姓名，分号分隔 "Name One;Name Two"')
    ap.add_argument("--title", help="--init: 团队标题（默认由 slug 生成）")
    ap.add_argument("--language", default="English", help="--init: 成员 Skill 与卡片的语言（默认 English）")
    ap.add_argument("--out", help="--init: team.json 写到哪（默认 <--root>/<slug>/team.json）")
    ap.add_argument("--root", default=str(DEFAULT_ROOT), help=f"团队目录的上级（默认 {display(DEFAULT_ROOT)}）")
    ap.add_argument("--templates", default=str(DEFAULT_TEMPLATES), help=f"模板目录（默认 {display(DEFAULT_TEMPLATES)}）")
    ap.add_argument("--add-member", action="append", metavar="SLUG", help="只铺这位（已写进 team.json 的）成员，可重复")
    ap.add_argument("--set", action="append", metavar="NAME=VALUE", help="补充或覆盖模板占位符，可重复")
    ap.add_argument("--force", action="store_true", help="覆盖已存在的文件")
    ap.add_argument("--dry-run", action="store_true", help="只显示会做什么")
    a = ap.parse_args()
    if a.init:
        if a.team_json or a.add_member:
            ap.error("--init 不能和 team.json / --add-member 同时用")
        if not a.field or not a.members:
            ap.error("--init 需要 --field 和 --members")
        sys.exit(init_team(a))
    if not a.team_json:
        ap.error("需要 team.json，或用 --init 起草一个")
    sys.exit(scaffold(a))


if __name__ == "__main__":
    main()
