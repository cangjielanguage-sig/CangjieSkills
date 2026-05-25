### static const COMMON_EVENT_ENTER_HIBERNATE

```cangjie
public static const COMMON_EVENT_ENTER_HIBERNATE: String = "usual.event.ENTER_HIBERNATE"
```

**功能：** 表示设备即将进入休眠模式的公共事件的动作。当设备即将进入休眠模式时，将会触发事件通知服务发布该系统公共事件。所有订阅者必须在1秒钟内处理该事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**起始版本：** 20

### static const COMMON_EVENT_EXIT_HIBERNATE

```cangjie
public static const COMMON_EVENT_EXIT_HIBERNATE: String = "usual.event.EXIT_HIBERNATE"
```

**功能：** 表示设备即将进入休眠模式的公共事件的动作。当设备退出休眠模式时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**起始版本：** 20

### static const COMMON_EVENT_MINORSMODE_ON

```cangjie
public static const COMMON_EVENT_MINORSMODE_ON: String = "usual.event.MINORSMODE_ON"
```

**功能：** 表示用户开启未成年人模式。在设备上开启未成年人模式，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**起始版本：** 20

### static const COMMON_EVENT_MINORSMODE_OFF

```cangjie
public static const COMMON_EVENT_MINORSMODE_OFF: String = "usual.event.MINORSMODE_OFF"
```

**功能：** 表示用户关闭未成年人模式。在设备上关闭未成年人模式，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**起始版本：** 20

### static const COMMON_EVENT_MANAGED_BROWSER_POLICY_CHANGED

```cangjie
public static const COMMON_EVENT_MANAGED_BROWSER_POLICY_CHANGED: String = "usual.event.MANAGED_BROWSER_POLICY_CHANGED"
```

**功能：** 表示浏览器托管策略已更改。当浏览器托管策略发生变化，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**起始版本：** 20