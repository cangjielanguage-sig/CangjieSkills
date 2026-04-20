## class StateChangeParam

```cangjie
public class StateChangeParam {}
```

**功能：** 描述profile状态改变参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### let cause

```cangjie
public let cause: DisconnectCause
```

**功能：** 表示连接失败的原因。

**类型：** [DisconnectCause](#enum-disconnectcause)

**读写能力：** 只读

**起始版本：** 19

### let deviceId

```cangjie
public let deviceId: String
```

**功能：** 表示蓝牙设备地址。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let state

```cangjie
public let state: ProfileConnectionState
```

**功能：** 表示蓝牙设备的profile连接状态。

**类型：** [ProfileConnectionState](cj-apis-bluetooth-constant.md#enum-profileconnectionstate)

**读写能力：** 只读

**起始版本：** 19