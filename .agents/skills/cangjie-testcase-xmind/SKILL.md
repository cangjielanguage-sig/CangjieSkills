---
name: cangjie-testcase-xmind
description: Generate Cangjie API test case JSON and XMind mind maps from structured interface and parameter information. Use when Codex needs to design Cangjie test cases, fill multi-parameter cases with Pair-wise coverage, validate the fixed testcase mind-map schema, or convert testcase JSON into a .xmind file.
---

# Cangjie Testcase XMind

## Overview

Create Cangjie API testcase mind maps by first producing structured JSON, then validating it, then converting it to `.xmind`. Keep this skill focused on testcase design and final mind-map output; do not recreate the full CIDA three-stage workflow unless the user explicitly asks for it.

## Workflow

1. Gather the component name, interface list, parameters, return values, exceptions, permissions, and any known special or combined scenarios.
2. Draft the testcase JSON using the required fixed schema. Read `references/xmind-format.md` before writing or repairing JSON, because it contains the exact Chinese node names.
3. Fill every multi-parameter case group with Pair-wise cases when the API has enough concrete parameter values. Read `references/pairwise.md` and use `scripts/generate_pairwise_cases.py` when deterministic generation is useful.
4. Validate the JSON before conversion:
   ```bash
   python scripts/validate_testcase_xmind_json.py path/to/testcase.json
   ```
5. Convert valid JSON to XMind:
   ```bash
   python scripts/json_to_xmind.py path/to/testcase.json path/to/testcase.xmind
   ```
6. Inspect the generated `.xmind` archive when needed by checking `content.xml` for expected node titles.

## JSON Design Rules

- Use one top-level component or module name.
- Keep the two top-level children and the seven fixed coverage nodes exactly as documented in `references/xmind-format.md`.
- Make interface names match exactly between the interface list and coverage sections.
- Use testcase entries with only two fields: the test flow field and the expected result field documented in `references/xmind-format.md`.
- Do not use generic testcase names such as numbered "case 1" labels; prefer names like `test_<API>_pairwise_case1`.
- Keep not-applicable markers as leaf nodes.

## Bundled Tools

- `scripts/generate_pairwise_cases.py`: Generate deterministic Pair-wise testcase JSON for one API.
- `scripts/validate_testcase_xmind_json.py`: Validate schema consistency, testcase shape, and Pair-wise coverage.
- `scripts/json_to_xmind.py`: Convert valid testcase JSON into an XMind-compatible `.xmind` zip.
- `assets/template.xmind`: Reference mind-map template copied from the original CIDA materials.

## Practical Defaults

- Build Pair-wise values from each parameter's default value, valid equivalence values, and special values; ignore empty or not-applicable values.
- If an interface has fewer than two parameters with usable values, or every usable parameter has only one value, mark the multi-parameter case group as not applicable.
- Keep test flow and expected result text concrete. The XMind converter uses those values directly as node titles and omits the field labels themselves.
