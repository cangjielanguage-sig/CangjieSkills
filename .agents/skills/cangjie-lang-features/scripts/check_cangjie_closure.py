#!/usr/bin/env python3
"""Deterministic preflight checks for generated Cangjie source files."""

from __future__ import annotations

import argparse
import bisect
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Literal


Severity = Literal["error", "warning"]


@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    column: int
    code: str
    message: str
    reference: str
    severity: Severity


ADVISORY_PATTERNS = (
    (
        "CJ024",
        re.compile(r"\.(?:isNone|isSome)\b(?!\s*\()"),
        "isNone/isSome without a call is receiver-specific; Option state checks are calls, but custom members must be verified against their own API.",
        "option/README.md",
    ),
    (
        "CJ034",
        re.compile(r"\bString\s*\(\s*[A-Za-z_]\w*\s*(?:%|\*|/|\+|-)"),
        "String(expression) may be an invalid numeric-formatting guess; verify the expression type before using value.toString(), interpolation, or a radix API.",
        "basic_data_type/README.md and cangjie-std/convert/formattable.md",
    ),
)

ERROR_PATTERNS = (
    (
        "CJ026",
        re.compile(r"\b(?:U?Int(?:8|16|32|64|Native))\.(?:MaxValue|MinValue)\b"),
        "Invalid integer extrema name; use the documented Max/Min member for the concrete integer type.",
        "basic_data_type/README.md",
    ),
    (
        "CJ038",
        re.compile(
            r"(?<![A-Za-z0-9_.])"
            r"(?:0[xX][0-9A-Fa-f_]+|0[bB][01_]+|0[oO][0-7_]+|\d[\d_]*)"
            r"(?:U?Int(?:8|16|32|64|Native)|Float(?:16|32|64))\b"
        ),
        "Invalid numeric type-name suffix; use i8/i16/i32/i64, u8/u16/u32/u64, f16/f32/f64, or an explicit type constructor.",
        "basic_data_type/README.md",
    ),
    (
        "CJ039",
        re.compile(r"(?<![A-Za-z0-9_~])~(?!>|init\b)"),
        "Cangjie uses ! for integer bitwise complement; ~ is reserved for forms such as ~init and the ~> composition operator.",
        "basic_data_type/README.md and class/README.md",
    ),
    (
        "CJ040",
        re.compile(
            r"(?:==|!=)\s*None\b(?!\s*<)|\bNone\b(?!\s*<)\s*(?:==|!=)"
        ),
        "Bare None in an equality comparison has no explicit type argument; use Option pattern matching/isSome()/isNone(), or a typed None<T> where a value is required.",
        "option/README.md",
    ),
    (
        "CJ043",
        re.compile(
            r"(?:\d[\d_]*\.[\d_]*|\.[\d_]+)(?:[eE][+-]?\d[\d_]*)?\s*%"
            r"|%\s*(?:\d[\d_]*\.[\d_]*|\.[\d_]+)(?:[eE][+-]?\d[\d_]*)?"
        ),
        "The % operator is integer-only; a floating-point operand requires an explicitly verified alternative.",
        "basic_data_type/README.md",
    ),
)

CONTROL_KEYWORD_RE = re.compile(r"\b(if|while|match)\b")
DECLARATION_KEYWORD_RE = re.compile(
    r"\b(?:func|main|class|struct|enum|interface|extend|let|var|const|type|foreign|macro)\b"
)
FUNC_RE = re.compile(
    r"\b(?:func\s+[A-Za-z_]\w*(?:\s*<[^>{};]*>)?|main)\s*"
    r"\([^{};]*\)[^{;]*\{"
)
VAR_RE = re.compile(r"\bvar\s+([A-Za-z_]\w*)")
IDENT_RE = re.compile(r"\b[A-Za-z_]\w*\b")
CASE_BRACE_RE = re.compile(r"\bcase\b[^{}]{0,500}?=>\s*(\{)")
DIRECT_FOR_RE = re.compile(
    r"\bfor\s*\(\s*([A-Za-z_]\w*)\s+in\s+([A-Za-z_]\w*)\s*\)\s*\{"
)
FOR_HEADER_RE = re.compile(
    r"\bfor\s*\((?P<pattern>[^{};]*?)\s+in\s+[^{};]*\)\s*\{"
)
CASE_HEADER_RE = re.compile(r"\bcase\b(?P<pattern>[^{}]{0,500}?)=>")
CONTROL_PATTERN_BODY_RE = re.compile(
    r"\b(?:if|while)\s*\((?P<header>[^{};]*)\)\s*\{"
)
SORT_CALL_RE = re.compile(r"(?<![.\w])sort\s*(\()")
ARRAYLIST_USE_RE = re.compile(r"(?<![.\w])ArrayList\b(?=\s*(?:<|\.|\())")
ARRAY_NAME_RE = re.compile(r"\bArray\b")
APPEND_USE_RE = re.compile(r"(?<!\.)\.\s*append\s*\(")
LENGTH_USE_RE = re.compile(r"(?<!\.)\.\s*length\b")
TO_INT64_USE_RE = re.compile(r"(?<!\.)\.\s*toInt64\s*\(")
REMOVE_AT_USE_RE = re.compile(r"(?<!\.)\.\s*removeAt\s*\(")
ARRAY_SORT_MEMBER_RE = re.compile(
    r"(?<!\.)\.\s*(?P<member>sort|sorted|sortBy)\s*\("
)
PUT_USE_RE = re.compile(r"(?<!\.)\.\s*put\s*\(")
STRING_MEMBER_RE = re.compile(
    r"(?<!\.)\.\s*(?P<member>subString|substring|toUpper|toLower)\s*\("
)
LOCAL_FUNC_RE = re.compile(
    r"\bfunc\s+(?P<name>[A-Za-z_]\w*)(?:\s*<[^>{};]*>)?\s*"
    r"\([^{};]*\)\s*(?P<return>:\s*[^{};]+)?\s*(?P<open>\{)"
)
IMPORT_TOKEN_RE = re.compile(r"\bimport\b")
CORE_NUMERIC_TYPES = {
    "Int8",
    "Int16",
    "Int32",
    "Int64",
    "IntNative",
    "UInt8",
    "UInt16",
    "UInt32",
    "UInt64",
    "UIntNative",
    "Float16",
    "Float32",
    "Float64",
}
INFERABLE_CONSTRUCTORS = CORE_NUMERIC_TYPES | {
    "Array",
    "ArrayList",
    "HashMap",
    "HashSet",
    "String",
    "StringBuilder",
}
NON_BYTE_LITERAL_FRAGMENT = (
    r"(?<![A-Za-z0-9_])(?:"
    r"r(?:'(?:\\.|[^'\\\r\n])*'|\"(?:\\.|[^\"\\\r\n])*\")|"
    r"'(?:\\.|[^'\\\r\n])*'|"
    r"\"(?:\\.|[^\"\\\r\n])*\""
    r")"
)
PLAIN_STRING_LITERAL_FRAGMENT = (
    r"(?<![A-Za-z0-9_#rb])(?:"
    r"'(?:\\.|[^'\\\r\n])*'|"
    r"\"(?:\\.|[^\"\\\r\n])*\""
    r")"
)
SCALAR_LITERAL_RE = re.compile(
    r"(?:true|false|[+-]?(?:0[xX][0-9A-Fa-f_]+|0[bB][01_]+|0[oO][0-7_]+|"
    r"(?:\d[\d_]*(?:\.[\d_]*)?|\.[\d_]+)(?:[eE][+-]?\d[\d_]*)?)"
    r"(?:i(?:8|16|32|64)|u(?:8|16|32|64)|f(?:16|32|64))?)"
)
STD_MATH_SYMBOLS = {
    "abs",
    "acos",
    "asin",
    "atan",
    "atan2",
    "cbrt",
    "ceil",
    "checkedAbs",
    "clamp",
    "cos",
    "exp",
    "exp2",
    "floor",
    "gcd",
    "lcm",
    "log",
    "log10",
    "log2",
    "pow",
    "rotate",
    "round",
    "sin",
    "sqrt",
    "tan",
    "trunc",
}


