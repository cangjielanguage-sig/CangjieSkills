import json
import re
import sys
from typing import Any


Requirement = tuple[str, list[str]]


COMMON_REQUIREMENTS: list[Requirement] = [
    ("提取核心诉求", [r"核心(?:诉求|需求|目标)", r"主要(?:诉求|目标)", r"完整需求分析", r"需求分析", r"需求拆解", r"项目概述", r"目标"]),
    ("输出功能点列表", [r"功能点", r"功能清单", r"功能模块", r"功能需求", r"需求拆解", r"主要功能"]),
    ("识别边界条件", [r"边界条件", r"范围边界", r"边界约束", r"不包含", r"非目标", r"异常", r"边界"]),
    ("列出待确认项", [r"待确认", r"确认项", r"不确定", r"需要确认", r"需确认"]),
    ("页面组件拆分", [r"页面[\/、和与]组件", r"页面.*组件", r"组件.*页面", r"页面拆分", r"组件拆分", r"技术架构", r"架构设计", r"三层架构", r"页面", r"弹窗", r"模块"]),
    ("状态管理方案", [r"状态管理", r"状态装饰器", r"@State", r"@Prop", r"@Link", r"数据状态", r"PushToken", r"token", r"Push Kit", r"PushManager", r"NotificationHelper", r"PushMessageService", r"HMS"]),
    ("布局方案", [r"布局", r"\bColumn\b", r"\bRow\b", r"\bStack\b", r"\bList\b", r"\bGrid\b", r"Notification Kit", r"NotificationHelper", r"通知槽位", r"页面", r"UI 表现", r"ArkUI", r"WantAgent"]),
    ("系统能力依赖", [r"系统能力", r"系统 API", r"系统依赖", r"权限", r"网络", r"路由", r"通知", r"文件", r"设备", r"接口定义", r"数据接口", r"Mock 数据", r"Push Kit", r"Notification Kit", r"HMS", r"WantAgent"]),
    ("数据流说明", [r"数据流", r"数据流转", r"状态流转", r"通信协议", r"通信层", r"设备通信", r"自动刷新", r"REST", r"WebSocket", r"PushToken", r"输入.*输出", r"请求.*响应", r"校验规则", r"路由图", r"联动", r"链路", r"推送"]),
    ("验收标准", [r"验收标准", r"验收定义", r"验收条件", r"可验证", r"验收"]),
    ("功能正确性验收", [r"功能正确", r"正确性", r"功能.*验收", r"功能.*正常", r"功能模块", r"功能点清单", r"核心包含"]),
    ("交互预期验收", [r"交互预期", r"交互", r"点击", r"输入", r"反馈", r"操作", r"控制", r"规格选择", r"加购", r"通知栏", r"WantAgent", r"用户"]),
    ("异常处理验收", [r"异常处理", r"异常", r"错误", r"失败", r"空状态", r"边界场景", r"边界约束", r"边界条件"]),
    ("未决事项或决策依赖", [r"未决事项", r"决策依赖", r"待确认", r"依赖.*决策", r"确认后"]),
    ("确认后移交实现", [r"用户确认后", r"用户确认", r"确认后.*实现", r"移交.*实现", r"实现类\s*Skill", r"进入编码", r"后续实现", r"待确认"]),
]


CASE_REQUIREMENTS: dict[str, list[Requirement]] = {
    "login-page-requirements": [
        ("覆盖手机号登录", [r"手机号", r"手机号码", r"登录页面"]),
        ("覆盖邮箱登录", [r"邮箱", r"邮件", r"登录页面"]),
        ("覆盖登录校验", [r"验证码", r"密码", r"校验", r"格式验证", r"表单验证"]),
        ("覆盖登录表单交互", [r"表单", r"输入框", r"登录按钮", r"切换.*登录", r"登录页面"]),
    ],
    "smart-home-requirements": [
        ("覆盖灯光控制", [r"灯光", r"灯", r"智能家居"]),
        ("覆盖空调控制", [r"空调", r"智能家居"]),
        ("覆盖窗帘控制", [r"窗帘", r"智能家居"]),
        ("覆盖设备在线状态", [r"在线状态", r"离线", r"设备状态", r"状态更新"]),
        ("覆盖控制反馈或同步", [r"状态同步", r"控制反馈", r"实时", r"刷新", r"控制"]),
    ],
    "push-notification-requirements": [
        ("覆盖离线推送", [r"离线推送", r"离线消息"]),
        ("覆盖通知栏展示", [r"通知栏", r"通知展示", r"系统通知", r"Notification Kit"]),
        ("覆盖推送权限或通道", [r"通知权限", r"Push", r"推送通道", r"订阅", r"token"]),
        ("覆盖服务端或数据来源", [r"服务端", r"后端", r"消息源", r"数据来源", r"Push Kit", r"HMS", r"PushToken", r"PushManager", r"PushMessageService"]),
    ],
    "direct-implementation-boundary": [
        ("覆盖图片轮播", [r"图片轮播", r"轮播", r"商品详情页", r"3大模块"]),
        ("覆盖规格选择", [r"规格选择", r"规格", r"商品详情页", r"3大模块"]),
        ("覆盖加购流程", [r"加购", r"购物车", r"商品详情页", r"3大模块"]),
        ("明确不直接进入实现", [r"不(?:直接)?进入实现", r"不写代码", r"先.*确认", r"确认后.*实现", r"移交实现", r"用户确认"]),
    ],
}


