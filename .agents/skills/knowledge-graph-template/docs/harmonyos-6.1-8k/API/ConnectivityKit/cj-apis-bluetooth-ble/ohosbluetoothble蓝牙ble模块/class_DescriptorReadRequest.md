## class DescriptorReadRequest

```cangjie
public class DescriptorReadRequest {
    public var deviceId: String
    public var transId: Int32
    public var offset: Int32
    public var descriptorUUID: String
    public var characteristicUUID: String
    public var serviceUUID: String
}
```

**功能：** 描述server端订阅client端读描述符请求事件后，接收到的事件参数结构。

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

**功能：** client端需要读取的描述符UUID。例如：00002902-0000-1000-8000-00805f9b34fb。

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

### var offset

```cangjie
public var offset: Int32
```

**功能：** client端读数据的偏移值。例如：k表示从第k个字节开始读。

server端回复响应时需填写相同的offset。

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

**功能：** client端读请求的标识符，server端回复时需填写相同的transId。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22