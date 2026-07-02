"""源码图谱提取器。基于 tree-sitter AST 的多语言提取。"""
from __future__ import annotations

import importlib
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional

from core.models import CodeNode, Edge, EdgeRelation


# ── LanguageConfig ───────────────────────────────────────────────────────────

@dataclass
class LanguageConfig:
    ts_module: str
    ts_language_fn: str = "language"
    class_types: frozenset = frozenset()
    function_types: frozenset = frozenset()
    import_types: frozenset = frozenset()
    call_types: frozenset = frozenset()
    name_field: str = "name"
    name_fallback_child_types: tuple = ()
    body_field: str = "body"
    body_fallback_child_types: tuple = ()
    call_function_field: str = "function"
    call_accessor_node_types: frozenset = frozenset()
    call_accessor_field: str = "attribute"
    function_boundary_types: frozenset = frozenset()
    import_handler: Optional[Callable] = None
    resolve_function_name_fn: Optional[Callable] = None
    function_label_parens: bool = True
    extra_walk_fn: Optional[Callable] = None
    member_types: frozenset = frozenset()
    enum_value_parent: str = ""
    extension_types: frozenset = frozenset()
    extend_type_child: str = ""


# ── Helpers ──────────────────────────────────────────────────────────────────

def _make_id(*parts: str) -> str:
    combined = "_".join(p.strip("_.") for p in parts if p)
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "_", combined)
    return cleaned.strip("_").lower()


def _read_text(node, source: bytes) -> str:
    return source[node.start_byte:node.end_byte].decode("utf-8", errors="replace")


def _resolve_name(node, source: bytes, config: LanguageConfig) -> Optional[str]:
    if config.resolve_function_name_fn:
        return None
    n = node.child_by_field_name(config.name_field)
    if n:
        return _read_text(n, source)
    for child in node.children:
        if child.type in config.name_fallback_child_types:
            return _read_text(child, source)
    return None


def _find_body(node, config: LanguageConfig):
    b = node.child_by_field_name(config.body_field)
    if b:
        return b
    for child in node.children:
        if child.type in config.body_fallback_child_types:
            return child
    return None


# ── Import handlers ─────────────────────────────────────────────────────────

def _import_python(node, source, file_nid, edges, str_path):
    t = node.type
    if t == "import_statement":
        for child in node.children:
            if child.type in ("dotted_name", "aliased_import"):
                raw = _read_text(child, source)
                module_name = raw.split(" as ")[0].strip().lstrip(".")
                tgt_nid = _make_id("import", module_name)
                edges.append(Edge(source=file_nid, target=tgt_nid, relation=EdgeRelation.USES.value,
                                  source_file=str_path, confidence="EXTRACTED", confidence_score=1.0))
    elif t == "import_from_statement":
        module_node = node.child_by_field_name("module_name")
        if module_node:
            raw = _read_text(module_node, source)
            tgt_nid = _make_id("import", raw.lstrip("."))
            edges.append(Edge(source=file_nid, target=tgt_nid, relation=EdgeRelation.USES.value,
                              source_file=str_path, confidence="EXTRACTED", confidence_score=1.0))


def _import_js(node, source, file_nid, edges, str_path):
    for child in node.children:
        if child.type == "string":
            raw = _read_text(child, source).strip("'\"` ")
            if raw:
                module_name = raw.split("/")[-1] if not raw.startswith(".") else raw.lstrip("./")
                tgt_nid = _make_id("import", module_name)
                edges.append(Edge(source=file_nid, target=tgt_nid, relation=EdgeRelation.USES.value,
                                  source_file=str_path, confidence="EXTRACTED", confidence_score=1.0))
            break


def _import_java(node, source, file_nid, edges, str_path):
    for child in node.children:
        if child.type in ("scoped_identifier", "identifier"):
            raw = _read_text(child, source)
            module_name = raw.split(".")[-1].strip("*").strip(".")
            if module_name:
                tgt_nid = _make_id("import", module_name)
                edges.append(Edge(source=file_nid, target=tgt_nid, relation=EdgeRelation.USES.value,
                                  source_file=str_path, confidence="EXTRACTED", confidence_score=1.0))
            break


