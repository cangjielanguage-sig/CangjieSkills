# HarmonyOS stdx Provisioning

Use the packaged tool only for HarmonyOS Cangjie modules that import `stdx.*`:

```powershell
python -B <harmonyos-project-bootstrap-skill>/tools/setup_harmonyos_stdx.py --project <project>/<module>
```

The default run:

1. Resolves the HarmonyOS Cangjie SDK from `--cangjie-sdk`, `CANGJIE_SDK_HOME`, `toolchain.cangjie_sdk`, or `~/.cangjie-sdk`.
2. Reads the compiler version with the SDK's `build-tools/bin/cjc -v`.
3. Selects the verified stdx release.
4. Installs `ohos-x64` for the x64 emulator and `ohos-aarch64` for ARM64 devices under `~/.cangjie/stdx`.
5. Updates both `cjpm.toml` target tables atomically and preserves unrelated binary dependency paths.

Supported targets are deliberately fixed:

| Release platform | `cjpm.toml` target | Use |
| --- | --- | --- |
| `ohos-x64` | `x86_64-linux-ohos` | x64 emulator |
| `ohos-aarch64` | `aarch64-linux-ohos` | ARM64 device |

No stdx release platform other than these two HarmonyOS targets is in scope. `--platform` may select one ABI for diagnosis; omit it for normal development so both targets remain ready.

Verified compatibility mappings are `1.1.0 → 1.1.0.1`, `1.1.3 → 1.1.3.1`, and `1.2.x → 1.2.0-beta.02.1`. Unknown compiler lines fail instead of guessing. Use `--stdx-version` only for a compatibility override already verified with the active SDK.

For offline setup, place both official archives in one directory and run:

```powershell
python -B <harmonyos-project-bootstrap-skill>/tools/setup_harmonyos_stdx.py `
  --project <project>/<module> `
  --archive-dir <archives> `
  --offline
```

Archive names must follow `cangjie-stdx-ohos-<abi>-<version>.zip`. The tool validates every selected local archive before installing either ABI. It installs all selected payloads before one atomic manifest update, so a missing or invalid second archive cannot leave a half-configured project. A first successful manifest edit creates `cjpm.toml.stdx.bak`; repeated runs are idempotent.

Use `--dry-run --json` to inspect resolution without writes. Use `--force` only to replace a damaged or deliberately refreshed installation. Run `cjpm clean` after changing the stdx version, linkage, or binary path, then rebuild with `harmonyos-build-run-diagnose`.
