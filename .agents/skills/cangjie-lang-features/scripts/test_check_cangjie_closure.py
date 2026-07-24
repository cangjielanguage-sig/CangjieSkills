#!/usr/bin/env python3
"""Regression tests for deterministic Cangjie closure checks."""

from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

from check_cangjie_closure import main, scan_source


def finding_codes(source: str) -> set[str]:
    return {finding.code for finding in scan_source(source, "test.cj")}


def finding_severities(source: str, code: str) -> set[str]:
    return {
        finding.severity
        for finding in scan_source(source, "test.cj")
        if finding.code == code
    }


def run_main_stdin(candidate: str, *options: str) -> tuple[int, str, str]:
    stdout = io.StringIO()
    stderr = io.StringIO()
    with (
        patch.object(sys, "argv", ["check_cangjie_closure.py", *options, "-"]),
        patch.object(sys, "stdin", io.StringIO(candidate)),
        redirect_stdout(stdout),
        redirect_stderr(stderr),
    ):
        exit_code = main()
    return exit_code, stdout.getvalue(), stderr.getvalue()


class ClosureCheckerTests(unittest.TestCase):
    def test_known_array_and_capture_diagnostics_are_errors(self) -> None:
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
        self.assertEqual(finding_severities(source, "CJ020"), {"error"})
        self.assertEqual(finding_severities(source, "CJ025"), {"error"})
        self.assertEqual(finding_severities(source, "CJ030"), {"error"})

    def test_string_builder_append_is_valid(self) -> None:
        source = """
func build(): String {
    let builder = StringBuilder()
    builder.append("Hello")
    return builder.toString()
}
"""
        self.assertNotIn("CJ020", finding_codes(source))

    def test_direct_string_builder_constructor_append_is_valid(self) -> None:
        source = 'func build(): Unit { StringBuilder().append("Hello") }'
        self.assertNotIn("CJ020", finding_codes(source))

    def test_direct_array_constructor_append_is_error(self) -> None:
        source = "func build(): Unit { Array<Int64>().append(1) }"
        self.assertEqual(finding_severities(source, "CJ020"), {"error"})

    def test_unknown_append_is_advisory(self) -> None:
        source = """
func addOne(target: CustomBuffer): Unit {
    target.append(1)
}
"""
        self.assertEqual(finding_severities(source, "CJ020"), {"warning"})

    def test_complex_receivers_are_advisory_instead_of_silently_skipped(self) -> None:
        source = """
func inspect(holder: Holder): Unit {
    makeBuffer().append(1)
    println(holder.value.length)
    println(holder.value.toInt64())
    holder.values.removeAt(0)
}
"""
        self.assertEqual(finding_severities(source, "CJ020"), {"warning"})
        self.assertEqual(finding_severities(source, "CJ023"), {"warning"})
        self.assertEqual(finding_severities(source, "CJ022"), {"warning"})
        self.assertEqual(finding_severities(source, "CJ027"), {"warning"})

    def test_range_operator_is_not_a_length_member_access(self) -> None:
        source = "func indices(length: Int64): Range<Int64> { return 0..length }"
        self.assertNotIn("CJ023", finding_codes(source))

    def test_out_of_scope_inner_type_does_not_prove_outer_receiver(self) -> None:
        source = """
func addOne(target: CustomBuffer, condition: Bool): Unit {
    if (condition) {
        let target: Array<Int64> = []
        println(target.size)
    }
    target.append(1)
}
"""
        self.assertEqual(finding_severities(source, "CJ020"), {"warning"})

    def test_typed_lambda_parameter_shadows_outer_array_type(self) -> None:
        source = """
func build(): (StringBuilder) -> Unit {
    let value: Array<Int64> = [1]
    return {value: StringBuilder => value.append("ok")}
}
"""
        self.assertNotIn("CJ020", finding_codes(source))

    def test_generic_array_lambda_parameter_proves_append_error(self) -> None:
        source = """
func build(): (Array<Int64>) -> Unit {
    let value: StringBuilder = StringBuilder()
    return {value: Array<Int64> => value.append(1)}
}
"""
        self.assertEqual(finding_severities(source, "CJ020"), {"error"})

    def test_generic_custom_lambda_parameter_does_not_inherit_outer_array(self) -> None:
        source = """
func build(): (Custom<Int64>) -> Unit {
    let value: Array<Int64> = [1]
    return {value: Custom<Int64> => value.append(1)}
}
"""
        self.assertEqual(finding_severities(source, "CJ020"), {"warning"})

    def test_for_binding_shadows_outer_array_type(self) -> None:
        source = """
func build(buffers: Array<CustomBuffer>): Unit {
    let value: Array<Int64> = [1]
    for (value in buffers) {
        value.append(1)
    }
}
"""
        self.assertEqual(finding_severities(source, "CJ020"), {"warning"})

    def test_match_pattern_binding_does_not_inherit_outer_array_type(self) -> None:
        source = """
func build(value: ?StringBuilder): Unit {
    let item: Array<Int64> = [1]
    match (value) {
        case Some(item) => item.append("ok")
        case None => ()
    }
}
"""
        self.assertEqual(finding_severities(source, "CJ020"), {"warning"})

    def test_if_let_binding_does_not_inherit_outer_array_type(self) -> None:
        source = """
func build(value: ?StringBuilder): Unit {
    let item: Array<Int64> = [1]
    if (let Some(item) <- value) {
        item.append("ok")
    }
}
"""
        self.assertEqual(finding_severities(source, "CJ020"), {"warning"})

    def test_known_array_parameter_append_is_error(self) -> None:
        source = """
func addOne(target: Array<Int64>): Unit {
    target.append(1)
}
"""
        self.assertEqual(finding_severities(source, "CJ020"), {"error"})

    def test_generic_function_array_parameter_append_is_error(self) -> None:
        source = """
func addOne<T>(target: Array<T>, item: T): Unit {
    target.append(item)
}
"""
        self.assertEqual(finding_severities(source, "CJ020"), {"error"})

    def test_array_literal_binding_append_is_error(self) -> None:
        source = """
func build(): Unit {
    let target = [1, 2]
    target.append(3)
}
"""
        self.assertEqual(finding_severities(source, "CJ020"), {"error"})

    def test_receiver_aware_length_conversion_and_remove_rules(self) -> None:
        source = """
import std.collection.*
func inspect(text: String, values: Array<Int64>, list: ArrayList<Int64>, custom: Custom): Unit {
    let n: Int32 = 1
    println(text.length)
    println(values.length)
    println(n.toInt64())
    list.removeAt(0)
    println(custom.length)
    println(custom.toInt64())
    custom.removeAt(0)
}
"""
        self.assertEqual(finding_severities(source, "CJ023"), {"error", "warning"})
        self.assertEqual(finding_severities(source, "CJ022"), {"error", "warning"})
        self.assertEqual(finding_severities(source, "CJ027"), {"error", "warning"})

    def test_control_headers_allow_spacing_and_targetless_match(self) -> None:
        source = """
func inspect(ok: Bool, value: Int64): Unit {
    if  (ok) {}
    while
        (ok) { break }
    match {
        case value > 0 => println(value)
        case _ => ()
    }
}
"""
        self.assertNotIn("CJ012", finding_codes(source))

    def test_escaped_keyword_identifiers_are_not_control_headers(self) -> None:
        source = "func echo(`if`: Bool): Bool { return `if` }"
        self.assertNotIn("CJ012", finding_codes(source))

    def test_invalid_control_headers_are_errors(self) -> None:
        source = """
func inspect(ok: Bool, value: Int64): Unit {
    if ok {}
    match value { case _ => () }
}
"""
        self.assertEqual(finding_severities(source, "CJ012"), {"error"})

    def test_import_inside_or_after_declaration_is_error(self) -> None:
        inside = """
func build(): Unit {
    import std.collection.*
}
"""
        after = """
func helper(): Unit {}
public import std.collection.*
"""
        self.assertEqual(finding_severities(inside, "CJ010"), {"error"})
        self.assertEqual(finding_severities(after, "CJ011"), {"error"})

    def test_inline_import_inside_or_after_declaration_is_error(self) -> None:
        inside = "func build(): Unit { import std.collection.* }"
        after = "func helper(): Unit {} import std.collection.*"
        self.assertEqual(finding_severities(inside, "CJ010"), {"error"})
        self.assertEqual(finding_severities(after, "CJ011"), {"error"})

    def test_typed_array_initializer_parameter_named_item_is_valid(self) -> None:
        source = """
func identityArray(size: Int64): Array<Int64> {
    return Array<Int64>(size, {item: Int64 => item})
}
"""
        self.assertNotIn("CJ025", finding_codes(source))

    def test_true_array_item_named_argument_is_error(self) -> None:
        source = """
func zeroes(size: Int64): Array<Int64> {
    return Array<Int64>(size, item: 0)
}
"""
        self.assertEqual(finding_severities(source, "CJ025"), {"error"})

    def test_array_init_element_label_is_error_but_positional_initializer_is_valid(
        self,
    ) -> None:
        invalid = """
func zeroes(size: Int64): Array<Int64> {
    return Array<Int64>(size, initElement: {i => i})
}
"""
        valid = """
func zeroes(size: Int64): Array<Int64> {
    return Array<Int64>(size, {i => i})
}
"""
        self.assertEqual(finding_severities(invalid, "CJ025"), {"error"})
        self.assertNotIn("CJ025", finding_codes(valid))

    def test_raw_and_triple_single_strings_are_masked(self) -> None:
        source = """
func notes(): Unit {
    let raw = #"if broken { target.append(1)"#
    let multiline = '''match broken { custom.length'''
}
"""
        codes = finding_codes(source)
        self.assertNotIn("CJ001", codes)
        self.assertNotIn("CJ012", codes)
        self.assertNotIn("CJ020", codes)
        self.assertNotIn("CJ023", codes)

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

    def test_expired_inner_string_binding_does_not_taint_outer_iterable(self) -> None:
        source = """
func keepRunes(data: Array<Rune>, condition: Bool): Rune {
    if (condition) {
        let data: String = "temporary"
        println(data)
    }
    var last: Rune = r' '
    for (item in data) {
        last = item
    }
    return last
}
"""
        self.assertNotIn("CJ031", finding_codes(source))

    def test_expired_inner_rune_binding_does_not_taint_byte_assignment(self) -> None:
        source = """
func lastByte(data: String, condition: Bool): UInt8 {
    var last: UInt8 = 0
    if (condition) {
        var last: Rune = r' '
        println(last)
    }
    for (item in data) {
        last = item
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
        self.assertEqual(finding_severities(source, "CJ032"), {"warning"})

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
        self.assertEqual(finding_severities(source, "CJ033"), {"warning"})

    def test_numeric_expression_is_not_a_string_constructor_argument(self) -> None:
        source = """