def _import_c(node, source, file_nid, edges, str_path):
    for child in node.children:
        if child.type in ("string_literal", "system_lib_string", "string"):
            raw = _read_text(child, source).strip('"<> ')
            module_name = raw.split("/")[-1].split(".")[0]
            if module_name:
                tgt_nid = _make_id("import", module_name)
                edges.append(Edge(source=file_nid, target=tgt_nid, relation=EdgeRelation.USES.value,
                                  source_file=str_path, confidence="EXTRACTED", confidence_score=1.0))
            break


def _import_cangjie(node, source, file_nid, edges, str_path):
    for child in node.children:
        if child.type == "scoped_identifier":
            raw = _read_text(child, source)
            module_name = raw.split(".")[-1].strip()
            if module_name:
                tgt_nid = _make_id("import", module_name)
                edges.append(Edge(source=file_nid, target=tgt_nid, relation=EdgeRelation.USES.value,
                                  source_file=str_path, confidence="EXTRACTED", confidence_score=1.0))
            break


# ── C/C++ function name helpers ─────────────────────────────────────────────

def _get_c_func_name(node, source):
    if node.type == "identifier":
        return _read_text(node, source)
    decl = node.child_by_field_name("declarator")
    if decl:
        return _get_c_func_name(decl, source)
    for child in node.children:
        if child.type == "identifier":
            return _read_text(child, source)
    return None


def _get_cpp_func_name(node, source):
    if node.type == "identifier":
        return _read_text(node, source)
    if node.type == "qualified_identifier":
        name_node = node.child_by_field_name("name")
        if name_node:
            return _read_text(name_node, source)
    decl = node.child_by_field_name("declarator")
    if decl:
        return _get_cpp_func_name(decl, source)
    for child in node.children:
        if child.type == "identifier":
            return _read_text(child, source)
    return None


# ── Language configs ────────────────────────────────────────────────────────

_CANGJIE_CONFIG = LanguageConfig(
    ts_module="tree_sitter_cangjie",
    ts_language_fn="language",
    class_types=frozenset({"structDefinition", "classDefinition", "enumDefinition", "interfaceDefinition"}),
    function_types=frozenset({"functionDefinition", "init"}),
    import_types=frozenset({"importList"}),
    call_types=frozenset({"postfixExpression"}),
    name_field="name",
    name_fallback_child_types=("structName", "className", "enumName", "funcName", "interfaceName"),
    body_field="body",
    body_fallback_child_types=("block", "classBody", "structBody", "enumBody", "interfaceBody", "extendBody"),
    function_boundary_types=frozenset({"functionDefinition", "init"}),
    import_handler=_import_cangjie,
    function_label_parens=True,
    member_types=frozenset({"variableDeclaration", "propertyDeclaration"}),
    enum_value_parent="enumBody",
    extension_types=frozenset({"extendDefinition"}),
    extend_type_child="extendType",
)

_PYTHON_CONFIG = LanguageConfig(
    ts_module="tree_sitter_python",
    class_types=frozenset({"class_definition"}),
    function_types=frozenset({"function_definition"}),
    import_types=frozenset({"import_statement", "import_from_statement"}),
    call_types=frozenset({"call"}),
    call_function_field="function",
    call_accessor_node_types=frozenset({"attribute"}),
    call_accessor_field="attribute",
    function_boundary_types=frozenset({"function_definition"}),
    import_handler=_import_python,
)

_JS_CONFIG = LanguageConfig(
    ts_module="tree_sitter_javascript",
    class_types=frozenset({"class_declaration"}),
    function_types=frozenset({"function_declaration", "method_definition"}),
    import_types=frozenset({"import_statement"}),
    call_types=frozenset({"call_expression"}),
    call_function_field="function",
    call_accessor_node_types=frozenset({"member_expression"}),
    call_accessor_field="property",
    function_boundary_types=frozenset({"function_declaration", "arrow_function", "method_definition"}),
    import_handler=_import_js,
)

_TS_CONFIG = LanguageConfig(
    ts_module="tree_sitter_typescript",
    ts_language_fn="language_typescript",
    class_types=frozenset({"class_declaration"}),
    function_types=frozenset({"function_declaration", "method_definition"}),
    import_types=frozenset({"import_statement"}),
    call_types=frozenset({"call_expression"}),
    call_function_field="function",
    call_accessor_node_types=frozenset({"member_expression"}),
    call_accessor_field="property",
    function_boundary_types=frozenset({"function_declaration", "arrow_function", "method_definition"}),
    import_handler=_import_js,
)