def mask_non_code(source: str) -> str:
    """Mask comments and literals while preserving offsets and newlines."""

    out = list(source)
    i = 0
    n = len(source)

    def blank(start: int, end: int) -> None:
        for j in range(start, end):
            if out[j] not in "\r\n":
                out[j] = " "

    while i < n:
        if source.startswith("//", i):
            end = source.find("\n", i + 2)
            end = n if end < 0 else end
            blank(i, end)
            i = end
        elif source.startswith("/*", i):
            depth = 1
            j = i + 2
            while j < n and depth:
                if source.startswith("/*", j):
                    depth += 1
                    j += 2
                elif source.startswith("*/", j):
                    depth -= 1
                    j += 2
                else:
                    j += 1
            blank(i, j)
            i = j
        elif source[i] == "#":
            raw = re.match(r"(#+)(['\"])", source[i:])
            if raw is None:
                i += 1
                continue
            hashes, quote = raw.groups()
            closing = quote + hashes
            end = source.find(closing, i + len(raw.group(0)))
            end = n if end < 0 else end + len(closing)
            blank(i, end)
            i = end
        elif source.startswith(('"""', "'''"), i):
            delimiter = source[i : i + 3]
            end = source.find(delimiter, i + 3)
            end = n if end < 0 else end + 3
            blank(i, end)
            i = end
        elif source[i] == "`":
            end = source.find("`", i + 1)
            end = n if end < 0 else end + 1
            blank(i, end)
            i = end
        elif source[i] == '"':
            j = i + 1
            while j < n:
                if source[j] == "\\":
                    j += 2
                elif source[j] == '"':
                    j += 1
                    break
                else:
                    j += 1
            blank(i, min(j, n))
            i = j
        elif source[i] == "'" or (
            source[i] in "rb" and i + 1 < n and source[i + 1] == "'"
        ):
            start = i
            quote = i if source[i] == "'" else i + 1
            j = quote + 1
            while j < n:
                if source[j] == "\\":
                    j += 2
                elif source[j] == "'":
                    j += 1
                    break
                else:
                    j += 1
            blank(start, min(j, n))
            i = j
        else:
            i += 1
    return "".join(out)


def line_starts(source: str) -> list[int]:
    starts = [0]
    starts.extend(i + 1 for i, ch in enumerate(source) if ch == "\n")
    return starts


def location(starts: list[int], offset: int) -> tuple[int, int]:
    row = bisect.bisect_right(starts, offset) - 1
    return row + 1, offset - starts[row] + 1


def add_finding(
    findings: list[Finding],
    path: str,
    starts: list[int],
    offset: int,
    code: str,
    message: str,
    reference: str,
    *,
    severity: Severity,
) -> None:
    line, column = location(starts, max(0, offset))
    findings.append(Finding(path, line, column, code, message, reference, severity))


def bracket_pairs(
    masked: str, path: str, starts: list[int], findings: list[Finding]
) -> dict[int, int]:
    opens = {"(": ")", "[": "]", "{": "}"}
    closes = {value: key for key, value in opens.items()}
    stack: list[tuple[str, int]] = []
    pairs: dict[int, int] = {}
    for i, ch in enumerate(masked):
        if ch in opens:
            stack.append((ch, i))
        elif ch in closes:
            if not stack or stack[-1][0] != closes[ch]:
                add_finding(
                    findings,
                    path,
                    starts,
                    i,
                    "CJ001",
                    f"Unmatched closing delimiter {ch!r}.",
                    "basic_concepts/README.md",
                    severity="error",
                )
                continue
            opening, pos = stack.pop()
            pairs[pos] = i
    for opening, pos in stack:
        add_finding(
            findings,
            path,
            starts,
            pos,
            "CJ002",
            f"Unclosed delimiter {opening!r}; expected {opens[opening]!r}.",
            "basic_concepts/README.md",
            severity="error",
        )
    return pairs


def top_level_argument_ranges(
    masked: str, opening: int, closing: int, pairs: dict[int, int]
) -> list[tuple[int, int]]:
    """Split a parenthesized construct without splitting nested calls or generics."""

    ranges: list[tuple[int, int]] = []
    start = opening + 1
    cursor = start
    angle_depth = 0
    while cursor < closing:
        char = masked[cursor]
        nested_close = pairs.get(cursor)
        if char in "([{" and nested_close is not None and nested_close < closing:
            cursor = nested_close + 1
            continue
        if char == "<" and not masked.startswith("<-", cursor):
            angle_depth += 1
        elif (
            char == ">"
            and angle_depth > 0
            and not (cursor > 0 and masked[cursor - 1] == "-")
        ):
            angle_depth -= 1
        elif char == "," and angle_depth == 0:
            if masked[start:cursor].strip():
                ranges.append((start, cursor))
            start = cursor + 1
        cursor += 1
    if masked[start:closing].strip():
        ranges.append((start, closing))
    return ranges


def scan_imports(
    masked: str, path: str, starts: list[int], findings: list[Finding]
) -> None:
    """Check every import token against its exact brace depth and declaration order."""

    events: list[tuple[int, str]] = [
        (match.start(), "import") for match in IMPORT_TOKEN_RE.finditer(masked)
    ]
    for match in DECLARATION_KEYWORD_RE.finditer(masked):
        previous = match.start() - 1
        while previous >= 0 and masked[previous].isspace():
            previous -= 1
        if previous >= 0 and masked[previous] == ".":
            continue
        events.append((match.start(), "declaration"))

    depth = 0
    seen_declaration = False
    cursor = 0
    for offset, kind in sorted(events):
        for char in masked[cursor:offset]:
            if char == "{":
                depth += 1
            elif char == "}":
                depth = max(0, depth - 1)
        cursor = offset
        if kind == "import":
            if depth > 0:
                add_finding(
                    findings,
                    path,
                    starts,
                    offset,
                    "CJ010",
                    "import is inside a declaration; imports must be at top level.",
                    "package/README.md",
                    severity="error",
                )
            elif seen_declaration:
                add_finding(
                    findings,
                    path,
                    starts,
                    offset,
                    "CJ011",
                    "import appears after another top-level declaration.",
                    "package/README.md",
                    severity="error",
                )
        elif depth == 0:
            seen_declaration = True


def imports_symbol(masked: str, package: str, symbol: str) -> bool:
    package_pattern = re.escape(package)
    symbol_pattern = re.escape(symbol)
    prefix = rf"(?m)^\s*(?:public\s+)?import\s+{package_pattern}\."
    return any(
        re.search(pattern, masked) is not None
        for pattern in (
            prefix + r"\*\s*$",
            prefix + symbol_pattern + r"\b",
            prefix + rf"\{{[^}}\r\n]*\b{symbol_pattern}\b[^}}\r\n]*\}}",
        )
    )


def function_ranges(masked: str, pairs: dict[int, int]) -> list[tuple[int, int, int]]:
    ranges: list[tuple[int, int, int]] = []
    for match in FUNC_RE.finditer(masked):
        opening = masked.rfind("{", match.start(), match.end())
        closing = pairs.get(opening)
        if closing is not None:
            ranges.append((match.start(), opening, closing))
    return ranges


