## enum BatteryPluggedType

```cangjie
public enum BatteryPluggedType <: Equatable<BatteryPluggedType> & ToString {
    | UnknownType
    | Ac
    | Usb
    | Wireless
    | ...
}
```

**功能：** 表示连接的充电器类型的枚举。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**父类型：**

- Equatable\<BatteryPluggedType>
- ToString

### Ac

```cangjie
Ac
```

**功能：** 表示连接的充电器类型为交流充电器。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### UnknownType

```cangjie
UnknownType
```

**功能：** 表示未获取到连接充电器类型。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### Usb

```cangjie
Usb
```

**功能：** 表示连接的充电器类型为USB。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### Wireless

```cangjie
Wireless
```

**功能：** 表示连接的充电器类型为无线充电器。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

### func !=(BatteryPluggedType)

```cangjie
public operator func !=(other: BatteryPluggedType): Bool
```

**功能：** 对充电器类型进行判不等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BatteryPluggedType](#enum-batterypluggedtype)|是|-|充电器类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool| 如果充电器类型不同返回true，否则返回false。|

### func ==(BatteryPluggedType)

```cangjie
public operator func ==(other: BatteryPluggedType): Bool
```

**功能：** 对充电器类型进行判等。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BatteryPluggedType](#enum-batterypluggedtype)|是|-|充电器类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool| 如果充电器类型相同返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回充电器类型信息的字符串表示。

**系统能力：** SystemCapability.PowerManager.BatteryManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String| 充电器类型值对应的字符串。 |