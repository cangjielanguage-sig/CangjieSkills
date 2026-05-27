## 应用调试/调优命令（process）

对应用进行调试或调优，IDE用该命令集成调试和调优工具。

```bash
# 调试应用
aa process -b <bundleName> -a <abilityName> [-m <moduleName>] [-D <debug-cmd>] [-S]

# 调优应用
aa process -b <bundleName> -a <abilityName> [-m <moduleName>] [-p <perf-cmd>] [-S]
```

**应用调试/调优命令参数列表**

| 参数 | 参数说明 |
| -------- | -------- |
| -h/--help | 帮助信息。 |
| -b | 必选参数，bundleName。 |
| -a | 必选参数，abilityName。 |
| -m | 可选参数，moduleName。 |
| -p | 可选参数，调优命令，与-D必须二选一。命令由调用方自定义。 |
| -D | 可选参数，调试命令，与-p必须二选一。命令由调用方自定义。 |
| -S | 可选参数，进入应用沙箱。 |

**返回值**：

当执行成功时，返回"start native process successfully."；当执行失败时，返回"error: failed to start native process."；当给定参数不合法时，返回"error: option requires a value."并打印帮助信息。

| 错误码ID | 错误信息 |
| ------- | -------- |
| 10105002 | Failed to obtain ability information. |
| 10105003 | Failed to connect to the app service. |
| 10106002 | The target application does not support debug mode. |

**示例**：

```bash
# 调试应用
aa process -b com.example.myapplication -a EntryAbility -D debug_cmd [-S]

# 调优应用
aa process -b com.example.myapplication -a EntryAbility -p perf-cmd [-S]
```