# Skill Library Topology Evidence SX-L1

- Build requests and inspection requests use independent trigger phrases and have different maintainers.
- The build half of `ops-suite` semantically duplicates the existing `release-build` Skill.
- Merge useful build knowledge into `release-build`; do not create another build Skill.
- Create `release-inspect` for the inspection capability and remove obsolete `ops-suite` after migration.
- `release-build` produces `dist/manifest.json`.
- `release-inspect` consumes `dist/manifest.json`, but users can request inspection independently for an existing artifact.
- Both resulting Skills require independent discovery and content evals.
