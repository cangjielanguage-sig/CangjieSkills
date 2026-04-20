## class BLECharacteristic

```cangjie
public class BLECharacteristic {
    public BLECharacteristic(
        public var serviceUuid: String,
        public var characteristicUuid: String,
        public var characteristicValue: Array<Byte>,
        public var descriptors: Array<BLEDescriptor>,
        public var properties: GattProperties
    )
}
```

**功能：** 描述characteristic的接口参数定义。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### var characteristicUuid

```cangjie
public var characteristicUuid: String
```

**功能：** 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var characteristicValue

```cangjie
public var characteristicValue: Array<Byte>
```

**功能：** 特征对应的二进制值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<Byte>

**读写能力：** 可读写

**起始版本：** 19

### var descriptors

```cangjie
public var descriptors: Array<BLEDescriptor>
```

**功能：** 特定特征的描述符列表。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<[BLEDescriptor](#class-bledescriptor)>

**读写能力：** 可读写

**起始版本：** 19

### var properties

```cangjie
public var properties: GattProperties
```

**功能：** 特定特征的属性描述。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** [GattProperties](#class-gattproperties)

**读写能力：** 可读写

**起始版本：** 19

### var serviceUuid

```cangjie
public var serviceUuid: String
```

**功能：** 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### BLECharacteristic(String, String, Array\<Byte>, Array\<BLEDescriptor>, GattProperties)

```cangjie
public BLECharacteristic(
    public var serviceUuid: String,
    public var characteristicUuid: String,
    public var characteristicValue: Array<Byte>,
    public var descriptors: Array<BLEDescriptor>,
    public var properties: GattProperties
)
```

**功能：** BLECharacteristic 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|serviceUuid|String|是|特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。|
|characteristicUuid|String|是|特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。|
|characteristicValue|Array\<Byte>|是|特征对应的二进制值。|
|descriptors|Array\<[BLEDescriptor](#class-bledescriptor)>|是|特定特征的描述符列表。|
|properties|[GattProperties](#class-gattproperties)|是|特定特征的属性描述。|