func bit(n: Int64): String {
    return String(n % 2)
}
"""
        self.assertIn("CJ034", finding_codes(source))
        self.assertEqual(finding_severities(source, "CJ034"), {"warning"})

    def test_array_sort_members_are_rejected_but_free_sort_is_not(self) -> None:
        invalid = """
func order(values: Array<Int64>): Unit {
    values.sort()
    let copy = values.sorted()
    values.sortBy({a, b => a < b})
}
"""
        valid = """
import std.sort.*
func order(values: Array<Int64>): Unit {
    sort(values)
}
"""
        self.assertEqual(finding_severities(invalid, "CJ035"), {"error"})
        self.assertNotIn("CJ035", finding_codes(valid))

    def test_std_hash_put_is_rejected_and_unproven_hash_put_is_advisory(self) -> None:
        standard = """
import std.collection.*
func update(values: HashMap<String, Int64>, seen: HashSet<Int64>): Unit {
    values.put("x", 1)
    seen.put(1)
}
"""
        unproven = """
func update(values: HashMap<String, Int64>): Unit {
    values.put("x", 1)
}
"""
        self.assertEqual(finding_severities(standard, "CJ036"), {"error"})
        self.assertEqual(finding_severities(unproven, "CJ036"), {"warning"})

    def test_known_string_legacy_members_are_errors_and_unknown_substring_is_warning(
        self,
    ) -> None:
        known = """
