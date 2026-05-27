## enum BluetoothBleGattServerCallbackType

```cangjie
public enum BluetoothBleGattServerCallbackType <: Equatable<BluetoothBleGattServerCallbackType> & Hashable & ToString {
    | CHARACTERISTIC_READ
    | CHARACTERISTIC_WRITE
    | DESCRIPTOR_READ
    | DESCRIPTOR_WRITE
    | CONNECTION_STATE_CHANGE
    | BLE_MTU_CHANGE
    | ...
}
```

**功能：** 服务端 on/off 事件的类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<BluetoothBleGattServerCallbackType>
- Hashable
- ToString

### BLE_MTU_CHANGE

```cangjie
BLE_MTU_CHANGE
```

**功能：** 表示MTU状态变化事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CHARACTERISTIC_READ

```cangjie
CHARACTERISTIC_READ
```

**功能：** 表示特征值读请求事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CHARACTERISTIC_WRITE

```cangjie
CHARACTERISTIC_WRITE
```

**功能：** 表示特征值写请求事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CONNECTION_STATE_CHANGE

```cangjie
CONNECTION_STATE_CHANGE
```

**功能：** 表示BLE连接状态变化事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### DESCRIPTOR_READ

```cangjie
DESCRIPTOR_READ
```

**功能：** 表示描述符读请求事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### DESCRIPTOR_WRITE

```cangjie
DESCRIPTOR_WRITE
```

**功能：** 表示描述符写请求事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(BluetoothBleGattServerCallbackType)

```cangjie
public operator func !=(other: BluetoothBleGattServerCallbackType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[BluetoothBleGattServerCallbackType](#enum-bluetoothblegattservercallbacktype)|是|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(BluetoothBleGattServerCallbackType)

```cangjie
public operator func ==(other: BluetoothBleGattServerCallbackType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[BluetoothBleGattServerCallbackType](#enum-bluetoothblegattservercallbacktype)|是|另一个枚举值。|

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

**起始版本：** 19

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

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|