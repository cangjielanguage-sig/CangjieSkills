#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

from itertools import combinations, product
from typing import Any, Dict, Iterable, List, Sequence, Tuple


FIXED_COVERAGE_NODES = [
    "单参数测试",
    "多参数组合",
    "返回值验证",
    "异常处理",
    "权限检查",
    "特殊场景",
    "组合场景",
]

CASE_KEYS = {"测试流程", "预期结果"}
VALUE_CATEGORIES = ["有效等价类", "特殊值"]
NO_DEFAULT_VALUES = {"", "无", "无默认值", "不涉及", "None", "none", "null", "NULL"}


def is_not_applicable(value: Any) -> bool:
    if value == "不涉及":
        return True
    if isinstance(value, dict) and set(value.keys()) == {"不涉及"}:
        child = value.get("不涉及")
        return child in ("", None, "不涉及")
    return False


def normalize_values(raw: Any) -> List[str]:
    values: List[str] = []
    if raw is None:
        return values
    if isinstance(raw, dict):
        iterable: Iterable[Any] = raw.keys()
    elif isinstance(raw, list):
        iterable = raw
    elif isinstance(raw, str):
        if raw.strip() == "不涉及":
            return values
        iterable = [part.strip() for part in raw.split(",")]
    else:
        iterable = [raw]

    for item in iterable:
        text = str(item).strip()
        if text and text != "不涉及" and text not in values:
            values.append(text)
    return values


def first_component(data: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
    if not isinstance(data, dict) or not data:
        raise ValueError("JSON root must be a non-empty object")
    name = next(iter(data.keys()))
    body = data[name]
    if not isinstance(body, dict):
        raise ValueError("Component value must be an object")
    return name, body


def find_interface_map(data: Dict[str, Any]) -> Dict[str, Any]:
    _, body = first_component(data)
    interface_map = body.get("接口列表")
    if not isinstance(interface_map, dict):
        raise ValueError("Missing or invalid 接口列表")
    return interface_map


def extract_parameter_values(data: Dict[str, Any], api: str | None = None) -> Tuple[str, Dict[str, List[str]]]:
    if "parameters" in data:
        api_name = str(data.get("api") or api or "api")
        params = data["parameters"]
        if not isinstance(params, dict):
            raise ValueError("parameters must be an object")
        return api_name, {str(name): normalize_values(values) for name, values in params.items()}

    interface_map = find_interface_map(data)
    api_name = api or (next(iter(interface_map.keys())) if interface_map else None)
    if not api_name:
        raise ValueError("No API name found; pass --api")
    if api_name not in interface_map:
        raise ValueError(f"API not found in 接口列表: {api_name}")

    api_info = interface_map[api_name]
    if not isinstance(api_info, dict):
        raise ValueError(f"接口列表.{api_name} must be an object")
    params = api_info.get("参数", {})
    if is_not_applicable(params):
        return api_name, {}
    if not isinstance(params, dict):
        raise ValueError(f"接口列表.{api_name}.参数 must be an object or 不涉及")

    extracted: Dict[str, List[str]] = {}
    for param_name, param_info in params.items():
        if str(param_name) == "不涉及":
            continue
        values: List[str] = []
        if isinstance(param_info, dict):
            default_value = str(param_info.get("默认值", "")).strip()
            if default_value not in NO_DEFAULT_VALUES:
                values.append(default_value)
            ranges = param_info.get("取值范围", param_info)
            if isinstance(ranges, dict):
                for category in VALUE_CATEGORIES:
                    for value in normalize_values(ranges.get(category)):
                        if value not in values:
                            values.append(value)
        extracted[str(param_name)] = values
    return api_name, extracted


def pairwise_needed(parameters: Dict[str, List[str]]) -> bool:
    usable = [values for values in parameters.values() if values]
    return len(usable) >= 2 and any(len(values) > 1 for values in usable)


def all_required_pairs(parameters: Dict[str, List[str]]) -> set[Tuple[str, str, str, str]]:
    names = [name for name, values in parameters.items() if values]
    required: set[Tuple[str, str, str, str]] = set()
    for left, right in combinations(names, 2):
        for left_value in parameters[left]:
            for right_value in parameters[right]:
                required.add((left, left_value, right, right_value))
    return required


def row_pairs(row: Dict[str, str]) -> set[Tuple[str, str, str, str]]:
    pairs: set[Tuple[str, str, str, str]] = set()
    for left, right in combinations(row.keys(), 2):
        pairs.add((left, row[left], right, row[right]))
    return pairs


def generate_pairwise_rows(parameters: Dict[str, List[str]], max_candidates: int = 200000) -> List[Dict[str, str]]:
    usable = {name: values for name, values in parameters.items() if values}
    if not pairwise_needed(usable):
        return []

    candidate_count = 1
    for values in usable.values():
        candidate_count *= len(values)
    if candidate_count > max_candidates:
        raise ValueError(
            f"Too many Cartesian candidates ({candidate_count}); reduce values or raise --max-candidates"
        )

    names = list(usable.keys())
    candidates = [
        dict(zip(names, values))
        for values in product(*(usable[name] for name in names))
    ]

    uncovered = all_required_pairs(usable)
    selected: List[Dict[str, str]] = []
    used: set[Tuple[str, ...]] = set()

    while uncovered:
        best_row = None
        best_key = None
        best_cover: set[Tuple[str, str, str, str]] = set()
        for row in candidates:
            row_key = tuple(row[name] for name in names)
            if row_key in used:
                continue
            cover = row_pairs(row) & uncovered
            score_key = (-len(cover), row_key)
            if best_row is None or score_key < best_key:
                best_row = row
                best_key = score_key
                best_cover = cover
        if best_row is None or not best_cover:
            raise ValueError("Unable to complete Pair-wise coverage")
        selected.append(best_row)
        used.add(tuple(best_row[name] for name in names))
        uncovered -= best_cover
    return selected


def testcase_from_rows(api: str, rows: Sequence[Dict[str, str]], result: str) -> Dict[str, Dict[str, str]]:
    cases: Dict[str, Dict[str, str]] = {}
    for index, row in enumerate(rows, start=1):
        name = f"test_{api}_pairwise_case{index}"
        flow = ", ".join(f"{param}={value}" for param, value in row.items())
        cases[name] = {
            "测试流程": flow,
            "预期结果": result,
        }
    return cases
