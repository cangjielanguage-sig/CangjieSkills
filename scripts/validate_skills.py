#!/usr/bin/env python3
"""Validate the release structure and run the repository test gates."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tomllib
from pathlib import Path
from urllib.parse import unquote


sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / ".agents" / "skills"
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
SECRET = re.compile(r"(?<![A-Za-z0-9])sk-[A-Za-z0-9_-]{16,}")
TEXT_SUFFIXES = {
    ".cj",
    ".css",
    ".html",
    ".json",
    ".json5",
    ".md",
    ".py",
    ".toml",
    ".ts",
    ".txt",
    ".xml",
    ".yaml",
    ".yml",
}
IGNORED_PARTS = {".git", "__pycache__", ".pytest_cache"}


def relative(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def text_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file() or any(part in IGNORED_PARTS for part in path.parts):
            continue
        if "data" in path.parts and "docs" in path.parts:
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"LICENSE"}:
            files.append(path)
    return sorted(files)


def parse_frontmatter(path: Path, errors: list[str]) -> dict[str, str] | None:
    text = path.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\r?\n(?P<body>.*?)\r?\n---(?:\r?\n|\Z)", text, re.DOTALL)
    if not match:
        errors.append(f"{relative(path)}: missing or malformed YAML front matter")
        return None
    result: dict[str, str] = {}
    for line in match.group("body").splitlines():
        item = re.fullmatch(r"([A-Za-z_][A-Za-z0-9_-]*):\s*(.+)", line)
        if not item:
            errors.append(f"{relative(path)}: unsupported front-matter line: {line!r}")
            continue
        key, raw = item.groups()
        if key in result:
            errors.append(f"{relative(path)}: duplicate front-matter key: {key}")
            continue
        if raw.startswith('"'):
            try:
                value = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"{relative(path)}: invalid quoted {key}: {exc}")
                continue
        else:
            value = raw.strip()
        if not isinstance(value, str):
            errors.append(f"{relative(path)}: {key} must be text")
            continue
        result[key] = value
    return result


def validate_structure(errors: list[str]) -> None:
    for name in ("README.md", "config/README.md", "config/cangjie.skills.toml", "LICENSE"):
        if not (REPO_ROOT / name).is_file():
            errors.append(f"missing repository file: {name}")
    if not SKILLS_ROOT.is_dir():
        errors.append("missing skill root: .agents/skills")
        return
    skills = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    if not skills:
        errors.append("no skills found under .agents/skills")
    for skill in skills:
        skill_file = skill / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{relative(skill)}: missing SKILL.md")
            continue
        frontmatter = parse_frontmatter(skill_file, errors)
        if frontmatter is None:
            continue
        unknown = sorted(set(frontmatter) - {"name", "description"})
        if unknown:
            errors.append(f"{relative(skill_file)}: unsupported front-matter keys: {', '.join(unknown)}")
        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "").strip()
        if name != skill.name:
            errors.append(f"{relative(skill_file)}: name {name!r} must match directory {skill.name!r}")
        if not SKILL_NAME.fullmatch(name):
            errors.append(f"{relative(skill_file)}: invalid skill name {name!r}")
        if not description:
            errors.append(f"{relative(skill_file)}: description must not be blank")
        if len(description) > 1024:
            errors.append(f"{relative(skill_file)}: description exceeds 1024 characters")
        if (skill / "agents" / "openai.yaml").exists():
            errors.append(f"{relative(skill)}: agents/openai.yaml is not part of this release")
    stdx_tool = SKILLS_ROOT / "harmonyos-project-bootstrap" / "tools" / "setup_harmonyos_stdx.py"
    if not stdx_tool.is_file():
        errors.append(f"missing HarmonyOS stdx tool: {relative(stdx_tool)}")
    for obsolete in (
        SKILLS_ROOT / "cangjie-coding" / "scripts" / "setup_stdx.py",
        SKILLS_ROOT / "cangjie-coding" / "scripts" / "stdx_setup",
        SKILLS_ROOT / "harmonyos-build-run-diagnose" / "tools" / "setup_harmonyos_stdx.py",
    ):
        if obsolete.exists() and (obsolete.is_file() or any(obsolete.iterdir())):
            errors.append(f"obsolete stdx implementation must not be released: {relative(obsolete)}")


def validate_links(files: list[Path], errors: list[str]) -> None:
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        for raw in MARKDOWN_LINK.findall(text):
            target = raw.strip().strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            resolved = (path.parent / unquote(target)).resolve()
            if not resolved.exists():
                errors.append(f"{relative(path)}: broken local link: {raw}")


def validate_sources(files: list[Path], errors: list[str]) -> None:
    stale_coordinator_name = "harmonyos-" + "cangjie-dev"
    for path in files:
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        if SECRET.search(text):
            errors.append(f"{relative(path)}: possible plaintext API key")
        if stale_coordinator_name in text:
            errors.append(f"{relative(path)}: stale coordinator name {stale_coordinator_name}")
        if path.suffix.lower() == ".md" and re.search(r"(?m)^\s*python (?!-B\b)", text):
            errors.append(f"{relative(path)}: documented Python commands must use `python -B`")
        if path.suffix.lower() == ".py":
            try:
                compile(text, str(path), "exec")
            except SyntaxError as exc:
                errors.append(f"{relative(path)}:{exc.lineno}: Python syntax error: {exc.msg}")
    tracked = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
    ).stdout.decode("utf-8", errors="replace").split("\0")
    for name in tracked:
        parts = Path(name).parts
        if "__pycache__" in parts or ".pytest_cache" in parts or name.endswith(".pyc"):
            errors.append(f"generated cache must not be tracked: {name}")


def validate_config(errors: list[str]) -> None:
    example = REPO_ROOT / "config" / "cangjie.skills.toml"
    try:
        tomllib.loads(example.read_text(encoding="utf-8-sig"))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        errors.append(f"cangjie.skills.toml: invalid TOML: {exc}")
        return

    tools = SKILLS_ROOT / "cangjie-harmonyos-dev" / "tools"
    sys.path.insert(0, str(tools))
    try:
        from config_loader import load_harmony_config, supported_config_keys

        loaded = load_harmony_config(config_paths=[example])
        if loaded.loaded_files != [example.resolve()]:
            errors.append("cangjie.skills.toml: canonical example was not loaded")
        documentation = (REPO_ROOT / "config" / "README.md").read_text(encoding="utf-8-sig")
        for key in supported_config_keys():
            if f"`{key}`" not in documentation:
                errors.append(f"config/README.md: missing public key `{key}`")
    except Exception as exc:  # noqa: BLE001 - aggregate an actionable release error
        errors.append(f"configuration contract failed: {exc}")
    finally:
        if sys.path and sys.path[0] == str(tools):
            sys.path.pop(0)


def validate_release_data(errors: list[str]) -> None:
    index = SKILLS_ROOT / "cangjie-harmonyos-knowledge" / "data" / "index.sqlite"
    if not index.is_file():
        errors.append(f"missing packaged knowledge index: {relative(index)}")
        return
    prefix = index.read_bytes()[:128]
    if not prefix.startswith(b"SQLite format 3\x00"):
        errors.append(f"{relative(index)}: not a SQLite database")


def run(command: list[str]) -> None:
    print(f"\n> {' '.join(command)}", flush=True)
    environment = os.environ.copy()
    environment["PYTHONDONTWRITEBYTECODE"] = "1"
    subprocess.run(command, cwd=REPO_ROOT, check=True, env=environment)


def run_full_tests() -> None:
    test_roots = sorted({path.parent for path in SKILLS_ROOT.glob("*/tests/test_*.py")})
    for tests in test_roots:
        if tests.parent.name == "cangjie-harmonyos-knowledge":
            continue
        run([sys.executable, "-m", "unittest", "discover", "-s", str(tests), "-p", "test_*.py", "-v"])

    knowledge = SKILLS_ROOT / "cangjie-harmonyos-knowledge"
    run([sys.executable, str(knowledge / "scripts" / "run_tests.py"), "--help"])
    run([sys.executable, str(knowledge / "scripts" / "run_tests.py")])
    run([sys.executable, str(knowledge / "scripts" / "knowledge.py"), "doctor", "--strict"])
    evaluation_gates = (
        ("retrieval.json", "1.0"),
        ("holdout.json", "0.90"),
        # Offline semantic retrieval is a diagnostic floor, not the online
        # embedding quality target. Keeping it explicit prevents accidental
        # claims that deterministic fallback is a semantic model.
        ("semantic.json", "0.40"),
        ("ood.json", "1.0"),
        ("agent_patterns.json", "1.0"),
    )
    for cases_name, fail_under in evaluation_gates:
        run([
            sys.executable,
            str(knowledge / "scripts" / "evaluate.py"),
            "--cases",
            str(knowledge / "tests" / "cases" / cases_name),
            "--embedding-mode",
            "off",
            "--fail-under",
            fail_under,
            "--max-p95-ms",
            "750",
        ])

    coding = SKILLS_ROOT / "cangjie-coding" / "scripts"
    run([sys.executable, str(coding / "search_docs.py"), "--query", "ArrayList add", "--max-results", "1", "--json"])
    run([
        sys.executable,
        str(SKILLS_ROOT / "harmonyos-project-bootstrap" / "tools" / "setup_harmonyos_stdx.py"),
        "--help",
    ])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full", action="store_true", help="also run unit, health, and retrieval tests")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    files = text_files()
    validate_structure(errors)
    validate_links(files, errors)
    validate_sources(files, errors)
    validate_config(errors)
    validate_release_data(errors)
    if errors:
        print("Validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Static validation passed: {len(list(SKILLS_ROOT.iterdir()))} skills, {len(files)} text/code files.")
    if args.full:
        try:
            run_full_tests()
        except subprocess.CalledProcessError as exc:
            print(f"Full validation failed with exit code {exc.returncode}.", file=sys.stderr)
            return exc.returncode or 1
        print("Full validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
