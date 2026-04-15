## class BleCharacteristic

```cangjie
public class BleCharacteristic {
    public var serviceUUID: String
    public var characteristicUUID: String
    public var characteristicValue: Array<Byte>
    public var descriptors: Array<BleDescriptor>
    public var properties: GattProperties
    public init(
        serviceUUID: String,
        characteristicUUID: String,
        characteristicValue: Array<Byte>,
        descriptors: Array<BleDescriptor>,
        properties!: GattProperties = GattProperties(),
        permissions!: GattPermissions = GattPermissions(),
        characteristicValueHandle!: UInt32 = 0
    )
}
```

**功能：** GATT特征值结构定义，是服务[GattService](#class-gattservice)的核心数据单元。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var characteristicUUID

```cangjie
public var characteristicUUID: String
```

**功能：** 特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var characteristicValue

```cangjie
public var characteristicValue: Array<Byte>
```

**功能：** 特征值的数据内容。

**类型：** Array\<Byte>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var descriptors

```cangjie
public var descriptors: Array<BleDescriptor>
```

**功能：** 特征值包含的描述符列表。

**类型：** Array\<[BleDescriptor](#class-bledescriptor)>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var properties

```cangjie
public var properties: GattProperties
```

**功能：** 特征值支持的属性。

**类型：** [GattProperties](#class-gattproperties)

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

### init(String, String, Array\<Byte>, Array\<BleDescriptor>, GattProperties, GattPermissions, UInt32)

```cangjie
public init(
    serviceUUID: String,
    characteristicUUID: String,
    characteristicValue: Array<Byte>,
    descriptors: Array<BleDescriptor>,
    properties!: GattProperties = GattProperties(),
    permissions!: GattPermissions = GattPermissions(),
    characteristicValueHandle!: UInt32 = 0
)
```

**功能：** BleCharacteristic 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|serviceUUID|String|是|-|特征值所属的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。|
|characteristicUUID|String|是|-|特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。|
|characteristicValue|Array\<Byte>|是|-|特征值的数据内容。|
|descriptors|Array\<[BleDescriptor](#class-bledescriptor)>|是|-|特征值包含的描述符列表。|
|properties|[GattProperties](#class-gattproperties)|否|GattProperties()|**命名参数。** 特征值支持的属性。|
|permissions|[GattPermissions](#class-gattpermissions)|否|GattPermissions()|**命名参数。** 特征值读写操作需要的权限。预留字段，本版本暂不支持。|
|characteristicValueHandle|UInt32|否|0|**命名参数。** 特征值的唯一标识句柄。当server端BLE蓝牙设备提供了多个相同UUID特征值时，可以通过此句柄区分不同的特征值。预留字段，本版本暂不支持。|