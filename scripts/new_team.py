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
       python3 new_team.py <team.json> [--root DIR] [--templates DIR] [--force] [--dry-run] [--base-tier] [--set NAME=VALUE]...
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
       --base-tier：确定只做轻量档（不深读）时用。DEEP-READING.md 换成模板开头注释里的两段轻量档说明；
       RESOURCES.md 删掉深读档占位行（第 3 行），第 1 行的 Notes 写 "not harvested (base tier)"、没有 Scholar id 时
       Link 写 "—"。其余 TODO 照旧由 team-layer.js（deep_tier: false）处理。

    3) 给已有团队加成员（先把他写进团队目录里的 team.json 的 members）
       python3 new_team.py <team.json> --add-member <slug> [--add-member <slug>]... [--root DIR] [--templates DIR] [--force] [--dry-run] [--base-tier]
       只铺这位成员的目录，并把他的一行插进 README.md 的成员表：有 <!-- members:start --> / <!-- members:end -->
       标记时把 {{MEMBER_TABLE}} 格式的一行插在 end 标记前；没有标记时照最后一个链接到成员文件夹的表格行造一行
       （同样的列数，slug / 姓名换成新成员，其余格 [TODO]）插在它后面；都找不到就在文末追加一条 [TODO]。
       圆桌 SKILL.md 和 DEEP-READING.md 不改，只在「下一步」里提醒。

    4) 改 team.json 里某位成员的字段（harvest 找到的 Scholar id、DBLP pid 等，不用手改 JSON）
       python3 new_team.py <team.json> --set-member <slug> KEY=VALUE [KEY=VALUE]... [--dry-run]
       KEY 是成员字段（scholar、dblp、orcid、homepage、hint、surname、family_name、living、student_mode、chase_hints）；
       living / student_mode 取 true/false，chase_hints 取 JSON 列表。只改这一位的这些字段，其余原样保留。

    5) 从 DBLP 补全成员的 dblp / orcid / homepage（只补空着的字段；要联网，走 sparql.dblp.org）
       python3 new_team.py <team.json> --lookup [--member slug,slug] [--dry-run]
       有 scholar id 时按 DBLP 人物页登记的 Scholar 链接找（唯一匹配才填，可靠）；找不到再按 orcid 找；
       都找不到时按姓名找，只有唯一一个完全同名的候选才填，并提示对照 hint 核对（同名的人很常见）。

