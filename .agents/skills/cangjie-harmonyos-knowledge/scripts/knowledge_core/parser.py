from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from .util import make_anchor, norm_text, read_text_lossless, relative_posix, sha256_bytes


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
SYMBOL_HEADING_RE = re.compile(
    r"^(?:(?:public|protected|private|internal|static|open|abstract|sealed|override|unsafe)\s+)*"
    r"(?P<kind>func|class|interface|enum|struct|type|var|let|const|prop|init|operator|macro|extend)\b\s*(?P<rest>.*)$",
    re.IGNORECASE,
)
IMPORT_RE = re.compile(r"^\s*import\s+([A-Za-z0-9_.*{}.,\s]+)")
PERMISSION_RE = re.compile(r"\bohos\.permission\.[A-Za-z0-9_.]+\b")
SYSCAP_RE = re.compile(r"\bSystemCapability\.[A-Za-z0-9_.]+\b")
SINCE_RE = re.compile(r"\*\*(?:起始版本|开始版本|Since)[:：]\*\*\s*([^\n<]+)", re.IGNORECASE)
ERROR_CODE_RE = re.compile(r"^\s*\|\s*(\d{5,})\s*\|", re.MULTILINE)


@dataclass(slots=True)
class CodeBlock:
    language: str
    code: str
    start_line: int
    end_line: int
    imports: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Link:
    text: str
    target: str
    line: int


@dataclass(slots=True)
class Section:
    title: str
    level: int
    breadcrumb: str
    anchor: str
    start_line: int
    end_line: int
    body: str
    kind: str
    parent_symbol: str | None = None
    code_blocks: list[CodeBlock] = field(default_factory=list)
    links: list[Link] = field(default_factory=list)
    contracts: dict[str, list[str]] = field(default_factory=dict)

    @property
    def ref_suffix(self) -> str:
        return f"#{self.anchor}" if self.anchor else ""


@dataclass(slots=True)
class ParsedDocument:
    path: Path
    rel_path: str
    doc_type: str
    kit: str
    title: str
    encoding: str
    digest: str
    size: int
    sections: list[Section]


def detect_doc_type(rel_path: str) -> str:
    parts = Path(rel_path).parts
    if len(parts) >= 2 and parts[0].lower() == "docs":
        return parts[1].lower()
    return "unknown"


def detect_kit(rel_path: str) -> str:
    parts = Path(rel_path).parts
    if len(parts) >= 3 and parts[0].lower() == "docs":
        return parts[2]
    if len(parts) >= 2:
        return parts[1]
    return ""


def classify_section(doc_type: str, level: int, title: str) -> tuple[str, str | None]:
    match = SYMBOL_HEADING_RE.match(norm_text(title))
    if doc_type == "api" and match:
        kind = match.group("kind").lower()
        return kind, None
    if title.lower().startswith("示例") or title.lower().startswith("example"):
        return "example-section", None
    if doc_type == "guide":
        return "guide", None
    return "section", None


def extract_symbol_name(title: str) -> tuple[str | None, str | None]:
    title = norm_text(title).strip("`")
    match = SYMBOL_HEADING_RE.match(title)
    if not match:
        return None, None
    kind = match.group("kind").lower()
    rest = match.group("rest").strip()
    if kind == "init":
        return kind, kind
    if kind == "operator":
        if rest.lower().startswith("func "):
            rest = rest[5:].lstrip()
        token = rest.split("(", 1)[0].strip().strip("`")
        return kind, f"{kind} {token}" if token else kind
    token = re.split(r"[\s(<:{]", rest, maxsplit=1)[0].strip()
    token = token.strip("`")
    return kind, token or None


