## class NotifyCharacteristic

```cangjie
public class NotifyCharacteristic {
    public var serviceUUID: String
    public var characteristicUUID: String
    public var characteristicValue: Array<Byte>
    public var confirm: Bool
    public init(
        serviceUUID: String,
        characteristicUUID: String,
        characteristicValue: Array<Byte>,
        confirm: Bool
    )
}
```

**功能：** 描述server端特征值发生变化时，server端发送特征值通知的参数结构。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var characteristicUUID

```cangjie
public var characteristicUUID: String
```

**功能：** 内容发生变化的特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var characteristicValue

```cangjie
public var characteristicValue: Array<Byte>
```

**功能：** 特征值对应的数据内容。

**类型：** Array\<Byte>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var confirm

```cangjie
public var confirm: Bool
```

**功能：** true表示发送的是指示，需要client端回复确认。false表示发送的是通知，不需要client端回复确认。

**类型：** Bool

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

### init(String, String, Array\<Byte>, Bool)

```cangjie
public init(
    serviceUUID: String,
    characteristicUUID: String,
    characteristicValue: Array<Byte>,
    confirm: Bool
)
```

**功能：** NotifyCharacteristic 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|serviceUUID|String|是|-|特征值所属的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。|
|characteristicUUID|String|是|-|内容发生变化的特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。|
|characteristicValue|Array\<Byte>|是|-|特征值对应的数据内容。|
|confirm|Bool|是|-|true表示发送的是指示，需要client端回复确认。false表示发送的是通知，不需要client端回复确认。|