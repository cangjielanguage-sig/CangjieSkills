## enum BluetoothAccessCallbackType

```cangjie
public enum BluetoothAccessCallbackType <: Equatable<BluetoothAccessCallbackType> & Hashable & ToString {
    | STATE_CHANGE
    | ...
}
```

**功能：** on/off事件的类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<BluetoothAccessCallbackType>
- Hashable
- ToString

### STATE_CHANGE

```cangjie
STATE_CHANGE
```

**功能：** 表示蓝牙状态改变事件。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(BluetoothAccessCallbackType)

```cangjie
public operator func !=(other: BluetoothAccessCallbackType): Bool
```

**功能：** 对回调事件类型进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[BluetoothAccessCallbackType](#enum-bluetoothaccesscallbacktype)|是|相比较的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两回调事件类型不同返回 true，否则返回 false。|

### func ==(BluetoothAccessCallbackType)

```cangjie
public operator func ==(other: BluetoothAccessCallbackType): Bool
```

**功能：** 对回调事件类型进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[BluetoothAccessCallbackType](#enum-bluetoothaccesscallbacktype)|是|相比较的回调事件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两回调事件类型相同返回 true，否则返回 false。|

### func hashCode()

```cangjie
public func hashCode(): Int64
```

**功能：** 获取回调事件类型的哈希值。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|回调事件类型的哈希值。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回回调事件的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|事件的字符串表示。|