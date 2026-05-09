#!/usr/bin/env python3
"""仓颉鸿蒙知识图谱 — 命令行工具。

用法：
    python cli.py search "List 组件"           # 搜索（定位文档）
    python cli.py traverse "List 组件"         # 图遍历（发现关联）
    python cli.py traverse "List 组件" --dfs   # DFS 遍历
    python cli.py path "UIAbility" "WindowStage"
    python cli.py explain "List"
    python cli.py neighbors "List"
    python cli.py god-nodes                    # 核心节点
    python cli.py surprises                    # 惊奇连接
    python cli.py questions                    # 建议问题
    python cli.py community 0                  # 社区详情
    python cli.py stats
    python cli.py analyze
    python cli.py optimize
    python cli.py graphs
"""

import argparse
import json
import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
_PROJECT_ROOT = Path(__file__).resolve().parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from query import create_session


def cmd_search(args):
    """执行搜索。"""
    session = create_session()
    result = session.search(args.query, limit=args.limit)

    print(f"\n查询: {args.query}")
    print(f"使用图谱: {result.graph_used}")
    print(f"耗时: {result.latency_ms:.1f}ms")
    print(f"找到 {len(result.paths)} 个结果\n")

    for i, path in enumerate(result.paths, 1):
        print(f"  {i}. {path}")

    if result.nodes:
        print(f"\n相关节点:")
        for node in result.nodes[:5]:
            layer_name = {1: "概念", 2: "API", 3: "实现"}.get(node.layer, "?")
            print(f"  [{layer_name}] {node.label}")

    if args.mark:
        session.mark_satisfied(args.query, args.mark == "good")
        print(f"\n已标记满意度: {args.mark}")


def cmd_path(args):
    """查找路径。"""
    session = create_session()
    path = session.find_path(args.node_a, args.node_b, max_depth=args.max_depth)

    print(f"\n路径: {args.node_a} → {args.node_b}")
    if path:
        for i, node in enumerate(path):
            layer_name = {1: "概念", 2: "API", 3: "实现"}.get(node.layer, "?")
            print(f"  {i+1}. [{layer_name}] {node.label}")
    else:
        print("  未找到路径")


def cmd_explain(args):
    """解释节点。"""
    session = create_session()
    info = session.explain(args.node)

    if info:
        print(f"\n节点: {info.label}")
        print(f"ID: {info.id}")
        layer_name = {1: "概念层", 2: "API 层", 3: "实现层"}.get(info.layer, "?")
        print(f"层级: {layer_name}")
        print(f"来源: {info.source_file}")
        print(f"连接数: {info.degree}")
        print(f"社区: {info.community}")

        neighbors = session.neighbors(args.node, max_count=10)
        if neighbors:
            print(f"\n关联节点 ({len(neighbors)} 个):")
            for n in neighbors:
                print(f"  - {n.label}")
    else:
        print(f"未找到节点: {args.node}")


def cmd_stats(args):
    """显示统计。"""
    session = create_session()
    stats = session.get_stats()

    print("\n=== 图谱统计 ===")
    mg = stats.get("merged_graph", {})
    if mg.get("loaded"):
        print(f"合并图谱: {mg['nodes']} 节点, {mg['edges']} 边")

    for name, sg in stats.get("subgraphs", {}).items():
        if sg.get("loaded"):
            print(f"子图谱 [{name}]: {sg['nodes']} 节点, {sg['edges']} 边")

    fb = stats.get("feedback", {})
    if fb:
        print(f"\n=== 使用统计 ===")
        print(f"总查询: {fb.get('total_queries', 0)}")
        print(f"失败查询: {fb.get('failed_queries', 0)}")
        if fb.get('satisfaction_rate') is not None:
            print(f"满意度: {fb['satisfaction_rate']:.0%}")

        hot = stats.get("hot_topics", [])
        if hot:
            print(f"\n热门查询:")
            for h in hot[:5]:
                print(f"  {h['count']}x: {h['query']}")


