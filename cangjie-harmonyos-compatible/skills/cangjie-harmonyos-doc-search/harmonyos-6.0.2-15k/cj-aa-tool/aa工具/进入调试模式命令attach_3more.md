## 进入调试模式命令（attach）

通过bundleName使指定应用进入调试模式。

```bash
aa attach -b <bundleName>
```

**进入调试模式命令参数列表**

| 参数 | 参数说明              |
| -------- |-------------------|
| -h/--help | 帮助信息。             |
| -b | 必选参数，bundleName。  |

**返回值：**

当应用成功进入调试模式时，返回"attach app debug successfully."；当给定参数不合法时，返回"fail: unknown option."并打印帮助信息。

**错误码：**

| 错误码ID | 错误信息 |
| ------- | -------- |
| 10105001 | Failed to connect to the ability service. |
| 10106001 | The current device is not in developer mode. |
| 10106002 | The target application does not support debug mode. |
| 10103601 | The specified bundleName does not exist. |
| 10108601 | An internal error occurs while attempting to enter/exit debug mode. |

**示例：**

```bash
# 通过bundleName使指定应用进入调试模式
aa attach -b com.example.myapplication
```

## 退出调试模式命令（detach）

通过bundleName使指定应用退出调试模式。

```bash
aa detach -b <bundleName>
```

**退出调试模式命令参数列表**

| 参数 | 参数说明              |
| -------- |-------------------|
| -h/--help | 帮助信息。             |
| -b | 必选参数，bundleName。  |

**返回值：**

当应用成功退出调试模式时，返回"detach app debug successfully."；当给定参数不合法时，返回"fail: unknown option."并打印帮助信息。

**错误码：**

| 错误码ID | 错误信息 |
| ------- | -------- |
| 10105001 | Failed to connect to the ability service.|
| 10106001 | The current device is not in developer mode. |
| 10106002 | The target application does not support debug mode. |
| 10103601 | The specified bundleName does not exist. |
| 10108601 | An internal error occurs while attempting to enter/exit debug mode. |

**示例：**

```bash
# 通过bundleName使指定应用退出调试模式
aa detach -b com.example.myapplication
```

## 等待调试命令（appdebug）

用于设置、取消设置应用等待调试状态，以及获取处于等待调试状态的应用包名和持久化信息。等待调试状态只对debug类型应用生效。appdebug的设置命令只对单个应用生效，当重复设置时，应用包名与持久化状态会替换成最新设置内容。

```bash
aa appdebug -b <bundleName> [-p]
```

**等待调试命令参数列表**

| 参数 | 二级参数 | 参数说明 |
| -------- | -------- | -------- |
| -h/--help | - | 帮助信息。 |
| -b/--bundlename | bundleName | 为指定应用设置等待调试状态。设置时，不会进行包名合法化的校验。 |
| -p/--persist | - | 可选参数；持久化标志位，加入该参数，代表持续设置应用为等待调试状态，无论重启设备、重装应用都可以持续生效；不加入该参数，代表等待调试状态仅可以在重启设备前生效一次。需要和-b参数组合使用，例如：aa&nbsp;appdebug&nbsp;-b&nbsp;&lt;bundleName&gt;&nbsp;-p。 |
| -c/--cancel | - | 取消等待调试状态。 |
| -g/--get | - | 获取等待调试状态的应用包名和持久化信息。 |

**返回值**：

当执行成功时，返回"app debug successfully."；当执行失败时，返回"error: failed to app debug."；当失败原因为非开发者模式时，返回"error: not developer mode."。

**错误码**：

| 错误码ID | 错误信息 |
| ------- | -------- |
| 10105003 | Failed to connect to the app service. |
| 10106001 | The current device is not in developer mode. |
| 10106701 | The target application is not a debug application. |

**示例**：

```bash
# 显示帮助信息
aa appdebug -h

# 为指定应用设置等待调试状态
aa appdebug -b com.example.myapplication [-p]

# 取消等待调试状态
aa appdebug -c

# 获取等待调试状态的应用包名和持久化信息
# 获取信息例： bundle name : com.example.publishsystem, persist : false
aa appdebug -g
```