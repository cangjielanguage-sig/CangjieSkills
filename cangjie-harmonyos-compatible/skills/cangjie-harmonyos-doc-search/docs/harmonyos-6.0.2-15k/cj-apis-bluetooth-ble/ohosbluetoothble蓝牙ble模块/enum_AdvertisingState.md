## enum AdvertisingState

```cangjie
public enum AdvertisingState <: Equatable<AdvertisingState> & ToString {
    | STARTED
    | ENABLED
    | DISABLED
    | STOPPED
    | ...
}
```

**功能：** 广播状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<AdvertisingState>
- ToString

### DISABLED

```cangjie
DISABLED
```

**功能：** 表示临时停止广播后的状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### ENABLED

```cangjie
ENABLED
```

**功能：** 表示临时启动广播后的状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### STARTED

```cangjie
STARTED
```

**功能：** 表示首次启动广播后的状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### STOPPED

```cangjie
STOPPED
```

**功能：** 表示完全停止广播后的状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(AdvertisingState)

```cangjie
public operator func !=(other: AdvertisingState): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[AdvertisingState](#enum-advertisingstate)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(AdvertisingState)

```cangjie
public operator func ==(other: AdvertisingState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[AdvertisingState](#enum-advertisingstate)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|