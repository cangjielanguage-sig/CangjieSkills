## class CharacteristicWriteRequest

```cangjie
public class CharacteristicWriteRequest {
    public CharacteristicWriteRequest(
        public let deviceId: String,
        public let transId: Int32,
        public let offset: Int32,
        public let isPrepared: Bool,
        public let needRsp: Bool,
        public let value: Array<Byte>,
        public let characteristicUuid: String,
        public let serviceUuid: String
    )
}
```

**功能：** 描述server端订阅后收到的特征值写请求事件参数类。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### let characteristicUuid

```cangjie
public let characteristicUuid: String
```

**功能：** 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let deviceId

```cangjie
public let deviceId: String
```

**功能：** 表示扫描到的设备地址，例如："XX:XX:XX:XX:XX:XX"。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let isPrepared

```cangjie
public let isPrepared: Bool
```

**功能：** 表示写请求是否立即执行。true表示立即执行。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let needRsp

```cangjie
public let needRsp: Bool
```

**功能：** 表示是否要给client端回复响应。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let offset

```cangjie
public let offset: Int32
```

**功能：** 表示写描述符数据的起始位置。例如：k表示从第k个字节开始写，server端回复响应时需填写相同的offset。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let serviceUuid

```cangjie
public let serviceUuid: String
```

**功能：** 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let transId

```cangjie
public let transId: Int32
```

**功能：** 表示写请求的传输ID，server端回复响应时需填写相同的传输ID。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let value

```cangjie
public let value: Array<Byte>
```

**功能：** 表示写入的描述符二进制数据。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Array\<Byte>

**读写能力：** 只读

**起始版本：** 19