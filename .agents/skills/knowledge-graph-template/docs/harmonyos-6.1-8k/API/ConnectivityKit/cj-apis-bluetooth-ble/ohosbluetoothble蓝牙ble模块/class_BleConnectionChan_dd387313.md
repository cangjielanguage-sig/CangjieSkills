## class BleConnectionChangeState

```cangjie
public class BleConnectionChangeState {
    public var deviceId: String
    public var state: ProfileConnectionState
}
```

**功能：** 描述GATT profile协议连接状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var deviceId

```cangjie
public var deviceId: String
```

**功能：** 对端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var state

```cangjie
public var state: ProfileConnectionState
```

**功能：** GATT profile连接状态。

**类型：** [ProfileConnectionState](cj-apis-bluetooth-constant.md#enum-profileconnectionstate)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22