def known_receiver_type(
    masked: str,
    receiver: str,
    use_offset: int,
    pairs: dict[int, int],
) -> str | None:
    """Return a type only when a local parameter/declaration proves it."""

    containing = [
        item for item in function_ranges(masked, pairs) if item[1] < use_offset < item[2]
    ]
    if containing:
        func_start, func_open, _ = min(
            containing, key=lambda item: item[2] - item[1]
        )
        signature = masked[func_start:func_open]
        body_start = func_open + 1
    else:
        func_start = 0
        signature = ""
        body_start = 0

    candidates: list[tuple[int, str | None]] = []
    receiver_pattern = re.escape(receiver)
    parameter_re = re.compile(
        rf"(?<![.\w]){receiver_pattern}!?\s*:\s*([A-Za-z_]\w*)\b"
    )
    for match in parameter_re.finditer(signature):
        candidates.append((func_start + match.start(), match.group(1)))

    for opening, closing in pairs.items():
        if masked[opening] != "{" or not (opening < use_offset < closing):
            continue
        arrow = top_level_arrow(masked, opening, closing)
        if arrow is None or use_offset <= arrow:
            continue
        header = masked[opening + 1 : arrow]
        if re.search(r"\bcase\b", header):
            continue
        lambda_parameter_re = re.compile(
            rf"(?<![.\w]){receiver_pattern}!?\s*(?=:|,|$)"
        )
        lambda_parameter = lambda_parameter_re.search(header)
        if lambda_parameter is not None:
            type_match = re.match(
                r"\s*:\s*([A-Za-z_]\w*)\b", header[lambda_parameter.end() :]
            )
            candidates.append(
                (
                    opening + 1 + lambda_parameter.start(),
                    type_match.group(1) if type_match is not None else None,
                )
            )

    for match in FOR_HEADER_RE.finditer(masked):
        opening = masked.rfind("{", match.start(), match.end())
        closing = pairs.get(opening)
        if closing is None or not (opening < use_offset < closing):
            continue
        if receiver in IDENT_RE.findall(match.group("pattern")):
            candidates.append((match.start(), None))

    latest_case_by_scope: dict[int, re.Match[str]] = {}
    for match in CASE_HEADER_RE.finditer(masked, 0, use_offset):
        containing_scopes = [
            (opening, closing)
            for opening, closing in pairs.items()
            if masked[opening] == "{" and opening < match.start() < closing
        ]
        if not containing_scopes:
            continue
        opening, closing = max(containing_scopes, key=lambda item: item[0])
        if use_offset >= closing:
            continue
        previous = latest_case_by_scope.get(opening)
        if previous is None or previous.start() < match.start():
            latest_case_by_scope[opening] = match
    for match in latest_case_by_scope.values():
        if receiver in IDENT_RE.findall(match.group("pattern")):
            candidates.append((match.start(), None))

    for match in CONTROL_PATTERN_BODY_RE.finditer(masked):
        opening = masked.rfind("{", match.start(), match.end())
        closing = pairs.get(opening)
        if closing is None or not (opening < use_offset < closing):
            continue
        for pattern_match in re.finditer(
            r"\blet\s+(?P<pattern>.*?)\s*<-", match.group("header")
        ):
            if receiver in IDENT_RE.findall(pattern_match.group("pattern")):
                candidates.append((match.start(), None))
                break

    prefix = masked[body_start:use_offset]
    local_type_re = re.compile(
        rf"\b(?:let|var)\s+{receiver_pattern}\s*:\s*([A-Za-z_]\w*)\b"
    )
    for match in local_type_re.finditer(prefix):
        declaration_offset = body_start + match.start()
        if binding_visible_at(masked, pairs, declaration_offset, use_offset):
            candidates.append((declaration_offset, match.group(1)))

    constructor_names = "|".join(
        sorted((re.escape(name) for name in INFERABLE_CONSTRUCTORS), key=len, reverse=True)
    )
    constructor_re = re.compile(
        rf"\b(?:let|var)\s+{receiver_pattern}\s*=\s*({constructor_names})\b"
    )
    for match in constructor_re.finditer(prefix):
        declaration_offset = body_start + match.start()
        if binding_visible_at(masked, pairs, declaration_offset, use_offset):
            candidates.append((declaration_offset, match.group(1)))

    array_literal_re = re.compile(
        rf"\b(?:let|var)\s+{receiver_pattern}\s*=\s*\["
    )
    for match in array_literal_re.finditer(prefix):
        declaration_offset = body_start + match.start()
        if binding_visible_at(masked, pairs, declaration_offset, use_offset):
            candidates.append((declaration_offset, "Array"))

    string_result_re = re.compile(
        rf"\b(?:let|var)\s+{receiver_pattern}\s*=\s*"
        r"[^\r\n;]*?\.toString\s*\("
    )
    for match in string_result_re.finditer(prefix):
        declaration_offset = body_start + match.start()
        if binding_visible_at(masked, pairs, declaration_offset, use_offset):
            candidates.append((declaration_offset, "String"))

    if not candidates:
        return None
    return max(candidates, key=lambda item: item[0])[1]


def binding_visible_at(
    masked: str,
    pairs: dict[int, int],
    declaration_offset: int,
    use_offset: int,
) -> bool:
    """Check the lexical brace scope of a local declaration."""

    containing_scopes = [
        (opening, closing)
        for opening, closing in pairs.items()
        if masked[opening] == "{" and opening < declaration_offset < closing
    ]
    if not containing_scopes:
        return True
    opening, closing = max(containing_scopes, key=lambda item: item[0])
    return opening < use_offset < closing


def simple_receiver_before(masked: str, member_offset: int) -> str | None:
    """Return a bare identifier receiver, excluding property/member chains."""

    match = re.search(r"([A-Za-z_]\w*)\s*$", masked[:member_offset])
    if match is None:
        return None
    previous = match.start(1) - 1
    while previous >= 0 and masked[previous].isspace():
        previous -= 1
    if previous >= 0 and masked[previous] == ".":
        return None
    return match.group(1)


def direct_constructor_type_before(
    masked: str, member_offset: int, pairs: dict[int, int]
) -> str | None:
    """Infer the type of a bare direct constructor expression before a member."""

    cursor = member_offset - 1
    while cursor >= 0 and masked[cursor].isspace():
        cursor -= 1
    if cursor < 0 or masked[cursor] != ")":
        return None

    call_open = next(
        (opening for opening, closing in pairs.items() if closing == cursor), None
    )
    if call_open is None or masked[call_open] != "(":
        return None

    cursor = call_open - 1
    while cursor >= 0 and masked[cursor].isspace():
        cursor -= 1
    if cursor >= 0 and masked[cursor] == ">":
        depth = 1
        cursor -= 1
        while cursor >= 0 and depth:
            if masked[cursor] == ">" and not (
                cursor > 0 and masked[cursor - 1] == "-"
            ):
                depth += 1
            elif masked[cursor] == "<":
                depth -= 1
            cursor -= 1
        if depth:
            return None
        while cursor >= 0 and masked[cursor].isspace():
            cursor -= 1

    type_match = re.search(r"([A-Za-z_]\w*)$", masked[: cursor + 1])
    if type_match is None or type_match.group(1) not in INFERABLE_CONSTRUCTORS:
        return None
    previous = type_match.start(1) - 1
    while previous >= 0 and masked[previous].isspace():
        previous -= 1
    if previous >= 0 and (masked[previous] == "." or masked[previous].isalnum()):
        return None
    return type_match.group(1)


def locally_known_receiver_type(
    masked: str, member_offset: int, pairs: dict[int, int]
) -> str | None:
    receiver = simple_receiver_before(masked, member_offset)
    if receiver is not None:
        return known_receiver_type(masked, receiver, member_offset, pairs)
    return direct_constructor_type_before(masked, member_offset, pairs)