def cmd_analyze(args):
    """分析反馈。"""
    session = create_session()
    analysis = session.get_analysis()

    print("\n=== 反馈分析 ===")
    for suggestion in analysis.get("optimization_suggestions", []):
        print(f"  - {suggestion}")

    missed = analysis.get("missed_queries", [])
    if missed:
        print(f"\n未命中查询 (Top {len(missed)}):")
        for m in missed[:10]:
            print(f"  {m['miss_count']}x: {m['query']}")


def cmd_optimize(args):
    """执行优化。"""
    session = create_session()
    report = session.optimize()

    print("\n=== 优化报告 ===")
    print(f"新增边: {report.get('edges_added', 0)}")
    print(f"新增别名: {report.get('aliases_added', 0)}")
    for s in report.get("suggestions", []):
        print(f"  - {s}")


def cmd_graphs(args):
    """列出可用图谱。"""
    session = create_session()
    graphs = session.available_graphs()

    print("\n可用图谱:")
    for g in graphs:
        print(f"  - {g}")


def cmd_traverse(args):
    """图遍历。"""
    session = create_session()
    result = session.traverse(args.query, mode=args.mode, depth=args.depth, token_budget=args.budget)

    print(f"\n遍历: {args.query}")
    print(f"模式: {result.mode.upper()}, 深度: {result.depth}")
    print(f"起点: {result.start_nodes}")
    print(f"图谱: {result.graph_name}")
    print(f"找到 {len(result.nodes)} 个节点, {len(result.edges)} 条边")

    print("\n节点:")
    for node in result.nodes[:10]:
        layer_name = {1: "概念", 2: "API", 3: "实现"}.get(node.get("layer", 3), "?")
        print(f"  [{layer_name}] {node['label']} (度={node['degree']})")

    print("\n边:")
    for edge in result.edges[:10]:
        conf_str = f" [{edge['confidence']}]" if edge.get("confidence") else ""
        print(f"  {edge['source_label']} --{edge['relation']}{conf_str}--> {edge['target_label']}")

    if result.actual_tokens > result.token_budget:
        print(f"\n... 输出截断至 ~{result.token_budget} tokens")


def cmd_neighbors(args):
    """获取邻居节点。"""
    session = create_session()
    neighbors = session.neighbors(args.node, max_count=args.limit)

    print(f"\n节点 {args.node} 的邻居 ({len(neighbors)} 个):")
    for n in neighbors:
        print(f"  - {n.label}")


def cmd_god_nodes(args):
    """核心节点。"""
    session = create_session()
    nodes = session.god_nodes(top_n=args.top_n)

    print(f"\n核心节点 (Top {args.top_n}):")
    for i, node in enumerate(nodes, 1):
        print(f"  {i}. {node['label']} (度={node['degree']}, src={node['source_file']})")


def cmd_surprises(args):
    """惊奇连接。"""
    session = create_session()
    edges = session.surprises(top_n=args.top_n)

    print(f"\n惊奇连接 (跨社区边 Top {args.top_n}):")
    for i, edge in enumerate(edges, 1):
        print(f"  {i}. {edge['source_label']} (社区 {edge['source_community']}) → {edge['target_label']} (社区 {edge['target_community']})")


def cmd_questions(args):
    """建议问题。"""
    session = create_session()
    questions = session.suggest_questions(top_n=args.top_n)

    print(f"\n建议问题 (Top {args.top_n}):")
    for i, q in enumerate(questions, 1):
        print(f"  {i}. {q['question']}")
        print(f"     理由: {q['rationale']}")


def cmd_community(args):
    """社区详情。"""
    session = create_session()
    info = session.community_info(args.community_id)

    if "error" in info:
        print(f"\n{info['error']}")
        return

    print(f"\n社区 {args.community_id}:")
    print(f"  节点数: {info['node_count']}")
    print(f"  凝聚力: {info['cohesion']}")
    print(f"\n核心节点:")
    for node in info['top_nodes']:
        print(f"  {node['label']} (度={node['degree']})")


