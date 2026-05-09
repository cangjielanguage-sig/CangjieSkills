## class BleDescriptor

```cangjie
public class BleDescriptor {
    public var serviceUUID: String
    public var characteristicUUID: String
    public var descriptorUUID: String
    public var descriptorValue: Array<Byte>
    public init(
        serviceUUID: String,
        characteristicUUID: String,
        descriptorUUID: String,
        descriptorValue: Array<Byte>,
        descriptorHandle!: UInt32 = 0,
        permissions!: GattPermissions = GattPermissions()
    )
}
```

**功能：** GATT描述符结构定义，是特征值[BleCharacteristic](#class-blecharacteristic)的数据单元，用于描述特征值的附加信息和属性。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var characteristicUUID

```cangjie
public var characteristicUUID: String
```

**功能：** 描述符所属的特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var descriptorUUID

```cangjie
public var descriptorUUID: String
```

**功能：** 描述符UUID。例如：00002902-0000-1000-8000-00805f9b34fb。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var descriptorValue

```cangjie
public var descriptorValue: Array<Byte>
```

**功能：** 描述符的数据内容。

**类型：** Array\<Byte>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var serviceUUID

```cangjie
public var serviceUUID: String
```

**功能：** 特征值所属的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### init(String, String, String, Array\<Byte>, UInt32, GattPermissions)

```cangjie
public init(
    serviceUUID: String,
    characteristicUUID: String,
    descriptorUUID: String,
    descriptorValue: Array<Byte>,
    descriptorHandle!: UInt32 = 0,
    permissions!: GattPermissions = GattPermissions()
)
```

**功能：** BleDescriptor 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|serviceUUID|String|是|-|特征值所属的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。|
|characteristicUUID|String|是|-|描述符所属的特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。|
|descriptorUUID|String|是|-|描述符UUID。例如：00002902-0000-1000-8000-00805f9b34fb。|
|descriptorValue|Array\<Byte>|是|-|描述符的数据内容。|
|descriptorHandle|UInt32|否|0|**命名参数。**  描述符的唯一标识句柄。当server端BLE蓝牙设备提供了多个相同UUID描述符时，可以通过此句柄区分不同的描述符。预留字段，本版本暂不支持。|
|permissions|[GattPermissions](#class-gattpermissions)|否|GattPermissions()|**命名参数。**  描述符读写操作需要的权限。预留字段，本版本暂不支持。|