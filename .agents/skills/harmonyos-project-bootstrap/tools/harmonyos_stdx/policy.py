"""Cangjie-to-stdx policy for HarmonyOS emulator and device targets only."""

from __future__ import annotations

import re

from .errors import SetupError
from .models import Release, Toolchain


REPOSITORY = "https://gitcode.com/Cangjie/cangjie_stdx"
OHOS_PLATFORMS = ("ohos-x64", "ohos-aarch64")
PLATFORM_TO_TARGET = {
    "ohos-x64": "x86_64-linux-ohos",
    "ohos-aarch64": "aarch64-linux-ohos",
}
RELEASES = {
    "1.1.0.1": Release("1.1.0.1"),
    "1.1.3.1": Release("1.1.3.1"),
    "1.2.0-beta.02.1": Release("1.2.0-beta.02.1"),
}
_CJC_VERSION = re.compile(r"^Cangjie Compiler:\s*([^\s]+)", re.MULTILINE)
_VERSION = re.compile(r"^(\d+)\.(\d+)\.(\d+)([-+][0-9A-Za-z.-]+)?$")


def release_for_cjc(version: str) -> Release:
    match = _VERSION.fullmatch(version)
    if not match:
        raise SetupError(f"unsupported cjc version format: {version!r}")
    core = tuple(int(match.group(index)) for index in range(1, 4))
    if core == (1, 1, 0):
        return RELEASES["1.1.0.1"]
    if core == (1, 1, 3):
        return RELEASES["1.1.3.1"]
    if core[:2] == (1, 2):
        return RELEASES["1.2.0-beta.02.1"]
    raise SetupError(
        f"no HarmonyOS stdx compatibility policy for cjc {version}; "
        "supported compiler lines are 1.1.0, 1.1.3, and 1.2.x"
    )


def release_by_version(version: str) -> Release:
    try:
        return RELEASES[version]
    except KeyError as exc:
        supported = ", ".join(RELEASES)
        raise SetupError(f"unsupported HarmonyOS stdx version {version!r}; supported versions: {supported}") from exc


def parse_cjc_output(output: str) -> Toolchain:
    match = _CJC_VERSION.search(output)
    if not match:
        raise SetupError("cannot parse compiler version from `cjc -v`")
    version = match.group(1)
    return Toolchain(version, release_for_cjc(version))


def require_platform(platform: str) -> str:
    if platform not in PLATFORM_TO_TARGET:
        raise SetupError(
            f"unsupported platform {platform!r}; HarmonyOS setup supports only: "
            f"{', '.join(OHOS_PLATFORMS)}"
        )
    return platform


def target_for_platform(platform: str) -> str:
    return PLATFORM_TO_TARGET[require_platform(platform)]


def asset_name(release: Release, platform: str) -> str:
    require_platform(platform)
    return f"cangjie-stdx-{platform}-{release.version}.zip"


def release_page(release: Release) -> str:
    return f"{REPOSITORY}/releases/v{release.version}"


def asset_url(release: Release, platform: str) -> str:
    return f"{REPOSITORY}/releases/download/v{release.version}/{asset_name(release, platform)}"
