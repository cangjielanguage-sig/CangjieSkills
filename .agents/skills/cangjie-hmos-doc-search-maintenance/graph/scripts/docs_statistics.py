#!/usr/bin/env python3
"""统计 docs 目录下所有文档的字数。

统计规则：
- 中文：按字统计
- 英文：按单词统计
- 符号：单独统计

输出：总数 + 各文件详情
"""

import re
from pathlib import Path
from collections import defaultdict

MAINTENANCE_DIR = Path(__file__).resolve().parent.parent.parent
SEARCH_SKILL_DIR = MAINTENANCE_DIR.parent / "cangjie-hmos-doc-search"
DOCS_DIR = SEARCH_SKILL_DIR / "docs"


def count_content(content: str) -> dict:
    """统计内容的中文、英文、符号数量。"""
    # 中文字符（包括中文标点）
    chinese_pattern = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff\uff00-\uffef]')
    chinese_chars = chinese_pattern.findall(content)
    
    # 英文单词（连续的英文字母）
    english_pattern = re.compile(r'[a-zA-Z]+')
    english_words = english_pattern.findall(content)
    
    # 符号（排除中文和英文后的其他字符）
    # 包括：空格、换行、数字、标点符号、特殊字符等
    all_chars = content
    # 移除中文和英文
    remaining = chinese_pattern.sub('', all_chars)
    remaining = english_pattern.sub('', remaining)
    
    # 统计各类符号
    symbols = {
        '空格': len([c for c in remaining if c == ' ']),
        '换行': len([c for c in remaining if c == '\n']),
        '数字': len([c for c in remaining if c.isdigit()]),
        '标点符号': len([c for c in remaining if c in '.,;:!?\'"()[]{}<>@#$%^&*+-=_/\\|~`']),
        '其他符号': len([c for c in remaining if c not in ' \n' and not c.isdigit() and c not in '.,;:!?\'"()[]{}<>@#$%^&*+-=_/\\|~`']),
    }
    
    return {
        'chinese_chars': len(chinese_chars),
        'english_words': len(english_words),
        'symbols': symbols,
        'total_symbols': len(remaining),
    }


def analyze_docs():
    """分析 docs 目录下所有文档。"""
    
    # 按子目录统计
    dir_stats = defaultdict(lambda: {
        'files': 0,
        'chinese_chars': 0,
        'english_words': 0,
        'symbols': defaultdict(int),
        'total_symbols': 0,
    })
    
    # 总统计
    total_stats = {
        'files': 0,
        'chinese_chars': 0,
        'english_words': 0,
        'symbols': defaultdict(int),
        'total_symbols': 0,
    }
    
    # 文件详情
    file_details = []
    
    # 遍历所有 .md 文件
    md_files = list(DOCS_DIR.rglob("*.md"))
    
    print(f"正在分析 {len(md_files)} 个文档文件...")
    
    for filepath in md_files:
        # 读取文件
        try:
            content = filepath.read_text(encoding='utf-8')
        except Exception as e:
            print(f"  警告: 无法读取 {filepath}: {e}")
            continue
        
        # 统计
        stats = count_content(content)
        
        # 确定子目录（docs 下的第一级目录）
        relative_path = filepath.relative_to(DOCS_DIR)
        if len(relative_path.parts) > 1:
            subdir = relative_path.parts[0]
        else:
            subdir = "root"
        
        # 更新子目录统计
        dir_stats[subdir]['files'] += 1
        dir_stats[subdir]['chinese_chars'] += stats['chinese_chars']
        dir_stats[subdir]['english_words'] += stats['english_words']
        for key, value in stats['symbols'].items():
            dir_stats[subdir]['symbols'][key] += value
        dir_stats[subdir]['total_symbols'] += stats['total_symbols']
        
        # 更新总统计
        total_stats['files'] += 1
        total_stats['chinese_chars'] += stats['chinese_chars']
        total_stats['english_words'] += stats['english_words']
        for key, value in stats['symbols'].items():
            total_stats['symbols'][key] += value
        total_stats['total_symbols'] += stats['total_symbols']
        
        # 记录文件详情（只记录较大的文件）
        if stats['chinese_chars'] > 100 or stats['english_words'] > 50:
            file_details.append({
                'path': str(relative_path),
                'chinese': stats['chinese_chars'],
                'english': stats['english_words'],
                'symbols': stats['total_symbols'],
            })
    
    # 输出结果
    print("\n" + "=" * 80)
    print("docs 目录文档统计报告")
    print("=" * 80)
    
    print(f"\n总计: {total_stats['files']} 个文件")
    print(f"\n{'类别':<15} {'数量':>15}")
    print("-" * 35)
    print(f"{'中文字符':<15} {total_stats['chinese_chars']:>15,}")
    print(f"{'英文单词':<15} {total_stats['english_words']:>15,}")
    print(f"{'符号总数':<15} {total_stats['total_symbols']:>15,}")
    
    print(f"\n符号分类统计:")
    print(f"{'符号类型':<15} {'数量':>15}")
    print("-" * 35)
    for key, value in sorted(total_stats['symbols'].items(), key=lambda x: -x[1]):
        print(f"{key:<15} {value:>15,}")
    
    print(f"\n按子目录统计:")
    print(f"{'子目录':<25} {'文件数':>10} {'中文':>12} {'英文':>12} {'符号':>12}")
    print("-" * 75)
    
    for subdir, stats in sorted(dir_stats.items(), key=lambda x: -x[1]['chinese_chars']):
        print(f"{subdir:<25} {stats['files']:>10} {stats['chinese_chars']:>12,} {stats['english_words']:>12,} {stats['total_symbols']:>12,}")
    
    print(f"\n主要文件（中文>100 或 英文>50）:")
    print(f"{'文件路径':<50} {'中文':>10} {'英文':>10} {'符号':>10}")
    print("-" * 80)
    
    # 只显示前20个大文件
    for detail in sorted(file_details, key=lambda x: -(x['chinese'] + x['english']))[:20]:
        path_display = detail['path'][:47] + '...' if len(detail['path']) > 50 else detail['path']
        print(f"{path_display:<50} {detail['chinese']:>10} {detail['english']:>10} {detail['symbols']:>10}")
    
    # 保存详细报告到 JSON
    import json
    report = {
        'total': {
            'files': total_stats['files'],
            'chinese_chars': total_stats['chinese_chars'],
            'english_words': total_stats['english_words'],
            'symbols': dict(total_stats['symbols']),
            'total_symbols': total_stats['total_symbols'],
        },
        'by_directory': {
            subdir: {
                'files': stats['files'],
                'chinese_chars': stats['chinese_chars'],
                'english_words': stats['english_words'],
                'symbols': dict(stats['symbols']),
                'total_symbols': stats['total_symbols'],
            }
            for subdir, stats in dir_stats.items()
        },
        'file_details': file_details[:50],  # 只保存前50个
    }
    
    output_path = DOCS_DIR.parent / "scripts" / "docs_statistics.json"
    output_path.parent.mkdir(exist_ok=True)
    with output_path.open('w', encoding='utf-8') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    
    print(f"\n详细报告已保存到: {output_path}")
    
    return report


if __name__ == "__main__":
    analyze_docs()