## enum BluetoothTransport

```cangjie
public enum BluetoothTransport <: Equatable<BluetoothTransport> & ToString {
    | TRANSPORT_BR_EDR
    | TRANSPORT_LE
    | ...
}
```

**功能：** 表示设备类型。例如传统蓝牙设备或低功耗蓝牙设备，支持双模默认使用TRANSPORT_BR_EDR。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<BluetoothTransport>
- ToString

### TRANSPORT_BR_EDR

```cangjie
TRANSPORT_BR_EDR
```

**功能：** 表示传统蓝牙(BR/EDR)设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### TRANSPORT_LE

```cangjie
TRANSPORT_LE
```

**功能：** 表示低功耗蓝牙(BLE)设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(BluetoothTransport)

```cangjie
public operator func !=(other: BluetoothTransport): Bool
```

**功能：** 对设备类型进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[BluetoothTransport](#enum-bluetoothtransport)|是|设备类型类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备类型不同返回 true，否则返回 false。|

### func ==(BluetoothTransport)

```cangjie
public operator func ==(other: BluetoothTransport): Bool
```

**功能：** 对设备类型进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[BluetoothTransport](#enum-bluetoothtransport)|是|设备类型类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果设备类型相同返回 true，否则返回 false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回设备类型的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|设备类型的字符串表示。|