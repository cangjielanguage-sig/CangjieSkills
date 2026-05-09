## enum BluetoothBleCallbackType

```cangjie
public enum BluetoothBleCallbackType <: Equatable<BluetoothBleCallbackType> & Hashable & ToString {
    | AdvertisingStateChange
    | BleDeviceFind
    | ...
}
```

**功能：** 广播扫描订阅事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**父类型：**

- Equatable\<BluetoothBleCallbackType>
- Hashable
- ToString

### AdvertisingStateChange

```cangjie
AdvertisingStateChange
```

**功能：** 表示广播状态事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### BleDeviceFind

```cangjie
BleDeviceFind
```

**功能：** 表示BLE设备发现事件类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### func !=(BluetoothBleCallbackType)

```cangjie
public operator func !=(other: BluetoothBleCallbackType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BluetoothBleCallbackType](#enum-bluetoothblecallbacktype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(BluetoothBleCallbackType)

```cangjie
public operator func ==(other: BluetoothBleCallbackType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BluetoothBleCallbackType](#enum-bluetoothblecallbacktype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取枚举值的哈希值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Int64|枚举值的哈希值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举值的字符串表达。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表达。|