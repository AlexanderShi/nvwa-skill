#!/usr/bin/env python3
"""
自动检查生成的SKILL.md是否通过Phase 4质量标准。
对照通过标准表格逐项检查，输出通过/不通过和具体原因。

支持两种模式（默认从frontmatter自动识别）：
- persona：人物Skill（心智模型/表达DNA/诚实边界...）
- research：研究Skill（frontmatter含 type: research-craft 或 name 以 -research-craft 结尾），
  检查研究方法/操作步骤/言行一致/研究品味/阶段工作流/代表作解剖/研究诚信规则

用法:
    python3 quality_check.py <SKILL.md路径> [--mode persona|research]

示例:
    python3 quality_check.py .claude/skills/elon-musk-perspective/SKILL.md
    python3 quality_check.py .claude/skills/hamming-research-craft/SKILL.md
"""

from __future__ import annotations

import sys
import re
from pathlib import Path


def get_section(content: str, pattern: str) -> str | None:
    """取出标题匹配pattern的 ## 章节正文（到下一个 ## 为止）。"""
    m = re.search(rf'^##\s+[^\n]*(?:{pattern})[^\n]*\n(.*?)(?=^##\s|\Z)', content, re.DOTALL | re.MULTILINE | re.IGNORECASE)
    return m.group(1) if m else None


def count_list_items(text: str) -> int:
    """无序列表和有序列表都计数。"""
    return len(re.findall(r'^\s*(?:[-*]|\d+[.)、])\s+', text, re.MULTILINE))


def check_mental_models(content: str) -> tuple[bool, str]:
    """检查心智模型数量（3-7个）"""
    # 匹配 ### 模型N: 或 ### N. 等模式
    models = re.findall(r'^###\s+(?:模型|Model|心智模型)\s*\d', content, re.MULTILINE)
    if not models:
        # fallback: 数「### 」开头的行在心智模型section中
        in_section = False
        count = 0
        for line in content.split('\n'):
            if re.match(r'^##\s+.*心智模型|Mental Model', line, re.IGNORECASE):
                in_section = True
                continue
            if in_section and re.match(r'^##\s+', line) and '心智模型' not in line:
                break
            if in_section and re.match(r'^###\s+', line):
                count += 1
        if count > 0:
            passed = 3 <= count <= 7
            return passed, f"{count}个心智模型 {'✅' if passed else '❌ (应为3-7个)'}"

    count = len(models)
    if count == 0:
        return False, "未检测到心智模型section"
    passed = 3 <= count <= 7
    return passed, f"{count}个心智模型 {'✅' if passed else '❌ (应为3-7个)'}"


def check_limitations(content: str) -> tuple[bool, str]:
    """检查每个模型是否有局限性"""
    has_limitation = bool(re.search(r'局限|失效|不适用|盲区|limitation|blind spot', content, re.IGNORECASE))
    return has_limitation, "有局限性标注 ✅" if has_limitation else "❌ 未找到局限性描述"


def check_expression_dna(content: str) -> tuple[bool, str]:
    """检查表达DNA辨识度"""
    dna_section = bool(re.search(r'表达DNA|Expression DNA|表达风格', content, re.IGNORECASE))
    if not dna_section:
        return False, "❌ 未找到表达DNA section"

    # 检查是否有具体的风格描述（句式、词汇等）
    style_markers = len(re.findall(r'句式|词汇|语气|幽默|节奏|确定性|引用|口头禅', content))
    passed = style_markers >= 3
    return passed, f"表达DNA特征: {style_markers}项 {'✅' if passed else '❌ (应≥3项)'}"


def check_honest_boundary(content: str) -> tuple[bool, str]:
    """检查诚实边界（至少3条）"""
    # 找诚实边界section
    boundary_match = re.search(r'(?:##\s+.*诚实边界|## Honest Boundary)(.*?)(?=\n##\s|\Z)', content, re.DOTALL | re.IGNORECASE)
    if not boundary_match:
        return False, "❌ 未找到诚实边界section"

    boundary_text = boundary_match.group(1)
    # 计算列表项
    count = count_list_items(boundary_text)
    passed = count >= 3
    return passed, f"诚实边界: {count}条 {'✅' if passed else '❌ (应≥3条)'}"