func convert(text: String): String {
    return text.subString(0, 1).toUpper()
}
"""
        unknown = """
func convert(text: CustomText): CustomText {
    return text.substring(0, 1)
}
"""
        self.assertEqual(finding_severities(known, "CJ037"), {"error"})
        self.assertEqual(finding_severities(unknown, "CJ021"), {"warning"})

    def test_invalid_numeric_suffix_bitwise_tilde_none_comparison_and_float_modulo(
        self,
    ) -> None:
        source = """
func inspect(value: ?Int64, number: Int64): Bool {
    let typed = 2Int64
    let complement = ~number
    let wrapped = 361.0 % 360.0
    return value != None
}
"""
        self.assertTrue(
            {"CJ038", "CJ039", "CJ040", "CJ043"} <= finding_codes(source)
        )
        for code in ("CJ038", "CJ039", "CJ040", "CJ043"):
            self.assertEqual(finding_severities(source, code), {"error"})

    def test_valid_suffix_destructor_composition_typed_none_and_integer_modulo_are_allowed(
        self,
    ) -> None:
        source = """
class Resource {
    ~init() {}
}
func first(value: Int64): Int64 { value + 1 }
func second(value: Int64): Int64 { value * 2 }
func inspect(number: Int64): Unit {
    let typed = 2i64
    let composed = first ~> second
    let missing = None<Int64>
    let remainder = number % 2
}
"""
        codes = finding_codes(source)
        self.assertFalse({"CJ038", "CJ039", "CJ040", "CJ043"} & codes)

    def test_string_index_character_semantics_are_rejected(self) -> None:
        source = """
