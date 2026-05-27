## enum BatteryCapacityLevel

```cangjie
public enum BatteryCapacityLevel <: Equatable<BatteryCapacityLevel> & ToString {
    | LEVEL_FULL
    | LEVEL_HIGH
    | LEVEL_NORMAL
    | LEVEL_LOW
    | LEVEL_WARNING
    | LEVEL_CRITICAL
    | LEVEL_SHUTDOWN
    | ...
}
```

**功能：** 表示电池电量等级。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

**父类型：**

- Equatable\<BatteryCapacityLevel>
- ToString

### LEVEL_CRITICAL

```cangjie
LEVEL_CRITICAL
```

**功能：** 表示电池电量等级为极低电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### LEVEL_FULL

```cangjie
LEVEL_FULL
```

**功能：** 表示电池电量等级为满电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### LEVEL_HIGH

```cangjie
LEVEL_HIGH
```

**功能：** 表示电池电量等级为高电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### LEVEL_LOW

```cangjie
LEVEL_LOW
```

**功能：** 表示电池电量等级为低电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### LEVEL_NORMAL

```cangjie
LEVEL_NORMAL
```

**功能：** 表示电池电量等级为正常电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### LEVEL_SHUTDOWN

```cangjie
LEVEL_SHUTDOWN
```

**功能：** 表示电池电量等级为关机电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### LEVEL_WARNING

```cangjie
LEVEL_WARNING
```

**功能：** 表示电池电量等级为告警电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### func !=(BatteryCapacityLevel)

```cangjie
public operator func !=(other: BatteryCapacityLevel): Bool
```

**功能：** 对电池电量等级进行判不等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BatteryCapacityLevel](#enum-batterycapacitylevel)|是|-|电池电量等级。|

**返回值：**

| 类型 | 说明 |
| :---- | :---- |
| Bool | 如果电池电量等级不同返回true，否则返回false。|

### func ==(BatteryCapacityLevel)

```cangjie
public operator func ==(other: BatteryCapacityLevel): Bool
```

**功能：** 对电池电量等级进行判等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BatteryCapacityLevel](#enum-batterycapacitylevel)|是|-|电池电量等级。|

**返回值：**

| 类型 | 说明 |
| :--- | :---- |
| Bool | 如果电池电量等级相同返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回电池电量等级的字符串表示。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

**返回值：**

| 类型  | 说明  |
| :------ | :------ |
| String | 电池电量等级值对应的字符串。 |