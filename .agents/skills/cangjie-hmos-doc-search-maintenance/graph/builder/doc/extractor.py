"""文档图谱提取器。1文档=1节点，纯示例文件不建节点。

本模块负责从 .md 文件提取图谱节点（DocNode）和边（Edge），是文档图谱
构建流水线的核心抽取步骤。主要功能：
- extract_doc_node: 从普通文档提取节点 + SEE_ALSO 边
- extract_overview_nodes: 从 .overview.md 提取概览节点 + CONTAINS 边
- 各种辅助函数：文档类型检测、层级推断、关键词提取、描述提取等

节点 ID 格式: {category}_{namespace}_{doc_type}_{label}
边关系类型: SEE_ALSO（文档间引用）、CONTAINS（概览包含子文档）

设计决策：
- 纯示例文件（代码多、文字少）不建节点，避免噪声
- .overview/.abstract 文件不建普通节点，而是建概览节点
- 概览节点 is_god_node=True，用于图谱搜索的入口导航
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Optional

from core.models import DocNode, Edge, EdgeRelation


def safe_read_text(path: Path) -> str:
    """读取文件内容，自动处理 Windows 长路径问题。"""
    full = str(path.resolve())
    if sys.platform == "win32" and len(full) > 240:
        full = "\\\\?\\" + full
    return Path(full).read_text(encoding="utf-8", errors="replace")


# === 停词表 ===

TITLE_STOP_ZH = {
    "注意事项", "示例", "示例代码", "运行结果", "说明", "备注", "相关文档", "参见",
    "导入模块", "权限列表", "使用说明", "通用属性", "通用事件", "创建组件", "参数", "返回值",
}
TITLE_STOP_EN = {
    "example", "note", "see also", "output", "result", "import", "permission",
    "usage", "parameters", "return value",
}


def is_pure_example(content: str) -> bool:
    """判断是否为纯示例文件：全文去代码后文字极少（中文<10字且英文<5词），
    或文件名明确标记为示例。纯示例文件不建节点，避免图谱噪声。"""
    text_without_code = re.sub(r"```[\s\S]*?```", "", content)
    text_clean = re.sub(r"[#*>`\-\[\]()]", "", text_without_code).strip()
    text_clean = re.sub(r"<[^>]+>", "", text_clean).strip()
    
    # 中文字符数 + 英文单词数
    zh_chars = len(re.findall(r"[\u4e00-\u9fff]", text_clean))
    en_words = len(re.findall(r"[A-Za-z]{3,}", text_clean))
    
    # 如果文字量极少（中文<10字且英文<5词），判定为纯示例
    # API 定义文件（函数/属性/枚举）即使文字少也应保留
    return zh_chars < 10 and en_words < 5


def clean_filename(stem: str) -> str:
    """清理文件名为展示 label：去除哈希后缀、类型前缀、Nmore 后缀。"""
    clean = re.sub(r"_[a-f0-9]{8}$", "", stem)
    for prefix in ["class_", "func_", "enum_", "interface_", "struct_", "prop_"]:
        if clean.startswith(prefix):
            clean = clean[len(prefix):]
            break
    clean = re.sub(r"_\d+more$", "", clean)
    clean = re.sub(r"__+$", "", clean)
    return clean if clean else stem


def clean_id_stem(stem: str) -> str:
    """清理文件名为 ID 组件：仅去除类型前缀，保留哈希/Nmore 后缀以确保唯一性。"""
    clean = stem
    for prefix in ["class_", "func_", "enum_", "interface_", "struct_", "prop_"]:
        if clean.startswith(prefix):
            clean = clean[len(prefix):]
            break
    return clean if clean else stem


def infer_layer(rel_path: str) -> int:
    """推断节点层级：L1=指南/概览/教程，L2=API/错误码/具体实现。
    层级影响搜索优先级——L1 概览节点更适合作为入口。"""
    path = rel_path.replace("\\", "/").lower()
    if path.endswith(".overview.md") or path.endswith(".abstract.md"):
        return 1
    # Guide/Tutorial 目录 → L1
    if any(x in path for x in ["guide/", "tutorial/", "overview/"]):
        return 1
    parent = Path(path).parent.name.lower()
    if parent in ("guide", "tutorial", "overview", "samples"):
        return 1
    # API 目录下的文件 → L2
    if "/api/" in path or path.startswith("api/"):
        return 2
    # 文件名含 class_/func_/enum_ 等 → L2
    if any(prefix in path for prefix in ["class_", "func_", "enum_", "interface_", "struct_", "prop_"]):
        return 2
    # 错误码 → L2
    if "errorcode" in path or "错误码" in rel_path:
        return 2
    # 有 **功能：** 标记 → L2
    return 1


def infer_category(rel_path: str, root_dir_name: str = "") -> str:
    """推断文档所属技术分类：harmonyos/std/stdx/lang/tools。
    分类影响节点 ID 前缀和搜索时的模块过滤。"""
    path = rel_path.replace("\\", "/").lower()
    if "harmonyos" in path or "harmonyos" in root_dir_name.lower():
        return "harmonyos"
    if "stdx" in path or root_dir_name.lower() == "stdx":
        return "stdx"
    if ("std" in path and "stdx" not in path) or root_dir_name.lower() == "std":
        return "std"
    if "lang-features" in path or root_dir_name.lower() in ("lang-features", "cangjie-lang-features"):
        return "lang"
    if "tools" in path or root_dir_name.lower() in ("tools", "cmd-tools"):
        return "tools"
    return "harmonyos"


def build_namespace(rel_path: str) -> str:
    """从文件路径构建命名空间标识，取最后 3 个有意义的路径段。
    跳过通用目录名（api/package/index 等）和 cj-/ohos 前缀。"""
    parts = rel_path.replace("\\", "/").split("/")
    ns_parts = []
    skip = {"api", "package", "index", "samples", "guide", "tutorial", "overview"}
    for p in parts:
        if p.startswith("cj-"):
            ns_parts.append(p[3:])
        elif p.startswith("ohos"):
            ns_parts.append(p[4:])
        elif p and not p.endswith(".md") and not p.startswith("."):
            clean = p.lower()
            if clean not in skip:
                ns_parts.append(p)
    meaningful = [p for p in ns_parts if p.lower() not in skip]
    return "_".join(meaningful[-3:]) if meaningful else "unknown"


def extract_label_zh(content: str) -> str:
    """从 H1/H2 标题提取中文标签。"""
    h2_match = re.search(r"^##\s+(.+)", content, re.MULTILINE)
    if h2_match:
        title = h2_match.group(1).strip()
        if any('\u4e00' <= c <= '\u9fff' for c in title):
            return title
    h1_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
    if h1_match:
        title = h1_match.group(1).strip()
        if any('\u4e00' <= c <= '\u9fff' for c in title):
            return title
    return ""


def extract_description(content: str) -> tuple[str, str]:
    """提取中英文描述。"""
    # 找 **功能：** 后的内容
    func_match = re.search(r"\*\*功能[：:]\*\*\s*(.+?)(?=\n|$)", content)
    if func_match:
        desc = func_match.group(1).strip()
        zh_chars = re.findall(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef，。！？；：""''（）【】《》]", desc)
        desc_zh = "".join(zh_chars)[:200]
        desc_en = desc[:500]
        return desc_zh, desc_en

    # 找 H1 后第一段
    h1_match = re.search(r"^#\s+.+\n(.+?)(?=\n##|\n#|\Z)", content, re.DOTALL)
    if h1_match:
        first_para = h1_match.group(1).strip()
        first_para = re.sub(r"<!--.*?-->", "", first_para, flags=re.DOTALL).strip()
        first_para = re.sub(r"```[\s\S]*?```", "", first_para).strip()
        zh_chars = re.findall(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef，。！？；：""''（）【】《》]", first_para)
        desc_zh = "".join(zh_chars)[:200]
        en_words = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", first_para)
        desc_en = " ".join(en_words)[:500]
        return desc_zh, desc_en

    return "", ""


def extract_keywords(content: str, doc_type: str, rel_path: str, label: str) -> tuple[list[str], list[str]]:
    """根据文档类型提取关键词。"""
    keywords_zh = []
    keywords_en = []

    if doc_type == "overview":
        # 从 Quick Navigation 提取
        nav = re.findall(r"\*\*\s*(.+?)\s*\*\*", content)
        for item in nav:
            zh = re.findall(r"[\u4e00-\u9fff]{2,}", item)
            keywords_zh.extend(zh)
            en = re.findall(r"@[A-Za-z_][A-Za-z0-9_]*|[A-Za-z]{3,}", item)
            keywords_en.extend(en)
    elif doc_type == "api":
        # 文件名 + 标题
        keywords_en.append(label.lower())
        h2_titles = re.findall(r"^##\s+(.+)", content, re.MULTILINE)
        for t in h2_titles:
            t_clean = t.strip()
            if t_clean not in TITLE_STOP_ZH and t_clean not in TITLE_STOP_EN:
                zh = re.findall(r"[\u4e00-\u9fff]{2,}", t_clean)
                keywords_zh.extend(zh)
                en = re.findall(r"@[A-Za-z_][A-Za-z0-9_]*|[A-Za-z]{3,}", t_clean)
                keywords_en.extend(en)
    elif doc_type == "guide":
        # 模块名 + 标题
        ns = build_namespace(rel_path)
        keywords_en.extend(ns.split("_"))
        h1_match = re.search(r"^#\s+(.+)", content, re.MULTILINE)
        if h1_match:
            title = h1_match.group(1).strip()
            zh = re.findall(r"[\u4e00-\u9fff]{2,}", title)
            keywords_zh.extend(zh)
            en = re.findall(r"@[A-Za-z_][A-Za-z0-9_]*|[A-Za-z]{3,}", title)
            keywords_en.extend(en)
    elif doc_type == "errorcode":
        # 错误码编号 + 模块名
        codes = re.findall(r"\b(\d{8})\b", content)
        keywords_en.extend(codes)
        ns = build_namespace(rel_path)
        keywords_en.extend(ns.split("_"))

    # 去重 + 停词过滤
    keywords_zh = list(dict.fromkeys(k for k in keywords_zh if k not in TITLE_STOP_ZH))[:15]
    # 保留 @ 符号，不转小写（@State 保持原样）
    keywords_en = list(dict.fromkeys(k for k in keywords_en if k.lower() not in TITLE_STOP_EN and len(k) >= 3))[:15]

    return keywords_zh, keywords_en


def detect_doc_type(rel_path: str, content: str) -> str:
    """检测文档类型：overview/guide/api/errorcode。
    影响关键词提取策略和节点 ID 格式。"""
    path = rel_path.replace("\\", "/").lower()
    if path.endswith(".overview.md"):
        return "overview"
    if "errorcode" in path or "错误码" in rel_path:
        return "errorcode"
    if any(x in path for x in ["Guide/", "Tutorial/"]):
        return "guide"
    if any(prefix in path for prefix in ["class_", "func_", "enum_", "interface_", "struct_", "prop_"]):
        return "api"
    # 检查是否有 **功能：** 标记
    if "**功能" in content or "**功能：" in content:
        return "api"
    return "guide"


def detect_doc_type_from_path(rel_path: str) -> str:
    """仅从路径推断文档类型（无需读取内容），用于边目标 ID 计算。"""
    path = rel_path.replace("\\", "/").lower()
    if path.endswith(".overview.md"):
        return "overview"
    if path.endswith(".abstract.md"):
        return "guide"
    if "errorcode" in path or "错误码" in rel_path:
        return "errorcode"
    if any(prefix in path for prefix in ["class_", "func_", "enum_", "interface_", "struct_", "prop_"]):
        return "api"
    return "guide"


def compute_node_id(rel_path: str, root_dir: Path, stem: str) -> str:
    """从文件相对路径和 stem 计算节点 ID，与 extract_doc_node 的 ID 公式一致。"""
    category = infer_category(rel_path, root_dir.name)
    namespace = build_namespace(rel_path)
    doc_type = detect_doc_type_from_path(rel_path)
    id_stem = clean_id_stem(stem)
    return f"{category}_{namespace}_{doc_type}_{id_stem}".replace(" ", "_").lower()


def _resolve_link_target(link_target: str, doc_path: Path, root_dir: Path) -> Optional[str]:
    """解析 Markdown 链接目标为 root_dir 下的相对路径。
    
    策略：
    1. 精确解析：doc_path.parent / link → resolve → relative_to(root_dir)
    2. 模糊匹配：精确解析失败时，在同目录找 clean_filename 匹配的 .md 文件
    """
    target_file_raw = link_target.split("#")[0]
    if not target_file_raw:
        return None
    stem = Path(target_file_raw).stem
    if stem.startswith("."):
        return None

    root_resolved = root_dir.resolve()

    # 策略 1：精确解析
    target_path = (doc_path.parent / target_file_raw).resolve()
    try:
        target_rel = str(target_path.relative_to(root_resolved))
        if target_path.is_file():
            return target_rel
    except ValueError:
        pass

    # 策略 2：模糊匹配 — 在同目录下找 clean_filename 匹配的 .md 文件
    link_stem_clean = clean_filename(stem)
    parent_dir = doc_path.parent
    for candidate in parent_dir.iterdir():
        if candidate.suffix == '.md' and not candidate.name.startswith("."):
            if clean_filename(candidate.stem) == link_stem_clean:
                try:
                    return str(candidate.resolve().relative_to(root_resolved))
                except ValueError:
                    continue

    return None


def extract_doc_node(doc_path: Path, root_dir: Path) -> Optional[tuple[DocNode, list[Edge]]]:
    """从 .md 文件提取节点和边。返回 None 表示不建节点（纯示例/overview/abstract）。

    节点构建步骤：读取内容 → 跳过纯示例 → 清理文件名 → 推断层级/分类/命名空间
    → 检测文档类型 → 提取标签/描述/关键词 → 构建 DocNode。
    边构建：从 Markdown 链接提取 SEE_ALSO 边（同分类同命名空间下的文档引用）。
    """
    rel_path = str(doc_path.relative_to(root_dir)).replace("\\", "/")

    # 跳过 overview/abstract
    if doc_path.name.startswith(".overview") or doc_path.name.startswith(".abstract"):
        return None

    try:
        content = safe_read_text(doc_path)
    except Exception:
        return None

    # 纯示例文件不建节点
    if is_pure_example(content):
        return None

    label = clean_filename(doc_path.stem)
    id_stem = clean_id_stem(doc_path.stem)
    label_zh = extract_label_zh(content)
    layer = infer_layer(rel_path)
    category = infer_category(rel_path, root_dir.name)
    namespace = build_namespace(rel_path)
    doc_type = detect_doc_type(rel_path, content)

    desc_zh, desc_en = extract_description(content)
    keywords_zh, keywords_en = extract_keywords(content, doc_type, rel_path, label)

    node = DocNode(
        id=f"{category}_{namespace}_{doc_type}_{id_stem}".replace(" ", "_").lower(),
        label=label,
        label_zh=label_zh,
        layer=layer,
        description_zh=desc_zh,
        description_en=desc_en,
        keywords_zh=keywords_zh,
        keywords_en=keywords_en,
        category=category,
        namespace=namespace,
        source_file=rel_path,
    )

    # 提取 SEE_ALSO 边：基于目标文件的实际路径计算 ID
    edges = []
    md_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
    for link_text, link_target in md_links:
        if link_target.startswith("./") or "/" in link_target:
            target_file_raw = link_target.split("#")[0]
            if not target_file_raw or Path(target_file_raw).stem.startswith("."):
                continue
            target_path = (doc_path.parent / target_file_raw).resolve()
            try:
                target_rel = str(target_path.relative_to(root_dir.resolve()))
            except ValueError:
                continue
            target_id = compute_node_id(target_rel, root_dir, Path(target_file_raw).stem)
            edges.append(Edge(
                source=node.id, target=target_id,
                relation=EdgeRelation.SEE_ALSO.value,
                source_file=rel_path,
            ))

    return node, edges


# === 概览节点关键词提取 ===

EN_STOP_WORDS = {
    "the", "this", "that", "with", "from", "for", "and", "are", "but", "not",
    "you", "all", "can", "had", "her", "was", "one", "our", "out",
    "directory", "comprehensive", "technical", "resource", "provides", "essential",
    "guidance", "developers", "framework", "specifically", "designed", "utilizing",
    "programming", "module", "reference", "documentation", "covers", "functions",
    "features", "includes", "overview", "introduction", "concept", "basic",
    "advanced", "usage", "example", "sample", "code", "implementation", "details",
    "information", "content", "following", "section", "chapter", "page", "part",
    "topic", "subject", "area", "field", "domain", "category", "type", "kind",
    "sort", "class", "group", "set", "collection", "list", "array", "table",
    "chart", "graph", "diagram", "figure", "image", "picture", "photo",
    "illustration", "drawing", "sketch", "outline", "summary", "abstract",
    "synopsis", "review", "survey", "analysis", "study", "research",
    "investigation", "examination", "inspection", "observation", "note", "remark",
    "comment", "statement", "declaration", "announcement", "proclamation",
    "publication", "release", "issue", "edition", "version", "revision", "update",
    "upgrade", "improvement", "enhancement", "modification", "alteration", "change",
    "adjustment", "adaptation", "conversion", "transformation", "translation",
    "interpretation", "explanation", "description", "definition", "meaning", "sense",
    "significance", "importance", "value", "worth", "merit", "quality",
    "characteristic", "feature", "attribute", "property", "trait", "aspect",
    "element", "component", "factor", "item", "piece", "portion", "segment",
    "fragment", "chunk", "block", "unit", "package", "bundle", "cluster", "batch",
    "series", "sequence", "chain", "string", "line", "row", "column", "matrix",
    "network", "system", "structure", "architecture", "design", "plan", "scheme",
    "pattern", "model", "template", "format", "style", "layout", "arrangement",
    "organization", "configuration", "setup", "installation", "deployment",
    "distribution", "delivery", "transfer", "transmission", "communication",
    "connection", "link", "relation", "relationship", "association", "correlation",
    "interaction", "interface", "integration", "combination", "merger", "fusion",
    "union", "alliance", "partnership", "collaboration", "cooperation",
    "coordination", "synchronization", "alignment", "matching", "correspondence",
    "agreement", "consensus", "harmony", "balance", "equilibrium", "stability",
    "consistency", "uniformity", "regularity", "predictability", "reliability",
    "dependability", "trustworthiness", "credibility", "authenticity", "validity",
    "accuracy", "precision", "correctness", "exactness", "perfection",
    "completeness", "thoroughness", "comprehensiveness", "extensiveness", "breadth",
    "scope", "range", "extent", "degree", "level", "stage", "phase", "step",
    "point", "moment", "time", "period", "duration", "interval", "span", "length",
    "width", "height", "depth", "size", "dimension", "measurement", "scale",
    "proportion", "ratio", "rate", "speed", "velocity", "pace", "tempo", "rhythm",
    "frequency", "occurrence", "appearance", "emergence", "arrival", "entry",
    "access", "admission", "entrance", "gateway", "door", "portal", "window",
    "opening", "hole", "gap", "space", "room", "zone", "region", "territory",
    "district", "neighborhood", "community", "society", "population", "people",
    "human", "person", "individual", "user", "client", "customer", "consumer",
    "buyer", "purchaser", "shopper", "visitor", "guest", "stranger", "foreigner",
    "alien", "immigrant", "emigrant", "migrant", "traveler", "tourist", "passenger",
    "rider", "driver", "operator", "controller", "manager", "administrator",
    "director", "leader", "chief", "head", "boss", "master", "owner", "proprietor",
    "holder", "keeper", "guardian", "protector", "defender", "supporter", "advocate",
    "champion", "promoter", "sponsor", "backer", "financier", "investor",
    "shareholder", "stakeholder", "participant", "member", "associate", "colleague",
    "partner", "ally", "friend", "companion", "mate", "buddy", "pal", "peer",
    "equal", "match", "rival", "competitor", "opponent", "adversary", "enemy", "foe",
    "antagonist", "villain", "criminal", "offender", "violator", "transgressor",
    "sinner", "wrongdoer", "culprit", "perpetrator", "author", "creator", "maker",
    "builder", "constructor", "developer", "producer", "manufacturer", "fabricator",
    "assembler", "installer", "implementer", "executor", "performer", "actor",
    "player", "artist", "craftsman", "artisan", "worker", "laborer", "employee",
    "staff", "personnel", "workforce", "crew", "team", "squad", "division",
    "department", "branch", "sector", "sphere", "realm", "kingdom", "empire",
    "nation", "country", "state", "province", "county", "city", "town", "village",
    "hamlet", "settlement", "colony", "outpost", "station", "post", "base", "camp",
    "site", "location", "place", "spot", "position", "venue", "facility",
    "building", "construction", "edifice", "house", "home", "residence", "dwelling",
    "apartment", "flat", "condo", "mansion", "palace", "castle", "fortress",
    "tower", "skyscraper", "office", "shop", "store", "market", "mall", "center",
    "complex", "plaza", "square", "park", "garden", "yard", "farm", "ranch",
    "estate", "property", "land", "ground", "soil", "earth", "world", "planet",
    "globe", "sphere", "orb", "ball", "circle", "ring", "loop", "cycle", "round",
    "turn", "revolution", "rotation", "spin", "twirl", "whirl", "swirl", "spiral",
    "coil", "spring", "helix", "curve", "arc", "bend", "fold", "crease", "wrinkle",
    "stroke", "mark", "trace", "track", "trail", "path", "way", "route", "road",
    "street", "avenue", "boulevard", "lane", "alley", "passage", "corridor", "hall",
    "hallway", "tunnel", "pipe", "tube", "hose", "cable", "wire", "cord", "thread",
    "fiber", "strand", "filament", "hair", "bristle", "whisker", "beard", "mustache",
    "eyebrow", "eyelash", "eyelid", "eye", "pupil", "iris", "cornea", "lens",
    "retina", "nerve", "brain", "mind", "thought", "idea", "notion", "belief",
    "opinion", "view", "perspective", "angle", "stance", "attitude", "approach",
    "method", "technique", "procedure", "process", "mechanism", "device", "tool",
    "instrument", "apparatus", "equipment", "gear", "kit", "outfit", "rig",
    "blueprint", "plot", "map", "atlas", "how", "use", "using", "used", "need",
    "also", "more", "other", "some", "such", "than", "then", "these", "through",
    "under", "what", "when", "where", "which", "while", "who", "will", "each",
    "about", "over", "after", "before", "between", "into", "during", "without",
    "against", "upon", "much", "many", "does", "did", "been", "being", "have",
    "has", "had", "do", "done", "make", "made", "take", "get", "got", "give",
    "given", "know", "think", "see", "come", "want", "look", "find", "tell",
    "become", "keep", "let", "begin", "show", "hear", "play", "run", "move",
    "like", "live", "believe", "hold", "bring", "happen", "must", "should",
    "would", "could", "may", "might", "shall", "provide", "allow", "enable",
    "help", "work", "support", "include", "contain", "represent", "refer",
    "describe", "define", "explain", "demonstrate", "illustrate", "indicate",
    "suggest", "recommend", "require", "ensure", "return", "create", "build",
    "call", "invoke", "handle", "manage", "process", "perform", "execute",
    "implement", "apply", "access", "connect", "send", "receive", "read", "write",
    "open", "close", "start", "stop", "end", "finish", "complete", "continue",
    "different", "various", "several", "multiple", "number", "first", "second",
    "third", "last", "next", "same", "another", "both", "either", "neither",
    "every", "any", "most", "few", "less", "least", "enough", "very", "just",
    "only", "even", "already", "still", "yet", "always", "never", "often",
    "sometimes", "usually", "generally", "typically", "commonly", "normally",
    "actually", "really", "quite", "rather", "fairly", "pretty", "almost",
    "nearly", "hardly", "simply", "clearly", "easily", "directly", "mainly",
    "largely", "mostly", "especially", "particularly", "specifically", "exactly",
    "probably", "possibly", "perhaps", "maybe", "certainly", "definitely",
    "obviously", "apparently", "generally", "overall", "basically", "essentially",
    "effectively", "efficiently", "successfully", "properly", "correctly",
    "appropriately", "suitably", "adequately", "well", "good", "better", "best",
    "great", "high", "low", "new", "old", "long", "short", "big", "small",
    "large", "little", "young", "right", "wrong", "true", "false", "real",
    "full", "empty", "hard", "soft", "easy", "difficult", "simple", "complex",
    "important", "necessary", "possible", "available", "ready", "able", "likely",
    "certain", "sure", "clear", "obvious", "main", "major", "key", "common",
    "public", "private", "local", "global", "general", "special", "particular",
    "current", "present", "recent", "latest", "final", "original", "initial",
    "primary", "secondary", "basic", "standard", "normal", "regular", "natural",
    "physical", "mental", "social", "political", "economic", "financial",
    "commercial", "industrial", "technical", "digital", "electronic", "virtual",
    "internal", "external", "external", "outside", "inside", "above", "below",
    "around", "back", "forward", "away", "down", "up", "off", "on", "in",
}


def _split_camel(s: str) -> list[str]:
    """Split camelCase into words."""
    parts = re.sub(r"([a-z])([A-Z])", r"\1 \2", s)
    return [p for p in re.split(r"[-_\s]+", parts) if len(p) > 1]


def extract_overview_keywords(dir_name: str, desc_text: str, rel_path: str) -> tuple[list[str], list[str]]:
    """从概览目录名和描述文本提取中英文关键词。"""
    keywords_en = []
    keywords_zh = []
    
    # 1. 从目录名提取英文关键词（去除 cj- 前缀，拆分驼峰/连字符/下划线）
    clean_dir = re.sub(r"^cj-", "", dir_name.lower())
    clean_dir = re.sub(r"-?\d+more$", "", clean_dir)
    clean_dir = re.sub(r"_[a-f0-9]{8}$", "", clean_dir)
    clean_dir = re.sub(r"^[._]+", "", clean_dir)
    if clean_dir and len(clean_dir) > 2:
        parts = re.findall(r"[A-Z][a-z]+|[a-z]+|\d+", clean_dir.replace("-", "_"))
        for p in parts:
            if len(p) > 2 and p.lower() not in EN_STOP_WORDS:
                keywords_en.append(p.lower())
        if clean_dir.lower() not in EN_STOP_WORDS and len(clean_dir) > 2:
            keywords_en.append(clean_dir.lower())
    
    # 2. 从描述提取英文关键词（API名、组件名、技术术语，保留 @ 符号）
    en_terms = re.findall(r"@[A-Za-z_][A-Za-z0-9_]*|[A-Z][a-zA-Z]{2,}|[A-Z]{2,}", desc_text)
    for w in en_terms:
        if w.lower() not in EN_STOP_WORDS and w.lower() not in keywords_en:
            keywords_en.append(w)
    
    # 3. 从描述提取中文关键词（2字以上连续中文）
    zh_chars = re.findall(r"[\u4e00-\u9fff]{2,}", desc_text[:500])
    for zh in zh_chars:
        if zh not in TITLE_STOP_ZH:
            keywords_zh.append(zh)
    
    # 去重
    keywords_en = list(dict.fromkeys(keywords_en))[:15]
    keywords_zh = list(dict.fromkeys(keywords_zh))[:15]
    
    return keywords_en, keywords_zh


def extract_overview_nodes(overview_path: Path, root_dir: Path) -> tuple[list[DocNode], list[Edge]]:
    """从 .overview.md 提取概览节点和 CONTAINS 边。

    概览节点是图谱中的"上帝节点"（is_god_node=True），代表一个文档模块的入口。
    CONTAINS 边来源：
    1. 快速导航章节中的 Markdown 链接
    2. 同目录下的 .md 文件和子目录（基于目录结构推断）
    """
    try:
        content = safe_read_text(overview_path)
    except Exception:
        return [], []

    rel_path = str(overview_path.relative_to(root_dir)).replace("\\", "/")
    category = infer_category(rel_path, root_dir.name)
    namespace = build_namespace(rel_path)
    dir_name = overview_path.parent.name

    desc_text = content[:500]
    zh_chars = re.findall(r"[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef，。！？；：""''（）【】《》]", desc_text)
    desc_zh = "".join(zh_chars)[:200]

    # 从目录名和描述提取关键词
    keywords_en, keywords_zh = extract_overview_keywords(dir_name, desc_text, rel_path)

    overview_node = DocNode(
        id=f"{category}_{namespace}_overview_{dir_name}".replace(" ", "_").lower(),
        label=dir_name,
        layer=1,
        namespace=namespace,
        category=category,
        source_file=rel_path,
        description_en=desc_text[:500],
        description_zh=desc_zh,
        keywords_zh=keywords_zh,
        keywords_en=keywords_en,
        is_god_node=True,
    )

    edges = []
    seen = set()
    nav_section = re.search(r"##\s*快速导航[\s\S]*?(?=##|$)", content)
    if nav_section:
        links = re.findall(r"[`]?([a-zA-Z0-9_./-]+\.md)[`]?", nav_section.group())
        for link in links:
            link_clean = link.strip().rstrip("/")
            if link_clean and link_clean != dir_name:
                target_path = (dir_path / link_clean).resolve()
                try:
                    target_rel = str(target_path.relative_to(root_dir.resolve()))
                    child_id = compute_node_id(target_rel, root_dir, Path(link_clean).stem)
                except ValueError:
                    child_id = None
                if child_id and child_id not in seen:
                    edges.append(Edge(
                        source=overview_node.id, target=child_id,
                        relation=EdgeRelation.CONTAINS.value,
                        source_file=rel_path,
                    ))
                    seen.add(child_id)

    # 基于目录结构自动建立 CONTAINS 边
    dir_path = overview_path.parent
    for item in dir_path.iterdir():
        if item.name.startswith(".") or item.name == overview_path.name:
            continue
        target_id = None
        if item.is_dir():
            sub_overview = item / ".overview.md"
            if sub_overview.exists():
                sub_rel_path = str(sub_overview.relative_to(root_dir)).replace("\\", "/")
                sub_category = infer_category(sub_rel_path, root_dir.name)
                sub_namespace = build_namespace(sub_rel_path)
                target_id = f"{sub_category}_{sub_namespace}_overview_{item.name}".replace(" ", "_").lower()
        elif item.is_file() and item.suffix == ".md":
            if item.name.startswith(".abstract") or item.name.startswith(".overview"):
                continue
            item_rel_path = str(item.relative_to(root_dir)).replace("\\", "/")
            target_id = compute_node_id(item_rel_path, root_dir, item.stem)

        if target_id and target_id not in seen:
            edges.append(Edge(
                source=overview_node.id, target=target_id,
                relation=EdgeRelation.CONTAINS.value,
                source_file=rel_path,
            ))
            seen.add(target_id)

    return [overview_node], edges
