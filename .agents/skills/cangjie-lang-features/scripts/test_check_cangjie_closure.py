#!/usr/bin/env python3
"""Regression tests for deterministic Cangjie closure checks."""

from __future__ import annotations

import io
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from unittest.mock import patch

from check_cangjie_closure import main, scan_source


def finding_codes(source: str) -> set[str]:
    return {finding.code for finding in scan_source(source, "test.cj")}


class ClosureCheckerTests(unittest.TestCase):
    def test_existing_array_and_capture_rules_cover_rollout_regressions(self) -> None:
        source = """
func build(xs: Array<Int64>): Array<Int64> {
    let appended = Array<Int64>()
    appended.append(1)
    let repeated = Array<Int64>(xs.size, item: 0)
    var sorted = xs
    return Array<Int64>(xs.size, {i => sorted[i]})
}
"""
        self.assertTrue({"CJ020", "CJ025", "CJ030"} <= finding_codes(source))

    def test_case_branch_brace_is_rejected(self) -> None:
        source = """
func value(input: ?Int64): Int64 {
    match (input) {
        case Some(v) => {
            v
        }
        case None => 0
    }
}
"""
        self.assertIn("CJ028", finding_codes(source))

    def test_multiline_case_expression_without_brace_is_allowed(self) -> None:
        source = """
func value(input: ?Int64): Int64 {
    match (input) {
        case Some(v) =>
            let doubled = v * 2
            doubled
        case None => 0
    }
}
"""
        self.assertNotIn("CJ028", finding_codes(source))

    def test_case_like_text_in_comments_and_strings_is_ignored(self) -> None:
        source = """
func value(): String {
    // case None => {
    return "case Some(v) => {"
}
"""
        self.assertNotIn("CJ028", finding_codes(source))

    def test_case_branch_returning_lambda_is_allowed(self) -> None:
        source = """
func mapper(input: ?Int64): (Int64) -> Int64 {
    match (input) {
        case Some(v) => {x => x + v}
        case None => {x => x}
    }
}
"""
        self.assertNotIn("CJ028", finding_codes(source))

    def test_direct_string_byte_assigned_to_rune_is_rejected(self) -> None:
        source = """
func lastRune(text: String): Rune {
    var last: Rune = r' '
    for (item in text) {
        last = item
    }
    return last
}
"""
        self.assertIn("CJ031", finding_codes(source))

    def test_direct_string_byte_iteration_is_allowed_for_byte_result(self) -> None:
        source = """
func lastByte(text: String): UInt8 {
    var last: UInt8 = 0
    for (item in text) {
        last = item
    }
    return last
}
"""
        self.assertNotIn("CJ031", finding_codes(source))

    def test_rune_iterator_is_allowed_for_rune_result(self) -> None:
        source = """
func lastRune(text: String): Rune {
    var last: Rune = r' '
    for (item in text.runes()) {
        last = item
    }
    return last
}
"""
        self.assertNotIn("CJ031", finding_codes(source))

    def test_explicit_byte_to_rune_conversion_is_allowed(self) -> None:
        source = """
func lastRune(text: String): Rune {
    var last: Rune = r' '
    for (item in text) {
        last = Rune(item)
    }
    return last
}
"""
        self.assertNotIn("CJ031", finding_codes(source))

    def test_string_binding_from_another_function_does_not_leak(self) -> None:
        source = """
func consumeText(data: String): Unit {}

func consumeRunes(data: Array<Rune>): Rune {
    var last: Rune = r' '
    for (item in data) {
        last = item
    }
    return last
}
"""
        self.assertNotIn("CJ031", finding_codes(source))

    def test_inner_non_string_binding_shadows_string_parameter(self) -> None:
        source = """
func consume(data: String): Rune {
    var last: Rune = r' '
    {
        let data: Array<Rune> = [r'a']
        for (item in data) {
            last = item
        }
    }
    return last
}
"""
        self.assertNotIn("CJ031", finding_codes(source))

    def test_direct_string_byte_character_comparisons_are_rejected(self) -> None:
        for expression in ("item == \"A\"", "item >= 'A'", "r'A' == item"):
            with self.subTest(expression=expression):
                source = f"""
func consume(text: String): Bool {{
    for (item in text) {{
        if ({expression}) {{ return true }}
    }}
    return false
}}
"""
                self.assertIn("CJ031", finding_codes(source))

    def test_direct_string_byte_literal_comparison_is_allowed(self) -> None:
        source = """
func consume(text: String): Bool {
    for (item in text) {
        if (item == b'A') { return true }
    }
    return false
}
"""
        self.assertNotIn("CJ031", finding_codes(source))

    def test_direct_string_byte_string_constructor_is_rejected(self) -> None:
        source = """
func consume(text: String): String {
    var result = ""
    for (item in text) {
        result = result + String(item)
    }
    return result
}
"""
        self.assertIn("CJ031", finding_codes(source))

    def test_string_byte_false_positives_in_comments_and_literals_are_ignored(self) -> None:
        source = """
func consume(text: String): Bool {
    let note = "item == 'A' and String(item)"
    for (item in text) {
        // item >= 'A'
        if (item == b'A') { return true }
    }
    return note.isEmpty()
}
"""
        self.assertNotIn("CJ031", finding_codes(source))

    def test_std_sort_untyped_trailing_lambda_is_rejected(self) -> None:
        source = """
import std.sort.*
func order(values: Array<Int64>): Unit {
    sort(values) {
        left, right => right - left
    }
}
"""
        self.assertIn("CJ032", finding_codes(source))

    def test_named_or_typed_sort_callbacks_are_not_flagged(self) -> None:
        named = """
import std.sort.*
func order(values: Array<Int64>): Unit {
    sort(values, by: {left: Int64, right: Int64 => right.compare(left)})
}
"""
        typed_trailing = """
import std.sort.*
func order(values: Array<Int64>): Unit {
    sort(values) {left: Int64, right: Int64 => right.compare(left)}
}
"""
        self.assertNotIn("CJ032", finding_codes(named))
        self.assertNotIn("CJ032", finding_codes(typed_trailing))

    def test_unrelated_trailing_lambda_is_not_flagged_as_sort(self) -> None:
        source = """
func apply(values: Array<Int64>, callback: (Int64) -> Int64): Unit {}
func transform(values: Array<Int64>): Unit {
    apply(values) {value => value + 1}
}
"""
        self.assertNotIn("CJ032", finding_codes(source))

    def test_arraylist_requires_visible_collection_import(self) -> None:
        source = """
func build(): ArrayList<Int64> {
    return ArrayList<Int64>()
}
"""
        self.assertIn("CJ033", finding_codes(source))

    def test_numeric_expression_is_not_a_string_constructor_argument(self) -> None:
        source = """
func bit(n: Int64): String {
    return String(n % 2)
}
"""
        self.assertIn("CJ034", finding_codes(source))

    def test_documented_string_constructors_are_not_numeric_conversion_findings(self) -> None:
        source = """
func text(runes: Array<Rune>): String {
    let empty = String()
    return empty + String(runes)
}
"""
        self.assertNotIn("CJ034", finding_codes(source))

    def test_arraylist_supported_import_forms_are_allowed(self) -> None:
        imports = (
            "import std.collection.*",
            "import std.collection.ArrayList",
            "import std.collection.{HashMap, ArrayList}",
        )
        for import_line in imports:
            with self.subTest(import_line=import_line):
                source = f"""
{import_line}
func build(): ArrayList<Int64> {{
    return ArrayList<Int64>()
}}
"""
                self.assertNotIn("CJ033", finding_codes(source))

    def test_local_arraylist_declaration_is_not_flagged(self) -> None:
        source = """
class ArrayList<T> {}
func build(): ArrayList<Int64> {
    return ArrayList<Int64>()
}
"""
        self.assertNotIn("CJ033", finding_codes(source))

    def test_empty_or_whitespace_stdin_is_an_input_error(self) -> None:
        for candidate in ("", " \r\n\t"):
            with self.subTest(candidate=repr(candidate)):
                stdout = io.StringIO()
                stderr = io.StringIO()
                with (
                    patch.object(sys, "argv", ["check_cangjie_closure.py", "-"]),
                    patch.object(sys, "stdin", io.StringIO(candidate)),
                    redirect_stdout(stdout),
                    redirect_stderr(stderr),
                ):
                    self.assertEqual(main(), 2)
                self.assertIn("input error", stderr.getvalue())

    def test_nonempty_stdin_can_pass(self) -> None:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with (
            patch.object(sys, "argv", ["check_cangjie_closure.py", "-"]),
            patch.object(sys, "stdin", io.StringIO("func ok(): Unit {}")),
            redirect_stdout(stdout),
            redirect_stderr(stderr),
        ):
            self.assertEqual(main(), 0)
        self.assertIn("closure-check: ok", stdout.getvalue())

    def test_powershell_utf8_bom_stdin_is_decoded_before_scanning(self) -> None:
        candidate = b"\xef\xbb\xbffunc consume(text: String): Bool {\n    for (item in text) {\n        if (item == 'A') { return true }\n    }\n    return false\n}\n"
        stdin = io.TextIOWrapper(
            io.BytesIO(candidate), encoding="gbk", errors="surrogateescape"
        )
        stdout = io.StringIO()
        stderr = io.StringIO()
        with (
            patch.object(sys, "argv", ["check_cangjie_closure.py", "-"]),
            patch.object(sys, "stdin", stdin),
            redirect_stdout(stdout),
            redirect_stderr(stderr),
        ):
            self.assertEqual(main(), 1)
        self.assertIn("CJ031", stdout.getvalue())

    def test_powershell_bom_only_stdin_is_an_input_error(self) -> None:
        stdin = io.TextIOWrapper(
            io.BytesIO(b"\xef\xbb\xbf\r\n"), encoding="gbk", errors="surrogateescape"
        )
        stdout = io.StringIO()
        stderr = io.StringIO()
        with (
            patch.object(sys, "argv", ["check_cangjie_closure.py", "-"]),
            patch.object(sys, "stdin", stdin),
            redirect_stdout(stdout),
            redirect_stderr(stderr),
        ):
            self.assertEqual(main(), 2)
        self.assertIn("input error", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
