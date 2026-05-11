"""分层标注器。

为图谱节点自动标注层级（L1 概念层、L2 API 层、L3 实现层）。
"""

import json
from pathlib import Path


def classify_layer(node_data: dict) -> int:
    """节点分层规则。

    Layer 1 (概念层): 开发指南、概述、错误码
    Layer 2 (API 层): 类/接口/组件/枚举定义、API 参考
    Layer 3 (实现层): 函数/属性、测试代码、内部实现
    """
    src = node_data.get("source_file", "").lower().replace("\\", "/")
    label = node_data.get("label", "").lower()
    ft = node_data.get("file_type", "")

    # === Layer 1: 概念层 ===
    if ft == "document" and not src.startswith("api/"):
        if src.startswith("guide/"):
            if not any(kw in src for kw in ["development", "development-guide", "guideline", "如何", "开发指导"]):
                return 1

    if any(kw in src for kw in [".overview", ".abstract", "/overview/", "/abstract/"]):
        if not src.startswith("api/"):
            return 1

    if any(kw in label for kw in ["概述", "概览", "简介", "overview", "abstract", "introduction"]):
        if not src.startswith("api/"):
            return 1

    if "errorcode" in src or "错误码" in label:
        return 1

    # === Layer 2: API 层 ===
    if src.startswith("api/"):
        if not any(kw in src for kw in ["/test/", "/example/", "/sample/"]):
            return 2

    if src.startswith("guide/"):
        if any(kw in src for kw in ["development", "development-guide", "guideline", "如何", "开发指导"]):
            return 2
        if any(kw in src for kw in ["api-reference", "api 参考", "接口"]):
            return 2

    if any(kw in src for kw in ["class_", "interface_", "enum_", "struct_", "type_"]):
        return 2

    if any(kw in label for kw in [" class ", " interface ", " component ", " enum ", " struct ",
                                   "class_", "interface_", "enum_", "struct_"]):
        return 2

    if "arkui" in src and any(kw in label for kw in ["component", "组件"]):
        return 2

    # === Layer 3: 实现层（默认） ===
    return 3


class LayerAnnotator:
    """分层标注器。

    为图谱 JSON 文件中的节点添加 layer 字段。
    """

    def annotate(self, input_path: str, output_path: str = None) -> dict:
        """对图谱进行分层标注。

        Args:
            input_path: 输入图谱 JSON 路径
            output_path: 输出路径，None 则覆盖原文件

        Returns:
            分层统计
        """
        data = json.loads(Path(input_path).read_text(encoding="utf-8"))

        layer_counts = {1: 0, 2: 0, 3: 0}
        for node in data.get("nodes", []):
            layer = classify_layer(node)
            node["layer"] = layer
            layer_counts[layer] += 1

        out_path = output_path or input_path
        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        Path(out_path).write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        return layer_counts

    def annotate_subgraph(self, subgraph_dir: str) -> dict:
        """对子图谱进行分层标注。

        Args:
            subgraph_dir: 子图谱目录（包含 graph.json）

        Returns:
            分层统计
        """
        input_path = Path(subgraph_dir) / "graph.json"
        output_path = Path(subgraph_dir) / "graph_layered.json"

        if not input_path.exists():
            raise FileNotFoundError(f"子图谱不存在: {input_path}")

        return self.annotate(str(input_path), str(output_path))
