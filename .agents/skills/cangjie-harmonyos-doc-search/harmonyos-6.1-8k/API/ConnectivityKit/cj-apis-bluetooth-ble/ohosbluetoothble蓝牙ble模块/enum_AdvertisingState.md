## enum AdvertisingState

```cangjie
public enum AdvertisingState <: Equatable<AdvertisingState> & ToString {
    | Started
    | Enabled
    | Disabled
    | Stopped
    | ...
}
```

**功能：** 枚举，不同操作对应的BLE广播状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**父类型：**

- Equatable\<AdvertisingState>
- ToString

### Disabled

```cangjie
Disabled
```

**功能：** 广播停止成功。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### Enabled

```cangjie
Enabled
```

**功能：** 广播启动成功。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### Started

```cangjie
Started
```

**功能：** 调用[startAdvertising](#func-startadvertisingadvertisingparams)方法后，广播首次启动成功，且会分配相关资源。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### Stopped

```cangjie
Stopped
```

**功能：** 调用[stopAdvertising](#func-stopadvertisinguint32)方法后，广播停止成功，且会释放首次启动广播时分配的相关资源。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### func !=(AdvertisingState)

```cangjie
public operator func !=(other: AdvertisingState): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AdvertisingState](#enum-advertisingstate)|是|-|另一个枚举值。|

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

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[AdvertisingState](#enum-advertisingstate)|是|-|另一个枚举值。|

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

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|