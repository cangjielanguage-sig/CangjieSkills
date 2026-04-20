## enum CommonEventBatteryChangedKey

```cangjie
public enum CommonEventBatteryChangedKey <: Equatable<CommonEventBatteryChangedKey> & ToString {
    | EXTRA_SOC
    | EXTRA_CHARGE_STATE
    | EXTRA_HEALTH_STATE
    | EXTRA_PLUGGED_TYPE
    | EXTRA_VOLTAGE
    | EXTRA_TECHNOLOGY
    | EXTRA_TEMPERATURE
    | EXTRA_PRESENT
    | EXTRA_CAPACITY_LEVEL
    | ...
}
```

**功能：** 表示COMMON_EVENT_BATTERY_CHANGED通用事件附加信息的查询键。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

**父类型：**

- Equatable\<CommonEventBatteryChangedKey>
- ToString

### EXTRA_CAPACITY_LEVEL

```cangjie
EXTRA_CAPACITY_LEVEL
```

**功能：** 表示当前设备电池电量等级的查询键。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### EXTRA_CHARGE_STATE

```cangjie
EXTRA_CHARGE_STATE
```

**功能：** 表示当前设备电池充电状态的查询键。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### EXTRA_HEALTH_STATE

```cangjie
EXTRA_HEALTH_STATE
```

**功能：** 表示当前设备电池健康状态的查询键。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### EXTRA_PLUGGED_TYPE

```cangjie
EXTRA_PLUGGED_TYPE
```

**功能：** 表示当前设备连接的充电器类型的查询键。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### EXTRA_PRESENT

```cangjie
EXTRA_PRESENT
```

**功能：** 表示当前设备是否支持电池或者电池是否在位的查询键。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### EXTRA_SOC

```cangjie
EXTRA_SOC
```

**功能：** 表示剩余电池电量百分比的查询键。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### EXTRA_TECHNOLOGY

```cangjie
EXTRA_TECHNOLOGY
```

**功能：** 表示当前设备电池技术型号的查询键。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### EXTRA_TEMPERATURE

```cangjie
EXTRA_TEMPERATURE
```

**功能：** 表示当前设备电池温度的查询键。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### EXTRA_VOLTAGE

```cangjie
EXTRA_VOLTAGE
```

**功能：** 表示当前设备电池电压的查询键。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### func !=(CommonEventBatteryChangedKey)

```cangjie
public operator func !=(other: CommonEventBatteryChangedKey): Bool
```

**功能：** 对通用事件附加信息的查询键进行判不等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CommonEventBatteryChangedKey](#enum-commoneventbatterychangedkey)|是|-|通用事件附加信息的查询键。|

**返回值：**

| 类型 | 说明 |
| :--- | :---- |
| Bool | 如果查询键相同返回true，否则返回false。|

### func ==(CommonEventBatteryChangedKey)

```cangjie
public operator func ==(other: CommonEventBatteryChangedKey): Bool
```

**功能：** 对通用事件附加信息的查询键进行判等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CommonEventBatteryChangedKey](#enum-commoneventbatterychangedkey)|是|-|通用事件附加信息的查询键。|

**返回值：**

| 类型 | 说明 |
| :--- | :---- |
| Bool | 如果查询键相同返回true，否则返回false。|