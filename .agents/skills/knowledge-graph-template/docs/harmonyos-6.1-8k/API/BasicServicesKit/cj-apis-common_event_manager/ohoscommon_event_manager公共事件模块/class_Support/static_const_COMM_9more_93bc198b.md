### static const COMMON_EVENT_PACKAGE_DATA_CLEARED

```cangjie
public static const COMMON_EVENT_PACKAGE_DATA_CLEARED: String = "usual.event.PACKAGE_DATA_CLEARED"
```

**功能：** 表示用户清除应用包数据。

在设备上指定用户清除应用包数据，将会触发事件通知服务发布该系统公共事件。

> **说明：**
>
> 三方应用只能监听自身应用的数据清理事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_PACKAGE_FIRST_LAUNCH

```cangjie
public static const COMMON_EVENT_PACKAGE_FIRST_LAUNCH: String = "usual.event.PACKAGE_FIRST_LAUNCH"
```

**功能：**（预留事件，暂未支持）应用程序在安装后首次启动。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_PACKAGE_FULLY_REMOVED

```cangjie
public static const COMMON_EVENT_PACKAGE_FULLY_REMOVED: String = "usual.event.PACKAGE_FULLY_REMOVED"
```

**功能：** 表示现有的应用程序包从设备上完全删除的事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_PACKAGE_NEEDS_VERIFICATION

```cangjie
public static const COMMON_EVENT_PACKAGE_NEEDS_VERIFICATION: String = "usual.event.PACKAGE_NEEDS_VERIFICATION"
```

**功能：**（预留事件，暂未支持）当一个包需要被验证时，由系统包验证者发送。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_PACKAGE_REMOVED

```cangjie
public static const COMMON_EVENT_PACKAGE_REMOVED: String = "usual.event.PACKAGE_REMOVED"
```

**功能：** 表示已从设备卸载已安装的应用程序，但应用程序数据保留的公共事件的操作。

在设备指定用户下卸载指定的应用程序包，将会触发事件通知服务发布该系统公共事件。

> **说明：**
>
> 三方应用只能监听自身应用的卸载事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_PACKAGE_REPLACED

```cangjie
public static const COMMON_EVENT_PACKAGE_REPLACED: String = "usual.event.PACKAGE_REPLACED"
```

**功能：**（预留事件，暂未支持）表示设备上安装了新版本的应用程序包并替换了旧版本的动作。数据包含包的名称。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_PACKAGE_RESTARTED

```cangjie
public static const COMMON_EVENT_PACKAGE_RESTARTED: String = "usual.event.PACKAGE_RESTARTED"
```

**功能：** 表示用户重启应用包并终止其所有进程。

在设备上指定用户重启应用包并终止其所有进程，将会触发事件通知服务发布该系统公共事件。

> **说明：**
>
> 三方应用只能监听自身应用的重启事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_PACKAGE_VERIFIED

```cangjie
public static const COMMON_EVENT_PACKAGE_VERIFIED: String = "usual.event.PACKAGE_VERIFIED"
```

**功能：**（预留事件，暂未支持）当一个包被验证时，由系统包验证者发送。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_POWER_CONNECTED

```cangjie
public static const COMMON_EVENT_POWER_CONNECTED: String = "usual.event.POWER_CONNECTED"
```

**功能：** 设备连接到外部电源的公共事件的动作。

当设备连接到外部可识别的充电器类型充电时，将会触发事件通知服务发布该系统公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22