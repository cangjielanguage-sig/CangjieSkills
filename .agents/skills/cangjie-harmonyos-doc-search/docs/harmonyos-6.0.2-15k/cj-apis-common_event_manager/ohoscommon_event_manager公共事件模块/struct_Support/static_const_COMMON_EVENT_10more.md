### static const COMMON_EVENT_WIFI_P2P_CURRENT_DEVICE_STATE_CHANGED

```cangjie
public static const COMMON_EVENT_WIFI_P2P_CURRENT_DEVICE_STATE_CHANGED: String = "usual.event.wifi.p2p.CURRENT_DEVICE_CHANGE"
```

**功能：** 表示Wi-Fi P2P当前设备状态变化的公共事件。

**订阅者所需权限：** ohos.permission.GET_WIFI_INFO

**类型：** String

**起始版本：** 12

### static const COMMON_EVENT_WIFI_P2P_GROUP_STATE_CHANGED

```cangjie
public static const COMMON_EVENT_WIFI_P2P_GROUP_STATE_CHANGED: String = "usual.event.wifi.p2p.GROUP_STATE_CHANGED"
```

**功能：** 表示Wi-Fi P2P群组信息已更改的公共事件。

**订阅者所需权限：** ohos.permission.GET_WIFI_INFO

**类型：** String

**起始版本：** 12

### static const COMMON_EVENT_WIFI_P2P_PEERS_DISCOVERY_STATE_CHANGED

```cangjie
public static const COMMON_EVENT_WIFI_P2P_PEERS_DISCOVERY_STATE_CHANGED: String = "usual.event.wifi.p2p.PEER_DISCOVERY_STATE_CHANGE"
```

**功能：** 表示Wi-Fi P2P发现状态变化的公共事件。

**订阅者所需权限：** ohos.permission.GET_WIFI_INFO

**类型：** String

**起始版本：** 12

### static const COMMON_EVENT_WIFI_P2P_PEERS_STATE_CHANGED

```cangjie
public static const COMMON_EVENT_WIFI_P2P_PEERS_STATE_CHANGED: String = "usual.event.wifi.p2p.DEVICES_CHANGE"
```

**功能：** 表示Wi-Fi P2P对等体状态变化的公共事件。

**订阅者所需权限：** ohos.permission.GET_WIFI_INFO

**类型：** String

**起始版本：** 12

### static const COMMON_EVENT_WIFI_P2P_STATE_CHANGED

```cangjie
public static const COMMON_EVENT_WIFI_P2P_STATE_CHANGED: String = "usual.event.wifi.p2p.STATE_CHANGE"
```

**功能：** 表示Wi-Fi P2P状态（如启用和禁用）公共事件的公共事件。

**订阅者所需权限：** ohos.permission.GET_WIFI_INFO

**类型：** String

**起始版本：** 12

### static const COMMON_EVENT_WIFI_POWER_STATE

```cangjie
public static const COMMON_EVENT_WIFI_POWER_STATE: String = "usual.event.wifi.POWER_STATE"
```

**功能：** 表示Wi-Fi状态（如启用和禁用）公共事件的公共事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**起始版本：** 12

### static const COMMON_EVENT_WIFI_RSSI_VALUE

```cangjie
public static const COMMON_EVENT_WIFI_RSSI_VALUE: String = "usual.event.wifi.RSSI_VALUE"
```

**功能：** 表示Wi-Fi信号强度（RSSI）改变的公共事件。

**订阅者所需权限：** ohos.permission.GET_WIFI_INFO

**类型：** String

**起始版本：** 12

### static const COMMON_EVENT_WIFI_SCAN_FINISHED

```cangjie
public static const COMMON_EVENT_WIFI_SCAN_FINISHED: String = "usual.event.wifi.SCAN_FINISHED"
```

**功能：** 表示Wi-Fi接入点已被扫描并证明可用的公共事件。

**订阅者所需权限：** ohos.permission.LOCATION

**类型：** String

**起始版本：** 12

### static const COMMON_EVENT_ENTER_FORCE_SLEEP

```cangjie
public static const COMMON_EVENT_ENTER_FORCE_SLEEP: String = "usual.event.ENTER_FORCE_SLEEP"
```

**功能：** 表示设备即将进入强制睡眠模式的公共事件的动作。当设备即将进入强制睡眠模式时，将会触发事件通知服务发布该系统公共事件。所有订阅者必须在1秒钟内处理该事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**起始版本：** 20

### static const COMMON_EVENT_EXIT_FORCE_SLEEP

```cangjie
public static const COMMON_EVENT_EXIT_FORCE_SLEEP: String = "usual.event.EXIT_FORCE_SLEEP"
```

**功能：** 表示设备退出强制睡眠模式的公共事件的动作。当设备退出强制睡眠模式时，将会触发事件通知服务发布该系统公共事件。

**系统能力：** SystemCapability\.Notification\.CommonEvent

**类型：** String

**起始版本：** 20