模板占位符（简单字符串替换，{{NAME}}）:
    团队级   {{TEAM_SLUG}} {{TEAM_TITLE}} {{FIELD}} {{LANGUAGE}} {{DATE}}（今天） {{ROUNDTABLE_SLUG}}
             {{MEMBER_TABLE}}（每位成员一行 | [Name](slug/SKILL.md) | lens: [TODO] | 状态 |）
             {{ROUNDTABLE_MEMBER_TABLE}}（圆桌 Team 表：每位成员一行 | `slug` | Name | [TODO: 一行 lens …] |）
             {{MEMBER_LIST}}（逗号分隔的姓名） {{MEMBER_COUNT}}
    成员级   以上全部，加 {{MEMBER_NAME}} {{MEMBER_SLUG}} {{MEMBER_SURNAME}}
             {{SCHOLAR_URL}}（https://scholar.google.com/citations?user=<id>&hl=en；没有 id 时为
             "— (no Scholar profile in team.json; list from DBLP/homepage)"，--base-tier 时为 "—"）
    --set NAME=VALUE 可补充或覆盖。模板里出现未知占位符或落单的 {{ 算错误：列出来，一个文件也不写。
    需要研究才能填的内容在模板里写成 [TODO: …]，`grep -rn "TODO" product/<团队>` 列出所有待办。

输出:
    逐行列出 + 新建 / = 已存在保留 / ! 覆盖 / ~ 更新（加成员时的 README），每个写入的文件后标 [TODO 数；
    两位成员 surname 相同（圆桌的 [Surname lens]、@Surname 会撞）时警告；
    用 git check-ignore 检查成员 references/sources/ 下的 PDF/PS/DjVu/EPUB、papers/txt/ 和 private/ 是否被忽略，
    没覆盖时打印要加进仓库根 .gitignore 的几行（与本仓库 .gitignore 里的写法相同）；最后打印「下一步」。
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
IGNORED_PROBES = ["references/sources/papers/x.pdf", "references/sources/papers/X.PDF", "references/sources/papers/x.ps",
                  "references/sources/papers/x.ps.gz", "references/sources/papers/x.djvu", "references/sources/talks/x.pdf",
                  "references/sources/essays/x.epub", "references/sources/papers/txt/x.txt",
                  "references/sources/private/x.md"]
TRACKED_PROBES = ["references/sources/private/README.md", "references/sources/RESOURCES.md",
                  "references/sources/papers/INDEX.md"]
# 仓库根 .gitignore 里的同一组规则（前面加团队目录的上级，如 product/）；没覆盖时原样打印这几行
GITIGNORE_RULES = ["**/references/sources/**/*.[pP][dD][fF]", "**/references/sources/**/*.[pP][sS]",
                   "**/references/sources/**/*.[pP][sS].[gG][zZ]", "**/references/sources/**/*.[dD][jJ][vV][uU]",
                   "**/references/sources/**/*.[eE][pP][uU][bB]", "**/references/sources/papers/txt/",
                   "**/references/sources/private/*", "!**/references/sources/private/README.md"]
NO_SCHOLAR = "— (no Scholar profile in team.json; list from DBLP/homepage)"
CARD_DIMS = [f"D{i}" for i in range(1, 9)]
MEMBER_STR_KEYS = ("surname", "family_name", "hint", "scholar", "dblp", "orcid", "homepage")
BASE_TIER_NOTES = "not harvested (base tier)"

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


def surname_clashes(members: list) -> list[str]:
    """surname 相同（不分大小写）的成员：圆桌用 [Surname lens]、@Surname 称呼成员，同姓会分不清。"""
    by: dict[str, list[str]] = {}
    for m in members:
        if isinstance(m, dict) and isinstance(m.get("name"), str) and m.get("name").strip():
            sur = (m.get("surname") or surname_of(m["name"])).strip()
            by.setdefault(sur.casefold(), []).append(f"{m.get('slug') or m['name']} ({sur})")
    return [f"⚠️ surname 重复：{', '.join(v)}。圆桌的 [Surname lens] 与 @Surname 会撞；在 team.json 里把 surname 改成"
            f"能区分的写法（如 \"M. Smith\" / \"J. Smith\"），工作流和圆桌都用这个字段" for v in by.values() if len(v) > 1]


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
    for w in surname_clashes(members):
        print(w)
    cfg = {"schema": 1, "team": team, "title": a.title or default_title(team), "field": a.field,
           "language": a.language, "created": today(), "roundtable": roundtable, "chase_hints": [],
           "card_dimensions": {}, "members": members}
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
    print("     没有 Scholar 主页的人 scholar 留空（harvest 先按姓名搜一次，再以 DBLP/主页为主列表）；")
    print(f"     python3 {display(HERE / 'new_team.py')} {display(out)} --lookup 可从 DBLP 补 dblp / orcid / homepage。")
    print("     领域不是数学/计算类时，填 card_dimensions（D3–D5 在这个领域指什么，见 team-templates/team.example.json）。")
    if not 3 <= len(members) <= 6:
        print(f"     注意：现在 {len(members)} 位；3–6 位视角互补、有公开分歧的研究者最合适。")
    root_opt = "" if same_path(Path(a.root), DEFAULT_ROOT) else f" --root {display(Path(a.root))}"
    print(f"  2. python3 {display(HERE / 'new_team.py')} {display(out)}{root_opt}      # 按模板铺团队目录"
          f"（确定只做轻量档、不深读时加 --base-tier）")
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
        for key in MEMBER_STR_KEYS:
            if key in m and not isinstance(m[key], str):
                errs.append(f"{where}: {key} 必须是字符串")
        for key in ("living", "student_mode"):
            if key in m and not isinstance(m[key], bool):
                errs.append(f"{where}: {key} 必须是 true/false")
        if "chase_hints" in m and not (isinstance(m["chase_hints"], list) and all(isinstance(x, str) for x in m["chase_hints"])):
            errs.append(f"{where}: chase_hints 必须是字符串列表")
    if "chase_hints" in cfg and not (isinstance(cfg["chase_hints"], list) and all(isinstance(x, str) for x in cfg["chase_hints"])):
        errs.append("chase_hints 必须是字符串列表")
    cd = cfg.get("card_dimensions")
    if cd is not None and not (isinstance(cd, dict) and all(k in CARD_DIMS and isinstance(v, str) for k, v in cd.items())):
        errs.append(f"card_dimensions 必须是对象，键只能是 {'/'.join(CARD_DIMS)}，值是字符串（这个领域里该维度指什么）")
    sl = cfg.get("source_labels")
    if sl is not None and not (isinstance(sl, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in sl.items())):
        errs.append('source_labels 必须是 {"网址关键词": "来源标签"} 形式的对象')
    return cfg, [f"{display(path)}: {e}" for e in errs]


# ---------- 模板 ----------

def member_row(team_dir: Path, m: dict) -> str:
    stage = "T1 base skill" if (team_dir / m["slug"] / "SKILL.md").exists() else "T0 scaffold"
    if m.get("student_mode"):
        stage += " · student mode"
    return f"| [{m['name']}]({m['slug']}/SKILL.md) | lens: [TODO] | {stage} |"


def roundtable_row(m: dict) -> str:
    return (f"| `{m['slug']}` | {m['name']} | [TODO: the lens in one line, condensed from this member's Roundtable Card "
            f"\"Lens (one line)\"; team-layer.js (T2)] |")


def team_values(cfg: dict, team_dir: Path, extra: dict) -> dict:
    ms = cfg["members"]
    v = {"TEAM_SLUG": cfg["team"], "TEAM_TITLE": cfg["title"], "FIELD": cfg["field"],
         "LANGUAGE": cfg.get("language") or "English", "DATE": today(), "ROUNDTABLE_SLUG": cfg["roundtable"],
         "MEMBER_TABLE": "\n".join(member_row(team_dir, m) for m in ms),
         "ROUNDTABLE_MEMBER_TABLE": "\n".join(roundtable_row(m) for m in ms),
         "MEMBER_LIST": ", ".join(m["name"] for m in ms), "MEMBER_COUNT": str(len(ms))}
    v.update(extra)
    return v


def member_values(base: dict, m: dict, extra: dict, base_tier: bool = False) -> dict:
    v = dict(base)
    sch = (m.get("scholar") or "").strip()
    v.update({"MEMBER_NAME": m["name"], "MEMBER_SLUG": m["slug"], "MEMBER_SURNAME": m.get("surname") or surname_of(m["name"]),
              "SCHOLAR_URL": f"https://scholar.google.com/citations?user={sch}&hl=en" if sch
              else ("—" if base_tier else NO_SCHOLAR)})
    v.update(extra)
    return v


def split_row(line: str) -> list[str]:
    return [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]


def base_tier_deep_reading(template: str) -> str | None:
    """DEEP-READING.md 模板开头注释里给轻量档的两段（标题 + 一段），缩进比注释正文深；找不到返回 None。"""
    lines = template.splitlines()
    k = next((i for i, ln in enumerate(lines) if "two paragraphs below" in ln), None)
    if k is None:
        return None
    body = []
    for ln in lines[k + 1:]:
        if not ln.startswith(" " * 12) or not ln.strip() or ln.strip().startswith(("Open work", "-->")):
            break
        body.append(ln.strip())
    if len(body) < 2 or not body[0].startswith("#"):
        return None
    return body[0] + "\n\n" + " ".join(body[1:]) + "\n"


def base_tier_resources(text: str) -> tuple[str, list[str]]:
    """RESOURCES.md 的轻量档写法：删深读档占位行（第 3 行），第 1 行 Notes = not harvested (base tier)，
    Link 里还有 TODO 时换成 —。返回 (新文本, 没做成的事)。"""
    out, missed, row1, row3 = [], [], False, False
    for ln in text.split("\n"):
        cells = split_row(ln) if ln.lstrip().startswith("|") else []
        if cells and cells[0] == "3" and "deep-tier" in ln:
            row3 = True
            continue
        if cells and cells[0] == "1" and len(cells) >= 3:
            row1 = True
            cells[-1] = BASE_TIER_NOTES
            cells = ["—" if "[TODO" in c and i == len(cells) - 4 else c for i, c in enumerate(cells)]
            ln = "| " + " | ".join(cells) + " |"
        out.append(ln)
    if not row1:
        missed.append("找不到第 1 行（出版物列表）")
    if not row3:
        missed.append("找不到深读档占位行（第 3 行）")
    return "\n".join(out), missed


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
    plan.notes += surname_clashes(cfg["members"])
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
    probe = member_values(base, cfg["members"][0], extra, a.base_tier)
    for t, _ in MEMBER_TEMPLATES:
        plan.errors += template_problems(t, templates[t], probe)
    deep_note = None
    if a.base_tier and not adding:
        deep_note = base_tier_deep_reading(templates.get("DEEP-READING.md", ""))
        if deep_note is None:
            plan.errors.append("--base-tier: DEEP-READING.md 模板开头注释里找不到轻量档的两段说明（\"two paragraphs below\" 之后）")
    if plan.errors:
        return plan

    if not adding:
        for t, dest in TEAM_TEMPLATES:
            text = deep_note if (t == "DEEP-READING.md" and deep_note) else templates[t]
            plan.file(dest.format(roundtable=cfg["roundtable"]), fill(text, base))
    for m in cfg["members"]:
        if adding and m["slug"] not in adding:
            continue
        mv = member_values(base, m, extra, a.base_tier)
        plan.dirs(m["slug"], MEMBER_DIRS)
        for t, dest in MEMBER_TEMPLATES:
            text = fill(templates[t], mv)
            if a.base_tier and t == "member-RESOURCES.md":
                text, missed = base_tier_resources(text)
                plan.notes += [f"⚠️ --base-tier: {m['slug']} 的 RESOURCES.md {x}，那部分照模板原样" for x in missed]
            plan.file(f"{m['slug']}/{dest}", text)
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
        return False, ("✅ git: 每位成员 references/sources/ 下的 PDF/PS/DjVu/EPUB、papers/txt/ 和 private/"
                       "（README.md 除外）都被 .gitignore 忽略")
    msg = ["❌ git: .gitignore 没覆盖这个团队目录，版权全文或私人材料可能被提交。在仓库根 .gitignore 加上:"]
    msg += [f"     {r}" for r in gitignore_lines(team_dir, Path(top.stdout.strip()))]
    msg += [f"     没被忽略: {p}" for p in leaks[:6]] + [f"     不该被忽略: {p}" for p in hidden[:3]]
    return True, "\n".join(msg)


def gitignore_lines(team_dir: Path, top: Path) -> list[str]:
    """要加进仓库根 .gitignore 的规则：GITIGNORE_RULES 前面加上团队目录的上级（相对仓库根，如 product/）。"""
    base = Path(os.path.relpath(team_dir.parent.resolve(), top.resolve())).as_posix()
    base = "" if base == "." else base + "/"
    return [f"!{base}{r[1:]}" if r.startswith("!") else f"{base}{r}" for r in GITIGNORE_RULES]


def next_steps(cfg: dict, team_dir: Path, adding: list[str], leak: bool, base_tier: bool = False) -> list[str]:
    t = display(team_dir)
    py = lambda s: f"python3 {display(HERE / s)}"
    wf = display(HERE / "workflows/README.md")
    out = ["下一步:"]
    ms = [m for m in cfg["members"] if not adding or m["slug"] in adding]
    no_sch = [m["slug"] for m in ms if not (m.get("scholar") or "").strip()]
    no_hint = [m["slug"] for m in ms if not (m.get("hint") or "").strip()]
    if no_sch or no_hint:
        out.append("  · 先补 team.json：" + "；".join(x for x in [
            f"没有 scholar id 的 {', '.join(no_sch)}（有主页就填；确实没有就留空：harvest 先按姓名搜一次，再以 DBLP/主页为主列表；"
            f"--lookup 可从 DBLP 补 dblp/orcid/homepage）" if no_sch else "",
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
        tier = "（轻量档：args.deep_tier = false）" if base_tier else "（只做轻量档时 args.deep_tier = false）"
        out.append(f"  · T2 团队层：{display(HERE / 'workflows/team-layer.js')}{tier}；闸门 {py('check_links.py')} {t}")
    out.append(f"  · 进度：{py('team_status.py')} {t}")
    out.append(f"  · 全流程见 {display(REPO / 'references/research-team-playbook.md')}；每个阶段结束就 commit（容器随时可能被回收）。")
    if leak:
        out.append("  · 先按上面补好 .gitignore 再提交：PDF/PS/DjVu/EPUB、papers/txt/ 和 private/（README.md 除外）不能进仓库。")
    else:
        out.append("  · PDF/PS/DjVu/EPUB、papers/txt/ 和 private/（README.md 除外）被 .gitignore 忽略：不要 git add -f，"
                   "版权全文与私人材料不进仓库；commit 前看一眼 git status。")
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
    for line in next_steps(cfg, plan.team_dir, adding, leak, a.base_tier):
        print(line)
    what = f"member {', '.join(adding)}" if adding else f"team {cfg['team']} ({len(cfg['members'])} members)"
    verb = "would scaffold" if a.dry_run else "scaffolded"
    print(f"{'❌' if leak else '✅'} {verb} {what}: created {counts['created']} files + {counts['dirs']} folders, "
          f"updated {counts['updated']}, kept {counts['kept']}, overwritten {counts['overwritten']} · "
          f"{todos} [TODO markers in written files" + (" · .gitignore does not cover it" if leak else ""))
    return 1 if leak else 0


# ---------- 改成员字段 / 从 DBLP 补全 ----------

def write_config(path: Path, cfg: dict, dry: bool, changes: list[str]) -> int:
    for c in changes:
        print(c)
    if not changes:
        print(f"= {display(path)}: nothing to change")
        return 0
    if dry:
        print(f"✅ (dry run) would update {display(path)} ({len(changes)} change(s))")
        return 0
    path.write_text(json.dumps(cfg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"✅ updated {display(path)} ({len(changes)} change(s)); commit it with the team")
    return 0


def set_member(a) -> int:
    path = Path(a.team_json)
    cfg, errs = load_config(path)
    if errs:
        for e in errs:
            print(f"❌ {e}")
        return 1
    m = next((x for x in cfg["members"] if x.get("slug") == a.set_member), None)
    if m is None:
        print(f"❌ {a.set_member!r} is not a member slug in {display(path)}: {', '.join(x['slug'] for x in cfg['members'])}")
        return 1
    allowed = set(MEMBER_STR_KEYS) | {"living", "student_mode", "chase_hints"}
    changes = []
    for kv in a.pairs:
        k, sep, v = kv.partition("=")
        if not sep or k not in allowed:
            print(f"❌ {kv!r}: use KEY=VALUE with KEY one of {', '.join(sorted(allowed))}")
            return 1
        if k in ("living", "student_mode"):
            if v.lower() not in ("true", "false"):
                print(f"❌ {k} takes true or false, not {v!r}")
                return 1
            val = v.lower() == "true"
        elif k == "chase_hints":
            try:
                val = json.loads(v)
            except json.JSONDecodeError as e:
                print(f"❌ chase_hints takes a JSON list of strings: {e}")
                return 1
            if not (isinstance(val, list) and all(isinstance(x, str) for x in val)):
                print("❌ chase_hints takes a JSON list of strings")
                return 1
        else:
            val = v.strip()
            if k == "dblp":
                val = re.sub(r"^https?://dblp\.org/pid/|\.html$", "", val)
            if k == "scholar":
                mm = re.search(r"user=([\w-]+)", val)
                val = mm.group(1) if mm else val
        if m.get(k) != val:
            changes.append(f"~ {a.set_member}.{k}: {json.dumps(m.get(k), ensure_ascii=False)} → {json.dumps(val, ensure_ascii=False)}")
            m[k] = val
    if any(".surname:" in c for c in changes):
        for w in surname_clashes(cfg["members"]):
            print(w)
    return write_config(path, cfg, a.dry_run, changes)


def lookup(a) -> int:
    path = Path(a.team_json)
    cfg, errs = load_config(path)
    if errs:
        for e in errs:
            print(f"❌ {e}")
        return 1
    sys.path.insert(0, str(HERE))
    import dblp_works as dw
    only = [x for x in (a.member or "").split(",") if x]
    changes, rc = [], 0
    for m in cfg["members"]:
        if only and m["slug"] not in only:
            continue
        pid, how = (m.get("dblp") or "").strip(), ""
        try:
            if not pid:
                pids = []
                if (m.get("scholar") or "").strip():
                    pids, how = dw.find_by_scholar(m["scholar"]), "its Scholar link on the DBLP person page"
                if not pids and (m.get("orcid") or "").strip():
                    pids, how = dw.find_by_orcid(m["orcid"]), "its ORCID"
                if not pids:
                    cand, exact = dw.find_by_name(m["name"])
                    pids, how = sorted(exact), "name only"
                    if len(exact) != 1:
                        print(f"· {m['slug']}: {len(exact)} exact-name DBLP candidates (of {len(cand)}); pick one by hand: "
                              f"python3 scripts/dblp_works.py --name \"{m['name']}\"")
                        continue
                if len(pids) != 1:
                    print(f"· {m['slug']}: {len(pids)} DBLP persons match {how}; not filled "
                          f"(python3 scripts/dblp_works.py --name \"{m['name']}\" lists candidates)")
                    continue
                pid = pids[0]
                changes.append(f"~ {m['slug']}.dblp: \"\" → \"{pid}\" (matched by {how}: https://dblp.org/pid/{pid}.html)")
                if how == "name only":
                    changes.append(f"  ⚠️ {m['slug']}: matched by name only; check https://dblp.org/pid/{pid}.html against the hint "
                                   f"({m.get('hint') or 'no hint'}) and clear dblp if it is someone else")
                m["dblp"] = pid
            info = dw.person_info([pid]).get(pid, {})
        except Exception as e:  # network or endpoint errors: report and go on
            print(f"❌ {m['slug']}: DBLP lookup failed ({e})")
            rc = 1
            continue
        orcids = [dw.short(o, "https://orcid.org/") for o in info.get("orcid", [])]
        homes = list(dict.fromkeys(info.get("primaryHomepage", []) + info.get("homepage", [])))
        if not (m.get("orcid") or "").strip() and len(orcids) == 1:
            changes.append(f"~ {m['slug']}.orcid: \"\" → \"{orcids[0]}\" (from DBLP {pid})")
            m["orcid"] = orcids[0]
        if not (m.get("homepage") or "").strip() and homes:
            changes.append(f"~ {m['slug']}.homepage: \"\" → \"{homes[0]}\" (from DBLP {pid})")
            m["homepage"] = homes[0]
    return write_config(path, cfg, a.dry_run, changes) or rc


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
    ap.add_argument("--base-tier", action="store_true",
                    help="只做轻量档：DEEP-READING.md 写成轻量档说明，RESOURCES.md 去掉深读档占位行")
    ap.add_argument("--set-member", metavar="SLUG", help="改 team.json 里这位成员的字段：后面跟 KEY=VALUE ...")
    ap.add_argument("pairs", nargs="*", metavar="KEY=VALUE", help="--set-member 的字段")
    ap.add_argument("--lookup", action="store_true", help="从 DBLP 补全空着的 dblp / orcid / homepage（联网）")
    ap.add_argument("--member", help="--lookup：只查这几位（逗号分隔 slug）")
    a = ap.parse_intermixed_args()
    if a.pairs and not a.set_member:
        ap.error(f"unexpected arguments: {' '.join(a.pairs)} (KEY=VALUE pairs go with --set-member)")
    if a.set_member or a.lookup:
        if not a.team_json or a.init or a.add_member or a.base_tier or (a.set_member and a.lookup):
            ap.error("--set-member / --lookup take a team.json and nothing else (no --init, --add-member, --base-tier)")
        if a.set_member and not a.pairs:
            ap.error("--set-member needs KEY=VALUE pairs, e.g. --set-member ada-example dblp=12/3456")
        sys.exit(set_member(a) if a.set_member else lookup(a))
    if a.init:
        if a.team_json or a.add_member or a.base_tier:
            ap.error("--init 不能和 team.json / --add-member / --base-tier 同时用（--base-tier 用在第 2 步）")
        if not a.field or not a.members:
            ap.error("--init 需要 --field 和 --members")
        sys.exit(init_team(a))
    if not a.team_json:
        ap.error("需要 team.json，或用 --init 起草一个")
    sys.exit(scaffold(a))


if __name__ == "__main__":
    main()
