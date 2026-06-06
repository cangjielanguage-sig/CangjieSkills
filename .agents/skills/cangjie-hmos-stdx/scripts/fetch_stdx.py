from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path


DEFAULT_VERSION = "1.1.0-beta.10.1"
RELEASES_API = "https://gitcode.com/api/v5/repos/Cangjie/cangjie_stdx/releases"
RELEASE_PAGE = "https://gitcode.com/Cangjie/cangjie_stdx/releases"
PLATFORM_MARKERS = {
    "x86_64": ("ohos-x86_64", "ohos-x64"),
    "aarch64": ("ohos-aarch64",),
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Download Cangjie stdx OHOS release packages.")
    parser.add_argument(
        "--platform",
        choices=("all", "x86_64", "aarch64"),
        default="all",
        help="Target OHOS package platform.",
    )
    parser.add_argument("--version", default=DEFAULT_VERSION, help="Release version, with or without leading v.")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Directory for downloaded zip files. Defaults to the cangjie-hmos-stdx skill directory.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite an existing zip file.")
    parser.add_argument("--dry-run", action="store_true", help="Print selected assets without downloading.")
    args = parser.parse_args()

    tag = _normalize_tag(args.version)
    platforms = ("x86_64", "aarch64") if args.platform == "all" else (args.platform,)
    release = _find_release(tag)
    assets = [_select_asset(release, platform) for platform in platforms]

    args.out_dir.mkdir(parents=True, exist_ok=True)
    for asset in assets:
        name = asset["name"]
        url = asset["browser_download_url"]
        target = args.out_dir / name
        if args.dry_run:
            print(f"{name}: {url}")
            continue
        if target.exists() and target.stat().st_size > 0 and not args.force:
            print(f"{target} already exists; use --force to overwrite")
            continue
        _download(url, target)
        print(f"downloaded {name} -> {target}")
    return 0


def _normalize_tag(version: str) -> str:
    version = version.strip()
    return version if version.startswith("v") else f"v{version}"


def _find_release(tag: str) -> dict[str, object]:
    releases = _request_json(RELEASES_API)
    if not isinstance(releases, list):
        raise SystemExit(f"Unexpected GitCode releases response. Open {RELEASE_PAGE} and download manually.")
    for release in releases:
        if release.get("tag_name") == tag or release.get("name") == tag:
            return release
    raise SystemExit(f"Release {tag} was not found. Open {RELEASE_PAGE} and download manually.")


def _select_asset(release: dict[str, object], platform: str) -> dict[str, str]:
    assets = release.get("assets")
    if not isinstance(assets, list):
        raise SystemExit(f"Release has no assets. Open {RELEASE_PAGE} and download manually.")
    markers = PLATFORM_MARKERS[platform]
    for marker in markers:
        for asset in assets:
            if not isinstance(asset, dict):
                continue
            name = str(asset.get("name", ""))
            url = str(asset.get("browser_download_url", ""))
            if marker in name and name.endswith(".zip") and url:
                return {"name": name, "browser_download_url": url}
    raise SystemExit(f"No OHOS {platform} zip was found. Open {RELEASE_PAGE} and download manually.")


def _request_json(url: str) -> object:
    request = urllib.request.Request(url, headers={"User-Agent": "cangjie-skills-fetch-stdx/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            data = response.read()
    except urllib.error.URLError as exc:
        raise SystemExit(f"Unable to query GitCode releases: {exc}. Open {RELEASE_PAGE} and download manually.")
    try:
        return json.loads(data.decode("utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Unexpected GitCode releases response: {exc}. Open {RELEASE_PAGE} and download manually.")


def _download(url: str, target: Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": "cangjie-skills-fetch-stdx/1.0"})
    temp = target.with_suffix(target.suffix + ".part")
    try:
        with urllib.request.urlopen(request, timeout=60) as response, temp.open("wb") as handle:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                handle.write(chunk)
        if temp.stat().st_size == 0:
            raise OSError("downloaded file is empty")
        temp.replace(target)
    except (OSError, urllib.error.URLError) as exc:
        try:
            temp.unlink()
        except OSError:
            pass
        raise SystemExit(f"Unable to download {url}: {exc}. Open {RELEASE_PAGE} and download manually.")


if __name__ == "__main__":
    sys.exit(main())
