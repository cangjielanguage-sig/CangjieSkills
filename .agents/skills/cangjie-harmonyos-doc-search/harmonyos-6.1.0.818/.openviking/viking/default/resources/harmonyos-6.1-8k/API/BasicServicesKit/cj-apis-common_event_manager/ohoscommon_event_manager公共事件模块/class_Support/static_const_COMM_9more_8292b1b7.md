### static const COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOFF

```cangjie
public static const COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOFF: String = "common.event.DISTRIBUTED_ACCOUNT_LOGOFF"
```

**功能：** 表示分布式账号注销的动作。

分布式账号注销成功会时触发事件通知服务发布该系统公共事件，事件携带系统账号ID。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT

```cangjie
public static const COMMON_EVENT_DISTRIBUTED_ACCOUNT_LOGOUT: String = "common.event.DISTRIBUTED_ACCOUNT_LOGOUT"
```

**功能：** 表示分布式账号登出成功的动作。

分布式账号登出时会触发事件通知服务发布该系统公共事件，事件携带系统账号ID。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_DISTRIBUTED_ACCOUNT_TOKEN_INVALID

```cangjie
public static const COMMON_EVENT_DISTRIBUTED_ACCOUNT_TOKEN_INVALID: String = "common.event.DISTRIBUTED_ACCOUNT_TOKEN_INVALID"
```

**功能：** 表示分布式账号token令牌无效的动作。

分布式账号的token令牌无效时会触发事件通知服务发布该系统公共事件，事件携带系统账号ID。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_DRIVE_MODE

```cangjie
public static const COMMON_EVENT_DRIVE_MODE: String = "common.event.DRIVE_MODE"
```

**功能：**（预留事件，暂未支持）表示系统处于驾驶模式的公共事件的动作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_EXTERNAL_APPLICATIONS_AVAILABLE

```cangjie
public static const COMMON_EVENT_EXTERNAL_APPLICATIONS_AVAILABLE: String = "usual.event.EXTERNAL_APPLICATIONS_AVAILABLE"
```

**功能：**（预留事件，暂未支持）表示安装在外部存储上的应用程序对系统可用的公共事件的操作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_EXTERNAL_APPLICATIONS_UNAVAILABLE

```cangjie
public static const COMMON_EVENT_EXTERNAL_APPLICATIONS_UNAVAILABLE: String = "usual.event.EXTERNAL_APPLICATIONS_UNAVAILABLE"
```

**功能：**（预留事件，暂未支持）表示安装在外部存储上的应用程序对系统不可用的公共事件的操作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_FOUNDATION_READY

```cangjie
public static const COMMON_EVENT_FOUNDATION_READY: String = "common.event.FOUNDATION_READY"
```

**功能：**（预留事件，暂未支持）表示foundation已准备好的公共事件的动作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_HOME_MODE

```cangjie
public static const COMMON_EVENT_HOME_MODE: String = "common.event.HOME_MODE"
```

**功能：**（预留事件，暂未支持）表示系统处于HOME模式的公共事件的动作。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22

### static const COMMON_EVENT_HTTP_PROXY_CHANGE

```cangjie
public static const COMMON_EVENT_HTTP_PROXY_CHANGE: String = "usual.event.HTTP_PROXY_CHANGE"
```

**功能：** 指示网络Http代理配置信息更新。

在系统全局代理或者各类网络（以太网、Wi-Fi、蜂窝等）Http代理配置信息发生变化时，将会触发事件通知服务发布该系统公共事件。

**类型：** String

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 22