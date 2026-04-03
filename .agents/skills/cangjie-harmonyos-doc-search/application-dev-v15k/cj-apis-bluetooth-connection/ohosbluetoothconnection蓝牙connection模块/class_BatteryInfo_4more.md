## class BatteryInfo

```cangjie
public class BatteryInfo {}
```

**功能：** 描述电量信息的内容。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### let batteryLevel

```cangjie
public let batteryLevel: Int32
```

**功能：** 表示远端设备的电量值，如果值为-1，表示没有电量信息。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let boxBatteryLevel

```cangjie
public let boxBatteryLevel: Int32
```

**功能：** 表示耳机仓的电量值，如果值为-1，表示没有电量信息。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let boxChargeState

```cangjie
public let boxChargeState: DeviceChargeState
```

**功能：** 表示耳机仓的充电状态。

**类型：** [DeviceChargeState](#enum-devicechargestate)

**读写能力：** 只读

**起始版本：** 19

### let leftEarBatteryLevel

```cangjie
public let leftEarBatteryLevel: Int32
```

**功能：** 表示左侧耳机的电量值，如果值为-1，表示没有电量信息。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let leftEarChargeState

```cangjie
public let leftEarChargeState: DeviceChargeState
```

**功能：** 表示左侧耳机的充电状态。

**类型：** [DeviceChargeState](#enum-devicechargestate)

**读写能力：** 只读

**起始版本：** 19

### let rightEarBatteryLevel

```cangjie
public let rightEarBatteryLevel: Int32
```

**功能：** 表示右侧耳机的电量值，如果值为-1，表示没有电量信息。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let rightEarChargeState

```cangjie
public let rightEarChargeState: DeviceChargeState
```

**功能：** 表示右侧耳机的充电状态。

**类型：** [DeviceChargeState](#enum-devicechargestate)

**读写能力：** 只读

**起始版本：** 19

## class BondStateParam

```cangjie
public class BondStateParam {}
```

**功能：** 描述配对状态参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### let cause

```cangjie
public let cause: UnbondCause
```

**功能：** 表示配对失败的原因。

**类型：** [UnbondCause](#enum-unbondcause)

**读写能力：** 只读

**起始版本：** 19

### let deviceId

```cangjie
public let deviceId: String
```

**功能：** 表示要配对的设备ID。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let state

```cangjie
public let state: BondState
```

**功能：** 表示配对设备的状态。

**类型：** [BondState](#enum-bondstate)

**读写能力：** 只读

**起始版本：** 19

## class DeviceClass

```cangjie
public class DeviceClass {}
```

**功能：** 描述蓝牙设备的类别。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### let classOfDevice

```cangjie
public let classOfDevice: Int32
```

**功能：** 表示设备类别。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let majorClass

```cangjie
public let majorClass: MajorClass
```

**功能：** 表示蓝牙设备主要类别。

**类型：** [MajorClass](cj-apis-bluetooth-constant.md#enum-majorclass)

**读写能力：** 只读

**起始版本：** 19

### let majorMinorClass

```cangjie
public let majorMinorClass: MajorMinorClass
```

**功能：** 表示主要次要蓝牙设备类别。

**类型：** [MajorMinorClass](cj-apis-bluetooth-constant.md#enum-majorminorclass)

**读写能力：** 只读

**起始版本：** 19

## class PinRequiredParam

```cangjie
public class PinRequiredParam {}
```

**功能：** 描述配对请求参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### let deviceId

```cangjie
public let deviceId: String
```

**功能：** 表示要配对的设备ID。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let pinCode

```cangjie
public let pinCode: String
```

**功能：** 表示要配对的密钥。

**类型：** String

**读写能力：** 只读

**起始版本：** 19