FORBIDDEN_OUTPUT: list[Requirement] = [
    ("未输出 ArkTS/Cangjie 实现代码", [r"```(?:arkts|ts|typescript|cangjie|cj)", r"@Entry\s*\n", r"build\s*\(\s*\)\s*\{"]),
    ("未给出构建命令或构建产物判定", [r"\bohpm\s+install\b", r"\bhvigor\b", r"assembleHap", r"build\.py", r"build\.log", r"BUILD SUCCESSFUL", r"\.hap\b"]),
    ("未声称已修改或生成文件", [r"已(?:经)?(?:修改|创建|写入|生成).*(?:文件|代码|页面|组件)", r"我已(?:经)?实现", r"代码已(?:经)?完成"]),
    ("未进行文档检索流程", [r"unified_search\.py", r"search_v3\.py"]),
    ("未进行运行诊断流程", [r"hdc\s+list\s+targets", r"ui_capture\.py", r"\bhilog\s+-", r"控件树.*hilog", r"截图.*hilog"]),
]


FORBIDDEN_TOOL_PATTERNS = [
    r"apply_patch",
    r"\bEdit\b",
    r"\bWrite\b",
    r"\bohpm\s+install\b",
    r"\bhvigor\b",
    r"assembleHap",
    r"build\.py",
    r"ui_capture\.py",
    r"hdc\s+list\s+targets",
    r"\bhilog\b",
    r"unified_search\.py",
    r"search_v3\.py",
]


def main() -> None:
    payload = json.loads(sys.stdin.read() or "{}")
    case_id = str(payload.get("case_id") or "")
    output = str(payload.get("output") or "")[:40000]

    requirements = COMMON_REQUIREMENTS + CASE_REQUIREMENTS.get(case_id, [])
    passed: list[str] = []
    failed: list[str] = []

    for label, patterns in requirements:
        if any(search(pattern, output) for pattern in patterns):
            passed.append(label)
        else:
            failed.append(label)

    for label, patterns in FORBIDDEN_OUTPUT:
        if any(search(pattern, output) for pattern in patterns):
            failed.append(label)
        else:
            passed.append(label)

    forbidden_tool_hits = collect_forbidden_tool_hits(payload)
    if forbidden_tool_hits:
        failed.append("未调用实现/构建/检索/诊断类工具")
    else:
        passed.append("未调用实现/构建/检索/诊断类工具")

    score = len(passed) / (len(passed) + len(failed)) if passed or failed else 0.0
    print(
        json.dumps(
            {
                "score": score,
                "reason": "ok" if not failed else "missing: " + ", ".join(failed),
                "metrics": {
                    "case_id": case_id,
                    "passed": passed,
                    "failed": failed,
                    "forbidden_tool_hits": forbidden_tool_hits,
                    "required_count": len(requirements),
                },
            },
            ensure_ascii=True,
        )
    )


def collect_forbidden_tool_hits(payload: dict[str, Any]) -> list[str]:
    snippets: list[str] = []
    collect_tool_call_snippets(payload.get("tool_calls"), snippets)
    trace = payload.get("trace")
    if isinstance(trace, dict):
        collect_tool_call_snippets(trace.get("tool_calls"), snippets)
        interactions = trace.get("session_interactions")
        if isinstance(interactions, list):
            for item in interactions:
                if not isinstance(item, dict) or item.get("type") != "tool_call":
                    continue
                snippets.append(
                    json.dumps(
                        {
                            "tool": item.get("tool"),
                            "raw_tool": item.get("raw_tool"),
                            "command": item.get("command"),
                            "input": item.get("input"),
                            "status": item.get("status"),
                        },
                        ensure_ascii=False,
                    )
                )

    hits: list[str] = []
    for snippet in snippets:
        for pattern in FORBIDDEN_TOOL_PATTERNS:
            if search(pattern, snippet):
                hits.append(snippet[:200])
                break
    return hits[:10]


def collect_tool_call_snippets(value: Any, snippets: list[str]) -> None:
    if isinstance(value, dict):
        snippets.append(
            json.dumps(
                {
                    "name": value.get("name"),
                    "tool": value.get("tool"),
                    "tool_name": value.get("tool_name"),
                    "command": value.get("command"),
                    "arguments": value.get("arguments"),
                    "input": value.get("input"),
                },
                ensure_ascii=False,
            )
        )
    elif isinstance(value, list):
        for item in value:
            collect_tool_call_snippets(item, snippets)


def search(pattern: str, text: str) -> bool:
    return re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL) is not None


if __name__ == "__main__":
    main()