_JAVA_CONFIG = LanguageConfig(
    ts_module="tree_sitter_java",
    class_types=frozenset({"class_declaration", "interface_declaration"}),
    function_types=frozenset({"method_declaration", "constructor_declaration"}),
    import_types=frozenset({"import_declaration"}),
    call_types=frozenset({"method_invocation"}),
    call_function_field="name",
    function_boundary_types=frozenset({"method_declaration", "constructor_declaration"}),
    import_handler=_import_java,
)

_C_CONFIG = LanguageConfig(
    ts_module="tree_sitter_c",
    class_types=frozenset(),
    function_types=frozenset({"function_definition"}),
    import_types=frozenset({"preproc_include"}),
    call_types=frozenset({"call_expression"}),
    call_function_field="function",
    call_accessor_node_types=frozenset({"field_expression"}),
    call_accessor_field="field",
    function_boundary_types=frozenset({"function_definition"}),
    import_handler=_import_c,
    resolve_function_name_fn=_get_c_func_name,
)

_CPP_CONFIG = LanguageConfig(
    ts_module="tree_sitter_cpp",
    class_types=frozenset({"class_specifier"}),
    function_types=frozenset({"function_definition"}),
    import_types=frozenset({"preproc_include"}),
    call_types=frozenset({"call_expression"}),
    call_function_field="function",
    call_accessor_node_types=frozenset({"field_expression", "qualified_identifier"}),
    call_accessor_field="field",
    function_boundary_types=frozenset({"function_definition"}),
    import_handler=_import_c,
    resolve_function_name_fn=_get_cpp_func_name,
)

_CSHARP_CONFIG = LanguageConfig(
    ts_module="tree_sitter_c_sharp",
    class_types=frozenset({"class_declaration", "interface_declaration"}),
    function_types=frozenset({"method_declaration"}),
    import_types=frozenset({"using_directive"}),
    call_types=frozenset({"invocation_expression"}),
    call_function_field="function",
    call_accessor_node_types=frozenset({"member_access_expression"}),
    call_accessor_field="name",
    body_fallback_child_types=("declaration_list",),
    function_boundary_types=frozenset({"method_declaration"}),
    import_handler=_import_c,
)

_KOTLIN_CONFIG = LanguageConfig(
    ts_module="tree_sitter_kotlin",
    class_types=frozenset({"class_declaration", "object_declaration"}),
    function_types=frozenset({"function_declaration"}),
    import_types=frozenset({"import_header"}),
    call_types=frozenset({"call_expression"}),
    name_fallback_child_types=("simple_identifier",),
    body_fallback_child_types=("function_body", "class_body"),
    function_boundary_types=frozenset({"function_declaration"}),
    import_handler=_import_java,
)

_SWIFT_CONFIG = LanguageConfig(
    ts_module="tree_sitter_swift",
    class_types=frozenset({"class_declaration", "protocol_declaration"}),
    function_types=frozenset({"function_declaration", "init_declaration", "deinit_declaration", "subscript_declaration"}),
    import_types=frozenset({"import_declaration"}),
    call_types=frozenset({"call_expression"}),
    name_fallback_child_types=("simple_identifier", "type_identifier", "user_type"),
    body_fallback_child_types=("class_body", "protocol_body", "function_body", "enum_class_body"),
    function_boundary_types=frozenset({"function_declaration", "init_declaration", "deinit_declaration", "subscript_declaration"}),
    import_handler=_import_js,
)

_GO_CONFIG = LanguageConfig(
    ts_module="tree_sitter_go",
    class_types=frozenset({"type_declaration"}),
    function_types=frozenset({"function_declaration", "method_declaration"}),
    import_types=frozenset({"import_declaration"}),
    call_types=frozenset({"call_expression"}),
    name_field="name",
    name_fallback_child_types=("type_identifier", "identifier", "field_identifier", "package_identifier"),
    body_field="body",
    body_fallback_child_types=("block",),
    call_function_field="function",
    call_accessor_node_types=frozenset({"selector_expression"}),
    call_accessor_field="field",
    function_boundary_types=frozenset({"function_declaration", "method_declaration"}),
    import_handler=_import_js,
)

