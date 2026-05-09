## enum BatteryChargeState

```cangjie
public enum BatteryChargeState <: Equatable<BatteryChargeState> & ToString {
    | UnknownChargeState
    | Enabled
    | Disabled
    | Full
    | ...
}
```

**功能：** 表示电池充电状态的枚举。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<BatteryChargeState>
- ToString

### Disabled

```cangjie
Disabled
```

**功能：** 表示电池充电状态为停止状态。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### Enabled

```cangjie
Enabled
```

**功能：** 表示电池充电状态为使能状态。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### Full

```cangjie
Full
```

**功能：** 表示电池充电状态为已充满状态。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### UnknownChargeState

```cangjie
UnknownChargeState
```

**功能：** 表示电池充电状态未知。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### func !=(BatteryChargeState)

```cangjie
public operator func !=(other: BatteryChargeState): Bool
```

**功能：** 对电池充电状态进行判不等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BatteryChargeState](#enum-batterychargestate)|是|-|电池充电状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool| 如果电池充电状态不同返回true，否则返回false。|

### func ==(BatteryChargeState)

```cangjie
public operator func ==(other: BatteryChargeState): Bool
```

**功能：**  对电池充电状态进行判等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BatteryChargeState](#enum-batterychargestate)|是|-|电池充电状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool| 如果电池充电状态相同返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回电池充电状态的字符串表示。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String| 电池充电状态值对应的字符串。 |