func inspect(text: String): Bool {
    if (text[0] == "a") { return true }
    let first = String(text[0])
    return false
}
"""
        self.assertEqual(finding_severities(source, "CJ041"), {"error"})

    def test_string_byte_index_and_string_slice_are_allowed(self) -> None:
        source = """
func inspect(text: String): Bool {
    let prefix = text[0..1]
    return text[0] == b'a' && prefix == "a"
}
"""
        self.assertNotIn("CJ041", finding_codes(source))

    def test_rune_array_requires_rune_literal_in_comparisons(self) -> None:
        invalid = """
func inspect(text: String): Bool {
    let runes = text.toRuneArray()
    return runes[0] == 'a'
}
"""
        valid = """
func inspect(text: String): Bool {
    let runes = text.toRuneArray()
    return runes[0] == r'a'
}
"""
        self.assertEqual(finding_severities(invalid, "CJ042"), {"error"})
        self.assertNotIn("CJ042", finding_codes(valid))

    def test_empty_match_case_is_rejected_and_explicit_unit_is_valid(self) -> None:
        invalid = """
func inspect(value: ?Int64): Unit {
    match (value) {
        case Some(item) => println(item)
        case None =>
    }
}
"""
        valid = """
func inspect(value: ?Int64): Unit {
    match (value) {
        case Some(item) => println(item)
        case None => ()
    }
}
"""
        self.assertEqual(finding_severities(invalid, "CJ044"), {"error"})
        self.assertNotIn("CJ044", finding_codes(valid))

    def test_recursive_local_function_without_return_type_is_advisory(self) -> None:
        invalid = """
func outer(): Unit {
    func visit(value: Int64) {
        if (value > 0) { visit(value - 1) }
    }
    visit(2)
}
"""
        valid = """
func outer(): Unit {
    func visit(value: Int64): Unit {
        if (value > 0) { visit(value - 1) }
    }
    visit(2)
}
"""
        self.assertEqual(finding_severities(invalid, "CJ045"), {"warning"})
        self.assertNotIn("CJ045", finding_codes(valid))

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

    def test_to_string_result_proves_string_byte_iteration(self) -> None:
        invalid = """
func inspect(value: Int64): Bool {
    let text = value.toString(radix: 16)
    for (item in text) {
        if (item >= 'a' && item <= 'f') { return true }
    }
    return false
}
"""
        valid = """
func inspect(value: Int64): Bool {
    let text = value.toString(radix: 16)
    for (item in text) {
        if (item >= b'a' && item <= b'f') { return true }
    }
    return false
}
"""
        self.assertEqual(finding_severities(invalid, "CJ031"), {"error"})
        self.assertNotIn("CJ031", finding_codes(valid))

    def test_control_operand_must_remain_inside_parentheses(self) -> None:
        invalid = """
func sum(n: Int64): Int64 {
    var i: Int64 = 0
    while (n - i) > 0 { i += 1 }
    return i
}
"""
        valid = """
func sum(n: Int64): Int64 {
    var i: Int64 = 0
    while (n - i > 0) { i += 1 }
    return i
}
"""
        self.assertEqual(finding_severities(invalid, "CJ012"), {"error"})
        self.assertNotIn("CJ012", finding_codes(valid))

    def test_tuple_match_selector_requires_inner_parentheses(self) -> None:
        invalid = """
func inspect(left: ?Int64, right: ?Int64): Bool {
    match (left, right) {
        case (Some(_), Some(_)) => true
        case _ => false
    }
}
"""
        valid = """
func inspect(left: ?Int64, right: ?Int64): Bool {
    match ((left, right)) {
        case (Some(_), Some(_)) => true
        case _ => false
    }
}
"""
        self.assertEqual(finding_severities(invalid, "CJ047"), {"error"})
        self.assertNotIn("CJ047", finding_codes(valid))

    def test_array_positional_scalar_repeat_is_rejected(self) -> None:
        invalid = "func zeroes(n: Int64): Array<Int64> { Array<Int64>(n, 0) }"
        named = "func zeroes(n: Int64): Array<Int64> { Array<Int64>(n, repeat: 0) }"
        initializer = (
            "func zeroes(n: Int64): Array<Int64> { "
            "Array<Int64>(n, {index: Int64 => index * 0}) }"
        )
        self.assertEqual(finding_severities(invalid, "CJ046"), {"error"})
        self.assertNotIn("CJ046", finding_codes(named))
        self.assertNotIn("CJ046", finding_codes(initializer))

    def test_function_parameters_are_not_assignable(self) -> None:
        invalid = """
