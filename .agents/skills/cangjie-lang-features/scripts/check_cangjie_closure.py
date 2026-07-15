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
        "CJ021",
        re.compile(r"\.(?:subString|substring)\s*\("),
        "substring is receiver-specific; verify the receiver API before replacing it. Core String uses documented range or search APIs.",
        "string/README.md",
    ),
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
)

CONTROL_KEYWORD_RE = re.compile(r"\b(if|while|match)\b")
DECLARATION_RE = re.compile(
    r"^(?:@[A-Za-z_]\w*|(?:(?:public|private|protected|internal|open|abstract|sealed|static|unsafe)\s+)*"
    r"(?:func|main|class|struct|enum|interface|extend|let|var|const|type|foreign|macro)\b)"
)
FUNC_RE = re.compile(r"\b(?:func\s+[A-Za-z_]\w*|main)\s*\([^{};]*\)[^{;]*\{")
VAR_RE = re.compile(r"\bvar\s+([A-Za-z_]\w*)")
IDENT_RE = re.compile(r"\b[A-Za-z_]\w*\b")
CASE_BRACE_RE = re.compile(r"\bcase\b[^{}]{0,500}?=>\s*(\{)")
EXPLICIT_TYPE_BINDING_RE = re.compile(
    r"\b([A-Za-z_]\w*)!?\s*:\s*([A-Za-z_]\w*)\b"
)
EXPLICIT_LOCAL_TYPE_RE = re.compile(
    r"\b(?:let|var)\s+([A-Za-z_]\w*)\s*:\s*([A-Za-z_]\w*)\b"
)
DIRECT_FOR_RE = re.compile(
    r"\bfor\s*\(\s*([A-Za-z_]\w*)\s+in\s+([A-Za-z_]\w*)\s*\)\s*\{"
)
SORT_CALL_RE = re.compile(r"(?<![.\w])sort\s*(\()")
ARRAYLIST_USE_RE = re.compile(r"(?<![.\w])ArrayList\b(?=\s*(?:<|\.|\())")
ARRAY_NAME_RE = re.compile(r"\bArray\b")
APPEND_USE_RE = re.compile(r"(?<![.\w])([A-Za-z_]\w*)\s*\.\s*append\s*\(")
LENGTH_USE_RE = re.compile(r"(?<![.\w])([A-Za-z_]\w*)\s*\.\s*length\b")
TO_INT64_USE_RE = re.compile(r"(?<![.\w])([A-Za-z_]\w*)\s*\.\s*toInt64\s*\(")
REMOVE_AT_USE_RE = re.compile(r"(?<![.\w])([A-Za-z_]\w*)\s*\.\s*removeAt\s*\(")
IMPORT_LINE_RE = re.compile(r"(?:public\s+)?import\b")
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
INFERABLE_CONSTRUCTORS = CORE_NUMERIC_TYPES | {"Array", "ArrayList", "StringBuilder"}
NON_BYTE_LITERAL_FRAGMENT = (
    r"(?<![A-Za-z0-9_])(?:"
    r"r(?:'(?:\\.|[^'\\\r\n])*'|\"(?:\\.|[^\"\\\r\n])*\")|"
    r"'(?:\\.|[^'\\\r\n])*'|"
    r"\"(?:\\.|[^\"\\\r\n])*\""
    r")"
)


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
    severity: Severity = "error",
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
        )
    return pairs


def scan_imports(
    masked: str, path: str, starts: list[int], findings: list[Finding]
) -> None:
    depth = 0
    seen_declaration = False
    offset = 0
    for line in masked.splitlines(keepends=True):
        stripped = line.strip()
        import_match = IMPORT_LINE_RE.match(stripped)
        if import_match is not None:
            import_column = line.find("import")
            if depth > 0:
                add_finding(
                    findings,
                    path,
                    starts,
                    offset + import_column,
                    "CJ010",
                    "import is inside a declaration; imports must be at top level.",
                    "package/README.md",
                )
            elif seen_declaration:
                add_finding(
                    findings,
                    path,
                    starts,
                    offset + import_column,
                    "CJ011",
                    "import appears after another top-level declaration.",
                    "package/README.md",
                )
        elif depth == 0 and stripped and DECLARATION_RE.match(stripped):
            seen_declaration = True
        depth += line.count("{") - line.count("}")
        offset += len(line)


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

    candidates: list[tuple[int, str]] = []
    receiver_pattern = re.escape(receiver)
    parameter_re = re.compile(
        rf"(?<![.\w]){receiver_pattern}!?\s*:\s*([A-Za-z_]\w*)\b"
    )
    for match in parameter_re.finditer(signature):
        candidates.append((func_start + match.start(), match.group(1)))

    prefix = masked[body_start:use_offset]
    local_type_re = re.compile(
        rf"\b(?:let|var)\s+{receiver_pattern}\s*:\s*([A-Za-z_]\w*)\b"
    )
    for match in local_type_re.finditer(prefix):
        candidates.append((body_start + match.start(), match.group(1)))

    constructor_names = "|".join(
        sorted((re.escape(name) for name in INFERABLE_CONSTRUCTORS), key=len, reverse=True)
    )
    constructor_re = re.compile(
        rf"\b(?:let|var)\s+{receiver_pattern}\s*=\s*({constructor_names})\b"
    )
    for match in constructor_re.finditer(prefix):
        candidates.append((body_start + match.start(), match.group(1)))

    if not candidates:
        return None
    return max(candidates, key=lambda item: item[0])[1]