_RUST_CONFIG = LanguageConfig(
    ts_module="tree_sitter_rust",
    class_types=frozenset({"struct_item", "enum_item", "trait_item", "impl_item"}),
    function_types=frozenset({"function_item", "function_signature_item"}),
    import_types=frozenset({"use_declaration"}),
    call_types=frozenset({"call_expression"}),
    name_field="name",
    name_fallback_child_types=("type_identifier", "identifier"),
    body_field="body",
    body_fallback_child_types=("block",),
    call_function_field="function",
    call_accessor_node_types=frozenset({"field_expression"}),
    call_accessor_field="field",
    function_boundary_types=frozenset({"function_item"}),
    import_handler=_import_js,
)

# Extension → config mapping
_LANG_MAP: dict[str, LanguageConfig] = {}


def _build_lang_map():
    for ext, cfg in [
        (".cj", _CANGJIE_CONFIG),
        (".py", _PYTHON_CONFIG),
        (".js", _JS_CONFIG),
        (".jsx", _JS_CONFIG),
        (".mjs", _JS_CONFIG),
        (".ts", _TS_CONFIG),
        (".tsx", _TS_CONFIG),
        (".java", _JAVA_CONFIG),
        (".c", _C_CONFIG),
        (".h", _C_CONFIG),
        (".cpp", _CPP_CONFIG),
        (".cc", _CPP_CONFIG),
        (".cxx", _CPP_CONFIG),
        (".hpp", _CPP_CONFIG),
        (".cs", _CSHARP_CONFIG),
        (".kt", _KOTLIN_CONFIG),
        (".kts", _KOTLIN_CONFIG),
        (".swift", _SWIFT_CONFIG),
        (".go", _GO_CONFIG),
        (".rs", _RUST_CONFIG),
    ]:
        _LANG_MAP[ext] = cfg


_build_lang_map()


def detect_language(file_path: Path) -> Optional[LanguageConfig]:
    ext = file_path.suffix.lower()
    return _LANG_MAP.get(ext)


# ── Generic extractor ───────────────────────────────────────────────────────