func search(low: Int64, high: Int64): Int64 {
    low = low + 1
    high -= 1
    return low + high
}
"""
        valid = """
func search(low: Int64, high: Int64): Int64 {
    var left = low
    var right = high
    left += 1
    right -= 1
    return left + right
}
"""
        self.assertEqual(finding_severities(invalid, "CJ048"), {"error"})
        self.assertNotIn("CJ048", finding_codes(valid))

    def test_non_unit_function_cannot_end_in_a_loop(self) -> None:
        invalid = """
func find(values: Array<Int64>): Int64 {
    while (true) {
        if (values.size > 0) { return values[0] }
    }
}
"""
        valid = """
func find(values: Array<Int64>): Int64 {
    while (values.size > 0) {
        return values[0]
    }
    return 0
}
"""
        self.assertEqual(finding_severities(invalid, "CJ049"), {"error"})
        self.assertNotIn("CJ049", finding_codes(valid))

    def test_array_of_tuple_requires_elementwise_equality(self) -> None:
        invalid = """
func same(
    left: Array<(Int64, Int64)>,
    right: Array<(Int64, Int64)>
): Bool {
    return left == right
}
"""
        scalar_array = """
func same(left: Array<Int64>, right: Array<Int64>): Bool {
    return left == right
}
"""
        self.assertEqual(finding_severities(invalid, "CJ050"), {"error"})
        self.assertNotIn("CJ050", finding_codes(scalar_array))

    def test_bare_std_math_calls_require_import_review(self) -> None:
        missing = """
func distance(value: Float64): Float64 {
    return pow(sin(value), 2.0) + sqrt(value)
}
"""
        imported = """
import std.math.*
func distance(value: Float64): Float64 {
    return pow(sin(value), 2.0) + sqrt(value)
}
"""
        self.assertEqual(finding_severities(missing, "CJ051"), {"warning"})
        self.assertNotIn("CJ051", finding_codes(imported))

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

    def test_warning_only_stdin_returns_success(self) -> None:
        exit_code, stdout, stderr = run_main_stdin(
            "func use(target: CustomBuffer): Unit { target.append(1) }"
        )
        self.assertEqual(exit_code, 0)
        self.assertEqual(stderr, "")
        self.assertIn("CJ020 [warning]", stdout)
        self.assertIn("passed with warnings; review required", stdout)

    def test_error_and_warning_stdin_returns_failure(self) -> None:
        source = """
func use(values: Array<Int64>, target: CustomBuffer): Unit {
    values.append(1)
    target.append(1)
}
"""
        exit_code, stdout, stderr = run_main_stdin(source)
        self.assertEqual(exit_code, 1)
        self.assertEqual(stderr, "")
        self.assertIn("CJ020 [error]", stdout)
        self.assertIn("CJ020 [warning]", stdout)
        self.assertIn("closure-check: failed", stdout)

    def test_json_output_includes_severity_without_dropping_existing_fields(self) -> None:
        exit_code, stdout, stderr = run_main_stdin(
            "func use(target: CustomBuffer): Unit { target.append(1) }",
            "--format",
            "json",
        )
        self.assertEqual(exit_code, 0)
        self.assertEqual(stderr, "")
        payload = json.loads(stdout)
        self.assertEqual(len(payload), 1)
        self.assertEqual(payload[0]["severity"], "warning")
        self.assertEqual(payload[0]["code"], "CJ020")
        self.assertTrue(
            {"path", "line", "column", "code", "message", "reference", "severity"}
            <= payload[0].keys()
        )

    def test_empty_file_and_directory_are_input_errors(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            empty_file = root / "empty.cj"
            empty_file.write_text("", encoding="utf-8")
            for candidate in (str(empty_file), str(root / "no_sources")):
                if candidate.endswith("no_sources"):
                    Path(candidate).mkdir()
                with self.subTest(candidate=candidate):
                    stdout = io.StringIO()
                    stderr = io.StringIO()
                    with (
                        patch.object(
                            sys, "argv", ["check_cangjie_closure.py", candidate]
                        ),
                        redirect_stdout(stdout),
                        redirect_stderr(stderr),
                    ):
                        self.assertEqual(main(), 2)
                    self.assertIn("input error", stderr.getvalue())

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
