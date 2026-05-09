## enum BatteryCapacityLevel

```cangjie
public enum BatteryCapacityLevel <: Equatable<BatteryCapacityLevel> & ToString {
    | LevelFull
    | LevelHigh
    | LevelNormal
    | LevelLow
    | LevelWarning
    | LevelCritical
    | LevelShutdown
    | ...
}
```

**功能：** 表示电池电量等级的枚举。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<BatteryCapacityLevel>
- ToString

### LevelCritical

```cangjie
LevelCritical
```

**功能：** 表示电池电量等级为极低电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### LevelFull

```cangjie
LevelFull
```

**功能：** 表示电池电量等级为满电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### LevelHigh

```cangjie
LevelHigh
```

**功能：** 表示电池电量等级为高电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### LevelLow

```cangjie
LevelLow
```

**功能：** 表示电池电量等级为低电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### LevelNormal

```cangjie
LevelNormal
```

**功能：** 表示电池电量等级为正常电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### LevelShutdown

```cangjie
LevelShutdown
```

**功能：** 表示电池电量等级为关机电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### LevelWarning

```cangjie
LevelWarning
```

**功能：** 表示电池电量等级为告警电量。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### func !=(BatteryCapacityLevel)

```cangjie
public operator func !=(other: BatteryCapacityLevel): Bool
```

**功能：** 对电池电量等级进行判不等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BatteryCapacityLevel](#enum-batterycapacitylevel)|是|-|电池电量等级。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool| 如果电池电量等级不同返回true，否则返回false。|

### func ==(BatteryCapacityLevel)

```cangjie
public operator func ==(other: BatteryCapacityLevel): Bool
```

**功能：** 对电池电量等级进行判等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BatteryCapacityLevel](#enum-batterycapacitylevel)|是|-|电池电量等级。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool| 如果电池电量等级相同返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回电池电量等级的字符串表示。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String| 电池电量等级值对应的字符串。 |