def scan_control_headers(
    masked: str, path: str, starts: list[int], findings: list[Finding]
) -> None:
    for match in CONTROL_KEYWORD_RE.finditer(masked):
        keyword = match.group(1)
        next_offset = match.end()
        while next_offset < len(masked) and masked[next_offset].isspace():
            next_offset += 1
        next_char = masked[next_offset] if next_offset < len(masked) else ""
        allowed = {"(", "{"} if keyword == "match" else {"("}
        if next_char in allowed:
            continue
        requirement = "'(' or a targetless '{'" if keyword == "match" else "'('"
        add_finding(
            findings,
            path,
            starts,
            match.start(),
            "CJ012",
            f"{keyword} must be followed by {requirement} after optional whitespace.",
            "basic_concepts/README.md",
        )


def scan_array_item_named_argument(
    masked: str,
    path: str,
    starts: list[int],
    pairs: dict[int, int],
    findings: list[Finding],
) -> None:
    """Reject only a top-level Array constructor argument named item:."""

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

        cursor = call_open + 1
        while cursor < call_close:
            if masked[cursor] in "([{":
                nested_close = pairs.get(cursor)
                if nested_close is not None:
                    cursor = nested_close + 1
                    continue
            item_match = re.match(r"item\b", masked[cursor:call_close])
            if item_match is not None:
                previous = cursor - 1
                while previous > call_open and masked[previous].isspace():
                    previous -= 1
                after = cursor + len(item_match.group(0))
                while after < call_close and masked[after].isspace():
                    after += 1
                if masked[previous] in "(," and after < call_close and masked[after] == ":":
                    add_finding(
                        findings,
                        path,
                        starts,
                        cursor,
                        "CJ025",
                        "Array has no top-level constructor argument named item:; use repeat: or an initializer function.",
                        "collections/array/README.md",
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

    for match in APPEND_USE_RE.finditer(masked):
        receiver = match.group(1)
        receiver_type = known_receiver_type(masked, receiver, match.start(), pairs)
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
        receiver = match.group(1)
        receiver_type = known_receiver_type(masked, receiver, match.start(), pairs)
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
        receiver = match.group(1)
        receiver_type = known_receiver_type(masked, receiver, match.start(), pairs)
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
        receiver = match.group(1)
        receiver_type = known_receiver_type(masked, receiver, match.start(), pairs)
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
        if "case" in header or not re.fullmatch(r"[A-Za-z0-9_\s,:()<>?]*", header):
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
                f"Escaping lambda captures local var binding(s): {names}; use immutable inputs or explicit control flow.",
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
    """Reject the documented bad std.sort trailing-lambda shape."""

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
            "Untyped trailing lambda after std.sort leaves the overload and comparator contract unresolved; use an explicit by:/lessThan:/key: argument and type every lambda parameter.",
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
        func_start, _, _ = min(containing, key=lambda item: item[2] - item[1])
        prefix = masked[func_start : match.start()]
        binding_types = {
            name: type_name
            for name, type_name in EXPLICIT_TYPE_BINDING_RE.findall(prefix)
        }
        if binding_types.get(iterable_name) != "String":
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
        local_types = {
            name: type_name
            for name, type_name in EXPLICIT_LOCAL_TYPE_RE.findall(prefix)
        }
        rune_names = {name for name, type_name in local_types.items() if type_name == "Rune"}
        for rune_name in rune_names:
            assignment = re.search(
                rf"(?<![.\w]){re.escape(rune_name)}\s*=(?!=)\s*"
                rf"{re.escape(loop_name)}\b{statement_end}",
                body,
            )
            if assignment is not None:
                sink_offsets.append(body_start + assignment.start())
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
        )


def scan_source(source: str, path: str) -> list[Finding]:
    masked = mask_non_code(source)
    starts = line_starts(source)
    findings: list[Finding] = []
    pairs = bracket_pairs(masked, path, starts, findings)
    scan_imports(masked, path, starts, findings)
    scan_control_headers(masked, path, starts, findings)

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
    scan_untyped_sort_trailing_lambda(masked, path, starts, pairs, findings)
    scan_arraylist_import(masked, path, starts, findings)
    scan_string_byte_to_rune(source, masked, path, starts, pairs, findings)
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
        description="Check generated Cangjie sources for deterministic closure violations."
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
                f"closure-check: ok ({len(inputs)} source(s); {len(warnings)} warning(s))"
            )
    else:
        print(f"closure-check: ok ({len(inputs)} source(s))")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
