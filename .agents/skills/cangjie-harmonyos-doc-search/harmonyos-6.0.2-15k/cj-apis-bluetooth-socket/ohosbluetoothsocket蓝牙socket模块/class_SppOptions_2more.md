## class SppOptions

```cangjie
public class SppOptions {
    public var uuid: String
    public var secure: Bool
    public var sppType: SppType
    public SppOptions(uuid: String, secure: Bool, sppType: SppType)
}
```

**功能：** 描述spp的配置参数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 20

### var secure

```cangjie
public var secure: Bool
```

**功能：**  是否是安全通道。true表示是安全通道，false表示非安全通道。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 20

### var sppType

```cangjie
public var sppType: SppType
```

**功能：** Spp链路类型。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** [SppType](#enum-spptype)

**读写能力：** 可读写

**起始版本：** 20

### var uuid

```cangjie
public var uuid: String
```

**功能：** spp单据的uuid。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 20

### SppOptions(String, Bool, SppType)

```cangjie
public SppOptions(uuid: String, secure: Bool, sppType: SppType)
```

**功能：** 构造函数。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uuid|String|是|-|spp单据的uuid。|
|secure|Bool|是|-|是否是安全通道。true表示是安全通道，false表示非安全通道。|
|sppType|[SppType](#enum-spptype)|是|-|Spp链路类型。|

## enum BluetoothSocketCallbackType

```cangjie
public enum BluetoothSocketCallbackType <: ToString & Equatable<BluetoothSocketCallbackType> {
    SppRead |
    ...
}
```

**功能：** spp请求事件。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**父类型：**

- ToString
- [Equatable\<BluetoothSocketCallbackType>](#enum-bluetoothsocketcallbacktype)

### SppRead

```cangjie
SppRead
```

**功能：** spp请求事件。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 20

### func !=(BluetoothSocketCallbackType)

```cangjie
public operator func !=(other: BluetoothSocketCallbackType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BluetoothSocketCallbackType](#enum-bluetoothsocketcallbacktype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值是否不相等。|

### func ==(BluetoothSocketCallbackType)

```cangjie
public operator func ==(other: BluetoothSocketCallbackType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[BluetoothSocketCallbackType](#enum-bluetoothsocketcallbacktype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值是否相等。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 枚举值的字符串表达。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表达。|