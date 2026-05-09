## class CharacteristicWriteRequest

```cangjie
public class CharacteristicWriteRequest {
    public var deviceId: String
    public var transId: Int32
    public var offset: Int32
    public var isPrepared: Bool
    public var needRsp: Bool
    public var value: Array<Byte>
    public var characteristicUUID: String
    public var serviceUUID: String
}
```

**功能：** 描述server端订阅client端写特征值请求事件后，接收到的事件参数结构。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var characteristicUUID

```cangjie
public var characteristicUUID: String
```

**功能：** client端需要写入的特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var deviceId

```cangjie
public var deviceId: String
```

**功能：** client端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var isPrepared

```cangjie
public var isPrepared: Bool
```

**功能：** 收到client端写请求后，是否立即回复。

true表示稍后回复，false表示立即回复。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var needRsp

```cangjie
public var needRsp: Bool
```

**功能：** 是否需要回复client端。

true表示需要回复，false表示不需要回复。

**类型：** Bool

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var offset

```cangjie
public var offset: Int32
```

**功能：** client端写数据的偏移值。例如：k表示从第k个字节开始写。

server端回复时需填写相同的offset。

**类型：** Int32

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

### var transId

```cangjie
public var transId: Int32
```

**功能：** client端写请求的标识符，server端回复时需填写相同的transId。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var value

```cangjie
public var value: Array<Byte>
```

**功能：** client端需要给特征值写入的数据。

**类型：** Array\<Byte>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22