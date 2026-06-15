#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

import argparse
import json
import re
import sys
from itertools import combinations
from typing import Any, Dict, List, Tuple

from common import (
    CASE_KEYS,
    FIXED_COVERAGE_NODES,
    INTERFACE_TYPE_VALUES,
    SINGLE_PARAMETER_CATEGORIES,
    all_required_pairs,
    extract_parameter_values,
    first_component,
    is_not_applicable,
    pairwise_needed,
)


GENERIC_CASE_RE = re.compile(r"^用例\d+$")


def add_error(errors: List[str], path: str, message: str) -> None:
    errors.append(f"{path}: {message}")


def validate_not_applicable_leaf(value: Any, path: str, errors: List[str]) -> None:
    if isinstance(value, dict) and "不涉及" in value and value["不涉及"] not in ("", None, "不涉及"):
        add_error(errors, f"{path}.不涉及", "不涉及 must be a leaf")


def walk_testcases(node: Any, path: str, errors: List[str]) -> None:
    validate_not_applicable_leaf(node, path, errors)
    if isinstance(node, dict):
        for key, value in node.items():
            child_path = f"{path}.{key}"
            if key == "不涉及":
                validate_not_applicable_leaf({key: value}, path, errors)
                continue
            if isinstance(value, dict) and (("测试流程" in value) or ("预期结果" in value)):
                if set(value.keys()) != CASE_KEYS:
                    add_error(errors, child_path, "testcase must contain only 测试流程 and 预期结果")
                if GENERIC_CASE_RE.match(str(key)):
                    add_error(errors, child_path, "testcase name must not be 用例N")
                for case_key in CASE_KEYS:
                    case_value = value.get(case_key)
                    if not isinstance(case_value, str) or not case_value.strip():
                        add_error(errors, f"{child_path}.{case_key}", "must be a non-empty string")
            else:
                walk_testcases(value, child_path, errors)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            walk_testcases(item, f"{path}[{index}]", errors)


def contains_testcase_object(node: Any) -> bool:
    if isinstance(node, dict):
        if CASE_KEYS.issubset(node.keys()):
            return True
        return any(contains_testcase_object(value) for value in node.values())
    if isinstance(node, list):
        return any(contains_testcase_object(item) for item in node)
    return False


def parameter_names(api_info: Dict[str, Any]) -> List[str]:
    params = api_info.get("参数", {})
    if is_not_applicable(params) or not isinstance(params, dict):
        return []
    return [str(name) for name in params.keys() if str(name) != "不涉及"]


def validate_interface_type(api: str, api_info: Dict[str, Any], errors: List[str]) -> None:
    path = f"接口列表.{api}.接口类型"
    value = api_info.get("接口类型")
    if not isinstance(value, str) or not value.strip():
        add_error(errors, path, "must be a non-empty string")
        return

    normalized = value.strip()
    if normalized not in INTERFACE_TYPE_VALUES:
        allowed = ", ".join(sorted(INTERFACE_TYPE_VALUES))
        add_error(errors, path, f"must use normalized interface type value: {allowed}")


def validate_single_parameter(api: str, api_info: Dict[str, Any], coverage: Dict[str, Any], errors: List[str]) -> None:
    params = parameter_names(api_info)
    single = coverage.get("单参数测试")
    path = f"测试覆盖.{api}.单参数测试"

    if not params:
        if not is_not_applicable(single):
            add_error(errors, path, "must be 不涉及 when the API has no parameters")
        return

    if not isinstance(single, dict) or is_not_applicable(single):
        add_error(errors, path, "must branch by parameter name for parameterized APIs")
        return

    single_names = set(str(name) for name in single.keys())
    expected_names = set(params)
    missing = sorted(expected_names - single_names)
    extra = sorted(single_names - expected_names)
    if missing:
        add_error(errors, path, f"missing parameter nodes: {', '.join(missing)}")
    if extra:
        add_error(errors, path, f"extra parameter nodes: {', '.join(extra)}")

    for key, value in single.items():
        child_path = f"{path}.{key}"
        if isinstance(value, dict) and (("测试流程" in value) or ("预期结果" in value)):
            add_error(errors, child_path, "testcase must be under 参数名 -> 分类节点")

    for param in sorted(expected_names & single_names):
        param_node = single[param]
        param_path = f"{path}.{param}"
        if not isinstance(param_node, dict) or is_not_applicable(param_node):
            add_error(errors, param_path, "must contain 有效等价类/无效等价类/边界值/特殊值")
            continue
        if ("测试流程" in param_node) or ("预期结果" in param_node):
            add_error(errors, param_path, "must contain category nodes before testcase fields")
            continue

        for category in SINGLE_PARAMETER_CATEGORIES:
            category_path = f"{param_path}.{category}"
            if category not in param_node:
                add_error(errors, param_path, f"missing category node {category}")
                continue
            category_value = param_node[category]
            if is_not_applicable(category_value):
                continue
            if not isinstance(category_value, dict):
                add_error(errors, category_path, "must be a testcase map or 不涉及 leaf")
                continue
            if ("测试流程" in category_value) or ("预期结果" in category_value):
                add_error(errors, category_path, "must contain named testcase objects")
                continue
            if not contains_testcase_object(category_value):
                add_error(errors, category_path, "must contain at least one testcase object or 不涉及")


