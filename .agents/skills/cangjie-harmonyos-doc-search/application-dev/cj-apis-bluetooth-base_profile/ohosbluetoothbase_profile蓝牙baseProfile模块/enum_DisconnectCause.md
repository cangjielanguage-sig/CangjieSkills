## enum DisconnectCause

```cangjie
public enum DisconnectCause <: Equatable<DisconnectCause> & ToString {
    | UserDisconnect
    | ConnectShouldFromKeyboard
    | ConnectShouldFromMouse
    | ConnectShouldFromCar
    | TooManyConnectedDevices
    | ConnectInternalFail
    | ...
}
```

**功能：** 连接失败原因。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**父类型：**

- Equatable\<DisconnectCause>
- ToString

### ConnectInternalFail

```cangjie
ConnectInternalFail
```

**功能：** 内部错误。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### ConnectShouldFromCar

```cangjie
ConnectShouldFromCar
```

**功能：** 应该从车机侧发起连接。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### ConnectShouldFromKeyboard

```cangjie
ConnectShouldFromKeyboard
```

**功能：** 应该从键盘侧发起连接。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### ConnectShouldFromMouse

```cangjie
ConnectShouldFromMouse
```

**功能：** 应该从鼠标侧发起连接。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### TooManyConnectedDevices

```cangjie
TooManyConnectedDevices
```

**功能：** 当前连接数超过上限。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### UserDisconnect

```cangjie
UserDisconnect
```

**功能：** 用户主动断开连接。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

### func !=(DisconnectCause)

```cangjie
public operator func !=(other: DisconnectCause): Bool
```

**功能：** 对连接失败原因进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DisconnectCause](#enum-disconnectcause)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果连接失败原因不同，返回true，否则返回false。|

### func ==(DisconnectCause)

```cangjie
public operator func ==(other: DisconnectCause): Bool
```

**功能：** 对连接失败原因进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[DisconnectCause](#enum-disconnectcause)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果连接失败原因相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回枚举值的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举值的字符串表示。|