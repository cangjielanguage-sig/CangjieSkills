## enum BluetoothBleGattClientDeviceCallbackType

```cangjie
public enum BluetoothBleGattClientDeviceCallbackType <: Equatable<BluetoothBleGattClientDeviceCallbackType> & Hashable & ToString {
    | BleCharacteristicChange
    | BleConnectionStateChange
    | ClientBleMtuChange
    | ...
}
```

**功能：** 客户端 on/off 事件的类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**父类型：**

- Equatable\<BluetoothBleGattClientDeviceCallbackType>
- Hashable
- ToString

### BleCharacteristicChange

```cangjie
BleCharacteristicChange
```

**功能：** 表示特征值变化事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### BleConnectionStateChange

```cangjie
BleConnectionStateChange
```

**功能：** 表示连接状态变化事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### ClientBleMtuChange

```cangjie
ClientBleMtuChange
```

**功能：** 表示MTU状态变化事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### func !=(BluetoothBleGattClientDeviceCallbackType)

```cangjie
public operator func !=(other: BluetoothBleGattClientDeviceCallbackType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BluetoothBleGattClientDeviceCallbackType](#enum-bluetoothblegattclientdevicecallbacktype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(BluetoothBleGattClientDeviceCallbackType)

```cangjie
public operator func ==(other: BluetoothBleGattClientDeviceCallbackType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BluetoothBleGattClientDeviceCallbackType](#enum-bluetoothblegattclientdevicecallbacktype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取输入数据的哈希值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int64|数据的哈希值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|