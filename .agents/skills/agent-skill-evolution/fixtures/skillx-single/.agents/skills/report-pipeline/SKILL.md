---
name: report-pipeline
description: "当用户要求把 CSV 数据转换成 JSON 报告时使用此 Skill，指导 Agent 执行报告转换与交付。"
---

# Report Pipeline

## Workflow

1. Run `python tools/report_tool.py --input data.csv --target report.json`.
2. Deliver the generated report.