def _extract_ast(file_path: Path, config: LanguageConfig) -> tuple[list[CodeNode], list[Edge]]:
    try:
        mod = importlib.import_module(config.ts_module)
        from tree_sitter import Language, Parser
        lang_fn = getattr(mod, config.ts_language_fn, None)
        if lang_fn is None:
            lang_fn = getattr(mod, "language", None)
        if lang_fn is None:
            return [], []
        language = Language(lang_fn())
    except ImportError:
        return [], []
    except Exception:
        return [], []

    try:
        parser = Parser(language)
        source = file_path.read_bytes()
        tree = parser.parse(source)
        root = tree.root_node
    except Exception:
        return [], []

    str_path = str(file_path)
    category = _infer_category(str_path)
    namespace = _build_namespace(str_path)

    nodes: list[CodeNode] = []
    edges: list[Edge] = []
    seen_ids: set[str] = set()
    function_bodies: list = []
    label_to_nid: dict[str, str] = {}
    node_by_id: dict[str, CodeNode] = {}

    def add_node(nid: str, label: str, api_kind: str, line: int, **kwargs):
        if nid not in seen_ids:
            seen_ids.add(nid)
            node = CodeNode(
                id=nid, label=label, api_kind=api_kind,
                namespace=namespace, category=category, source_file=str_path,
                **kwargs
            )
            nodes.append(node)
            node_by_id[nid] = node
            label_to_nid[label.lower()] = nid
            label_to_nid[label.lower().rstrip("()").lstrip(".")] = nid

    def add_edge(src: str, tgt: str, relation: str, line: int):
        edges.append(Edge(
            source=src, target=tgt, relation=relation,
            source_file=str_path, confidence="EXTRACTED", confidence_score=1.0
        ))

    file_nid = _make_id("file", str_path)
    add_node(file_nid, file_path.name, "file", 1)

    def walk(node, parent_class_nid: Optional[str] = None):
        t = node.type

        if t in config.import_types:
            if config.import_handler:
                config.import_handler(node, source, file_nid, edges, str_path)
            return

        if t in config.class_types:
            name_node = node.child_by_field_name(config.name_field)
            if name_node is None:
                for child in node.children:
                    if child.type in config.name_fallback_child_types:
                        name_node = child
                        break
            if not name_node:
                return

            class_name = _read_text(name_node, source)
            api_kind = "class"
            if "enum" in t.lower():
                api_kind = "enum"
            elif "interface" in t.lower() or "protocol" in t.lower():
                api_kind = "interface"
            elif "struct" in t.lower():
                api_kind = "struct"

            class_nid = _make_id(namespace, api_kind, class_name)
            line = node.start_point[0] + 1
            add_node(class_nid, class_name, api_kind, line)
            add_edge(file_nid, class_nid, EdgeRelation.CONTAINS.value, line)

            parent_type = _extract_inheritance(node, source, config)
            if parent_type:
                parent_lower = parent_type.lower().rstrip("()").lstrip(".")
                existing_nid = label_to_nid.get(parent_lower)
                if existing_nid and existing_nid in seen_ids:
                    parent_nid = existing_nid
                else:
                    parent_nid = _make_id(namespace, "class", parent_type)
                    add_node(parent_nid, parent_type, "class", line)
                add_edge(class_nid, parent_nid, EdgeRelation.EXTENDS.value, line)
                node_by_id[class_nid].parent_type = parent_type

            body = _find_body(node, config)
            if body:
                if api_kind == "enum" and config.enum_value_parent:
                    _extract_enum_values(body, source, class_nid, node_by_id)
                for child in body.children:
                    walk(child, parent_class_nid=class_nid)
            return

        if t in config.extension_types:
            target_name = None
            for child in node.children:
                if child.type == config.extend_type_child:
                    target_name = _read_text(child, source)
                    break
            if not target_name:
                return

            ext_nid = _make_id(namespace, "extension", target_name)
            line = node.start_point[0] + 1
            add_node(ext_nid, target_name, "extension", line)
            add_edge(file_nid, ext_nid, EdgeRelation.CONTAINS.value, line)

            tgt_nid = _make_id(namespace, "class", target_name)
            if tgt_nid in seen_ids:
                add_edge(ext_nid, tgt_nid, EdgeRelation.EXTENSION_OF.value, line)
            else:
                if _is_user_type(target_name):
                    node_by_id[ext_nid].keywords.append(target_name)
                    label_to_nid[target_name.lower()] = tgt_nid

            body = _find_body(node, config)
            if body:
                for child in body.children:
                    walk(child, parent_class_nid=ext_nid)
            return

        if t in config.function_types:
            func_name = None
            if config.resolve_function_name_fn:
                declarator = node.child_by_field_name("declarator")
                if declarator:
                    func_name = config.resolve_function_name_fn(declarator, source)
            elif t == "init":
                func_name = "init"
            else:
                func_name = _resolve_name(node, source, config)

            if not func_name:
                return

            line = node.start_point[0] + 1
            if parent_class_nid:
                node_by_id[parent_class_nid].methods.append(func_name)
                caller_nid = parent_class_nid
            else:
                caller_nid = _make_id(namespace, "function", func_name)
                add_node(caller_nid, f"{func_name}()", "function", line)
                add_edge(file_nid, caller_nid, EdgeRelation.CONTAINS.value, line)

            body = _find_body(node, config)
            if body:
                function_bodies.append((caller_nid, body))

            _extract_param_types(node, source, config, caller_nid, namespace, seen_ids,
                                 label_to_nid, node_by_id, edges, str_path)
            _extract_return_type(node, source, config, caller_nid, namespace, seen_ids,
                                 label_to_nid, node_by_id, edges, str_path)
            return

        if t in config.member_types:
            if parent_class_nid and parent_class_nid in node_by_id:
                _extract_member(node, source, parent_class_nid, node_by_id, namespace,
                                seen_ids, label_to_nid, edges, str_path, config)
            return

        if config.extra_walk_fn:
            if config.extra_walk_fn(node, source, file_nid, str_path,
                                     nodes, edges, seen_ids, function_bodies,
                                     parent_class_nid, add_node, add_edge):
                return

        for child in node.children:
            walk(child, parent_class_nid=parent_class_nid)

    walk(root)

    seen_call_pairs: set = set()
    for func_nid, body_node in function_bodies:
        _walk_calls(body_node, func_nid, source, config, label_to_nid, seen_call_pairs,
                     file_nid, str_path, edges, add_node, namespace)

    for node_obj in nodes:
        for kw in node_obj.keywords:
            target_id = _make_id(namespace, "class", kw)
            if target_id != node_obj.id and target_id in seen_ids:
                edges.append(Edge(
                    source=node_obj.id, target=target_id,
                    relation=EdgeRelation.USES.value,
                    source_file=str_path, confidence="EXTRACTED", confidence_score=1.0
                ))

    return nodes, edges


