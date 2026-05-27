### 10100102 aa start命令无法拉起UIExtensionAbility

**错误信息**

The aa start command cannot be used to launch a UIExtensionAbility.

**错误描述**

aa工具无法拉起UIExtensionAbility。

**可能原因**

aa start命令不支持启动UIExtensionAbility。

**处理步骤**

确认目标Ability是否为UIExtensionAbility，aa start命令无法拉起UIExtensionAbility。

### 10103101 隐式启动未查找到匹配应用

**错误信息**

Failed to find a matching application for implicit launch.

**错误描述**

隐式启动无法查找到匹配的Ability。

**可能原因**

- 如果为隐式启动，可能是启动参数配置有误或指定的HAP包未安装。
- 如果为显式启动，可能是命令中指定了bundleName、却未指定abilityName。

**处理步骤**

- 指定的HAP如果为隐式启动，需要确保启动参数配置正确，且包已安装。
- 如果为显式启动，需要确保abilityName传参正确。

### 10103102 传入的AppCloneIndex是一个无效值

**错误信息**

The passed appCloneIndex is invalid.

**错误描述**

传入一个无效的AppCloneIndex，返回该错误码。

**可能原因**

aa start命令的参数中携带的AppCloneIndex是一个无效值，则返回该错误码。

**处理步骤**

确认AppCloneIndex是否合法。

### 10106101 上一个Ability未启动完成，先缓存在队列中等待后续启动

**错误信息**

The current ability will be placed in the queue to wait for the previous ability to finish launching.

**错误描述**

需要启动的Ability过多，由于系统处理能力有限，会先将请求缓存在队列中，按照顺序依次处理。

**可能原因**

系统并发大。

**处理步骤**

无需处理，等待启动即可。

### 10106102 启动应用时，设备处于锁屏状态

**错误信息**

The device screen is locked during the application launch.

**错误描述**

启动应用时，设备处于锁屏状态。

**可能原因**

启动应用时无法解锁屏幕。

**处理步骤**

解释屏幕后重新尝试即可。

### 10106103 目标应用为到期众测应用

**错误信息**

The target application is an expired crowdtesting application.

**错误描述**

当目标应用为众测应用并且到达测试期限时，方法将返回该错误码。

**可能原因**

众测应用到期，无法打开。

**处理步骤**

请检查应用是否众测到期，已过有效期的众测应用无法启动。

### 10106105 目标应用被管控

**错误信息**

The target application is under control.

**错误描述**

当目标应用受到应用市场管控时，方法将返回该错误码。

**可能原因**

目标应用疑似存在恶意行为，受到应用市场管控不允许启动。

**处理步骤**

建议卸载该应用。

### 10106106 目标应用被EDM管控

**错误信息**

The target application is managed by EDM.

**错误描述**

当目标应用受到企业设备管理管控时，方法将返回该错误码。

**可能原因**

目标应用被企业管理服务设置为禁止启动。

**处理步骤**

该设备是一个企业设备，目标应用被设置为禁止启动，开发者无法处理。

### 10106107 当前设备不支持使用窗口选项

**错误信息**

The current device does not support using window options.

**错误描述**

尝试使用窗口选项但设备不支持。

**可能原因**

用户使用aa start命令指定了WindowOptions，但设备不支持。

**处理步骤**

删除aa start命令中代表WindowOptions的参数wl、wt、wh、ww后重试。

### 10107102 指定的进程权限校验失败

**错误信息**

Permission verification failed for the specified process.

**错误描述**

当指定的进程权限校验失败时，方法将返回该错误码。

**可能原因**

指定的进程权限校验失败。

**处理步骤**

确认指定进程的权限是否正确。