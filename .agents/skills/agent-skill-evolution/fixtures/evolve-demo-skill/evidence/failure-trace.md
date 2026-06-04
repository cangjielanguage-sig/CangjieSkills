# Failure Trace T-F1

- Task: update a JSON report.
- Actions: wrote the file and immediately reported success without reading it back.
- Result: the downstream consumer found an empty `items` field.
