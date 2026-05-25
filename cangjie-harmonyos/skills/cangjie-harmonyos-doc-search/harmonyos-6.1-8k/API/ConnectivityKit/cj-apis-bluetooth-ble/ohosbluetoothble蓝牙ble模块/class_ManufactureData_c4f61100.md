## class ManufactureData

```cangjie
public class ManufactureData {
    public var manufactureId: UInt16
    public var manufactureValue: Array<Byte>
    public init(
        manufactureId: UInt16,
        manufactureValue: Array<Byte>
    )
}
```

**功能：** 描述BLE广播报文中制造商数据内容。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var manufactureId

```cangjie
public var manufactureId: UInt16
```

**功能：** 制造商的标识，由蓝牙技术联盟分配。

**类型：** UInt16

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var manufactureValue

```cangjie
public var manufactureValue: Array<Byte>
```

**功能：** 制造商特定的数据。

**类型：** Array\<Byte>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### init(UInt16, Array\<Byte>)

```cangjie
public init(
    manufactureId: UInt16,
    manufactureValue: Array<Byte>
)
```

**功能：** ManufactureData 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|manufactureId|UInt16|是|-|制造商的标识，由蓝牙技术联盟分配。|
|manufactureValue|Array\<Byte>|是|-|制造商特定的数据。|