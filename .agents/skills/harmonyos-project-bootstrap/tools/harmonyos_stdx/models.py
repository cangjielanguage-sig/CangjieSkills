"""Immutable values exchanged between HarmonyOS stdx setup stages."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Release:
    version: str


@dataclass(frozen=True)
class Toolchain:
    version: str
    release: Release


@dataclass(frozen=True)
class PlatformPlan:
    platform: str
    target: str
    linkage: str
    release_page: str
    asset_url: str
    destination: Path
    cache_dir: Path
    installation: Path

    def as_dict(self) -> dict[str, Any]:
        return {
            "platform": self.platform,
            "target": self.target,
            "linkage": self.linkage,
            "release_page": self.release_page,
            "asset_url": self.asset_url,
            "destination": str(self.destination),
            "cache_dir": str(self.cache_dir),
            "installation": str(self.installation),
        }
