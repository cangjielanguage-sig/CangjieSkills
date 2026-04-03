## enum BatteryStatus

```cangjie
public enum BatteryStatus {
    | BATTERY_STATUS_LOW
    | BATTERY_STATUS_OKAY
    | BATTERY_STATUS_LOW_OR_OKAY
    |...
}
```

**功能：** 触发延迟回调的电池状态。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### BATTERY_STATUS_LOW

```cangjie
BATTERY_STATUS_LOW
```

**功能：** 表示这个触发条件是低电告警。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### BATTERY_STATUS_LOW_OR_OKAY

```cangjie
BATTERY_STATUS_LOW_OR_OKAY
```

**功能：** 表示这个触发条件是从低电恢复到正常电量或者低电告警。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### BATTERY_STATUS_OKAY

```cangjie
BATTERY_STATUS_OKAY
```

**功能：** 表示这个触发条件是从低电恢复到正常电量。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

## enum ChargingType

```cangjie
public enum ChargingType {
    | CHARGING_PLUGGED_ANY
    | CHARGING_PLUGGED_AC
    | CHARGING_PLUGGED_USB
    | CHARGING_PLUGGED_WIRELESS
    |...
}
```

**功能：** 触发延迟回调的充电类型。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### CHARGING_PLUGGED_AC

```cangjie
CHARGING_PLUGGED_AC
```

**功能：** 表示这个触发条件是直流充电器连接。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### CHARGING_PLUGGED_ANY

```cangjie
CHARGING_PLUGGED_ANY
```

**功能：** 表示这个触发条件是任何类型的充电器连接。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### CHARGING_PLUGGED_USB

```cangjie
CHARGING_PLUGGED_USB
```

**功能：** 表示这个触发条件是USB充连接。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### CHARGING_PLUGGED_WIRELESS

```cangjie
CHARGING_PLUGGED_WIRELESS
```

**功能：** 表示这个触发条件是无线充电器连接。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

## enum NetworkType

```cangjie
public enum NetworkType {
    | NETWORK_TYPE_ANY
    | NETWORK_TYPE_MOBILE
    | NETWORK_TYPE_WIFI
    | NETWORK_TYPE_BLUETOOTH
    | NETWORK_TYPE_WIFI_P2P
    | NETWORK_TYPE_ETHERNET
    |...
}
```

**功能：** 触发延迟回调的网络类型。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### NETWORK_TYPE_ANY

```cangjie
NETWORK_TYPE_ANY
```

**功能：** 表示这个触发条件是任何类型的网络连接。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### NETWORK_TYPE_BLUETOOTH

```cangjie
NETWORK_TYPE_BLUETOOTH
```

**功能：** 表示这个触发条件是Bluetooth网络连接。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### NETWORK_TYPE_ETHERNET

```cangjie
NETWORK_TYPE_ETHERNET
```

**功能：** 表示这个触发条件是有线网络连接。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### NETWORK_TYPE_MOBILE

```cangjie
NETWORK_TYPE_MOBILE
```

**功能：** 表示这个触发条件是Mobile网络连接。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### NETWORK_TYPE_WIFI

```cangjie
NETWORK_TYPE_WIFI
```

**功能：** 表示这个触发条件是Wifi类型的网络连接。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12

### NETWORK_TYPE_WIFI_P2P

```cangjie
NETWORK_TYPE_WIFI_P2P
```

**功能：** 表示这个触发条件是Wifi P2P网络连接。

**系统能力：** SystemCapability.ResourceSchedule.WorkScheduler

**起始版本：** 12