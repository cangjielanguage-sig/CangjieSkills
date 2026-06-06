## enum DeviceChargeState

```cangjie
public enum DeviceChargeState <: Equatable<DeviceChargeState> & ToString {
    | DEVICE_NORMAL_CHARGE_NOT_CHARGED
    | DEVICE_NORMAL_CHARGE_IN_CHARGING
    | DEVICE_SUPER_CHARGE_NOT_CHARGED
    | DEVICE_SUPER_CHARGE_IN_CHARGING
    | ...
}
```

**功能：** 表示充电状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<DeviceChargeState>
- ToString

### DEVICE_NORMAL_CHARGE_IN_CHARGING

```cangjie
DEVICE_NORMAL_CHARGE_IN_CHARGING
```

**功能：** 正在充电，不支持超级充电。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### DEVICE_NORMAL_CHARGE_NOT_CHARGED

```cangjie
DEVICE_NORMAL_CHARGE_NOT_CHARGED
```

**功能：** 未充电，不支持超级充电。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### DEVICE_SUPER_CHARGE_IN_CHARGING

```cangjie
DEVICE_SUPER_CHARGE_IN_CHARGING
```

**功能：** 正在充电，支持超级充电。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### DEVICE_SUPER_CHARGE_NOT_CHARGED

```cangjie
DEVICE_SUPER_CHARGE_NOT_CHARGED
```

**功能：** 未充电，支持超级充电。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(DeviceChargeState)

```cangjie
public operator func !=(other: DeviceChargeState): Bool
```

**功能：** 对充电状态进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[DeviceChargeState](#enum-devicechargestate)|是|充电状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个充电状态不同返回 true，否则返回 false。|

### func ==(DeviceChargeState)

```cangjie
public operator func ==(other: DeviceChargeState): Bool
```

**功能：** 对充电状态进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[DeviceChargeState](#enum-devicechargestate)|是|充电状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果充电状态相同返回 true，否则返回 false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回充电状态的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|充电状态的字符串表示。|