## class BLEConnectionChangeState

```cangjie
public class BLEConnectionChangeState {
    public BLEConnectionChangeState(
        public let deviceId: String,
        public var state: ProfileConnectionState
    )
}
```

**功能：** 描述Gatt profile连接状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### var state

```cangjie
public var state: ProfileConnectionState
```

**功能：** 表示BLE连接状态的枚举。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** [ProfileConnectionState](cj-apis-bluetooth-constant.md#enum-profileconnectionstate)

**读写能力：** 可读写

**起始版本：** 19

### let deviceId

```cangjie
public let deviceId: String
```

**功能：** 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### BLEConnectionChangeState(String, ProfileConnectionState)

```cangjie
public BLEConnectionChangeState(
    public let deviceId: String,
    public var state: ProfileConnectionState
)
```

**功能：** BLEConnectionChangeState 构造器。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|deviceId|String|是|表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。|
|state|[ProfileConnectionState](cj-apis-bluetooth-constant.md#enum-profileconnectionstate)|是|表示BLE连接状态的枚举。|