def _extract_inheritance(node, source, config):
    if config.ts_module == "tree_sitter_cangjie":
        for child in node.children:
            if child.type == "superOrInterface":
                for sub in child.children:
                    if sub.type == "identifier":
                        return _read_text(sub, source)
    elif config.ts_module == "tree_sitter_python":
        args = node.child_by_field_name("superclasses")
        if args:
            for arg in args.children:
                if arg.type == "identifier":
                    return _read_text(arg, source)
    elif config.ts_module == "tree_sitter_java":
        sup = node.child_by_field_name("superclass")
        if sup:
            for sub in sup.children:
                if sub.type == "type_identifier":
                    return _read_text(sub, source)
    elif config.ts_module == "tree_sitter_swift":
        for child in node.children:
            if child.type == "inheritance_specifier":
                for sub in child.children:
                    if sub.type in ("user_type", "type_identifier"):
                        return _read_text(sub, source)
    elif config.ts_module == "tree_sitter_c_sharp":
        for child in node.children:
            if child.type == "base_list":
                for sub in child.children:
                    if sub.type in ("identifier", "generic_name"):
                        if sub.type == "generic_name":
                            name_child = sub.child_by_field_name("name")
                            return _read_text(name_child, source) if name_child else _read_text(sub.children[0], source)
                        return _read_text(sub, source)
    return ""


_BUILTIN_TYPES = frozenset({
    "Int", "Int8", "Int16", "Int32", "Int64", "UInt", "UInt8", "UInt16", "UInt32", "UInt64", "UIntNative",
    "Float", "Float16", "Float32", "Float64",
    "Bool", "Unit", "String", "CString", "Array", "Option", "Result", "Map", "Set", "HashMap", "HashSet",
    "Nothing", "None", "CPointer", "CFunc", "RuneInt",
})


def _is_user_type(type_name: str) -> bool:
    return type_name not in _BUILTIN_TYPES and not type_name.startswith("C")


def _extract_type_name_from_userType(node, source) -> Optional[str]:
    for child in node.children:
        if child.type == "identifier":
            name = _read_text(child, source)
            if _is_user_type(name):
                return name
    return None


def _extract_enum_values(body_node, source, class_nid, node_by_id):
    for child in body_node.children:
        if child.type == "identifier" and child.is_named:
            value_name = _read_text(child, source)
            if value_name and value_name[0].isupper():
                node_by_id[class_nid].enum_values.append(value_name)


def _extract_member(node, source, parent_nid, node_by_id, namespace,
                    seen_ids, label_to_nid, edges, str_path, config):
    t = node.type
    if t == "variableDeclaration":
        for child in node.children:
            if child.type == "variableName":
                for sub in child.children:
                    if sub.type == "varBindingPattern":
                        field_name = _read_text(sub, source)
                        node_by_id[parent_nid].fields.append(field_name)
                        break
            if child.type == "userType":
                type_name = _extract_type_name_from_userType(child, source)
                if type_name:
                    node_by_id[parent_nid].keywords.append(type_name)
                    tgt_nid = _make_id(namespace, "class", type_name)
                    if tgt_nid not in seen_ids:
                        label_to_nid[type_name.lower()] = tgt_nid
    elif t == "propertyDefinition":
        for child in node.children:
            if child.type == "propertyName":
                field_name = _read_text(child, source)
                node_by_id[parent_nid].fields.append(field_name)
            if child.type == "userType":
                type_name = _extract_type_name_from_userType(child, source)
                if type_name:
                    node_by_id[parent_nid].keywords.append(type_name)
                    tgt_nid = _make_id(namespace, "class", type_name)
                    if tgt_nid not in seen_ids:
                        label_to_nid[type_name.lower()] = tgt_nid


