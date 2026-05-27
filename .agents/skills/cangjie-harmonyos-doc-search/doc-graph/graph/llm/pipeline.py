"""LLM 增强流水线编排 — 并发处理。"""
from __future__ import annotations

import json
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

from graph.llm.enhancer import create_batches, call_llm, merge_llm_results, MAX_BATCH_CHARS


def _process_single_batch(
    batch_idx: int,
    batch: list[tuple[str, str]],
    nodes_dict: dict,
    graph_data: dict[str, Any],
    output_path: Path | None,
) -> tuple[int, int, int]:
    """处理单个批次，返回 (batch_idx, merged_count, batch_size)。"""
    from graph.llm.enhancer import build_batch_prompt
    
    prompt = build_batch_prompt(batch)
    result = None
    for retry in range(3):
        result = call_llm(prompt)
        if result:
            break
        time.sleep(2)

    if not result:
        return (batch_idx, 0, len(batch))

    merged = merge_llm_results(nodes_dict, result)
    
    # 回写 nodes list 到 graph_data
    if isinstance(graph_data.get("nodes"), list):
        graph_data["nodes"] = list(nodes_dict.values())
    
    return (batch_idx, merged, len(batch))


def enhance_graph_from_files(
    graph_data: dict[str, Any],
    source_files: list[str],
    docs_dir: Path,
    batch_chars: int = MAX_BATCH_CHARS,
    batch_limit: int = 0,
    resume: bool = True,
    checkpoint_interval: int = 10,
    max_workers: int = 5,
    output_path: Path | None = None,
    total_timeout: int = 0,
) -> dict[str, Any]:
    nodes = graph_data.get("nodes", [])
    if isinstance(nodes, list):
        nodes_dict = {i: n for i, n in enumerate(nodes)}
    else:
        nodes_dict = nodes

    files_to_enhance = []
    if resume:
        for sf in source_files:
            found = False
            for node in nodes_dict.values():
                nsf = node.get("source_file", "")
                if nsf == sf or nsf.endswith(sf) or sf.endswith(nsf):
                    if node.get("llm_enhanced"):
                        found = True
                        break
            if not found:
                files_to_enhance.append(sf)
    else:
        files_to_enhance = source_files

    print(f"待增强文档: {len(files_to_enhance)} / {len(source_files)}")

    if not files_to_enhance:
        print("所有目标文档已增强，跳过。")
        return graph_data

    batches = create_batches(files_to_enhance, docs_dir, batch_chars)
    total_batches_all = len(batches)
    print(f"分批策略: {total_batches_all} 个批次 (容量 {batch_chars} chars, 并发 {max_workers})")

    if batch_limit > 0:
        batches = batches[:batch_limit]
        print(f"批次限制: 本次只处理前 {batch_limit} 个批次")

    enhanced_count = 0
    failed_count = 0
    total_docs = sum(len(b) for b in batches)
    processed_docs = 0
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        for batch_idx, batch in enumerate(batches, 1):
            future = executor.submit(
                _process_single_batch,
                batch_idx, batch, nodes_dict, graph_data, output_path,
            )
            futures[future] = batch_idx

        for future in as_completed(futures):
            # 检查总超时
            if total_timeout > 0 and (time.time() - start_time) > total_timeout:
                print("\n  [总超时] 达到预设时间限制，停止处理。")
                executor.shutdown(wait=False, cancel_futures=True)
                break

            batch_idx, merged, batch_size = future.result()
            processed_docs += batch_size
            
            if merged > 0:
                enhanced_count += merged
            else:
                failed_count += batch_size

            # 每批次完成后立即保存，防止中断丢失数据
            if isinstance(graph_data.get("nodes"), list):
                graph_data["nodes"] = list(nodes_dict.values())
            _save_graph(graph_data, output_path)

            # 进度输出
            elapsed = time.time() - start_time
            progress = (processed_docs / total_docs) * 100 if total_docs > 0 else 0
            avg_time = elapsed / processed_docs if processed_docs > 0 else 0
            remaining = avg_time * (total_docs - processed_docs)
            print(f"\r  进度: {progress:.1f}% | {processed_docs}/{total_docs} | 成功: {enhanced_count} | 失败: {failed_count} | 耗时: {elapsed:.0f}s | 预计剩余: {remaining:.0f}s", end="", flush=True)

    print()  # 换行
    _save_graph(graph_data, output_path)

    elapsed = time.time() - start_time
    print(f"\n增强完成! 成功: {enhanced_count} | 失败: {failed_count} | 总耗时: {elapsed:.0f}s")
    if batch_limit > 0:
        remaining_batches = total_batches_all - len(batches)
        if remaining_batches > 0:
            print(f"  提示: 还有 {remaining_batches} 个批次未处理，再次运行继续")

    return graph_data


def _save_graph(graph_data: dict, output_path: Path | None) -> None:
    if output_path is None:
        return
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(graph_data, f, ensure_ascii=False, indent=2)
