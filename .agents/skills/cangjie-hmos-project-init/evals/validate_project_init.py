import json
import sys
from pathlib import Path


EXPECTATIONS = {
    "init-default-myapplication": {
        "project_name": "MyApplication",
        "bundle_name": "com.example.myapplication",
        "allow_default_bundle": True,
    },
    "init-custom-bookshelf": {
        "project_name": "BookShelf",
        "bundle_name": "com.acme.bookshelf",
        "allow_default_bundle": False,
    },
}

REQUIRED_FILES = [
    ".gitignore",
    "build-profile.json5",
    "code-linter.json5",
    "hvigorfile.ts",
    "oh-package.json5",
    "AppScope/app.json5",
    "entry/build-profile.json5",
    "entry/hvigorfile.ts",
    "entry/oh-package.json5",
    "entry/cjpm.toml",
    "entry/cjpm.lock",
    "entry/src/main/module.json5",
    "entry/src/main/cangjie/ability_stage.cj",
    "entry/src/main/cangjie/index.cj",
    "entry/src/main/cangjie/main_ability.cj",
    "entry/src/ohosTest/cangjie/cjpm.toml",
    "entry/src/test/cangjie/cjpm.toml",
    "entry/src/main/resources/base/element/string.json",
    "entry/src/main/resources/base/element/color.json",
    "entry/src/main/resources/base/profile/main_pages.json",
    "entry/src/main/resources/base/media/layered_image.json",
    "entry/src/main/resources/base/media/background.png",
    "entry/src/main/resources/base/media/foreground.png",
    "entry/src/main/resources/base/media/startIcon.png",
    "hvigor/hvigor-config.json5",
]

SOURCE_FILES = [
    "entry/src/main/cangjie/ability_stage.cj",
    "entry/src/main/cangjie/index.cj",
    "entry/src/main/cangjie/main_ability.cj",
]

PNG_FILES = [
    "entry/src/main/resources/base/media/background.png",
    "entry/src/main/resources/base/media/foreground.png",
    "entry/src/main/resources/base/media/startIcon.png",
]


def main() -> None:
    payload = json.loads(sys.stdin.read() or "{}")
    case_id = str(payload.get("case_id") or "")
    workspace_dir = Path(str(payload.get("workspace_dir") or "")).resolve()
    expected = EXPECTATIONS.get(case_id)

    failures: list[str] = []
    metrics: dict[str, object] = {"case_id": case_id}

    if expected is None:
        failures.append(f"unknown case_id: {case_id}")
        finish(failures, metrics)
        return

    project_name = str(expected["project_name"])
    bundle_name = str(expected["bundle_name"])
    project_dir = workspace_dir / project_name
    metrics.update({"project_name": project_name, "bundle_name": bundle_name})

    if not project_dir.is_dir():
        failures.append(f"missing project directory: {project_name}")
        finish(failures, metrics)
        return

    missing_files = [rel for rel in REQUIRED_FILES if not (project_dir / rel).is_file()]
    metrics["required_files"] = len(REQUIRED_FILES)
    metrics["missing_files"] = missing_files
    failures.extend(f"missing file: {rel}" for rel in missing_files)

    app_json = read_text(project_dir / "AppScope/app.json5")
    if app_json is not None:
        if bundle_name not in app_json:
            failures.append(f"AppScope/app.json5 missing bundleName {bundle_name}")
        if not expected["allow_default_bundle"] and "com.example.myapplication" in app_json:
            failures.append("AppScope/app.json5 still contains default bundleName com.example.myapplication")

    module_json = read_text(project_dir / "entry/src/main/module.json5")
    if module_json is not None:
        if "ohos_app_cangjie_entry.MyAbilityStage" not in module_json:
            failures.append("module.json5 missing MyAbilityStage srcEntry")
        if "ohos_app_cangjie_entry.MainAbility" not in module_json:
            failures.append("module.json5 missing MainAbility srcEntry")

    for rel in SOURCE_FILES:
        source = read_text(project_dir / rel)
        if source is None:
            continue
        if "package ohos_app_cangjie_entry" not in source:
            failures.append(f"{rel} missing package ohos_app_cangjie_entry")

    index_source = read_text(project_dir / "entry/src/main/cangjie/index.cj")
    if index_source is not None:
        for marker in ("@Entry", "@Component", "Hello World"):
            if marker not in index_source:
                failures.append(f"index.cj missing {marker}")

    empty_pngs = [rel for rel in PNG_FILES if (project_dir / rel).is_file() and (project_dir / rel).stat().st_size <= 0]
    metrics["empty_pngs"] = empty_pngs
    failures.extend(f"empty png file: {rel}" for rel in empty_pngs)

    finish(failures, metrics)


def read_text(path: Path) -> str | None:
    if not path.is_file():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def finish(failures: list[str], metrics: dict[str, object]) -> None:
    if failures:
        print(
            json.dumps(
                {
                    "score": 0.0,
                    "reason": "; ".join(failures[:12]),
                    "metrics": {**metrics, "failure_count": len(failures)},
                },
                ensure_ascii=False,
            )
        )
        return

    print(json.dumps({"score": 1.0, "reason": "project files ok", "metrics": metrics}, ensure_ascii=False))


if __name__ == "__main__":
    main()