def cmd_search_with_neighbors(args):
    """搜索 + 邻居。"""
    session = create_session()
    result = session.search_with_neighbors(args.query, limit=args.limit, neighbor_count=args.neighbors)

    print(f"\n查询: {args.query}")
    print(f"找到 {len(result.paths)} 个结果")

    for i, path in enumerate(result.paths, 1):
        print(f"\n{i}. {path.get('label', path.get('node', ''))}")
        neighbors = path.get("neighbors", [])
        if neighbors:
            print(f"   关联节点:")
            for n in neighbors[:args.neighbors]:
                print(f"     - {n['label']} [{n['relation']}]")


def cmd_build(args):
    """构建图谱。完整流程：检测 → 提取 → 构建 → 聚类 → 分层 → 保存。对齐 graphify。"""
    from builders import detect, detect_incremental, build_from_json, build_merge, cluster, save_graph, assign_communities_to_nodes, annotate_layers, collect_files, extract, load_graph
    
    root = Path(args.path).resolve()
    deep_mode = args.mode == "deep"
    directed = args.directed
    
    default_output = root / "graphify-out" / "graph.json"
    output_path = Path(args.output) if args.output else default_output
    
    if args.cluster_only:
        if not output_path.exists():
            print(f"错误: 图谱不存在: {output_path}")
            print("  先运行 build 命令创建图谱")
            return
        
        print(f"\n重新聚类: {output_path}")
        G = load_graph(output_path)
        print(f"  节点: {G.number_of_nodes()}, 边: {G.number_of_edges()}")
        
        print("\n聚类...")
        communities = cluster(G)
        assign_communities_to_nodes(G, communities)
        print(f"  社区: {len(communities)}")
        
        save_graph(G, output_path)
        print(f"\n完成！图谱保存至: {output_path}")
        return
    
    print(f"\n扫描目录: {root}")
    
    if args.update:
        print("  增量更新模式")
        detected = detect_incremental(root)
        code_files = detected.get("new_files", {}).get("code", [])
        doc_files = detected.get("new_files", {}).get("document", [])
        print(f"  新增/变化: {detected.get('new_total', 0)} 文件")
        
        if detected.get('new_total', 0) == 0:
            print("  无变化，跳过")
            return
    else:
        detected = detect(root)
        code_files = detected.get("files", {}).get("code", [])
        doc_files = detected.get("files", {}).get("document", [])
    
    print(f"文件数: {detected['total_files']}")
    print(f"词数: ~{detected['total_words']}")
    
    if detected.get("warning"):
        print(f"警告: {detected['warning']}")
    
    extractions = []
    
    if code_files:
        print(f"\nAST 提取 ({len(code_files)} 个代码文件)...")
        if deep_mode:
            print("  深度模式：启用更激进的 INFERRED 边")
        
        try:
            import os
            orig_dir = os.getcwd()
            try:
                os.chdir(root)
                code_paths = collect_files(Path("."), root=Path("."))
            finally:
                os.chdir(orig_dir)
            
            if code_paths:
                code_paths = [root / p for p in code_paths]
                print(f"  找到 {len(code_paths)} 个代码文件")
                ast_result = extract(code_paths, cache_root=root)
                extractions.append(ast_result)
                print(f"  节点: {len(ast_result.get('nodes', []))}")
                print(f"  边: {len(ast_result.get('edges', []))}")
            else:
                print("  未找到代码文件")
        except ImportError as e:
            print(f"  警告: tree-sitter 未安装，跳过 AST 提取")
            print(f"  错误: {e}")
            print("  安装: pip install tree-sitter tree-sitter-python tree-sitter-cangjie")
        except Exception as e:
            print(f"  警告: AST 提取失败: {e}")
            import traceback
            traceback.print_exc()
    
    if doc_files:
        print(f"\n语义提取 ({len(doc_files)} 个文档文件)...")
        
        import os
        api_key = os.environ.get("OPENAI_API_KEY")
        
        if api_key:
            print("  使用 LLM 语义提取（提取概念、rationale、跨文档关联）")
            if deep_mode:
                print("  深度模式：启用更激进的 INFERRED 边")
            
            try:
                from builders.extract_semantic_llm import extract_docs_with_llm_sync, LLMConfig
                
                config = LLMConfig(
                    api_key=api_key,
                    model="gpt-4o-mini",
                    temperature=0.3,
                )
                
                doc_result = extract_docs_with_llm_sync(
                    doc_files,
                    root,
                    config=config,
                    deep_mode=deep_mode,
                    chunk_size=22,
                    max_concurrent=3,
                )
                
                extractions.append(doc_result)
                print(f"  节点: {len(doc_result.get('nodes', []))}")
                print(f"  边: {len(doc_result.get('edges', []))}")
                print(f"  超边: {len(doc_result.get('hyperedges', []))}")
                print(f"  Token: {doc_result.get('input_tokens', 0)} 输入, {doc_result.get('output_tokens', 0)} 输出")
                
            except ImportError as e:
                print(f"  警告: LLM 语义提取模块导入失败: {e}")
                print("  回退到简化版语义提取")
                from builders.extract_semantic import extract_docs_simple
                doc_result = extract_docs_simple(doc_files, root)
                extractions.append(doc_result)
                print(f"  节点: {len(doc_result.get('nodes', []))}")
                print(f"  边: {len(doc_result.get('edges', []))}")
                
            except Exception as e:
                print(f"  警告: LLM 语义提取失败: {e}")
                print("  回退到简化版语义提取")
                from builders.extract_semantic import extract_docs_simple
                doc_result = extract_docs_simple(doc_files, root)
                extractions.append(doc_result)
                print(f"  节点: {len(doc_result.get('nodes', []))}")
                print(f"  边: {len(doc_result.get('edges', []))}")
        else:
            print("  提示: OPENAI_API_KEY 未设置，使用简化版（仅提取标题和链接）")
            print("  设置环境变量以启用 LLM 语义提取：")
            print("    export OPENAI_API_KEY=sk-...")
            try:
                from builders.extract_semantic import extract_docs_simple
                doc_result = extract_docs_simple(doc_files, root)
                extractions.append(doc_result)
                print(f"  节点: {len(doc_result.get('nodes', []))}")
                print(f"  边: {len(doc_result.get('edges', []))}")
            except ImportError:
                print("  譕告: 语义提取模块未实现")
            except Exception as e:
                print(f"  譕告: 语义提取失败: {e}")
    
    if not extractions:
        print("\n错误: 无提取结果，图谱为空")
        print("  可能原因: 无代码文件 / tree-sitter 未安装 / 无文档文件")
        return
    
    print("\n构建图谱...")
    if args.update and output_path.exists():
        print("  合并到现有图谱...")
        G = build_merge(extractions, graph_path=str(output_path), directed=directed)
    else:
        G = build_from_json(extractions[0], directed=directed)
        for ext in extractions[1:]:
            from builders.build import build
            G = build([{"nodes": [{"id": n, **d} for n, d in G.nodes(data=True)], "edges": [{"source": u, "target": v, **d} for u, v, d in G.edges(data=True)]}, ext], directed=directed)
    
    if G.number_of_nodes() == 0:
        print("错误: 图谱为空")
        return
    
    print(f"  节点: {G.number_of_nodes()}")
    print(f"  边: {G.number_of_edges()}")
    
    print("\n聚类...")
    communities = cluster(G)
    assign_communities_to_nodes(G, communities)
    print(f"  社区: {len(communities)}")
    
    print("\n分层标注...")
    annotate_layers(G)
    layer_dist = {}
    for _, data in G.nodes(data=True):
        layer = data.get("layer", 3)
        layer_dist[layer] = layer_dist.get(layer, 0) + 1
    print(f"  L1: {layer_dist.get(1, 0)}, L2: {layer_dist.get(2, 0)}, L3: {layer_dist.get(3, 0)}")
    
    save_graph(G, output_path)
    print(f"\n完成！图谱保存至: {output_path}")


