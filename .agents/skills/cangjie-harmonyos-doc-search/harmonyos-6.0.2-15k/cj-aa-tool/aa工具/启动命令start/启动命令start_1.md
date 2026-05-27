## 启动命令（start）

启动一个应用组件，目标组件可以是Stage模型的UIAbility或ServiceExtensionAbility组件，且目标组件相应配置文件中的exported标签不能配置为false。

```bash
# 显示启动Ability
aa start [-d <deviceId>] [-a <abilityName> -b <bundleName>] [-m <moduleName>] [-D] [-R] [-S] [--pi <key> <integer-value>] [--pb <key> <bool-value: true/false/t/f大小写不敏感] [--ps <key> <value>] [--psn <key>] [--wl <windowLeft>] [--wt <windowTop>] [--wh <windowHeight>] [--ww <windowWidth>] [-p <perf-cmd>]

# 隐式启动Ability。如果命令中的参数都不填，会导致启动失败。
aa start [-d <deviceId>] [-U <URI>] [-t <type>] [-A <action>] [-e <entity>] [-D] [-R] [--pi <key> <integer-value>] [--pb <key> <bool-value: true/false/t/f大小写不敏感] [--ps <key> <value>] [--psn <key>] [--wl <windowLeft>] [--wt <windowTop>] [--wh <windowHeight>] [--ww <windowWidth>] [-p <perf-cmd>]
```

**启动命令参数列表**

| 参数 | 参数说明    |
| -------- |-------------------|
| -h/--help | 帮助信息。   |
| -d | 可选参数，deviceId。    |
| -a | 可选参数，abilityName。 |
| -b | 可选参数，bundleName。  |
| -m | 可选参数，moduleName。  |
| -U | 可选参数，URI。         |
| -A | 可选参数，action。      |
| -e | 可选参数，entity。      |
| -t | 可选参数，type。        |
| --pi  | 可选参数，整型类型键值对。     |
| --pb  | 可选参数，布尔类型键值对。     |
| --ps  | 可选参数，字符串类型键值对。    |
| --psn | 可选参数，空字符串关键字。     |
| --wl | 可选参数，windowLeft，窗口左边距，单位px。<br>**约束：**<br>仅当2in1设备处于开发者模式下，且被启动应用采用调试签名时，该字段生效。|
| --wt | 可选参数，windowTop，窗口上边距，单位px。<br>**约束：**<br>仅当2in1设备处于开发者模式下，且被启动应用采用调试签名时，该字段生效。|
| --wh | 可选参数，windowHeight，窗口高度，单位px。<br>**约束：**<br>仅当2in1设备处于开发者模式下，且被启动应用采用调试签名时，该字段生效。|
| --ww | 可选参数，windowWidth，窗口宽度，单位px。<br>**约束：**<br>仅当2in1设备处于开发者模式下，且被启动应用采用调试签名时，该字段生效。|
| -R | 可选参数，调试时是否开启多线程错误检测。携带该参数代表开启，不携带代表关闭。|
| -S | 可选参数，调试时是否进入应用沙箱。携带该参数代表进入，不携带代表不进入。 |
| -D | 可选参数，调试模式。 |
| -p | 可选参数，调优命令。命令由调用方自定义。 |

**返回值：**

当启动成功时，返回"start ability successfully."；当启动失败时，返回"error: failed to start ability."，同时会包含相应的失败信息。

**错误码：**

| 错误码ID | 错误信息 |
| ------- | -------- |
| 10103001 | Failed to verify the visibility of the target ability. |
| 10104001 | The specified ability does not exist. |
| 10105001 | Failed to connect to the ability service. |
| 10105002 | Failed to obtain ability information. |
| 10106002 | The target application does not support debug mode. |
| 10100101 | Failed to obtain application information. |
| 10100102 | The aa start command cannot be used to launch a UIExtensionAbility. |
| 10103101 | Failed to find a matching application for implicit launch. |
| 10103102 | The passed appCloneIndex is invalid. |
| 10106101 | The current ability will be placed in the queue to wait for the previous ability to finish launching. |
| 10106102 | The device screen is locked during the application launch. |
| 10106103 | The target application is an expired crowdtesting application. |
| 10106105 | The target application is under control. |
| 10106106 | The target application is managed by EDM. |
| 10106107 | The current device does not support using window options. |
| 10107102 | Permission verification failed for the specified process. |
| 10108101 | An internal error occurs while attempting to launch the ability. |

**示例：**

以隐式启动Ability为例。