def _extract_param_types(node, source, config, caller_nid, namespace, seen_ids,
                         label_to_nid, node_by_id, edges, str_path):
    params_node = node.child_by_field_name("parameterList")
    if not params_node:
        return
    for child in params_node.children:
        if child.type in ("parameter", "namedParameter"):
            for sub in child.children:
                if sub.type in ("userType", "identifier"):
                    type_name = None
                    if sub.type == "userType":
                        type_name = _extract_type_name_from_userType(sub, source)
                    elif sub.type == "identifier" and _is_user_type(_read_text(sub, source)):
                        type_name = _read_text(sub, source)
                    if type_name and caller_nid in node_by_id:
                        node_by_id[caller_nid].keywords.append(type_name)
                        tgt_nid = _make_id(namespace, "class", type_name)
                        if tgt_nid not in seen_ids:
                            label_to_nid[type_name.lower()] = tgt_nid


def _extract_return_type(node, source, config, caller_nid, namespace, seen_ids,
                         label_to_nid, node_by_id, edges, str_path):
    ret_node = node.child_by_field_name("returnType")
    if not ret_node:
        return
    for child in ret_node.children:
        if child.type in ("userType", "identifier"):
            type_name = None
            if child.type == "userType":
                type_name = _extract_type_name_from_userType(child, source)
            elif child.type == "identifier" and _is_user_type(_read_text(child, source)):
                type_name = _read_text(child, source)
            if type_name and caller_nid in node_by_id:
                node_by_id[caller_nid].keywords.append(type_name)
                tgt_nid = _make_id(namespace, "class", type_name)
                if tgt_nid not in seen_ids:
                    label_to_nid[type_name.lower()] = tgt_nid


def _walk_calls(node, caller_nid, source, config, label_to_nid, seen_pairs,
                file_nid, str_path, edges, add_node, namespace):
    """Walk call sites and emit USES edges."""
    if node.type in config.function_boundary_types:
        return

    if node.type in config.call_types:
        callee_name = _extract_callee_name(node, source, config)
        if callee_name:
            callee_lower = callee_name.lower()
            target_nid = label_to_nid.get(callee_lower)
            if target_nid and target_nid != caller_nid:
                pair = (caller_nid, target_nid)
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    edges.append(Edge(
                        source=caller_nid, target=target_nid,
                        relation=EdgeRelation.USES.value,
                        source_file=str_path, confidence="EXTRACTED", confidence_score=1.0
                    ))

    for child in node.children:
        _walk_calls(child, caller_nid, source, config, label_to_nid, seen_pairs,
                    file_nid, str_path, edges, add_node, namespace)


