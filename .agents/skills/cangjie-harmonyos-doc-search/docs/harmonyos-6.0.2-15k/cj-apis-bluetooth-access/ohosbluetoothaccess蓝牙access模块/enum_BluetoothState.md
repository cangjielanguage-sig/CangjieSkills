## enum BluetoothState

```cangjie
public enum BluetoothState <: Equatable<BluetoothState> & ToString {
    | STATE_OFF
    | STATE_TURNING_ON
    | STATE_ON
    | STATE_TURNING_OFF
    | STATE_BLE_TURNING_ON
    | STATE_BLE_ON
    | STATE_BLE_TURNING_OFF
    | ...
}
```

**功能：** 蓝牙开关状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<BluetoothState>
- ToString

### STATE_BLE_ON

```cangjie
STATE_BLE_ON
```

**功能：** 表示蓝牙正处于LE-only模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### STATE_BLE_TURNING_OFF

```cangjie
STATE_BLE_TURNING_OFF
```

**功能：** 表示蓝牙正在关闭LE-only模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### STATE_BLE_TURNING_ON

```cangjie
STATE_BLE_TURNING_ON
```

**功能：** 表示蓝牙正在打开LE-only模式。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### STATE_OFF

```cangjie
STATE_OFF
```

**功能：** 表示蓝牙已关闭。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### STATE_ON

```cangjie
STATE_ON
```

**功能：** 表示蓝牙已打开。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### STATE_TURNING_OFF

```cangjie
STATE_TURNING_OFF
```

**功能：** 表示蓝牙正在关闭。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### STATE_TURNING_ON

```cangjie
STATE_TURNING_ON
```

**功能：** 表示蓝牙正在打开。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(BluetoothState)

```cangjie
public operator func !=(other: BluetoothState): Bool
```

**功能：** 对蓝牙开关状态进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[BluetoothState](#enum-bluetoothstate)|是|蓝牙开关状态类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两蓝牙开关状态不同返回 true，否则返回 false。|

### func ==(BluetoothState)

```cangjie
public operator func ==(other: BluetoothState): Bool
```

**功能：** 对蓝牙开关状态进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[BluetoothState](#enum-bluetoothstate)|是|蓝牙开关状态。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两蓝牙开关状态相同返回 true，否则返回 false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回蓝牙开关状态的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|蓝牙开关状态的字符串表示。|