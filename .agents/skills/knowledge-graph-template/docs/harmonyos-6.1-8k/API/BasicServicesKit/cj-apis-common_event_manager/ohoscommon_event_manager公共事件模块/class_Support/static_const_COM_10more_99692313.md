### static const COMMON_EVENT_DATE_CHANGED

```cangjie
public static const COMMON_EVENT_DATE_CHANGED: String = "usual.event.DATE_CHANGED"
```

**功能：**（预留事件，暂未支持）表示系统日期已更改的公共事件的动作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_DEVICE_IDLE_MODE_CHANGED

```cangjie
public static const COMMON_EVENT_DEVICE_IDLE_MODE_CHANGED: String = "usual.event.DEVICE_IDLE_MODE_CHANGED"
```

**功能：** 表示设备上待机状态变化，触发公共事件发布动作。

如果用户一段时间没有使用设备且屏幕已经关闭情况下，系统延迟后台应用程序CPU和网络访问，将会触发公共事件服务发布该系统公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_DISCHARGING

```cangjie
public static const COMMON_EVENT_DISCHARGING: String = "usual.event.DISCHARGING"
```

**功能：** 表示系统停止为电池充电的公共事件的动作。

当系统停止为电池充电时，将会触发事件通知服务发布该系统公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_DISK_BAD_REMOVAL

```cangjie
public static const COMMON_EVENT_DISK_BAD_REMOVAL: String = "usual.event.data.DISK_BAD_REMOVAL"
```

**功能：**（预留事件，暂未支持）外部存储设备状态变更为挂载状态下移除时发送此公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_DISK_EJECT

```cangjie
public static const COMMON_EVENT_DISK_EJECT: String = "usual.event.data.DISK_EJECT"
```

**功能：**（预留事件，暂未支持）用户已表示希望删除外部存储介质时发送此公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_DISK_MOUNTED

```cangjie
public static const COMMON_EVENT_DISK_MOUNTED: String = "usual.event.data.DISK_MOUNTED"
```

**功能：**（预留事件，暂未支持）外部存储设备状态变更为挂载时发送此公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_DISK_REMOVED

```cangjie
public static const COMMON_EVENT_DISK_REMOVED: String = "usual.event.data.DISK_REMOVED"
```

**功能：**（预留事件，暂未支持）外部存储设备状态变更为移除时发送此公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_DISK_UNMOUNTABLE

```cangjie
public static const COMMON_EVENT_DISK_UNMOUNTABLE: String = "usual.event.data.DISK_UNMOUNTABLE"
```

**功能：**（预留事件，暂未支持）外部存储设备状态变更为插卡情况下无法挂载时发送此公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_DISK_UNMOUNTED

```cangjie
public static const COMMON_EVENT_DISK_UNMOUNTED: String = "usual.event.data.DISK_UNMOUNTED"
```

**功能：**（预留事件，暂未支持）外部存储设备状态变更为卸载时发送此公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGIN

```cangjie
public static const COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGIN: String = "common.event.DISTRIBUTED_ACCOUNT_LOGIN"
```

**功能：** 表示分布式账号登录成功的动作。

分布式账号登录成功时会触发事件通知服务发布该系统公共事件，事件携带系统账号ID。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22