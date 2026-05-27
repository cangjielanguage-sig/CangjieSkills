## class NotifyCharacteristic

```cangjie
public class NotifyCharacteristic {
    public NotifyCharacteristic(
        public var serviceUuid: String,
        public var characteristicUuid: String,
        public var characteristicValue: Array<Byte>,
        public var confirm: Bool
    )
}
```

**功能：** 描述server端特征值变化时发送的特征通知参数定义。

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

### var confirm

```cangjie
public var confirm: Bool
```

**功能：** 如果是indication，对端需要回复确认，则设置为true；如果是notification，对端不需要回复确认，则设置为false。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Bool

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

### NotifyCharacteristic(String, String, Array\<Byte>, Bool)

```cangjie
public NotifyCharacteristic(
    public var serviceUuid: String,
    public var characteristicUuid: String,
    public var characteristicValue: Array<Byte>,
    public var confirm: Bool
)
```

**功能：** NotifyCharacteristic 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|serviceUuid|String|是|特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。|
|characteristicUuid|String|是|特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。|
|characteristicValue|Array\<Byte>|是|特征对应的二进制值。|
|confirm|Bool|是|如果是indication，对端需要回复确认，则设置为true；如果是notification，对端不需要回复确认，则设置为false。|