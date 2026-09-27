#!/usr/bin/env python3
"""
校验研究Skill「精简」（tighten）是否无损：长证据从 SKILL.md 移进 references/research/09-evidence-ledger.md 后，
什么都没丢，SKILL.md 指向证据账本的锚点也都存在。

总是检查:
    锚点   SKILL.md 里指向账本的每个锚点都能在账本里找到（标题的 GitHub slug 或 <a id="...">，
           与 check_links.py 同一套规则）。识别的写法：
             references/research/09-evidence-ledger.md#method-1          （Markdown 链接或反引号里）
             `...09-evidence-ledger.md#taste-marks`, `#taste-warnings`   （同一行里跟在账本后面的 `#锚点`）
             ledger `#anti-patterns`                                     （行内先出现 ledger / 账本 / 台账 字样）
             `#method-1` … `#method-7`、`#heuristic-1` to `#heuristic-10` （范围：… ... to – — ~ 至 到，逐个展开）
             `#heuristic-N`、`#signature-<card>`                         （占位写法：账本里至少有一个同前缀锚点）
           同一行里跟在别的 .md 文件后面的 `#锚点` 属于那个文件，不查；不在账本里、但在 SKILL.md 自身里的算本文件锚点。

加 --before <精简前的 SKILL.md 副本> 时再检查:
    卡片ID  精简前出现的每个卡片ID（S012、D003、B001、X001、R007、H002…：一个大写字母 + 3–4 位数字）
            都还在 SKILL.md 或账本里
    引页    精简前每条「ID + 页码」引用（如 [S025 p. 11; S018 pp. 27–28]、[card S012, pp. 20–21]、[S012 第3页]）的每个页码，
            在 SKILL.md 或账本里仍和同一个ID一起出现（页码按单页/区间逐个比，写法变了不算丢）
    引文    精简前每段 ≥20 字的引号内文字（“…”、"…"、「…」）都原样在 SKILL.md 或账本里（空白差异不计）
    原样    front matter 与 Activation Rules / Research Integrity Rules / Student Mode
            （中文：激活规则 / 研究诚信规则 / 学生模式）各节，与精简前逐字节相同（精简前没有的节不查）

--allow <项,项>：按设计会变的地方，明确放行（不再让 agent 凭眼睛判断「这处差异是不是故意的」）。
放行的差异不算问题，但仍逐条打印成「~ allowed」信息行，方便复核。可选项:
    frontmatter-date      front matter 只有日期行不同（researched: / updated: / date: / 调研时间: / 更新时间:）
    frontmatter           front matter 除 name: 与 type: 外都可以变（汇总会改 description 里的覆盖数字；name/type 仍须相同）
    activation-numbers    Activation Rules（激活规则）一节只有数字不同（覆盖数、年份、百分比），文字须逐字相同
    activation-disclaimer Activation Rules 里提到首次激活免责声明的行（含 disclaimer / first activation /
                          免责 / 首次激活 字样）可以整行改写，其余行须逐字相同
Research Integrity Rules 与 Student Mode 没有放行项：它们永远逐字节相同。
各步用法（工作流 prompt 里照此写）:
    T3.6 汇总 team-synthesize.js   --allow frontmatter,activation-disclaimer   （改 researched: 与 description，
                                    把「没读全文」的免责声明改成覆盖数）
    T3.7 精简 team-tighten.js      不加 --allow（精简不动 front matter 和 Activation Rules）
    T4   增量 team-increment.js    --allow frontmatter-date,activation-numbers  （只改 researched: 与免责声明里的数字）

用法:
    python3 check_ledger.py <skill目录> [--before <SKILL.before.md>] [--allow ITEM,ITEM] [--ledger PATH] [--show N]

示例:
    cp product/<团队>/<成员>/SKILL.md /tmp/SKILL.before.md         # 精简前先存一份
    python3 scripts/check_ledger.py product/<团队>/<成员> --before /tmp/SKILL.before.md
    python3 scripts/check_ledger.py product/<团队>/<成员> --before /tmp/SKILL.before-inc.md --allow frontmatter-date,activation-numbers

输出:
    每个问题一行（✗ 类别: 内容），然后是只供参考的账本锚点统计（账本里没被 SKILL.md 引用的锚点不算错），
    最后一行汇总：✅/❌ …；有问题时退出码为 1，路径不存在为 2。
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_links import HTML_ANCHOR_RE, Checker, prose_lines  # noqa: E402  同一套 GitHub slug / <a id> 规则

LEDGER_REL = Path("references/research/09-evidence-ledger.md")
PROTECTED = {
    "Activation Rules": ("activation rules", "激活规则"),
    "Research Integrity Rules": ("research integrity rules", "研究诚信规则"),
    "Student Mode": ("student mode", "学生模式"),
}

CARD_ID_RE = re.compile(r"(?<![A-Za-z0-9_])([A-Z]\d{3,4})(?![0-9])")
_RANGE = r"(?:\s*[-–—]\s*(?:\d+|[ivxlc]+))?"
_PAGES = (r"(?:\d+|[ivxlc]+)" + _RANGE                        # 第一页可以是罗马数字（前言页）
          + r"(?:\s*,\s*(?:\d+|[ivxlc]{2,})" + _RANGE + r")*")  # 后续页：数字或 ≥2 位罗马数字（避开 “, i.e.”）
CITE_RE = re.compile(r"(?<![A-Za-z0-9_])([A-Z]\d{3,4})(?![0-9]),?\s*(?:(?<=[\s,])pp?\.\s*(" + _PAGES
                     + r")(?![A-Za-z0-9])|第\s*(" + _PAGES + r")\s*页)")
QUOTE_RES = [re.compile(r"“([^“”]{20,2000}?)”"), re.compile(r"「([^「」]{20,2000}?)」")]
ANCHOR_TOKEN_RE = re.compile(r"(?:(?P<file>[^\s`'\"()\[\]<>]*?\.md))?#(?P<anc>[\w\-]+(?:<[^<>\s]+>[\w\-]*)?)")
LEDGER_WORD_RE = re.compile(r"ledger|账本|台账", re.I)
RANGE_SEP_RE = re.compile(r"^[`\s]*(?:…|\.\.\.|to|through|–|—|~|至|到)[`\s]*$")
RANGE_END_RE = re.compile(r"^(.*?)(\d+|[a-z])$")
MD_FILE_RE = re.compile(r"[^\s`'\"()\[\]<>]+\.md\b")
ALLOWANCES = {
    "frontmatter-date": "front matter may differ in its date line only",
    "frontmatter": "front matter may differ except name: and type:",
    "activation-numbers": "Activation Rules may differ in numbers only",
    "activation-disclaimer": "Activation Rules may rewrite the first-activation disclaimer line(s)",
}
FM_DATE_RE = re.compile(r"^(?:researched|updated|date|last[_-]?updated|调研时间|更新时间)\s*[:：]", re.I)
FM_KEEP_RE = re.compile(r"^(?:name|type)\s*:", re.I)
NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)*")
DISCLAIMER_RE = re.compile(r"disclaimer|first[ -]activation|免责|首次激活", re.I)


def norm_ws(s: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()


def frontmatter(text: str) -> str | None:
    if not text.startswith("---"):
        return None
    m = re.match(r"---[ \t]*\r?\n.*?\r?\n(?:---|\.\.\.)[ \t]*(?:\r?\n|$)", text, re.S)
    return m.group(0) if m else None


def sections(text: str, names: tuple[str, ...]) -> list[str]:
    """标题文字以 names 之一开头（不分大小写）的各节原文：从标题行到下一个同级或更高级标题之前。"""
    lines = text.splitlines(keepends=True)
    prose = prose_lines(text)  # 代码块、front matter 里的 # 不算标题
    heads = []
    for i, line in enumerate(prose):
        m = re.match(r"^ {0,3}(#{1,6})[ \t]+(.*?)[ \t#]*$", line)
        if m:
            heads.append((i, len(m.group(1)), m.group(2).strip()))
    out = []
    for k, (i, level, title) in enumerate(heads):
        if not title.lower().startswith(names):
            continue
        end = next((j for j, lv, _ in heads[k + 1:] if lv <= level), len(lines))
        out.append("".join(lines[i:end]))
    return out


def page_units(pages: str) -> list[str]:
    units = []
    for u in re.split(r"\s*,\s*", pages.strip()):
        u = re.sub(r"\s*[-–—]\s*", "-", u.strip())
        if u:
            units.append(u)
    return units


def citations(text: str) -> dict[str, set[str]]:
    cites: dict[str, set[str]] = {}
    for m in CITE_RE.finditer(text):
        cites.setdefault(m.group(1), set()).update(page_units(m.group(2) or m.group(3)))
    return cites


def quotes(text: str) -> list[str]:
    """≥20 字的引号内文字。直引号 "…" 在每行里按出现顺序两两配对（不会把两段引文之间的正文当成引文）。"""
    spans = [m.group(1) for rx in QUOTE_RES for m in rx.finditer(text)]
    for line in text.splitlines():
        parts = line.split('"')
        spans += parts[1:len(parts) - 1:2]  # 第 1、3、5… 段在一对直引号之内；最后一段没闭合就不要
    found: dict[str, None] = {}
    for s in spans:
        q = norm_ws(s)
        if len(q) >= 20:
            found.setdefault(q, None)
    return list(found)


def ledger_refs(skill_text: str, ledger_name: str) -> list[tuple[int, str]]:
    """SKILL.md 里指向账本的锚点 → [(行号, 锚点)]；范围已展开，占位写法原样保留。"""
    refs = []
    for no, line in enumerate(prose_lines(skill_text), 1):
        if ledger_name not in line and not LEDGER_WORD_RE.search(line):
            continue
        toks = []  # (start, end, anchor)，只收属于账本的
        for m in ANCHOR_TOKEN_RE.finditer(line):
            f, anc = m.group("file"), m.group("anc")
            if f:
                if Path(f).name == ledger_name:
                    toks.append((m.start(), m.end(), anc))
                continue
            if m.start() == 0 or line[m.start() - 1] != "`":
                continue  # 裸 #xxx 只在反引号里才当锚点（避免把 “#1” 之类的正文当锚点）
            before = line[:m.start()]
            files = MD_FILE_RE.findall(before)
            if files:
                if Path(files[-1]).name == ledger_name:
                    toks.append((m.start(), m.end(), anc))
            elif LEDGER_WORD_RE.search(before):
                toks.append((m.start(), m.end(), anc))
        for k, (_, _, anc) in enumerate(toks):
            refs.append((no, anc))
            if k + 1 < len(toks):
                gap = line[toks[k][1]:toks[k + 1][0]]
                a, b = RANGE_END_RE.match(anc), RANGE_END_RE.match(toks[k + 1][2])
                if RANGE_SEP_RE.match(gap) and a and b and a.group(1) == b.group(1):
                    lo, hi = a.group(2), b.group(2)
                    if lo.isdigit() and hi.isdigit():
                        mids = [str(i) for i in range(int(lo) + 1, int(hi))]
                    elif lo.isalpha() and hi.isalpha():
                        mids = [chr(c) for c in range(ord(lo) + 1, ord(hi))]
                    else:
                        mids = []
                    refs += [(no, a.group(1) + x) for x in mids]
    return refs


def fm_lines(fm: str, allow: set[str]) -> list[str]:
    """front matter 里要逐字比较的行：frontmatter-date 去掉日期行；frontmatter 只留 name: / type:。"""
    lines = fm.splitlines()
    if "frontmatter" in allow:
        return [ln for ln in lines if FM_KEEP_RE.match(ln)]
    if "frontmatter-date" in allow:
        return [ln for ln in lines if not FM_DATE_RE.match(ln)]
    return lines


def activation_view(sec: str, allow: set[str]) -> str:
    """Activation Rules 一节按放行项规整后的样子：数字换成 #，免责声明行去掉。"""
    if "activation-disclaimer" in allow:
        sec = "".join(ln for ln in sec.splitlines(keepends=True) if not DISCLAIMER_RE.search(ln))
    if "activation-numbers" in allow:
        sec = NUMBER_RE.sub("#", sec)
    return sec


