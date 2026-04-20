## enum BatteryHealthState

```cangjie
public enum BatteryHealthState <: Equatable<BatteryHealthState> & ToString {
    | UnknownHealthState
    | Good
    | Overheat
    | Overvoltage
    | Cold
    | Dead
    | ...
}
```

**功能：** 表示电池健康状态的枚举。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<BatteryHealthState>
- ToString

### Cold

```cangjie
Cold
```

**功能：**  表示电池健康状态为低温。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### Dead

```cangjie
Dead
```

**功能：** 表示电池健康状态为僵死状态。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### Good

```cangjie
Good
```

**功能：** 表示电池健康状态为正常。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### Overheat

```cangjie
Overheat
```

**功能：** 表示电池健康状态为过热。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### Overvoltage

```cangjie
Overvoltage
```

**功能：** 表示电池健康状态为过压。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### UnknownHealthState

```cangjie
UnknownHealthState
```

**功能：** 表示电池健康状态未知。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### func !=(BatteryHealthState)

```cangjie
public operator func !=(other: BatteryHealthState): Bool
```

**功能：** 对电池健康状态进行判不等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BatteryHealthState](#enum-batteryhealthstate)|是|-|电池健康状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool| 如果电池健康状态不同返回true，否则返回false。|

### func ==(BatteryHealthState)

```cangjie
public operator func ==(other: BatteryHealthState): Bool
```

**功能：** 对电池健康状态进行判等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BatteryHealthState](#enum-batteryhealthstate)|是|-|电池健康状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool| 如果电池健康状态相同返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回电池健康状态的字符串表示。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String| 电池健康状态值对应的字符串。 |