def _extract_callee_name(node, source, config):
    """Extract callee function name from a call node."""
    if config.ts_module == "tree_sitter_cangjie":
        has_call = any(c.type == "callSuffix" for c in node.children)
        if has_call:
            deepest = node
            for child in node.children:
                if child.type == "postfixExpression":
                    deepest = child
                    break
            for child in deepest.children:
                if child.type == "fieldAccess":
                    for sub in child.children:
                        if sub.type == "simpleIdentifier":
                            return _read_text(sub, source)
                elif child.type == "atomicVariable":
                    return _read_text(child, source)
    elif config.ts_module == "tree_sitter_python":
        func_node = node.child_by_field_name(config.call_function_field)
        if func_node:
            if func_node.type == "identifier":
                return _read_text(func_node, source)
            elif func_node.type == "attribute":
                attr = node.child_by_field_name(config.call_accessor_field)
                if attr:
                    return _read_text(attr, source)
    elif config.ts_module in ("tree_sitter_javascript", "tree_sitter_typescript"):
        func_node = node.child_by_field_name(config.call_function_field)
        if func_node:
            if func_node.type == "identifier":
                return _read_text(func_node, source)
            elif func_node.type in ("member_expression",):
                prop = node.child_by_field_name(config.call_accessor_field)
                if prop:
                    return _read_text(prop, source)
    elif config.ts_module == "tree_sitter_java":
        name_node = node.child_by_field_name("name")
        if name_node:
            return _read_text(name_node, source)
    elif config.ts_module == "tree_sitter_c":
        func_node = node.child_by_field_name(config.call_function_field)
        if func_node:
            if func_node.type == "identifier":
                return _read_text(func_node, source)
            elif func_node.type == "field_expression":
                field = node.child_by_field_name(config.call_accessor_field)
                if field:
                    return _read_text(field, source)
    elif config.ts_module == "tree_sitter_cpp":
        func_node = node.child_by_field_name(config.call_function_field)
        if func_node:
            if func_node.type == "identifier":
                return _read_text(func_node, source)
            elif func_node.type in ("field_expression", "qualified_identifier"):
                name = func_node.child_by_field_name("field") or func_node.child_by_field_name("name")
                if name:
                    return _read_text(name, source)
    elif config.ts_module == "tree_sitter_c_sharp":
        name_node = node.child_by_field_name("name")
        if name_node:
            return _read_text(name_node, source)
        for child in node.children:
            if child.is_named:
                raw = _read_text(child, source)
                if "." in raw:
                    return raw.split(".")[-1]
                return raw
    elif config.ts_module == "tree_sitter_kotlin":
        first = node.children[0] if node.children else None
        if first:
            if first.type == "simple_identifier":
                return _read_text(first, source)
            elif first.type == "navigation_expression":
                for child in reversed(first.children):
                    if child.type == "simple_identifier":
                        return _read_text(child, source)
    elif config.ts_module == "tree_sitter_swift":
        first = node.children[0] if node.children else None
        if first:
            if first.type == "simple_identifier":
                return _read_text(first, source)
            elif first.type == "navigation_expression":
                for child in first.children:
                    if child.type == "navigation_suffix":
                        for sc in child.children:
                            if sc.type == "simple_identifier":
                                return _read_text(sc, source)
    elif config.ts_module == "tree_sitter_go":
        func_node = node.child_by_field_name(config.call_function_field)
        if func_node:
            if func_node.type == "identifier":
                return _read_text(func_node, source)
            elif func_node.type == "selector_expression":
                field = node.child_by_field_name(config.call_accessor_field)
                if field:
                    return _read_text(field, source)
    elif config.ts_module == "tree_sitter_rust":
        func_node = node.child_by_field_name(config.call_function_field)
        if func_node:
            if func_node.type == "identifier":
                return _read_text(func_node, source)
            elif func_node.type == "field_expression":
                field = node.child_by_field_name(config.call_accessor_field)
                if field:
                    return _read_text(field, source)
    return None


# ── Category / namespace inference ──────────────────────────────────────────

def _infer_category(rel_path: str) -> str:
    path = rel_path.replace("\\", "/").lower()
    if path.startswith("stdx/") or "/stdx/" in path:
        return "stdx"
    if path.startswith("std/") or "/std/" in path:
        return "std"
    if "harmonyos" in path:
        return "harmonyos"
    if "lang-features" in path:
        return "lang"
    return "code"


def _build_namespace(rel_path: str) -> str:
    parts = rel_path.replace("\\", "/").split("/")
    ns_parts = []
    skip = {"api", "package", "index", "samples", "guide", "tutorial", "overview", "src"}
    for p in parts[:-1]:
        if p.startswith("cj-"):
            ns_parts.append(p[3:])
        elif p and not p.startswith("."):
            clean = p.lower()
            if clean not in skip:
                ns_parts.append(p)
    return "_".join(ns_parts[-3:]) if ns_parts else "unknown"


# ── Public API ──────────────────────────────────────────────────────────────

def collect_files(root_dir: Path, extensions: Optional[set[str]] = None) -> list[Path]:
    """Collect source files from directory."""
    if extensions is None:
        extensions = set(_LANG_MAP.keys())
    files = []
    for ext in extensions:
        files.extend(root_dir.rglob(f"*{ext}"))
    return sorted(files)


def extract_file(file_path: Path, root_dir: Path) -> tuple[list[CodeNode], list[Edge]]:
    """Extract nodes and edges from a single source file using tree-sitter AST."""
    config = detect_language(file_path)
    if config is None:
        return [], []
    return _extract_ast(file_path, config)


def extract_files(file_paths: list[Path], root_dir: Path) -> tuple[list[CodeNode], list[Edge]]:
    """Extract from multiple source files."""
    all_nodes: list[CodeNode] = []
    all_edges: list[Edge] = []
    for fp in file_paths:
        nodes, edges = extract_file(fp, root_dir)
        all_nodes.extend(nodes)
        all_edges.extend(edges)
    return all_nodes, all_edges
