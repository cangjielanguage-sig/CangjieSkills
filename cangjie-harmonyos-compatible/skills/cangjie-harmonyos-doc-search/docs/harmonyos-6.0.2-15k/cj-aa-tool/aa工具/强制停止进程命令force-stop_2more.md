## 强制停止进程命令（force-stop）

通过bundleName强制停止一个进程。

```bash
aa force-stop <bundleName>
```

**返回值：**

当成功强制停止该进程时，返回"force stop process successfully."；当强制停止失败时，返回"error: failed to force stop process."。

**错误码：**

| 错误码ID | 错误信息 |
| ------- | -------- |
| 10105001 | Failed to connect to the ability service. |
| 10104002 | Failed to retrieve specified package information. |
| 10106401 | Failed to terminate the process. |
| 10106402 | Persistent processes cannot be terminated. |

**示例：**

```bash
# 通过bundleName强制停止一个进程
aa force-stop com.example.myapplication
```

## 启动测试框架命令（test）

根据所携带的参数启动测试框架。

```bash
aa test -b <bundleName> [-m <module-name>] [-p <package-name>] [-s class <test-class>] [-s level <test-level>] [-s size <test-size>] [-s testType <test-testType>] [-s timeout <test-timeout>] [-s <any-key> <any-value>] [-w <wait-time>] -s unittest <testRunner>
```

> **说明：**
>
> 关于class、level、size、testType等参数的详细说明请参见[aa test命令执行配置参数](../application-test/cj-arkxtest-guidelines.md#在cmd执行)。

**启动测试框架命令参数列表**

| 参数 | 参数说明 |
| -------- | -------- |
| -h/--help | 帮助信息。 |
| -b | 必选参数，bundleName。 |
| -s unittest | 必选参数，testRunner。 |
| -m | 可选参数，testRunner的moduleName。<br>**说明**：该可选参数仅可在Stage模型下使用。 |
| -s class | 可选参数，指定要执行的测试套或测试用例。 |
| -s level | 可选参数，指定要执行用例的用例级别。 |
| -s size | 可选参数，指定要执行用例的用例规模。 |
| -s testType | 可选参数，指定要执行用例的用例类型。 |
| -s timeout | 可选参数，测试用例执行的超时时间（单位ms），默认为5000。 |
| -s \<any-key> | 可选参数，任意键值对。 |
| -w | 可选参数，指定测试运行时间（单位ms）。 |
| -D | 可选参数，调试模式。 |

**返回值**：

当成功启动测试框架时，返回"user test started."；当启动失败时，返回"error: failed to start user test."和对应的错误信息。

**错误码**：

| 错误码ID | 错误信息 |
| ------- | -------- |
| 10104002 | Failed to retrieve specified package information. |
| 10105001 | Failed to connect to the ability service. |
| 10106002 | The target application does not support debug mode. |
| 10108501 | An internal error occurs during the execution of the aa test command. |

**示例**：

```bash
# 启动测试框架
aa test -b com.example.myapplication -s unittest ActsAbilityTest
# 启动测试框架并设置moduleName
aa test -b com.example.myapplication -m entry_test -s unittest ActsAbilityTest
# 启动测试框架并指定超时时间
aa test -b com.example.myapplication -m entry_test -s timeout 10000 -s unittest ActsAbilityTest
```