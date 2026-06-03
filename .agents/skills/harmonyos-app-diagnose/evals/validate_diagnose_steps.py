import json
import re
import sys


Requirement = tuple[str, list[str]]


COMMON_REQUIREMENTS: list[Requirement] = [
    ("确认设备连接", [r"hdc\s+list\s+targets", r"确认.*设备", r"设备.*连接"]),
    ("安装或确认应用", [r"--hap", r"hdc\s+install\s+-r", r"\.hap", r"安装最新", r"确认已安装", r"应用已安装", r"最新构建"]),
    ("UI 采集入口", [r"ui_capture\.py", r"截图.*控件树", r"控件树.*截图", r"手动采集"]),
    ("采集截图", [r"screenshot\.(?:png|jpe?g)", r"截图", r"snapshot_display", r"screenCap"]),
    ("采集控件树", [r"layout\.json", r"控件树", r"dumpLayout"]),
    ("生成 UI 摘要", [r"ui_summary\.md", r"统计摘要", r"UI\s*摘要", r"摘要"]),
    ("采集 hilog", [r"\bhilog\b", r"运行日志", r"日志采集"]),
    ("清空旧 hilog", [r"hilog\s+-r", r"清空.*hilog", r"清理.*日志"]),
    ("导出全量 hilog", [r"hilog\s+-x", r"hilog_full\.txt", r"全量.*hilog", r"全量.*日志", r"抓取.*hilog"]),
    ("提取错误 hilog", [r"hilog\s+-L\s+[EFW](?:\s+-x)?", r"hilog_error\.txt", r"ERROR.*FATAL", r"FATAL.*ERROR", r"错误.*日志"]),
    ("日志优先级", [r"FATAL", r"ERROR", r"WARN", r"致命", r"错误"]),
    ("截图控件树日志三重验证", [r"截图.*控件树.*(?:hilog|日志)", r"控件树.*截图.*(?:hilog|日志)", r"三重验证", r"交叉验证"]),
    ("报告当前状态", [r"当前状态", r"运行健康", r"界面表现", r"状态"]),
    ("报告日志摘要", [r"运行日志摘要", r"日志摘要", r"hilog.*摘要", r"日志.*关键", r"级别分布"]),
    ("报告发现或根因", [r"发现的问题", r"关键发现", r"根因", r"定位原因", r"错误摘要"]),
    ("报告迭代建议", [r"迭代建议", r"下一步建议", r"修复建议", r"建议"]),
]


CASE_REQUIREMENTS: dict[str, list[Requirement]] = {
    "white-screen-full-flow": [
        ("白屏现象", [r"白屏"]),
        ("关键控件检查", [r"关键控件", r"控件完整", r"控件缺失", r"bundleName"]),
        ("桌面或目标包校验", [r"目标\s*bundle", r"bundleName", r"控件树无目标", r"桌面"]),
    ],
    "crash-sigsegv-full-flow": [
        ("SIGSEGV 识别", [r"SIGSEGV", r"Signal\s*:?\s*11", r"SIGABRT"]),
        ("堆栈分析", [r"堆栈", r"stack", r"调用栈"]),
        ("源码定位", [r"源码", r"源代码", r"源码位置", r"函数名", r"符号"]),
        ("崩溃前日志窗口", [r"0\.5\s*-\s*2", r"0\.5", r"2\s*秒", r"崩溃前", r"触发.*前后"]),
    ],
    "interaction-button-full-flow": [
        ("自动场景", [r"auto_scenario\.json", r"--scenario", r"自动.*场景", r"场景"]),
        ("点击动作", [r"\bclick\b", r"点击"]),
        ("断言检查", [r"断言", r"\bassert"]),
        ("交互后快照", [r"after[/\\]screenshot", r"after", r"交互后"]),
        ("差异数据", [r"diff\.json", r"差异"]),
        ("交互报告", [r"interaction_report\.md", r"交互验证报告", r"交互报告"]),
    ],
    "ui-health-full-flow": [
        ("布局合理性", [r"布局", r"重叠", r"溢出", r"截断", r"留白"]),
        ("触控尺寸", [r"48x48", r"48×48", r"48\s*x\s*48", r">=\s*48", r"48vp", r"点击区域", r"点击热区"]),
        ("字体尺寸", [r"14fp", r"18fp", r"字号", r"字体"]),
        ("运行时健康", [r"运行时健康", r"ERROR/FATAL", r"无.*ERROR", r"无.*FATAL"]),
        ("无需改动", [r"无需改动", r"确认正常"]),
    ],
    "anr-full-flow": [
        ("ANR 识别", [r"ANR", r"Application Not Responding"]),
        ("主线程阻塞", [r"主线程", r"阻塞", r"耗时操作"]),
        ("准确时间点", [r"准确.*时间", r"出现.*时间", r"时间点", r"前后日志"]),
        ("异步化建议", [r"异步", r"耗时操作", r"线程", r"任务拆分"]),
    ],
}


def main() -> None:
    payload = json.loads(sys.stdin.read() or "{}")
    case_id = str(payload.get("case_id") or "")
    output = str(payload.get("output") or "")

    requirements = COMMON_REQUIREMENTS + CASE_REQUIREMENTS.get(case_id, [])
    passed: list[str] = []
    missing: list[str] = []
    for label, patterns in requirements:
        if any(_search(pattern, output) for pattern in patterns):
            passed.append(label)
        else:
            missing.append(label)

    score = len(passed) / len(requirements) if requirements else 0.0
    print(
        json.dumps(
            {
                "score": score,
                "reason": "ok" if not missing else "missing: " + ", ".join(missing),
                "metrics": {
                    "case_id": case_id,
                    "passed": passed,
                    "missing": missing,
                    "required_count": len(requirements),
                },
            },
            ensure_ascii=False,
        )
    )


def _search(pattern: str, text: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL) is not None


if __name__ == "__main__":
    main()
