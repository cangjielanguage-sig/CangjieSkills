## class ManufactureData

```cangjie
public class ManufactureData {
    public ManufactureData(
        public var manufactureId: UInt16,
        public var manufactureValue: Array<Byte>
    )
}
```

**功能：** 描述BLE广播数据包的内容。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### var manufactureId

```cangjie
public var manufactureId: UInt16
```

**功能：** 表示制造商的ID，由蓝牙SIG分配。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** UInt16

**读写能力：** 可读写

**起始版本：** 19

### var manufactureValue

```cangjie
public var manufactureValue: Array<Byte>
```

**功能：** 表示制造商发送的制造商数据。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<Byte>

**读写能力：** 可读写

**起始版本：** 19

### ManufactureData(UInt16, Array\<Byte>)

```cangjie
public ManufactureData(
    public var manufactureId: UInt16,
    public var manufactureValue: Array<Byte>
)
```

**功能：** ManufactureData 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|manufactureId|UInt16|是|表示制造商的ID，由蓝牙SIG分配。|
|manufactureValue|Array\<Byte>|是|表示制造商发送的制造商数据。|