def changed_lines(old: str, new: str, limit: int = 3) -> str:
    """两段文字里不同的行（给「~ allowed」信息行看），最多 limit 对。"""
    import difflib
    out = []
    for ln in difflib.unified_diff(old.splitlines(), new.splitlines(), lineterm="", n=0):
        if ln.startswith(("---", "+++", "@@")):
            continue
        out.append(ln.strip()[:160])
    return "; ".join(out[: 2 * limit]) + (" …" if len(out) > 2 * limit else "")


def is_placeholder(anc: str) -> bool:
    return "<" in anc or bool(re.search(r"-[A-Z]$", anc))


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("skill_dir", help="研究Skill目录（含 SKILL.md），也可直接给 SKILL.md")
    ap.add_argument("--before", default="", help="精简前的 SKILL.md 副本")
    ap.add_argument("--ledger", default="", help=f"证据账本路径（默认 <skill目录>/{LEDGER_REL.as_posix()}）")
    ap.add_argument("--allow", default="", metavar="ITEM,ITEM",
                    help="按设计会变、明确放行的差异（逗号分隔）：" + "；".join(f"{k} = {v}" for k, v in ALLOWANCES.items())
                    + "。需要 --before")
    ap.add_argument("--show", type=int, default=60, help="每类问题最多列几条（默认60）")
    a = ap.parse_args()
    allow = {x.strip() for x in a.allow.split(",") if x.strip()}
    unknown = sorted(allow - set(ALLOWANCES))
    if unknown:
        print(f"❌ --allow: unknown item(s) {', '.join(unknown)}; choose from {', '.join(ALLOWANCES)}", file=sys.stderr)
        sys.exit(2)
    if allow and not a.before:
        print("❌ --allow only makes sense with --before", file=sys.stderr)
        sys.exit(2)

    sk = Path(a.skill_dir)
    skill_md = sk if sk.is_file() else sk / "SKILL.md"
    sk = skill_md.parent
    if not skill_md.is_file():
        print(f"❌ no SKILL.md: {skill_md}", file=sys.stderr)
        sys.exit(2)
    ledger = Path(a.ledger) if a.ledger else sk / LEDGER_REL
    before_path = Path(a.before) if a.before else None
    if before_path and not before_path.is_file():
        print(f"❌ no such file: {before_path}", file=sys.stderr)
        sys.exit(2)

    new = skill_md.read_text(encoding="utf-8")
    led = ledger.read_text(encoding="utf-8") if ledger.is_file() else ""
    problems: dict[str, list[str]] = {}
    allowed: list[str] = []  # 放行的差异（--allow），只打印不计为问题

    def problem(kind: str, msg: str):
        problems.setdefault(kind, []).append(msg)

    # ---- 锚点 ----
    checker = Checker()
    refs = ledger_refs(new, ledger.name)
    have = checker.anchors(ledger) if ledger.is_file() else set()
    own = checker.anchors(skill_md)
    used: set[str] = set()
    for no, anc in refs:
        if is_placeholder(anc):
            prefix = re.split(r"<|-[A-Z]$", anc)[0]
            hits = {h for h in have if h.startswith(prefix)}
            used |= hits
            if not hits:
                problem("anchor", f"SKILL.md:{no}: #{anc} (placeholder; no ledger anchor starts with '{prefix}')")
        elif anc in have or anc.lower() in have:
            used.add(anc if anc in have else anc.lower())
        elif not ledger.is_file():
            problem("anchor", f"SKILL.md:{no}: #{anc} (ledger file missing: {ledger})")
        elif anc not in own and anc.lower() not in own:
            problem("anchor", f"SKILL.md:{no}: #{anc} (missing in {ledger.name})")

    # ---- 精简前 vs 精简后 ----
    stats = ""
    if before_path:
        old = before_path.read_text(encoding="utf-8")
        both = new + "\n" + led

        # 原样检查在前：通过 --allow 放行的区域（改过的 front matter / Activation Rules）记下来，
        # 只出现在这些区域里的卡片ID、引页、引文（例如免责声明本身就是一段引文）跟着放行，不算丢失
        kept = []
        regions: list[str] = []  # 精简前副本里被放行改动的原文
        fo, fn = frontmatter(old), frontmatter(new)
        if fo is not None:
            fm_allow = allow & {"frontmatter", "frontmatter-date"}
            if fo == fn:
                kept.append("front matter")
            elif fn is None:
                problem("verbatim", "front matter missing (the before copy has one)")
            elif fm_allow and fm_lines(fo, fm_allow) == fm_lines(fn, fm_allow):
                allowed.append(f"{'/'.join(sorted(fm_allow))}: {changed_lines(fo, fn)}")
                kept.append(f"front matter (allowed: {'/'.join(sorted(fm_allow))})")
                regions.append(fo)
            else:
                why = (" beyond what --allow " + ",".join(sorted(fm_allow)) + " permits") if fm_allow else ""
                problem("verbatim", f"front matter differs from the before copy{why}: {changed_lines(fo, fn)}")
        act_allow = allow & {"activation-numbers", "activation-disclaimer"}
        for label, names in PROTECTED.items():
            so, sn = sections(old, names), sections(new, names)
            if not so:
                continue
            if so == sn:
                kept.append(label)
                continue
            if label == "Activation Rules" and act_allow and len(so) == len(sn) and \
                    [activation_view(x, act_allow) for x in so] == [activation_view(x, act_allow) for x in sn]:
                allowed.append(f"{'/'.join(sorted(act_allow))}: {changed_lines(''.join(so), ''.join(sn))}")
                kept.append(f"{label} (allowed: {'/'.join(sorted(act_allow))})")
                regions += so
                continue
            what = "missing" if not sn else "differs"
            why = (" beyond what --allow " + ",".join(sorted(act_allow)) + " permits") \
                if label == "Activation Rules" and act_allow else ""
            detail = f": {changed_lines(''.join(so), ''.join(sn))}" if sn else ""
            problem("verbatim", f"section '{label}' {what}{why} (before: {len(so)} section(s), now: {len(sn)}){detail}")
        rest = old  # 精简前副本去掉放行区域后的部分：这里的东西一样都不能丢
        for r in regions:
            rest = rest.replace(r, "\n", 1)
        in_region = 0

        old_ids = set(CARD_ID_RE.findall(old))
        rest_ids = set(CARD_ID_RE.findall(rest))
        new_ids = set(CARD_ID_RE.findall(both))
        for i in sorted(old_ids - new_ids):
            if i in rest_ids:
                problem("card id", i)
            else:
                in_region += 1

        old_cites, rest_cites, new_cites = citations(old), citations(rest), citations(both)
        n_cites = 0
        for cid, pages in sorted(old_cites.items()):
            for p in sorted(pages):
                n_cites += 1
                if p not in new_cites.get(cid, set()):
                    if p in rest_cites.get(cid, set()):
                        problem("cited page", f"{cid} {'pp.' if '-' in p else 'p.'} {p}")
                    else:
                        in_region += 1

        nb, nrest = norm_ws(both), norm_ws(rest)
        old_quotes = quotes(old)
        for q in old_quotes:
            if q not in nb:
                if q in nrest or not regions:
                    problem("quote", f"“{q[:200]}{'…' if len(q) > 200 else ''}”")
                else:
                    in_region += 1
        if in_region:
            allowed.append(f"{in_region} card id / cited page / quote item(s) of the before copy lived only in the "
                           f"allowed region(s) above and changed with them")
        stats = (f"; before: {len(old_ids)} card ids, {n_cites} cited pages, {len(old_quotes)} quotes, "
                 f"verbatim: {', '.join(kept) or 'none found'}")

    # ---- 输出 ----
    n_bad = sum(len(v) for v in problems.values())
    for kind, msgs in problems.items():
        for msg in msgs[: a.show]:
            print(f"  ✗ {kind}: {msg}")
        if len(msgs) > a.show:
            print(f"  … {len(msgs) - a.show} more {kind} problems")
    for msg in allowed:
        print(f"  ~ allowed {msg}")
    if ledger.is_file():
        explicit = set(HTML_ANCHOR_RE.findall("\n".join(prose_lines(led))))
        pool = explicit or have  # 有 <a id> 时只统计显式锚点，否则统计标题锚点
        unused = sorted(pool - used - {x.lower() for x in used})
        print(f"ledger: {len(pool)} {'<a id> ' if explicit else 'heading '}anchors, "
              f"{len(pool) - len(unused)} referenced from SKILL.md, {len(unused)} not referenced (info only)"
              + (f": {', '.join(unused[:12])}{' …' if len(unused) > 12 else ''}" if unused else ""))
    else:
        print(f"ledger: none at {ledger}" + (" (SKILL.md refers to it)" if refs else ""))
    mark = "❌" if n_bad else "✅"
    counts = ", ".join(f"{len(v)} {k}" for k, v in problems.items())
    print(f"{mark} {skill_md}: {len(refs)} ledger anchor refs{stats}"
          + (f" — {n_bad} problems ({counts})" if n_bad else ""))
    sys.exit(1 if n_bad else 0)


if __name__ == "__main__":
    main()
