## class ServiceData

```cangjie
public class ServiceData {
    public var serviceUUID: String
    public var serviceValue: Array<Byte>
    public init(
        serviceUUID: String,
        serviceValue: Array<Byte>
    )
}
```

**功能：** 描述BLE广播报文中的服务数据内容。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var serviceUUID

```cangjie
public var serviceUUID: String
```

**功能：** 服务UUID。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var serviceValue

```cangjie
public var serviceValue: Array<Byte>
```

**功能：** 服务数据。

**类型：** Array\<Byte>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### init(String, Array\<Byte>)

```cangjie
public init(
    serviceUUID: String,
    serviceValue: Array<Byte>
)
```

**功能：** 描述广播包中服务数据内容。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|serviceUUID|String|是|-|服务UUID。|
|serviceValue|Array\<Byte>|是|-|服务数据。|