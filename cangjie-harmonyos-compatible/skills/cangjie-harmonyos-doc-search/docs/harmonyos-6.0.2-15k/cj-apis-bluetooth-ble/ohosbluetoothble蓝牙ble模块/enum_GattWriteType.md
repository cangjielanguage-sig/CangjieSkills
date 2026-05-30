## enum GattWriteType

```cangjie
public enum GattWriteType <: Equatable<GattWriteType> & ToString {
    | WRITE
    | WRITE_NO_RESPONSE
    | ...
}
```

**功能：** 表示gatt写入类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<GattWriteType>
- ToString

### WRITE

```cangjie
WRITE
```

**功能：** 表示写入特征值，需要对端设备的回复。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### WRITE_NO_RESPONSE

```cangjie
WRITE_NO_RESPONSE
```

**功能：** 表示写入特征值，不需要对端设备的回复。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(GattWriteType)

```cangjie
public operator func !=(other: GattWriteType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[GattWriteType](#enum-gattwritetype)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(GattWriteType)

```cangjie
public operator func ==(other: GattWriteType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[GattWriteType](#enum-gattwritetype)|是|另一个枚举值。|

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