def check_tensions(content: str) -> tuple[bool, str]:
    """检查内在张力（至少2对）"""
    tension_markers = len(re.findall(r'张力|矛盾|tension|paradox|一方面.*另一方面|既.*又', content, re.IGNORECASE))
    passed = tension_markers >= 2
    return passed, f"内在张力: {tension_markers}处 {'✅' if passed else '❌ (应≥2处)'}"


def check_primary_sources(content: str) -> tuple[bool, str]:
    """检查一手来源占比"""
    # 找调研来源section
    source_section = re.search(r'(?:##\s+.*来源|## Source|## Reference)(.*?)(?=\n##\s|\Z)', content, re.DOTALL | re.IGNORECASE)
    if not source_section:
        return True, "未找到来源section（跳过检查）"

    source_text = source_section.group(1)
    primary = len(re.findall(r'一手|primary|本人著作|原始', source_text, re.IGNORECASE))
    secondary = len(re.findall(r'二手|secondary|转述|评论', source_text, re.IGNORECASE))
    total = primary + secondary
    if total == 0:
        return True, "未标记来源类型（跳过检查）"

    ratio = primary / total
    passed = ratio > 0.5
    return passed, f"一手来源占比: {primary}/{total} ({ratio:.0%}) {'✅' if passed else '❌ (应>50%)'}"


# ---------- 研究Skill检查 ----------

def split_methods(content: str) -> list[str]:
    """把「核心研究方法」章节切成每个 ### 方法 的正文块。"""
    section = get_section(content, r'研究方法|Research Method')
    if not section:
        return []
    return [b for b in re.split(r'^###\s+', section, flags=re.MULTILINE)[1:] if b.strip()]


def check_research_methods(content: str) -> tuple[bool, str]:
    """核心研究方法 3-7 个"""
    methods = split_methods(content)
    if not methods:
        return False, "❌ 未找到「核心研究方法」章节或其中没有 ### 方法"
    count = len(methods)
    passed = 3 <= count <= 7
    return passed, f"{count}个研究方法 {'✅' if passed else '❌ (应为3-7个)'}"


def check_method_steps(content: str) -> tuple[bool, str]:
    """每个方法都有可执行的操作步骤（≥2步）"""
    methods = split_methods(content)
    if not methods:
        return False, "❌ 无研究方法可检查"
    missing = []
    for block in methods:
        steps = re.search(r'(?:操作步骤|Steps?)[^\n]*\n(.*?)(?=\n\*\*|\Z)', block, re.DOTALL | re.IGNORECASE)
        if not steps or len(re.findall(r'^\s*\d+[.)、]\s+', steps.group(1), re.MULTILINE)) < 2:
            missing.append(block.split('\n', 1)[0].strip()[:20])
    passed = not missing
    return passed, ("每个方法都有≥2步操作步骤 ✅" if passed
                    else f"❌ 缺可执行步骤: {', '.join(missing)}")


def check_say_do(content: str) -> tuple[bool, str]:
    """每个方法标注言行一致性（自述 vs 实践证据）"""
    methods = split_methods(content)
    if not methods:
        return False, "❌ 无研究方法可检查"
    marked = sum(bool(re.search(r'言行一致|实践[：:]|say.?do', b, re.IGNORECASE)) for b in methods)
    passed = marked == len(methods)
    return passed, f"言行一致标注: {marked}/{len(methods)} {'✅' if passed else '❌ (每个方法都要对照自述与实践证据)'}"


def check_taste(content: str) -> tuple[bool, str]:
    """研究品味章节，含≥3条判据"""
    section = get_section(content, r'研究品味|Research Taste')
    if not section:
        return False, "❌ 未找到「研究品味」章节"
    count = count_list_items(section)
    passed = count >= 3
    return passed, f"研究品味条目: {count} {'✅' if passed else '❌ (应≥3条)'}"


def check_workflows(content: str) -> tuple[bool, str]:
    """≥3个阶段工作流，且有检查点"""
    section = get_section(content, r'阶段工作流|Workflows?')
    if not section:
        return False, "❌ 未找到「阶段工作流」章节"
    count = len(re.findall(r'^###\s+', section, re.MULTILINE))
    checkpoints = len(re.findall(r'检查点|CHECKPOINT|止损', section, re.IGNORECASE))
    passed = count >= 3 and checkpoints >= 1
    return passed, (f"阶段工作流: {count}个，检查点{checkpoints}处 "
                    f"{'✅' if passed else '❌ (应≥3个工作流且含检查点)'}")