def cmd_build_subgraph(args):
    """构建子图谱。"""
    from builders import detect, build_from_json, build, cluster, save_graph, assign_communities_to_nodes, annotate_layers, collect_files, extract
    
    root = Path(args.path).resolve()
    name = args.name
    deep_mode = args.mode == "deep"
    directed = args.directed
    
    output_dir = Path("data/subgraphs") / name
    output_path = output_dir / "graph.json"
    
    print(f"\n构建子图谱: {name}")
    print(f"输入目录: {root}")
    print(f"输出路径: {output_path}")
    
    print(f"\n扫描目录: {root}")
    detected = detect(root)
    code_files = detected.get("files", {}).get("code", [])
    doc_files = detected.get("files", {}).get("document", [])
    
    print(f"文件数: {detected['total_files']}")
    print(f"词数: ~{detected['total_words']}")
    
    extractions = []
    
    if code_files:
        print(f"\nAST 提取 ({len(code_files)} 个代码文件)...")
        
        try:
            import os
            orig_dir = os.getcwd()
            try:
                os.chdir(root)
                code_paths = collect_files(Path("."), root=Path("."))
            finally:
                os.chdir(orig_dir)
            
            if code_paths:
                code_paths = [root / p for p in code_paths]
                print(f"  找到 {len(code_paths)} 个代码文件")
                ast_result = extract(code_paths, cache_root=root)
                extractions.append(ast_result)
                print(f"  节点: {len(ast_result.get('nodes', []))}")
                print(f"  边: {len(ast_result.get('edges', []))}")
            else:
                print("  未找到代码文件")
        except Exception as e:
            print(f"  AST 提取失败: {e}")
    
    if doc_files:
        print(f"\n语义提取 ({len(doc_files)} 个文档文件)...")
        
        import os
        
        # LLM Provider 配置
        llm_provider = getattr(args, 'llm_provider', 'skip')
        api_key = getattr(args, 'api_key', None) or os.environ.get("OPENAI_API_KEY") or os.environ.get("GLM_API_KEY") or os.environ.get("DASHSCOPE_API_KEY")
        api_base = getattr(args, 'api_base', None)
        model = getattr(args, 'model', None)
        
        # Provider 默认配置
        provider_defaults = {
            "openai": {
                "api_base": "https://api.openai.com/v1",
                "model": "gpt-4o-mini",
            },
            "glm-5": {
                "api_base": "https://open.bigmodel.cn/api/paas/v4",  # 智谱 AI
                "model": "glm-4",  # GLM-4 是智谱的最新模型
            },
            "dashscope": {
                "api_base": "https://dashscope.aliyuncs.com/compatible-mode/v1",  # 阿里云 DashScope (OpenAI-compatible)
                "model": "qwen-turbo",  # 通义千问
            },
        }
        
        if llm_provider != "skip" and api_key:
            # 应用 provider 默认配置
            if llm_provider in provider_defaults:
                defaults = provider_defaults[llm_provider]
                api_base = api_base or defaults["api_base"]
                model = model or defaults["model"]
            
            print(f"  使用 LLM 语义提取 ({llm_provider}: {model})...")
            print(f"  API Base: {api_base}")
            
            try:
                from builders.extract_semantic_llm import extract_docs_with_llm_sync, LLMConfig
                
                config = LLMConfig(
                    api_base=api_base,
                    api_key=api_key,
                    model=model,
                    temperature=0.3,
                    max_tokens=4096,
                    timeout=120,
                )
                
                sem_result = extract_docs_with_llm_sync(
                    doc_files,
                    root,
                    config=config,
                    deep_mode=deep_mode,
                    chunk_size=22,
                    max_concurrent=3,
                    use_cache=True,
                )
                
                extractions.append(sem_result)
                print(f"  节点: {len(sem_result.get('nodes', []))}")
                print(f"  边: {len(sem_result.get('edges', []))}")
                print(f"  超边: {len(sem_result.get('hyperedges', []))}")
                print(f"  Tokens: {sem_result.get('input_tokens', 0)} → {sem_result.get('output_tokens', 0)}")
            except Exception as e:
                print(f"  LLM 提取失败: {e}")
                print("  回退到简化语义提取...")
                from builders.extract_semantic import extract_docs_simple
                sem_result = extract_docs_simple(doc_files, root)
                extractions.append(sem_result)
                print(f"  节点: {len(sem_result.get('nodes', []))}")
                print(f"  边: {len(sem_result.get('edges', []))}")
        else:
            print("  使用简化语义提取...")
            from builders.extract_semantic import extract_docs_simple
            sem_result = extract_docs_simple(doc_files, root)
            extractions.append(sem_result)
            print(f"  节点: {len(sem_result.get('nodes', []))}")
            print(f"  边: {len(sem_result.get('edges', []))}")
    
    if not extractions:
        print("\n错误: 未提取到任何节点")
        return
    
    print("\n构建图谱...")
    G = build_from_json(extractions[0] if len(extractions) == 1 else build(extractions), directed=directed)
    print(f"  节点: {G.number_of_nodes()}")
    print(f"  边: {G.number_of_edges()}")
    
    print("\n聚类...")
    communities = cluster(G)
    assign_communities_to_nodes(G, communities)
    print(f"  社区: {len(communities)}")
    
    annotate_layers(G)
    
    G.graph["subgraph_name"] = name
    
    save_graph(G, output_path)
    print(f"\n完成！子图谱保存至: {output_path}")


