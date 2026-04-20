## class StateChangeParam

```cangjie
public class StateChangeParam {
    public var deviceId: String
    public var state: ProfileConnectionState
    public var cause: DisconnectCause
}
```

**功能：** 描述profile状态改变参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var cause

```cangjie
public var cause: DisconnectCause
```

**功能：** 表示连接失败的原因。

**类型：** [DisconnectCause](#enum-disconnectcause)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var deviceId

```cangjie
public var deviceId: String
```

**功能：** 表示蓝牙设备地址。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### var state

```cangjie
public var state: ProfileConnectionState
```

**功能：** 表示蓝牙设备的profile连接状态。

**类型：** [ProfileConnectionState](cj-apis-bluetooth-constant.md#enum-profileconnectionstate)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22