#!/usr/bin/env python3
"""
合并6个Agent的调研结果，生成Phase 1.5调研Review检查点的摘要表格。
扫描 references/research/ 目录下的01-06 md文件，统计每个维度的来源数量、
一手/二手占比、关键发现。

支持两种模式（默认按目录里的文件名自动识别）：
- persona：人物Skill（01-writings ... 06-timeline）
- research：研究Skill（01-publications ... 06-trajectory），来源数额外统计DOI/arXiv ID

用法:
    python3 merge_research.py <skill目录路径> [--mode persona|research]

示例:
    python3 merge_research.py .claude/skills/elon-musk-perspective
    python3 merge_research.py .claude/skills/hamming-research-craft --mode research

输出: 打印markdown格式的摘要表格到stdout
"""

import sys
import re
from pathlib import Path

MODES = {
    'persona': {
        '01-writings': '著作',
        '02-conversations': '对话',
        '03-expression-dna': '表达',
        '04-external-views': '他者',
        '05-decisions': '决策',
        '06-timeline': '时间线',
    },
    'research': {
        '01-publications': '代表作',
        '02-methodology': '方法论自述',
        '03-process-evidence': '过程证据',
        '04-mentorship': '学生合作者',
        '05-peer-critique': '同行批评',
        '06-trajectory': '研究轨迹',
    },
}
AGENTS = MODES['persona']

ARXIV_RE = re.compile(r'\barXiv:\s*(\d{4}\.\d{4,5})', re.IGNORECASE)
DOI_RE = re.compile(r'\b(10\.\d{4,9}/[^\s\)\]\|,;]+)')


def detect_mode(research_dir: Path) -> str:
    """按两种模式各自命中的文件数判断，平局按persona处理（兼容旧目录）。"""
    hits = {m: sum((research_dir / f"{k}.md").exists() for k in agents) for m, agents in MODES.items()}
    return 'research' if hits['research'] > hits['persona'] else 'persona'


def count_sources(content: str, mode: str = 'persona') -> dict:
    """统计来源数量和一手/二手占比"""
    # 计算URL数量作为来源数
    urls = re.findall(r'https?://[^\s\)]+', content)
    if mode == 'research':
        # 论文常以 arXiv:XXXX.XXXXX 或裸DOI引用而不带链接，也计为来源
        bare = re.sub(r'https?://[^\s\)]+', ' ', content)
        urls += [f"arxiv:{m}" for m in ARXIV_RE.findall(bare)]
        urls += [f"doi:{m.lower()}" for m in DOI_RE.findall(bare)]
        # 同一篇论文的链接和裸标识归一，避免重复计数
        urls = [f"doi:{u.split('doi.org/', 1)[1].lower()}" if 'doi.org/10.' in u
                else f"arxiv:{re.split(r'/(?:abs|pdf)/', u)[1].removesuffix('.pdf')}" if re.search(r'arxiv\.org/(?:abs|pdf)/\d', u)
                else u for u in urls]

    # 检测一手/二手标记
    primary_markers = len(re.findall(r'一手|primary|本人|原文|原始|直接引用', content, re.IGNORECASE))
    secondary_markers = len(re.findall(r'二手|secondary|转述|总结|评论|分析', content, re.IGNORECASE))

    return {
        'url_count': len(urls),
        'unique_urls': len(set(urls)),
        'primary_markers': primary_markers,
        'secondary_markers': secondary_markers,
    }


def extract_key_findings(content: str, max_items: int = 3) -> list[str]:
    """提取关键发现（取前几个二级标题或加粗项）"""
    # 尝试提取##标题
    headings = re.findall(r'^##\s+(.+)$', content, re.MULTILINE)
    if headings:
        return headings[:max_items]

    # fallback: 提取加粗项
    bolds = re.findall(r'\*\*(.+?)\*\*', content)
    if bolds:
        return bolds[:max_items]

    # fallback: 取前3个非空行
    lines = [l.strip() for l in content.split('\n') if l.strip() and not l.startswith('#')]
    return [l[:50] + '...' if len(l) > 50 else l for l in lines[:max_items]]


