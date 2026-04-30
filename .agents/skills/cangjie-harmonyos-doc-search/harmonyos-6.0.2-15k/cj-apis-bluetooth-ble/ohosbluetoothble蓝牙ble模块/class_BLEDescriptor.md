## class BLEDescriptor

```cangjie
public class BLEDescriptor {
    public BLEDescriptor(
        public var serviceUuid: String,
        public var characteristicUuid: String,
        public var descriptorUuid: String,
        public var descriptorValue: Array<Byte>
    )
}
```

**功能：** 描述descriptor的接口参数定义。

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

### var descriptorUuid

```cangjie
public var descriptorUuid: String
```

**功能：** 描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var descriptorValue

```cangjie
public var descriptorValue: Array<Byte>
```

**功能：** 描述符对应的二进制值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<Byte>

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

### BLEDescriptor(String, String, String, Array\<Byte>)

```cangjie
public BLEDescriptor(
    public var serviceUuid: String,
    public var characteristicUuid: String,
    public var descriptorUuid: String,
    public var descriptorValue: Array<Byte>
)
```

**功能：** BLEDescriptor 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|serviceUuid|String|是|特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。|
|characteristicUuid|String|是|特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。|
|descriptorUuid|String|是|描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。|
|descriptorValue|Array\<Byte>|是|描述符对应的二进制值。|