def parse_markdown(path: Path, root: Path) -> ParsedDocument:
    data = path.read_bytes()
    text, encoding = read_text_lossless(path)
    rel_path = relative_posix(path, root)
    doc_type = detect_doc_type(rel_path)
    kit = detect_kit(rel_path)
    lines = text.splitlines()
    anchors: dict[str, int] = {}
    headings: list[tuple[int, int, str, str]] = []
    active_fence: tuple[str, int] | None = None
    for idx, line in enumerate(lines, 1):
        fence = FENCE_RE.match(line)
        if fence:
            marker = fence.group(1)
            if active_fence is None:
                active_fence = (marker[0], len(marker))
            elif marker[0] == active_fence[0] and len(marker) >= active_fence[1]:
                active_fence = None
            continue
        if active_fence is not None:
            continue
        match = HEADING_RE.match(line)
        if match:
            level = len(match.group(1))
            title = norm_text(match.group(2))
            headings.append((idx, level, title, make_anchor(title, anchors)))
    if not headings:
        headings.append((1, 1, path.stem, make_anchor(path.stem, anchors)))

    doc_title = headings[0][2]
    sections: list[Section] = []
    stack: list[tuple[int, str]] = []
    for pos, (start, level, title, anchor) in enumerate(headings):
        end = headings[pos + 1][0] - 1 if pos + 1 < len(headings) else len(lines)
        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, title))
        breadcrumb = " > ".join(item[1] for item in stack)
        body = "\n".join(lines[start:end])
        kind, parent_symbol = classify_section(doc_type, level, title)
        sections.append(
            Section(
                title=title,
                level=level,
                breadcrumb=breadcrumb,
                anchor=anchor,
                start_line=start,
                end_line=end,
                body=body,
                kind=kind,
                parent_symbol=parent_symbol,
                code_blocks=[],
                links=[],
                contracts=extract_contracts(f"{title}\n{body}"),
            )
        )

    attach_blocks_and_links(lines, sections)
    attach_parent_symbols(sections)
    return ParsedDocument(
        path=path,
        rel_path=rel_path,
        doc_type=doc_type,
        kit=kit,
        title=doc_title,
        encoding=encoding,
        digest=sha256_bytes(data),
        size=len(data),
        sections=sections,
    )


def extract_contracts(text: str) -> dict[str, list[str]]:
    """Extract stable HarmonyOS API contracts without model inference."""

    result: dict[str, list[str]] = {}
    values = sorted(set(PERMISSION_RE.findall(text)))
    if values:
        result["permissions"] = values
    values = sorted(set(SYSCAP_RE.findall(text)))
    if values:
        result["syscaps"] = values
    values = [norm_text(item).strip(" .") for item in SINCE_RE.findall(text)]
    values = list(dict.fromkeys(item for item in values if item))
    if values:
        result["since"] = values
    if "错误码" in text or "BusinessException" in text:
        values = list(dict.fromkeys(ERROR_CODE_RE.findall(text)))
        if values:
            result["error_codes"] = values
    return result


def attach_parent_symbols(sections: list[Section]) -> None:
    symbol_stack: list[tuple[int, str]] = []
    for section in sections:
        kind, name = extract_symbol_name(section.title)
        if kind and name and section.level <= 2:
            symbol_stack = [(section.level, name)]
            continue
        while symbol_stack and symbol_stack[-1][0] >= section.level:
            symbol_stack.pop()
        if section.kind in {
            "func",
            "class",
            "interface",
            "enum",
            "struct",
            "type",
            "var",
            "let",
            "const",
            "prop",
            "init",
            "operator",
            "macro",
            "extend",
        }:
            if symbol_stack:
                section.parent_symbol = symbol_stack[-1][1]
        if kind and name:
            symbol_stack.append((section.level, name))


def attach_blocks_and_links(lines: list[str], sections: list[Section]) -> None:
    section_iter = iter(sections)
    current = next(section_iter, None)
    next_section = next(section_iter, None)
    active_fence: tuple[str, int] | None = None
    fence_lang = ""
    fence_start = 0
    fence_lines: list[str] = []

    def advance(line_no: int) -> Section | None:
        nonlocal current, next_section
        while next_section and line_no >= next_section.start_line:
            current = next_section
            next_section = next(section_iter, None)
        return current

    for idx, line in enumerate(lines, 1):
        sec = advance(idx)
        fence = FENCE_RE.match(line)
        if fence:
            marker = fence.group(1)
            if active_fence is not None and marker[0] == active_fence[0] and len(marker) >= active_fence[1]:
                code = "\n".join(fence_lines)
                imports = [m.group(1).strip() for m in map(IMPORT_RE.match, fence_lines) if m]
                target = sec or current
                if target:
                    target.code_blocks.append(
                        CodeBlock(
                            language=fence_lang.strip().lower(),
                            code=code,
                            start_line=fence_start,
                            end_line=idx,
                            imports=imports,
                        )
                    )
                active_fence = None
                fence_lines = []
            elif active_fence is None:
                active_fence = (marker[0], len(marker))
                fence_lang = fence.group(2).strip()
                fence_start = idx
                fence_lines = []
            continue
        if active_fence is not None:
            fence_lines.append(line)
            continue
        if sec:
            for match in LINK_RE.finditer(line):
                sec.links.append(Link(text=match.group(1), target=match.group(2), line=idx))

    if active_fence is not None and current:
        code = "\n".join(fence_lines)
        imports = [m.group(1).strip() for m in map(IMPORT_RE.match, fence_lines) if m]
        current.code_blocks.append(
            CodeBlock(
                language=fence_lang.strip().lower(),
                code=code,
                start_line=fence_start,
                end_line=len(lines),
                imports=imports,
            )
        )