def find_contradictions(files: dict[str, str], agents: dict = AGENTS) -> list[str]:
    """简单检测跨文件矛盾（同一关键词出现不同判断）"""
    contradictions = []
    # 检测「但是」「然而」「相反」「矛盾」等矛盾标记
    for name, content in files.items():
        matches = re.findall(r'(?:矛盾|相反|但实际上|然而.*?不同|争议).{0,100}', content)
        for m in matches:
            contradictions.append(f"{agents.get(name, name)}: {m[:80]}")
    return contradictions[:5]  # 最多5条


def main():
    args = sys.argv[1:]
    mode = None
    if '--mode' in args:
        i = args.index('--mode')
        mode = args[i + 1] if i + 1 < len(args) else None
        args = args[:i] + args[i + 2:]
        if mode not in MODES:
            print(f"❌ 未知模式: {mode}（可选: {', '.join(MODES)}）")
            sys.exit(1)
    if not args:
        print("用法: python3 merge_research.py <skill目录路径> [--mode persona|research]")
        sys.exit(1)

    skill_dir = Path(args[0])
    research_dir = skill_dir / 'references' / 'research'

    if not research_dir.exists():
        print(f"❌ 目录不存在: {research_dir}")
        sys.exit(1)

    mode = mode or detect_mode(research_dir)
    agents = MODES[mode]
    print(f"模式: {'研究Skill' if mode == 'research' else '人物Skill'}")

    files = {}
    rows = []
    total_sources = 0
    total_primary = 0
    total_secondary = 0
    missing = []

    for key, label in agents.items():
        md_file = research_dir / f"{key}.md"
        if not md_file.exists():
            missing.append(label)
            rows.append(f"│ {label:<12} │ {'❌ 缺失':<8} │ {'—':<24} │")
            continue

        content = md_file.read_text(encoding='utf-8')
        files[key] = content
        stats = count_sources(content, mode)
        findings = extract_key_findings(content)

        total_sources += stats['unique_urls']
        total_primary += stats['primary_markers']
        total_secondary += stats['secondary_markers']

        findings_str = ', '.join(findings) if findings else '—'
        if len(findings_str) > 40:
            findings_str = findings_str[:37] + '...'

        rows.append(f"│ {label:<12} │ {stats['unique_urls']:<8} │ {findings_str:<24} │")

    # 矛盾检测
    contradictions = find_contradictions(files, agents)

    # 输出
    print("┌──────────────┬──────────┬──────────────────────────┐")
    print("│ Agent        │ 来源数量  │ 关键发现                  │")
    print("├──────────────┼──────────┼──────────────────────────┤")
    for row in rows:
        print(row)
    print("├──────────────┼──────────┼──────────────────────────┤")

    primary_ratio = f"{total_primary}/{total_primary + total_secondary}" if (total_primary + total_secondary) > 0 else "未标记"
    print(f"│ 总来源数      │ {total_sources:<8} │ 一手占比: {primary_ratio:<15} │")

    if contradictions:
        print(f"│ 矛盾点        │ {len(contradictions)}处      │ {contradictions[0][:24]:<24} │")
    else:
        print(f"│ 矛盾点        │ 0处      │ {'—':<24} │")

    if missing:
        print(f"│ 信息不足维度   │ {len(missing)}个      │ {', '.join(missing):<24} │")
    else:
        print(f"│ 信息不足维度   │ 无       │ {'—':<24} │")

    print("└──────────────┴──────────┴──────────────────────────┘")

    # 总结
    if total_sources < 10:
        print("\n⚠️ 总来源数 <10，建议降低期望或补充调研")
    if missing:
        print(f"\n⚠️ 缺失维度: {', '.join(missing)}，建议补充或在诚实边界中标注")
    if mode == 'research':
        core = [agents[k] for k in ('01-publications', '02-methodology', '03-process-evidence') if agents[k] in missing]
        if core:
            print(f"\n⚠️ 研究Skill最小可用集缺失: {', '.join(core)}——没有「自述 vs 过程证据」就无法做言行一致验证")


if __name__ == '__main__':
    main()