def scan_control_headers(
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    for match in CONTROL_KEYWORD_RE.finditer(masked):
        keyword = match.group(1)
        next_offset = match.end()
        while next_offset < len(masked) and masked[next_offset].isspace():
            next_offset += 1
        next_char = masked[next_offset] if next_offset < len(masked) else ""
        allowed = {"(", "{"} if keyword == "match" else {"("}
        if next_char not in allowed:
            requirement = "'(' or a targetless '{'" if keyword == "match" else "'('"
            add_finding(
                findings,
                path,
                starts,
                match.start(),
                "CJ012",
                f"{keyword} must be followed by {requirement} after optional whitespace.",
                "basic_concepts/README.md",
                severity="error",
            )
            continue
        if next_char == "{":
            continue
        closing = pairs.get(next_offset)
        if closing is None:
            continue
        after = closing + 1
        while after < len(masked) and masked[after].isspace():
            after += 1
        if after >= len(masked) or masked[after] != "{":
            add_finding(
                findings,
                path,
                starts,
                closing,
                "CJ012",
                f"{keyword} condition or selector must remain entirely inside its parentheses; the next token after ')' must be '{{'.",
                "basic_concepts/README.md",
                severity="error",
            )
            continue
        if (
            keyword == "match"
            and len(top_level_argument_ranges(masked, next_offset, closing, pairs)) > 1
        ):
            add_finding(
                findings,
                path,
                starts,
                next_offset,
                "CJ047",
                "match accepts one parenthesized selector; a tuple selector needs its own inner parentheses, for example match ((left, right)).",
                "pattern_match/README.md",
                severity="error",
            )


def scan_array_item_named_argument(
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    """Reject unsupported named labels in top-level Array constructor arguments."""

    for match in ARRAY_NAME_RE.finditer(masked):
        cursor = match.end()
        while cursor < len(masked) and masked[cursor].isspace():
            cursor += 1
        if cursor >= len(masked) or masked[cursor] != "<":
            continue

        angle_depth = 0
        while cursor < len(masked):
            char = masked[cursor]
            if char == "<":
                angle_depth += 1
            elif char == ">" and not (cursor > 0 and masked[cursor - 1] == "-"):
                angle_depth -= 1
                if angle_depth == 0:
                    cursor += 1
                    break
            cursor += 1
        if angle_depth != 0:
            continue
        while cursor < len(masked) and masked[cursor].isspace():
            cursor += 1
        if cursor >= len(masked) or masked[cursor] != "(":
            continue
        call_open = cursor
        call_close = pairs.get(call_open)
        if call_close is None:
            continue

        argument_ranges = top_level_argument_ranges(
            masked, call_open, call_close, pairs
        )
        if len(argument_ranges) >= 2:
            second_start, second_end = argument_ranges[1]
            second = masked[second_start:second_end].strip()
            if SCALAR_LITERAL_RE.fullmatch(second) is not None:
                add_finding(
                    findings,
                    path,
                    starts,
                    second_start,
                    "CJ046",
                    "A positional scalar cannot satisfy Array's (Int64) -> T initializer parameter; use repeat: value or a positional initializer lambda.",
                    "collections/array/README.md",
                    severity="error",
                )

        cursor = call_open + 1
        while cursor < call_close:
            if masked[cursor] in "([{":
                nested_close = pairs.get(cursor)
                if nested_close is not None:
                    cursor = nested_close + 1
                    continue
            argument_match = re.match(
                r"(?P<name>item|initElement)\b", masked[cursor:call_close]
            )
            if argument_match is not None:
                previous = cursor - 1
                while previous > call_open and masked[previous].isspace():
                    previous -= 1
                after = cursor + len(argument_match.group(0))
                while after < call_close and masked[after].isspace():
                    after += 1
                if masked[previous] in "(," and after < call_close and masked[after] == ":":
                    name = argument_match.group("name")
                    message = (
                        "Array has no top-level constructor argument named item:; use repeat: or a positional initializer function."
                        if name == "item"
                        else "Array initElement is a positional function parameter, not a named parameter; use Array<T>(size, {index => ...}) or repeat: for a repeated value."
                    )
                    add_finding(
                        findings,
                        path,
                        starts,
                        cursor,
                        "CJ025",
                        message,
                        "collections/array/README.md",
                        severity="error",
                    )
                    break
            cursor += 1


def scan_receiver_aware_members(
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    arraylist_is_std = imports_symbol(masked, "std.collection", "ArrayList")
    hashmap_is_std = imports_symbol(masked, "std.collection", "HashMap")
    hashset_is_std = imports_symbol(masked, "std.collection", "HashSet")

    for match in APPEND_USE_RE.finditer(masked):
        receiver_type = locally_known_receiver_type(masked, match.start(), pairs)
        if receiver_type == "StringBuilder":
            continue
        is_known_collection = receiver_type == "Array" or (
            receiver_type == "ArrayList" and arraylist_is_std
        )
        add_finding(
            findings,
            path,
            starts,
            match.start(),
            "CJ020",
            (
                f"{receiver_type} has no documented append member; Array is fixed-length and std.collection.ArrayList uses add."
                if is_known_collection
                else "append is receiver-specific and cannot be rejected without a proven receiver API; StringBuilder.append is valid."
            ),
            "collections/README.md and cangjie-std/collection/README.md",
            severity="error" if is_known_collection else "warning",
        )

    for match in LENGTH_USE_RE.finditer(masked):
        receiver_type = locally_known_receiver_type(masked, match.start(), pairs)
        is_core_sized = receiver_type in {"Array", "String"}
        add_finding(
            findings,
            path,
            starts,
            match.start(),
            "CJ023",
            (
                f"Core {receiver_type} uses size rather than length."
                if is_core_sized
                else "length is receiver-specific; verify the receiver contract because some APIs define length while core String and Array use size."
            ),
            "basic_data_type/README.md and string/README.md",
            severity="error" if is_core_sized else "warning",
        )

    for match in TO_INT64_USE_RE.finditer(masked):
        receiver_type = locally_known_receiver_type(masked, match.start(), pairs)
        is_core_numeric = receiver_type in CORE_NUMERIC_TYPES
        add_finding(
            findings,
            path,
            starts,
            match.start(),
            "CJ022",
            (
                f"Core numeric {receiver_type} converts with Int64(value), not .toInt64()."
                if is_core_numeric
                else "toInt64 is receiver-specific; core numerics use Int64(value), but other documented APIs may define this member."
            ),
            "basic_data_type/README.md",
            severity="error" if is_core_numeric else "warning",
        )

    for match in REMOVE_AT_USE_RE.finditer(masked):
        receiver_type = locally_known_receiver_type(masked, match.start(), pairs)
        is_known_collection = receiver_type == "Array" or (
            receiver_type == "ArrayList" and arraylist_is_std
        )
        add_finding(
            findings,
            path,
            starts,
            match.start(),
            "CJ027",
            (
                "Array is fixed-length and std.collection.ArrayList documents remove(at: index), not removeAt."
                if is_known_collection
                else "removeAt is receiver-specific; verify the receiver API before replacing it."
            ),
            "collections/arraylist/README.md and cangjie-std/collection/README.md",
            severity="error" if is_known_collection else "warning",
        )

    for match in ARRAY_SORT_MEMBER_RE.finditer(masked):
        receiver_type = locally_known_receiver_type(masked, match.start(), pairs)
        if receiver_type != "Array":
            continue
        member = match.group("member")
        add_finding(
            findings,
            path,
            starts,
            match.start(),
            "CJ035",
            f"Array has no {member} member; std.sort provides free sort(...) functions that mutate the passed collection and return Unit.",
            "collections/array/README.md and cangjie-std/sort/README.md",
            severity="error",
        )

    for match in PUT_USE_RE.finditer(masked):
        receiver_type = locally_known_receiver_type(masked, match.start(), pairs)
        if receiver_type not in {"HashMap", "HashSet"}:
            continue
        is_std_collection = (receiver_type == "HashMap" and hashmap_is_std) or (
            receiver_type == "HashSet" and hashset_is_std
        )
        replacement = (
            "HashMap uses add(key, value) or indexed assignment"
            if receiver_type == "HashMap"
            else "HashSet uses add(element)"
        )
        add_finding(
            findings,
            path,
            starts,
            match.start(),
            "CJ036",
            (
                f"std.collection.{receiver_type} has no put member; {replacement}."
                if is_std_collection
                else f"{receiver_type}.put is not documented for std.collection; verify whether this is a same-package custom type before using {replacement}."
            ),
            "collections/hashmap/README.md, collections/hashset/README.md, and cangjie-std/collection/README.md",
            severity="error" if is_std_collection else "warning",
        )

    for match in STRING_MEMBER_RE.finditer(masked):
        receiver_type = locally_known_receiver_type(masked, match.start(), pairs)
        member = match.group("member")
        if receiver_type == "String":
            replacement = (
                "use a documented byte-range slice"
                if member in {"subString", "substring"}
                else "use toAsciiUpper/toAsciiLower for ASCII or std.unicode for Unicode casing"
            )
            add_finding(
                findings,
                path,
                starts,
                match.start(),
                "CJ037",
                f"Core String has no {member} member; {replacement}.",
                "string/README.md and cangjie-std/unicode/README.md",
                severity="error",
            )
        elif member in {"subString", "substring"}:
            add_finding(
                findings,
                path,
                starts,
                match.start(),
                "CJ021",
                "substring is receiver-specific; verify the receiver API before replacing it. Core String uses documented byte-range slices.",
                "string/README.md",
                severity="warning",
            )


def top_level_arrow(masked: str, opening: int, closing: int) -> int | None:
    depth = 0
    i = opening + 1
    while i < closing - 1:
        ch = masked[i]
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
        elif depth == 0 and masked.startswith("=>", i):
            return i
        i += 1
    return None


def scan_case_branch_braces(
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    for match in CASE_BRACE_RE.finditer(masked):
        opening = match.start(1)
        closing = pairs.get(opening)
        if closing is None or top_level_arrow(masked, opening, closing) is not None:
            continue
        add_finding(
            findings,
            path,
            starts,
            opening,
            "CJ028",
            "A match case branch cannot use a braced statement block after =>; write branch expressions directly.",
            "pattern_match/README.md",
            severity="error",
        )


def scan_mutable_lambda_capture(
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    functions: list[tuple[int, int]] = []
    for match in FUNC_RE.finditer(masked):
        opening = masked.rfind("{", match.start(), match.end())
        closing = pairs.get(opening)
        if closing is not None:
            functions.append((opening, closing))

    for opening, closing in pairs.items():
        if masked[opening] != "{":
            continue
        arrow = top_level_arrow(masked, opening, closing)
        if arrow is None:
            continue
        header = masked[opening + 1 : arrow].strip()
        if re.search(r"\bcase\b", header) or not re.fullmatch(
            r"[A-Za-z0-9_\s,:()<>?]*", header
        ):
            continue
        after = masked[closing + 1 :].lstrip()
        if after.startswith("("):
            continue
        containing = [item for item in functions if item[0] < opening < item[1]]
        if not containing:
            continue
        func_open, _ = min(containing, key=lambda item: item[1] - item[0])
        mutable_names = set(VAR_RE.findall(masked[func_open + 1 : opening]))
        parameter_names = {
            token.split(":", 1)[0].strip()
            for token in header.split(",")
            if token.strip()
        }
        body = masked[arrow + 2 : closing]
        used = (mutable_names - parameter_names) & set(IDENT_RE.findall(body))
        if used:
            names = ", ".join(sorted(used))
            add_finding(
                findings,
                path,
                starts,
                opening,
                "CJ030",
                f"Lambda captures local var binding(s) and is not called directly: {names}; such a closure cannot escape, so use immutable inputs, an immediate call, or explicit control flow.",
                "function/README.md",
                severity="error",
            )


def binding_shadowed_in_function(
    masked: str,
    pairs: dict[int, int],
    name: str,
    func_open: int,
    func_close: int,
    use_offset: int,
) -> bool:
    body_start = func_open + 1
    prefix = masked[body_start:use_offset]
    local_re = re.compile(rf"\b(?:let|var|const)\s+{re.escape(name)}\b")
    for match in local_re.finditer(prefix):
        declaration_offset = body_start + match.start()
        if binding_visible_at(masked, pairs, declaration_offset, use_offset):
            return True

    for opening, closing in pairs.items():
        if (
            masked[opening] != "{"
            or not (func_open < opening < use_offset < closing < func_close)
        ):
            continue
        arrow = top_level_arrow(masked, opening, closing)
        if arrow is None or use_offset <= arrow:
            continue
        header = masked[opening + 1 : arrow]
        if re.search(r"\bcase\b", header) is None and name in IDENT_RE.findall(header):
            return True

    for match in FOR_HEADER_RE.finditer(masked, func_open + 1, use_offset):
        opening = masked.rfind("{", match.start(), match.end())
        closing = pairs.get(opening)
        if (
            closing is not None
            and opening < use_offset < closing
            and name in IDENT_RE.findall(match.group("pattern"))
        ):
            return True

    latest_case_by_scope: dict[int, re.Match[str]] = {}
    for match in CASE_HEADER_RE.finditer(masked, func_open + 1, use_offset):
        containing_scopes = [
            (opening, closing)
            for opening, closing in pairs.items()
            if masked[opening] == "{"
            and func_open < opening < match.start() < use_offset < closing < func_close
        ]
        if not containing_scopes:
            continue
        opening, _ = max(containing_scopes, key=lambda item: item[0])
        previous = latest_case_by_scope.get(opening)
        if previous is None or previous.start() < match.start():
            latest_case_by_scope[opening] = match
    if any(name in IDENT_RE.findall(match.group("pattern")) for match in latest_case_by_scope.values()):
        return True

    for match in CONTROL_PATTERN_BODY_RE.finditer(masked, func_open + 1, use_offset):
        opening = masked.rfind("{", match.start(), match.end())
        closing = pairs.get(opening)
        if closing is None or not (opening < use_offset < closing):
            continue
        for pattern_match in re.finditer(
            r"\blet\s+(?P<pattern>.*?)\s*<-", match.group("header")
        ):
            if name in IDENT_RE.findall(pattern_match.group("pattern")):
                return True
    return False


def scan_parameter_reassignment(
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    functions = function_ranges(masked, pairs)
    for func_start, func_open, func_close in functions:
        params_open = masked.find("(", func_start, func_open)
        params_close = pairs.get(params_open)
        if params_open < 0 or params_close is None or params_close > func_open:
            continue
        parameter_names: list[str] = []
        for start, end in top_level_argument_ranges(
            masked, params_open, params_close, pairs
        ):
            parameter = re.match(
                r"\s*([A-Za-z_]\w*)!?\s*:", masked[start:end]
            )
            if parameter is not None:
                parameter_names.append(parameter.group(1))

        for name in parameter_names:
            escaped = re.escape(name)
            write_patterns = (
                re.compile(
                    rf"(?<![.\w])(?P<name>{escaped})\b\s*"
                    r"(?:\+\+|--|<<=|>>=|\+=|-=|\*=|/=|%=|&=|\|=|\^=|=(?!=|>))"
                ),
                re.compile(rf"(?<![.\w])(?:\+\+|--)\s*(?P<name>{escaped})\b"),
            )
            offsets: set[int] = set()
            for pattern in write_patterns:
                for match in pattern.finditer(masked, func_open + 1, func_close):
                    offset = match.start("name")
                    containing = [
                        item for item in functions if item[1] < offset < item[2]
                    ]
                    if not containing:
                        continue
                    innermost = min(
                        containing, key=lambda item: item[2] - item[1]
                    )
                    if innermost[1] != func_open:
                        continue
                    if binding_shadowed_in_function(
                        masked,
                        pairs,
                        name,
                        func_open,
                        func_close,
                        offset,
                    ):
                        continue
                    offsets.add(offset)
            for offset in sorted(offsets):
                add_finding(
                    findings,
                    path,
                    starts,
                    offset,
                    "CJ048",
                    f"Function parameter {name!r} is immutable; copy it into a local var before updating search bounds or accumulated state.",
                    "function/README.md and basic_concepts/README.md",
                    severity="error",
                )


def scan_non_unit_tail_loops(
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    for func_start, func_open, func_close in function_ranges(masked, pairs):
        params_open = masked.find("(", func_start, func_open)
        params_close = pairs.get(params_open)
        if params_open < 0 or params_close is None:
            continue
        tail_signature = masked[params_close + 1 : func_open]
        return_type = re.search(r":\s*(\??[A-Za-z_]\w*)", tail_signature)
        if return_type is None or return_type.group(1).lstrip("?") in {"Unit", "Nothing"}:
            continue

        last = func_close - 1
        while last > func_open and (
            masked[last].isspace() or masked[last] == ";"
        ):
            last -= 1
        if masked[last] != "}":
            continue

        loop_re = re.compile(r"\b(?P<keyword>while|for)\b")
        for match in loop_re.finditer(masked, func_open + 1, last + 1):
            condition_open = match.end()
            while (
                condition_open < last and masked[condition_open].isspace()
            ):
                condition_open += 1
            if condition_open >= last or masked[condition_open] != "(":
                continue
            condition_close = pairs.get(condition_open)
            if condition_close is None:
                continue
            body_open = condition_close + 1
            while body_open < last and masked[body_open].isspace():
                body_open += 1
            if (
                body_open < last
                and masked[body_open] == "{"
                and pairs.get(body_open) == last
            ):
                add_finding(
                    findings,
                    path,
                    starts,
                    match.start(),
                    "CJ049",
                    f"A trailing {match.group('keyword')} expression has type Unit in a non-Unit function even when its body contains return; add an explicit reachable return after the loop or restructure control flow.",
                    "basic_concepts/README.md",
                    severity="error",
                )
                break


def scan_empty_case_branches(
    masked: str, path: str, starts: list[int], findings: list[Finding]
) -> None:
    for match in CASE_HEADER_RE.finditer(masked):
        cursor = match.end()
        while cursor < len(masked) and masked[cursor].isspace():
            cursor += 1
        if cursor >= len(masked):
            continue
        if masked.startswith("case", cursor) or masked[cursor] == "}":
            add_finding(
                findings,
                path,
                starts,
                match.start(),
                "CJ044",
                "A match case must contain at least one expression after =>; use () for an explicit Unit branch.",
                "pattern_match/README.md",
                severity="error",
            )


def scan_recursive_local_functions(
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    functions = function_ranges(masked, pairs)
    for match in LOCAL_FUNC_RE.finditer(masked):
        opening = match.start("open")
        closing = pairs.get(opening)
        if closing is None or match.group("return") is not None:
            continue
        if not any(
            outer_open < match.start() < outer_close
            for _, outer_open, outer_close in functions
            if outer_open != opening
        ):
            continue
        name = match.group("name")
        body = masked[opening + 1 : closing]
        if re.search(rf"(?<![.\w]){re.escape(name)}\s*\(", body) is None:
            continue
        add_finding(
            findings,
            path,
            starts,
            match.start(),
            "CJ045",
            f"Recursive local function {name!r} has no explicit return type; add one when recursive inference is not uniquely determined.",
            "function/README.md",
            severity="warning",
        )


def scan_untyped_sort_trailing_lambda(
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    """Flag the documented risky std.sort trailing-lambda shape."""

    if not imports_symbol(masked, "std.sort", "sort"):
        return
    for match in SORT_CALL_RE.finditer(masked):
        call_open = match.start(1)
        call_close = pairs.get(call_open)
        if call_close is None:
            continue
        tail = re.match(r"\s*(\{)", masked[call_close + 1 :])
        if tail is None:
            continue
        lambda_open = call_close + 1 + tail.start(1)
        lambda_close = pairs.get(lambda_open)
        if lambda_close is None:
            continue
        arrow = top_level_arrow(masked, lambda_open, lambda_close)
        if arrow is None:
            continue
        header = masked[lambda_open + 1 : arrow].strip()
        if re.fullmatch(r"[A-Za-z_]\w*(?:\s*,\s*[A-Za-z_]\w*)?", header) is None:
            continue
        add_finding(
            findings,
            path,
            starts,
            lambda_open,
            "CJ032",
            "Untyped trailing lambda after std.sort may leave the overload or comparator contract unresolved; verify the selected overload, and prefer an explicit by:/lessThan:/key: argument with typed lambda parameters.",
            "collections/array/README.md and cangjie-std/sort/README.md",
            severity="warning",
        )


def scan_arraylist_import(
    masked: str, path: str, starts: list[int], findings: list[Finding]
) -> None:
    """Find conservative bare ArrayList uses without a visible import."""

    use = ARRAYLIST_USE_RE.search(masked)
    if use is None:
        return
    if re.search(r"(?m)^\s*package\s+std\.collection\b", masked):
        return
    if re.search(
        r"\b(?:class|struct|interface|enum|type)\s+ArrayList\b", masked
    ):
        return
    if imports_symbol(masked, "std.collection", "ArrayList"):
        return
    add_finding(
        findings,
        path,
        starts,
        use.start(),
        "CJ033",
        "Bare ArrayList use has no visible std.collection ArrayList import.",
        "collections/arraylist/README.md and cangjie-std/collection/README.md",
        severity="warning",
    )


def known_array_tuple_binding(
    masked: str,
    receiver: str,
    use_offset: int,
    pairs: dict[int, int],
) -> bool:
    containing = [
        item for item in function_ranges(masked, pairs) if item[1] < use_offset < item[2]
    ]
    if containing:
        func_start, func_open, _ = min(
            containing, key=lambda item: item[2] - item[1]
        )
        signature = masked[func_start:func_open]
        body_start = func_open + 1
    else:
        func_start = 0
        signature = ""
        body_start = 0

    receiver_pattern = re.escape(receiver)
    candidates: list[tuple[int, bool]] = []
    parameter_re = re.compile(
        rf"(?<![.\w]){receiver_pattern}!?\s*:\s*"
        r"(?P<type>Array\s*<\s*\(|[A-Za-z_]\w*)"
    )
    for match in parameter_re.finditer(signature):
        candidates.append(
            (
                func_start + match.start(),
                re.match(r"Array\s*<\s*\(", match.group("type")) is not None,
            )
        )

    prefix = masked[body_start:use_offset]
    declaration_re = re.compile(
        rf"\b(?:let|var)\s+{receiver_pattern}\b(?P<tail>[^\r\n;]*)"
    )
    for match in declaration_re.finditer(prefix):
        declaration_offset = body_start + match.start()
        if binding_visible_at(masked, pairs, declaration_offset, use_offset):
            candidates.append(
                (
                    declaration_offset,
                    re.search(r":\s*Array\s*<\s*\(", match.group("tail"))
                    is not None,
                )
            )
    if not candidates:
        return False
    return max(candidates, key=lambda item: item[0])[1]


def scan_array_tuple_equality(
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    if re.search(r"\boperator\s+func\s+(?:==|!=)", masked) is not None:
        return
    pattern = re.compile(
        r"(?<![.\w])(?P<left>[A-Za-z_]\w*)\s*"
        r"(?P<operator>==|!=)\s*(?P<right>[A-Za-z_]\w*)\b"
    )
    for match in pattern.finditer(masked):
        if not known_array_tuple_binding(
            masked, match.group("left"), match.start("left"), pairs
        ):
            continue
        if not known_array_tuple_binding(
            masked, match.group("right"), match.start("right"), pairs
        ):
            continue
        add_finding(
            findings,
            path,
            starts,
            match.start("operator"),
            "CJ050",
            "Array<(...)> has no default direct equality from tuple fields; compare sizes, then destructure elements and compare fields.",
            "collections/array/README.md",
            severity="error",
        )


def scan_std_math_imports(
    masked: str,
    path: str,
    starts: list[int],
    findings: list[Finding],
) -> None:
    missing: list[tuple[int, str]] = []
    for symbol in sorted(STD_MATH_SYMBOLS):
        if imports_symbol(masked, "std.math", symbol) or imports_symbol(
            masked, "std.math.numeric", symbol
        ):
            continue
        escaped = re.escape(symbol)
        if re.search(
            rf"\bfunc\s+{escaped}\s*\(|\b(?:let|var|const)\s+{escaped}\b|"
            rf"(?<![.\w]){escaped}!?\s*:",
            masked,
        ) is not None:
            continue
        call = re.search(rf"(?<![.\w]){escaped}\s*\(", masked)
        if call is not None:
            missing.append((call.start(), symbol))
    if not missing:
        return
    names = ", ".join(symbol for _, symbol in sorted(missing))
    add_finding(
        findings,
        path,
        starts,
        min(offset for offset, _ in missing),
        "CJ051",
        f"Bare math call(s) {names} have no visible std.math import; verify same-package declarations or add the documented top-level import.",
        "cangjie-std/math/README.md",
        severity="warning",
    )


def scan_string_byte_to_rune(
    source: str,
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    """Find direct String iteration values used with Rune/String character semantics."""

    functions: list[tuple[int, int, int]] = []
    for func_match in FUNC_RE.finditer(masked):
        func_open = masked.rfind("{", func_match.start(), func_match.end())
        func_close = pairs.get(func_open)
        if func_close is not None:
            functions.append((func_match.start(), func_open, func_close))

    for match in DIRECT_FOR_RE.finditer(masked):
        loop_name, iterable_name = match.groups()
        containing = [item for item in functions if item[1] < match.start() < item[2]]
        if not containing:
            continue
        if known_receiver_type(masked, iterable_name, match.start(), pairs) != "String":
            continue

        opening = masked.rfind("{", match.start(), match.end())
        closing = pairs.get(opening)
        if closing is None:
            continue
        body = masked[opening + 1 : closing]

        body_start = opening + 1
        source_body = source[body_start:closing]
        sink_offsets: list[int] = []
        statement_end = r"(?=\s*(?:;|\r?\n|\}|$))"
        assignment_re = re.compile(
            rf"(?<![.\w])(?P<name>[A-Za-z_]\w*)\s*=(?!=)\s*"
            rf"{re.escape(loop_name)}\b{statement_end}"
        )
        for assignment in assignment_re.finditer(body):
            assignment_offset = body_start + assignment.start()
            if (
                known_receiver_type(
                    masked, assignment.group("name"), assignment_offset, pairs
                )
                == "Rune"
            ):
                sink_offsets.append(assignment_offset)
        declaration = re.search(
            rf"\b(?:let|var)\s+[A-Za-z_]\w*\s*:\s*Rune\s*=\s*"
            rf"{re.escape(loop_name)}\b{statement_end}",
            body,
        )
        if declaration is not None:
            sink_offsets.append(body_start + declaration.start())

        string_constructor = re.search(
            rf"(?<![.\w])String\s*\(\s*(?P<loop>{re.escape(loop_name)})\s*\)",
            body,
        )
        if string_constructor is not None:
            sink_offsets.append(body_start + string_constructor.start("loop"))

        comparison_patterns = (
            re.compile(
                rf"(?P<loop>(?<![.\w]){re.escape(loop_name)}\b)\s*"
                rf"(?P<operator>==|!=|<=|>=|<|>)\s*"
                rf"(?P<literal>{NON_BYTE_LITERAL_FRAGMENT})"
            ),
            re.compile(
                rf"(?P<literal>{NON_BYTE_LITERAL_FRAGMENT})\s*"
                rf"(?P<operator>==|!=|<=|>=|<|>)\s*"
                rf"(?P<loop>(?<![.\w]){re.escape(loop_name)}\b)"
            ),
        )
        for pattern in comparison_patterns:
            for comparison in pattern.finditer(source_body):
                loop_offset = body_start + comparison.start("loop")
                operator_offset = body_start + comparison.start("operator")
                operator = comparison.group("operator")
                if masked[loop_offset : loop_offset + len(loop_name)] != loop_name:
                    continue
                if masked[operator_offset : operator_offset + len(operator)] != operator:
                    continue
                sink_offsets.append(loop_offset)
                break

        if not sink_offsets:
            continue
        add_finding(
            findings,
            path,
            starts,
            min(sink_offsets),
            "CJ031",
            f"Direct iteration over String {iterable_name!r} yields UInt8, but {loop_name!r} is used with Rune/String character semantics; keep byte semantics with UInt8 and b'...', or iterate {iterable_name}.runes() and use Rune values.",
            "string/README.md and basic_data_type/README.md",
            severity="error",
        )


def scan_string_index_character_semantics(
    source: str,
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    indexed = (
        r"(?P<receiver>[A-Za-z_]\w*)\s*"
        r"\[(?P<index>[^\]\r\n]+)\]"
    )
    comparison_patterns = (
        re.compile(
            indexed
            + r"\s*(?P<operator>==|!=|<=|>=|<|>)\s*"
            + rf"(?P<literal>{NON_BYTE_LITERAL_FRAGMENT})"
        ),
        re.compile(
            rf"(?P<literal>{NON_BYTE_LITERAL_FRAGMENT})\s*"
            r"(?P<operator>==|!=|<=|>=|<|>)\s*"
            + indexed
        ),
    )
    sink_offsets: set[int] = set()
    for pattern in comparison_patterns:
        for match in pattern.finditer(source):
            receiver = match.group("receiver")
            receiver_offset = match.start("receiver")
            operator = match.group("operator")
            operator_offset = match.start("operator")
            if ".." in match.group("index"):
                continue
            if masked[receiver_offset : receiver_offset + len(receiver)] != receiver:
                continue
            if masked[operator_offset : operator_offset + len(operator)] != operator:
                continue
            if known_receiver_type(masked, receiver, receiver_offset, pairs) == "String":
                sink_offsets.add(receiver_offset)

    constructor_pattern = re.compile(
        r"(?<![.\w])String\s*\(\s*" + indexed + r"\s*\)"
    )
    for match in constructor_pattern.finditer(source):
        receiver = match.group("receiver")
        receiver_offset = match.start("receiver")
        if ".." in match.group("index"):
            continue
        if masked[receiver_offset : receiver_offset + len(receiver)] != receiver:
            continue
        if known_receiver_type(masked, receiver, receiver_offset, pairs) == "String":
            sink_offsets.add(receiver_offset)

    for offset in sorted(sink_offsets):
        add_finding(
            findings,
            path,
            starts,
            offset,
            "CJ041",
            "Direct String indexing yields UInt8; compare with b'...', use a byte-range slice for String, or use runes()/toRuneArray() with Rune values for character semantics.",
            "string/README.md and basic_data_type/README.md",
            severity="error",
        )


def known_rune_array(
    masked: str,
    receiver: str,
    use_offset: int,
    pairs: dict[int, int],
) -> bool:
    containing = [
        item for item in function_ranges(masked, pairs) if item[1] < use_offset < item[2]
    ]
    if containing:
        func_start, func_open, _ = min(
            containing, key=lambda item: item[2] - item[1]
        )
        signature = masked[func_start:func_open]
        body_start = func_open + 1
    else:
        func_start = 0
        signature = ""
        body_start = 0

    receiver_pattern = re.escape(receiver)
    candidates: list[tuple[int, bool]] = []
    parameter_re = re.compile(
        rf"(?<![.\w]){receiver_pattern}!?\s*:\s*"
        r"(?P<type>Array\s*<\s*Rune\s*>|[A-Za-z_]\w*)"
    )
    for match in parameter_re.finditer(signature):
        candidates.append(
            (
                func_start + match.start(),
                re.fullmatch(r"Array\s*<\s*Rune\s*>", match.group("type"))
                is not None,
            )
        )

    prefix = masked[body_start:use_offset]
    declaration_re = re.compile(
        rf"\b(?:let|var)\s+{receiver_pattern}\b(?P<tail>[^\r\n;]*)"
    )
    for match in declaration_re.finditer(prefix):
        declaration_offset = body_start + match.start()
        if not binding_visible_at(masked, pairs, declaration_offset, use_offset):
            continue
        tail = match.group("tail")
        is_rune_array = (
            re.search(r":\s*Array\s*<\s*Rune\s*>", tail) is not None
            or re.search(r"=\s*[A-Za-z_]\w*\.toRuneArray\s*\(\s*\)", tail)
            is not None
        )
        candidates.append((declaration_offset, is_rune_array))

    if not candidates:
        return False
    return max(candidates, key=lambda item: item[0])[1]


def scan_rune_array_literal_comparisons(
    source: str,
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    indexed = (
        r"(?P<receiver>[A-Za-z_]\w*)\s*"
        r"\[(?P<index>[^\]\r\n]+)\]"
    )
    patterns = (
        re.compile(
            indexed
            + r"\s*(?P<operator>==|!=|<=|>=|<|>)\s*"
            + rf"(?P<literal>{PLAIN_STRING_LITERAL_FRAGMENT})"
        ),
        re.compile(
            rf"(?P<literal>{PLAIN_STRING_LITERAL_FRAGMENT})\s*"
            r"(?P<operator>==|!=|<=|>=|<|>)\s*"
            + indexed
        ),
    )
    offsets: set[int] = set()
    for pattern in patterns:
        for match in pattern.finditer(source):
            receiver = match.group("receiver")
            receiver_offset = match.start("receiver")
            operator = match.group("operator")
            operator_offset = match.start("operator")
            if masked[receiver_offset : receiver_offset + len(receiver)] != receiver:
                continue
            if masked[operator_offset : operator_offset + len(operator)] != operator:
                continue
            if known_rune_array(masked, receiver, receiver_offset, pairs):
                offsets.add(receiver_offset)
    for offset in sorted(offsets):
        add_finding(
            findings,
            path,
            starts,
            offset,
            "CJ042",
            "Array<Rune> element comparisons require Rune literals such as r'0'; plain string literals do not convert in comparison expressions.",
            "basic_data_type/README.md",
            severity="error",
        )


def scan_source(source: str, path: str) -> list[Finding]:
    masked = mask_non_code(source)
    starts = line_starts(source)
    findings: list[Finding] = []
    pairs = bracket_pairs(masked, path, starts, findings)
    scan_imports(masked, path, starts, findings)
    scan_control_headers(masked, path, starts, pairs, findings)

    for code, pattern, message, reference in ERROR_PATTERNS:
        for match in pattern.finditer(masked):
            add_finding(
                findings,
                path,
                starts,
                match.start(),
                code,
                message,
                reference,
                severity="error",
            )

    for code, pattern, message, reference in ADVISORY_PATTERNS:
        for match in pattern.finditer(masked):
            add_finding(
                findings,
                path,
                starts,
                match.start(),
                code,
                message,
                reference,
                severity="warning",
            )

    scan_array_item_named_argument(masked, path, starts, pairs, findings)
    scan_receiver_aware_members(masked, path, starts, pairs, findings)
    scan_case_branch_braces(masked, path, starts, pairs, findings)
    scan_mutable_lambda_capture(masked, path, starts, pairs, findings)
    scan_parameter_reassignment(masked, path, starts, pairs, findings)
    scan_non_unit_tail_loops(masked, path, starts, pairs, findings)
    scan_empty_case_branches(masked, path, starts, findings)
    scan_recursive_local_functions(masked, path, starts, pairs, findings)
    scan_untyped_sort_trailing_lambda(masked, path, starts, pairs, findings)
    scan_arraylist_import(masked, path, starts, findings)
    scan_array_tuple_equality(masked, path, starts, pairs, findings)
    scan_std_math_imports(masked, path, starts, findings)
    scan_string_byte_to_rune(source, masked, path, starts, pairs, findings)
    scan_string_index_character_semantics(
        source, masked, path, starts, pairs, findings
    )
    scan_rune_array_literal_comparisons(
        source, masked, path, starts, pairs, findings
    )
    return sorted(set(findings), key=lambda item: (item.path, item.line, item.column, item.code))


def read_stdin_source() -> str:
    """Read piped source without letting the Windows code page corrupt a UTF-8 BOM."""

    buffer = getattr(sys.stdin, "buffer", None)
    if buffer is None:
        return sys.stdin.read()
    raw = buffer.read()
    try:
        return raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        return raw.decode(sys.stdin.encoding or "utf-8")


def source_inputs(paths: Iterable[str]) -> Iterable[tuple[str, str]]:
    for raw in paths:
        if raw == "-":
            source = read_stdin_source()
            if not source.strip():
                raise ValueError("stdin did not contain non-whitespace Cangjie source")
            yield "<stdin>", source
            continue
        path = Path(raw)
        if path.is_dir():
            for child in sorted(path.rglob("*.cj")):
                source = child.read_text(encoding="utf-8")
                if not source.strip():
                    raise ValueError(f"{child} did not contain non-whitespace Cangjie source")
                yield str(child), source
        elif path.is_file():
            source = path.read_text(encoding="utf-8")
            if not source.strip():
                raise ValueError(f"{path} did not contain non-whitespace Cangjie source")
            yield str(path), source
        else:
            raise FileNotFoundError(raw)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check generated Cangjie sources for deterministic closure diagnostics."
    )
    parser.add_argument("paths", nargs="+", help=".cj files, directories, or '-' for stdin")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    try:
        inputs = list(source_inputs(args.paths))
        if not inputs:
            raise ValueError("no Cangjie sources found")
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"closure-check: input error: {exc}", file=sys.stderr)
        return 2

    findings = [finding for path, source in inputs for finding in scan_source(source, path)]
    errors = [finding for finding in findings if finding.severity == "error"]
    warnings = [finding for finding in findings if finding.severity == "warning"]
    if args.format == "json":
        print(json.dumps([asdict(item) for item in findings], ensure_ascii=False, indent=2))
    elif findings:
        for item in findings:
            print(
                f"{item.path}:{item.line}:{item.column}: {item.code} [{item.severity}] {item.message} "
                f"[{item.reference}]"
            )
        if errors:
            print(
                f"closure-check: failed ({len(errors)} error(s), {len(warnings)} warning(s))"
            )
        else:
            print(
                "closure-check: passed with warnings; review required "
                f"({len(inputs)} source(s); {len(warnings)} warning(s))"
            )
    else:
        print(f"closure-check: ok ({len(inputs)} source(s))")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
