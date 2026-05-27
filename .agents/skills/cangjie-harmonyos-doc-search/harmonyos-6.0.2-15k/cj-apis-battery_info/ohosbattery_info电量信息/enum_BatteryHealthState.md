## enum BatteryHealthState

```cangjie
public enum BatteryHealthState <: Equatable<BatteryHealthState> & ToString {
    | UNKNOWN
    | GOOD
    | OVERHEAT
    | OVERVOLTAGE
    | COLD
    | DEAD
    | ...
}
```

**功能：** 表示电池健康状态。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

**父类型：**

- Equatable\<BatteryHealthState>
- ToString

### COLD

```cangjie
COLD
```

**功能：** 表示电池健康状态为低温。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### DEAD

```cangjie
DEAD
```

**功能：** 表示电池健康状态为僵死状态。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### GOOD

```cangjie
GOOD
```

**功能：** 表示电池健康状态为正常。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### OVERHEAT

```cangjie
OVERHEAT
```

**功能：** 表示电池健康状态为过热。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### OVERVOLTAGE

```cangjie
OVERVOLTAGE
```

**功能：** 表示电池健康状态为过压。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 表示电池健康状态未知。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

### func !=(BatteryHealthState)

```cangjie
public operator func !=(other: BatteryHealthState): Bool
```

**功能：** 对电池健康状态进行判不等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BatteryHealthState](#enum-batteryhealthstate)|是|-|电池健康状态。|

**返回值：**

| 类型 | 说明 |
| :---- | :---- |
| Bool | 如果电池健康状态不同返回true，否则返回false。|

### func ==(BatteryHealthState)

```cangjie
public operator func ==(other: BatteryHealthState): Bool
```

**功能：** 对电池健康状态进行判等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BatteryHealthState](#enum-batteryhealthstate)|是|-|电池健康状态。|

**返回值：**

| 类型 | 说明 |
| :--- | :---- |
| Bool | 如果电池健康状态相同返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回电池健康状态的字符串表示。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 19

**返回值：**

| 类型  | 说明  |
| :------ | :------ |
| String | 电池健康状态值对应的字符串。 |