def cmd_merge(args):
    """合并多个子图谱。"""
    from builders import merge_graphs
    
    graph_paths = args.graphs
    output_path = args.output
    deduplicate = not args.no_deduplicate
    recluster = not args.no_recluster
    directed = args.directed
    
    print(f"\n合并图谱:")
    print(f"  输入: {len(graph_paths)} 个图谱")
    for p in graph_paths:
        print(f"    - {p}")
    print(f"  输出: {output_path}")
    print(f"  去重: {deduplicate}")
    print(f"  重聚类: {recluster}")
    
    G = merge_graphs(
        graph_paths,
        output_path,
        deduplicate=deduplicate,
        recluster=recluster,
        annotate=True,
        directed=directed,
    )
    
    print(f"\n完成！合并图谱: {G.number_of_nodes()} 节点, {G.number_of_edges()} 边")


def cmd_export(args):
    """导出图谱。"""
    from export import to_json, to_html, generate_report
    from engines import GraphifyEngine
    
    graph_path = Path(args.graph)
    if not graph_path.exists():
        print(f"错误: 图谱文件不存在: {graph_path}")
        return
    
    engine = GraphifyEngine()
    engine.load(str(graph_path))
    G = engine._graph
    
    # 从节点属性中提取已有的 community 信息，避免重新聚类
    communities: dict[int, list[str]] = {}
    for node_id, data in G.nodes(data=True):
        cid = data.get("community")
        if cid is not None:
            communities.setdefault(int(cid), []).append(node_id)
    
    if not communities:
        print("图谱缺少 community 信息，正在聚类...")
        from builders.cluster import cluster, assign_communities_to_nodes
        communities = cluster(G)
        assign_communities_to_nodes(G, communities)
    
    output_dir = Path(args.output_dir) if args.output_dir else graph_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    format_name = args.format.lower()
    
    if format_name == "json":
        output_file = output_dir / "graph_export.json"
        to_json(G, communities, str(output_file))
        print(f"JSON 导出完成: {output_file}")
    
    elif format_name == "html":
        output_file = output_dir / "graph.html"
        try:
            to_html(G, communities, str(output_file))
            print(f"HTML 导出完成: {output_file}")
        except ValueError as e:
            print(f"警告: {e}")
    
    elif format_name == "report":
        output_file = output_dir / "GRAPH_REPORT.md"
        generate_report(G, communities, output_path=str(output_file))
        print(f"报告导出完成: {output_file}")
    
    elif format_name == "all":
        to_json(G, communities, str(output_dir / "graph_export.json"))
        print(f"JSON: {output_dir / 'graph_export.json'}")
        
        try:
            to_html(G, communities, str(output_dir / "graph.html"))
            print(f"HTML: {output_dir / 'graph.html'}")
        except ValueError as e:
            print(f"HTML: {e}")
        
        generate_report(G, communities, output_path=str(output_dir / "GRAPH_REPORT.md"))
        print(f"报告: {output_dir / 'GRAPH_REPORT.md'}")
    
    else:
        print(f"未知格式: {format_name}。可用: json, html, report, all")


