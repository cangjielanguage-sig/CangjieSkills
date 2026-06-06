# Evolution

## FIX-EVC001: Missing generated resource mapping

Signal in `build.log`:

```text
ERROR EVC001 Missing generated resource mapping
```

Verified fix:

1. Create `config/fixed.txt`.
2. The file content must include `resource mapping synced`.
3. Re-run `python .agents/skills/cangjie-hmos-build/build.py --project-root .`.

Only record the solution after the rerun contains `BUILD SUCCESSFUL`.
