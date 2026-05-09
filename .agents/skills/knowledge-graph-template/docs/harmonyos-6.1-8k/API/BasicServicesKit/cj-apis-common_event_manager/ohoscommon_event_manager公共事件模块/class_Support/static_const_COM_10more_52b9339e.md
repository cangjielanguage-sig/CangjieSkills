### static const COMMON_EVENT_USER_INFO_UPDATED

```cangjie
public static const COMMON_EVENT_USER_INFO_UPDATED: String = "usual.event.USER_INFO_UPDATED"
```

**功能：** 表示用户信息已更新。

分布式账号信息变更、系统账号头像信息变更、系统账号名称变更将会触发事件通知服务发布该系统公共事件，事件携带系统账号ID。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_USER_REMOVED

```cangjie
public static const COMMON_EVENT_USER_REMOVED: String = "usual.event.USER_REMOVED"
```

**功能：** 表示用户已从系统中删除的公共事件的动作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_USER_STARTED

```cangjie
public static const COMMON_EVENT_USER_STARTED: String = "usual.event.USER_STARTED"
```

**功能：**（预留事件，暂未支持）表示用户已启动的公共事件的动作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_USER_STARTING

```cangjie
public static const COMMON_EVENT_USER_STARTING: String = "usual.event.USER_STARTING"
```

**功能：**（预留事件，暂未支持）表示要启动用户的公共事件的动作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_USER_STOPPED

```cangjie
public static const COMMON_EVENT_USER_STOPPED: String = "usual.event.USER_STOPPED"
```

**功能：**（预留事件，暂未支持）表示用户已停止的公共事件的动作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_USER_STOPPING

```cangjie
public static const COMMON_EVENT_USER_STOPPING: String = "usual.event.USER_STOPPING"
```

**功能：**（预留事件，暂未支持）表示要停止用户的公共事件的动作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_USER_SWITCHED

```cangjie
public static const COMMON_EVENT_USER_SWITCHED: String = "usual.event.USER_SWITCHED"
```

**功能：** 表示用户切换正在发生的公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_USER_UNLOCKED

```cangjie
public static const COMMON_EVENT_USER_UNLOCKED: String = "usual.event.USER_UNLOCKED"
```

**功能：** 表示设备重启后解锁时，当前用户的凭据加密存储已解锁的公共事件的动作。

切换到带有锁屏密码的用户，并且首次解锁会发出触发事件通知服务发布该系统公共事件，事件携带标识该用户的系统账号ID。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_VISIBLE_ACCOUNTS_UPDATED

```cangjie
public static const COMMON_EVENT_VISIBLE_ACCOUNTS_UPDATED: String = "usual.event.data.VISIBLE_ACCOUNTS_UPDATED"
```

**功能：**（预留事件，暂未支持）表示账户可见更改的公共事件的动作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_VOLUME_BAD_REMOVAL

```cangjie
public static const COMMON_EVENT_VOLUME_BAD_REMOVAL: String = "usual.event.data.VOLUME_BAD_REMOVAL"
```

**功能：** 表示外部存储设备状态变更为挂载状态下移除的公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22