def find_assignment(flow: str, param: str, values: List[str]) -> str | None:
    for value in sorted(values, key=len, reverse=True):
        if f"{param}={value}" in flow:
            return value
    return None


def validate_pairwise(api: str, data: Dict[str, Any], coverage: Dict[str, Any], errors: List[str]) -> None:
    _, parameters = extract_parameter_values(data, api)
    multi = coverage.get("多参数组合")
    path = f"测试覆盖.{api}.多参数组合"
    if not pairwise_needed(parameters):
        if not is_not_applicable(multi):
            add_error(errors, path, "must be 不涉及 when Pair-wise is not needed")
        return

    if not isinstance(multi, dict) or is_not_applicable(multi):
        add_error(errors, path, "must contain Pair-wise testcase objects")
        return

    rows: List[Dict[str, str]] = []
    for case_name, case_value in multi.items():
        if not isinstance(case_value, dict) or set(case_value.keys()) != CASE_KEYS:
            add_error(errors, f"{path}.{case_name}", "must be a testcase object")
            continue
        flow = case_value["测试流程"]
        row: Dict[str, str] = {}
        for param, values in parameters.items():
            if not values:
                continue
            matched = find_assignment(flow, param, values)
            if matched is None:
                add_error(errors, f"{path}.{case_name}.测试流程", f"cannot find assignment for {param}")
            else:
                row[param] = matched
        if row:
            rows.append(row)

    required = all_required_pairs({name: values for name, values in parameters.items() if values})
    covered = set()
    for row in rows:
        for left, right in combinations(row.keys(), 2):
            covered.add((left, row[left], right, row[right]))
    missing = sorted(required - covered)
    if missing:
        preview = "; ".join(f"{a}={av} + {b}={bv}" for a, av, b, bv in missing[:10])
        add_error(errors, path, f"missing Pair-wise combinations: {preview}")


def validate(data: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    component_name, body = first_component(data)
    interface_map = body.get("接口列表")
    coverage_map = body.get("测试覆盖")

    if not isinstance(interface_map, dict):
        add_error(errors, component_name, "missing object node 接口列表")
        return errors
    if not isinstance(coverage_map, dict):
        add_error(errors, component_name, "missing object node 测试覆盖")
        return errors

    interface_names = set(interface_map.keys())
    coverage_names = set(coverage_map.keys())
    if interface_names != coverage_names:
        missing = sorted(interface_names - coverage_names)
        extra = sorted(coverage_names - interface_names)
        if missing:
            add_error(errors, "测试覆盖", f"missing interfaces: {', '.join(missing)}")
        if extra:
            add_error(errors, "测试覆盖", f"extra interfaces: {', '.join(extra)}")

    for api in sorted(interface_names & coverage_names):
        api_info = interface_map.get(api)
        if not isinstance(api_info, dict):
            add_error(errors, f"接口列表.{api}", "must be an object")
            continue
        validate_interface_type(api, api_info, errors)

        coverage = coverage_map.get(api)
        if not isinstance(coverage, dict):
            add_error(errors, f"测试覆盖.{api}", "must be an object")
            continue
        for node_name in FIXED_COVERAGE_NODES:
            if node_name not in coverage:
                add_error(errors, f"测试覆盖.{api}", f"missing fixed node {node_name}")
        if "单参数测试" in coverage:
            validate_single_parameter(api, api_info, coverage, errors)
        walk_testcases(coverage, f"测试覆盖.{api}", errors)
        if "多参数组合" in coverage:
            validate_pairwise(api, data, coverage, errors)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Cangjie testcase XMind JSON.")
    parser.add_argument("json_file")
    args = parser.parse_args()

    with open(args.json_file, "r", encoding="utf-8-sig") as handle:
        data = json.load(handle)

    errors = validate(data)
    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("Validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