def check_signature_works(content: str) -> tuple[bool, str]:
    """≥2篇代表作解剖"""
    section = get_section(content, r'代表作解剖|Signature Work')
    if not section:
        return False, "❌ 未找到「代表作解剖」章节"
    count = len(re.findall(r'^###\s+', section, re.MULTILINE))
    passed = count >= 2
    return passed, f"代表作解剖: {count}篇 {'✅' if passed else '❌ (应≥2篇)'}"


def check_integrity(content: str) -> tuple[bool, str]:
    """研究诚信规则：至少覆盖不编造引用"""
    section = get_section(content, r'研究诚信|Research Integrity')
    if not section:
        return False, "❌ 未找到「研究诚信规则」章节"
    has_citation = bool(re.search(r'引用|citation', section, re.IGNORECASE))
    return has_citation, "研究诚信规则含引用核实 ✅" if has_citation else "❌ 研究诚信规则未覆盖「不编造引用」"


def check_citations(content: str) -> tuple[bool, str]:
    """引用可核实：来源附录中有DOI/arXiv/URL标识"""
    section = get_section(content, r'调研来源|来源|Source|Reference')
    if not section:
        return False, "❌ 未找到调研来源章节"
    ids = set(re.findall(r'https?://[^\s\)]+|arXiv:\s*\d{4}\.\d{4,5}|\b10\.\d{4,9}/[^\s\)\]|,;]+', section, re.IGNORECASE))
    passed = len(ids) >= 5
    return passed, f"可核实标识(URL/DOI/arXiv): {len(ids)}个 {'✅' if passed else '❌ (应≥5个)'}"


PERSONA_CHECKS = [
    ("心智模型数量", check_mental_models),
    ("模型局限性", check_limitations),
    ("表达DNA辨识度", check_expression_dna),
    ("诚实边界", check_honest_boundary),
    ("内在张力", check_tensions),
    ("一手来源占比", check_primary_sources),
]

RESEARCH_CHECKS = [
    ("研究方法数量", check_research_methods),
    ("方法可执行", check_method_steps),
    ("言行一致", check_say_do),
    ("方法局限性", check_limitations),
    ("研究品味", check_taste),
    ("阶段工作流", check_workflows),
    ("代表作解剖", check_signature_works),
    ("研究诚信规则", check_integrity),
    ("诚实边界", check_honest_boundary),
    ("内在张力", check_tensions),
    ("引用可核实", check_citations),
    ("一手来源占比", check_primary_sources),
]


def detect_mode(content: str) -> str:
    front = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    head = front.group(1) if front else ''
    if re.search(r'^type:\s*research-craft\s*$', head, re.MULTILINE) or \
            re.search(r'^name:\s*\S+-research-craft\s*$', head, re.MULTILINE):
        return 'research'
    return 'persona'


def main():
    args = sys.argv[1:]
    mode = None
    if '--mode' in args:
        i = args.index('--mode')
        mode = args[i + 1] if i + 1 < len(args) else None
        args = args[:i] + args[i + 2:]
        if mode not in ('persona', 'research'):
            print(f"❌ 未知模式: {mode}（可选: persona, research）")
            sys.exit(1)
    if not args:
        print("用法: python3 quality_check.py <SKILL.md路径> [--mode persona|research]")
        sys.exit(1)

    skill_path = Path(args[0])
    if not skill_path.exists():
        print(f"❌ 文件不存在: {skill_path}")
        sys.exit(1)

    content = skill_path.read_text(encoding='utf-8')
    mode = mode or detect_mode(content)
    checks = RESEARCH_CHECKS if mode == 'research' else PERSONA_CHECKS

    print(f"质量检查: {skill_path.name}（{'研究Skill' if mode == 'research' else '人物Skill'}）")
    print("=" * 50)

    passed_count = 0
    total = len(checks)

    for name, check_fn in checks:
        passed, detail = check_fn(content)
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {name:<12} {status}  {detail}")
        if passed:
            passed_count += 1

    print("=" * 50)
    print(f"结果: {passed_count}/{total} 通过")

    if passed_count == total:
        print("🎉 全部通过，可以交付")
    elif passed_count >= total - 1:
        print("⚠️ 基本通过，建议修复不通过项后交付")
    else:
        print("❌ 多项不通过，建议回到Phase 2迭代")

    sys.exit(0 if passed_count == total else 1)


if __name__ == '__main__':
    main()