def main():
    parser = argparse.ArgumentParser(description="仓颉鸿蒙知识图谱 CLI")
    subparsers = parser.add_subparsers(dest="command", help="子命令")

    # search
    p_search = subparsers.add_parser("search", help="搜索图谱（定位文档）")
    p_search.add_argument("query", help="查询字符串")
    p_search.add_argument("--limit", type=int, default=10, help="返回数量")
    p_search.add_argument("--mark", choices=["good", "bad"], help="标记满意度")
    p_search.set_defaults(func=cmd_search)

    # traverse
    p_traverse = subparsers.add_parser("traverse", help="图遍历（发现关联）")
    p_traverse.add_argument("query", help="查询字符串")
    p_traverse.add_argument("--mode", choices=["bfs", "dfs"], default="bfs", help="遍历模式")
    p_traverse.add_argument("--depth", type=int, default=3, help="遍历深度")
    p_traverse.add_argument("--budget", type=int, default=2000, help="token 上限")
    p_traverse.set_defaults(func=cmd_traverse)

    # path
    p_path = subparsers.add_parser("path", help="查找关系路径")
    p_path.add_argument("node_a", help="起点节点")
    p_path.add_argument("node_b", help="终点节点")
    p_path.add_argument("--max-depth", type=int, default=5, help="最大深度")
    p_path.set_defaults(func=cmd_path)

    # explain
    p_explain = subparsers.add_parser("explain", help="解释节点")
    p_explain.add_argument("node", help="节点 ID 或名称")
    p_explain.set_defaults(func=cmd_explain)

    # neighbors
    p_neighbors = subparsers.add_parser("neighbors", help="获取邻居节点")
    p_neighbors.add_argument("node", help="节点 ID 或名称")
    p_neighbors.add_argument("--limit", type=int, default=20, help="数量上限")
    p_neighbors.set_defaults(func=cmd_neighbors)

    # god-nodes
    p_god = subparsers.add_parser("god-nodes", help="核心节点（连接最多）")
    p_god.add_argument("--top-n", type=int, default=10, help="数量")
    p_god.set_defaults(func=cmd_god_nodes)

    # surprises
    p_surprises = subparsers.add_parser("surprises", help="惊奇连接（跨社区边）")
    p_surprises.add_argument("--top-n", type=int, default=5, help="数量")
    p_surprises.set_defaults(func=cmd_surprises)

    # questions
    p_questions = subparsers.add_parser("questions", help="建议问题")
    p_questions.add_argument("--top-n", type=int, default=7, help="数量")
    p_questions.set_defaults(func=cmd_questions)

    # community
    p_community = subparsers.add_parser("community", help="社区详情")
    p_community.add_argument("community_id", type=int, help="社区 ID")
    p_community.set_defaults(func=cmd_community)

    # search-with-neighbors
    p_search_neighbors = subparsers.add_parser("search-with-neighbors", help="搜索 + 邻居")
    p_search_neighbors.add_argument("query", help="查询字符串")
    p_search_neighbors.add_argument("--limit", type=int, default=5, help="搜索结果数")
    p_search_neighbors.add_argument("--neighbors", type=int, default=5, help="每个结果的邻居数")
    p_search_neighbors.set_defaults(func=cmd_search_with_neighbors)

    # stats
    p_stats = subparsers.add_parser("stats", help="显示统计")
    p_stats.set_defaults(func=cmd_stats)

    # analyze
    p_analyze = subparsers.add_parser("analyze", help="分析反馈")
    p_analyze.set_defaults(func=cmd_analyze)

    # optimize
    p_optimize = subparsers.add_parser("optimize", help="执行优化")
    p_optimize.set_defaults(func=cmd_optimize)

    # graphs
    p_graphs = subparsers.add_parser("graphs", help="列出可用图谱")
    p_graphs.set_defaults(func=cmd_graphs)

    # build
    p_build = subparsers.add_parser("build", help="构建图谱（对齐 graphify）")
    p_build.add_argument("path", nargs="?", default=".", help="输入目录（默认当前目录）")
    p_build.add_argument("--output", help="输出路径（默认 graphify-out/graph.json）")
    p_build.add_argument("--mode", choices=["normal", "deep"], default="normal", help="提取模式：normal（默认）/ deep（更激进的 INFERRED 边）")
    p_build.add_argument("--update", action="store_true", help="增量更新（仅处理变化文件）")
    p_build.add_argument("--directed", action="store_true", help="生成有向图")
    p_build.add_argument("--cluster-only", action="store_true", help="仅重新聚类（不提取）")
    p_build.set_defaults(func=cmd_build)

    # build-subgraph
    p_build_subgraph = subparsers.add_parser("build-subgraph", help="构建子图谱")
    p_build_subgraph.add_argument("path", help="输入目录")
    p_build_subgraph.add_argument("--name", required=True, help="子图谱名称（如 api/core/ui）")
    p_build_subgraph.add_argument("--mode", choices=["normal", "deep"], default="normal", help="提取模式")
    p_build_subgraph.add_argument("--directed", action="store_true", help="生成有向图")
    p_build_subgraph.add_argument("--llm-provider", choices=["openai", "glm-5", "dashscope", "skip"], default="skip", help="LLM provider (skip=不使用LLM)")
    p_build_subgraph.add_argument("--api-key", help="API Key (或通过环境变量设置)")
    p_build_subgraph.add_argument("--api-base", help="API Base URL")
    p_build_subgraph.add_argument("--model", help="模型名称")
    p_build_subgraph.set_defaults(func=cmd_build_subgraph)

    # merge
    p_merge = subparsers.add_parser("merge", help="合并多个子图谱")
    p_merge.add_argument("graphs", nargs="+", help="图谱文件路径（多个）")
    p_merge.add_argument("--output", required=True, help="合并后的输出路径")
    p_merge.add_argument("--no-deduplicate", action="store_true", help="不去重")
    p_merge.add_argument("--no-recluster", action="store_true", help="不重新聚类")
    p_merge.add_argument("--directed", action="store_true", help="生成有向图")
    p_merge.set_defaults(func=cmd_merge)

    # export
    p_export = subparsers.add_parser("export", help="导出图谱")
    p_export.add_argument("--format", choices=["json", "html", "report", "all"], default="all", help="导出格式")
    p_export.add_argument("--graph", default="data/merged/graph_layered.json", help="图谱路径")
    p_export.add_argument("--output-dir", help="输出目录")
    p_export.set_defaults(func=cmd_export)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
