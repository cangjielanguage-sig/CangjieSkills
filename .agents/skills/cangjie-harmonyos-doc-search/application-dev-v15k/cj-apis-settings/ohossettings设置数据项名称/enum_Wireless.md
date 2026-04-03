## enum Wireless

```cangjie
public enum Wireless <: ToString {
    | AIRPLANE_MODE_RADIOS
    | BLUETOOTH_STATUS
    | BLUETOOTH_DISCOVER_ABILITY_STATUS
    | BLUETOOTH_DISCOVER_TIMEOUT
    | WIFI_DHCP_MAX_RETRY_COUNT
    | WIFI_TO_MOBILE_DATA_AWAKE_TIMEOUT
    | WIFI_STATUS
    | WIFI_WATCHDOG_STATUS
    | OWNER_LOCKDOWN_WIFI_CFG
    | ...
}
```

**功能：** 提供设置无线网络信息的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**父类型：**

- ToString

### AIRPLANE_MODE_RADIOS

```cangjie
AIRPLANE_MODE_RADIOS
```

**功能：** 启用飞行模式时要禁用的无线电信号列表。

多个无线电信号用逗号(,)分隔。取值包括以下常量：BLUETOOTH_RADIO、 CELL_RADIO、 NFC_RADIO、 WIFI_RADIO。

**起始版本：** 19

### BLUETOOTH_DISCOVER_ABILITY_STATUS

```cangjie
BLUETOOTH_DISCOVER_ABILITY_STATUS
```

**功能：** 设备是否可以被其他设备通过蓝牙发现或连接。值为0表示设备不可以被连接或发现；值为1表示设备可以被连接但不可以被发现；值为2表示设备可以被连接和发现。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### BLUETOOTH_DISCOVER_TIMEOUT

```cangjie
BLUETOOTH_DISCOVER_TIMEOUT
```

**功能：** 可以通过蓝牙发现设备的持续时间（以秒为单位）。这段时间之后，设备不可以被蓝牙搜寻到。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### BLUETOOTH_STATUS

```cangjie
BLUETOOTH_STATUS
```

**功能：** 蓝牙是否可用。值为true表示蓝牙可用；值为false表示蓝牙不可用。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### OWNER_LOCKDOWN_WIFI_CFG

```cangjie
OWNER_LOCKDOWN_WIFI_CFG
```

**功能：** 是否应锁定由设备所有者的应用程序创建的Wi-Fi配置。值为true表示Wi-Fi配置应该被锁定；值为false表示不应该被锁定。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### WIFI_DHCP_MAX_RETRY_COUNT

```cangjie
WIFI_DHCP_MAX_RETRY_COUNT
```

**功能：** 尝试从DHCP服务器获取IP地址的最大次数。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### WIFI_STATUS

```cangjie
WIFI_STATUS
```

**功能：** Wi-Fi是否可用。值为true表示Wi-Fi可用；值为false表示Wi-Fi不可用。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### WIFI_TO_MOBILE_DATA_AWAKE_TIMEOUT

```cangjie
WIFI_TO_MOBILE_DATA_AWAKE_TIMEOUT
```

**功能：** Wi-Fi连接断开后等待移动数据连接建立时保持唤醒锁的最长时间。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### WIFI_WATCHDOG_STATUS

```cangjie
WIFI_WATCHDOG_STATUS
```

**功能：** Wi-Fi的WatchDog是否可用。值为true表示可用；值为false表示不可用。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

### func toString()

```cangjie
public override func toString(): String
```

**功能：** 返回设置无线网络信息的数据项。

**系统能力：** SystemCapability.Applications.Settings.Core

**起始版本：** 19

**返回值：**

| 类型  | 说明  |
| :------ | :------ |
| String | 设置无线网络信息的数据项。 |