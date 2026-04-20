### static const COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_UUID_VALUE

```cangjie
public static const COMMON_EVENT_BLUETOOTH_REMOTEDEVICE_UUID_VALUE: String = "usual.event.bluetooth.remotedevice.UUID_VALUE"
```

**功能：** 远程蓝牙设备UUID连接状态公共事件的动作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_BOOT_COMPLETED

```cangjie
public static const COMMON_EVENT_BOOT_COMPLETED: String = "usual.event.BOOT_COMPLETED"
```

**功能：** 表示用户已完成引导并加载系统的公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_BUNDLE_REMOVED

```cangjie
public static const COMMON_EVENT_BUNDLE_REMOVED: String = "usual.event.BUNDLE_REMOVED"
```

**功能：** 表示现有的应用程序包从设备中移除的事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_CALL_STATE_CHANGED

```cangjie
public static const COMMON_EVENT_CALL_STATE_CHANGED: String = "usual.event.CALL_STATE_CHANGED"
```

**功能：** 提示呼叫状态更新。

在设备呼叫状态更新时，将会触发事件通知服务发布该系统公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_CHARGE_IDLE_MODE_CHANGED

```cangjie
public static const COMMON_EVENT_CHARGE_IDLE_MODE_CHANGED: String = "usual.event.CHARGE_IDLE_MODE_CHANGED"
```

**功能：** 表示设备进入充电空闲模式的公共事件的动作。

当设备处于空闲、正在充电并且温升可接受的一种状态时，将会触发事件通知服务发布该系统公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_CHARGING

```cangjie
public static const COMMON_EVENT_CHARGING: String = "usual.event.CHARGING"
```

**功能：** 表示系统开始为电池充电的公共事件的动作。

当系统开始为电池充电时，将会触发事件通知服务发布该系统公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_CLOSE_SYSTEM_DIALOGS

```cangjie
public static const COMMON_EVENT_CLOSE_SYSTEM_DIALOGS: String = "usual.event.CLOSE_SYSTEM_DIALOGS"
```

**功能：**（预留事件，暂未支持）表示用户关闭临时系统对话框的公共事件的动作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_CONFIGURATION_CHANGED

```cangjie
public static const COMMON_EVENT_CONFIGURATION_CHANGED: String = "usual.event.CONFIGURATION_CHANGED"
```

**功能：**（预留事件，暂未支持）表示设备状态（例如，方向和区域设置）已更改的公共事件的操作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_CONNECTIVITY_CHANGE

```cangjie
public static const COMMON_EVENT_CONNECTIVITY_CHANGE: String = "usual.event.CONNECTIVITY_CHANGE"
```

**功能：** 指示网络连接状态变化。

各类网络（以太网、Wi-Fi、蜂窝等）在发生连接状态状态变化时（断开、断开中、连接中、已连接等），将会触发事件通知服务发布该系统公共事件。
具体枚举值及其对应的连接状态如下表所示：

| 枚举值  |  连接状态  |
| ------ | ---------- |
|    2   |   连接中   |
|    3   |   已连接   |
|    4   |   正在断开 |
|    5   |   已断开   |

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22