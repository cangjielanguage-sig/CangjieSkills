## enum DisconnectCause

```cangjie
public enum DisconnectCause <: Equatable<DisconnectCause> & ToString {
    | USER_DISCONNECT
    | CONNECT_FROM_KEYBOARD
    | CONNECT_FROM_MOUSE
    | CONNECT_FROM_CAR
    | TOO_MANY_CONNECTED_DEVICES
    | CONNECT_FAIL_INTERNAL
    | ...
}
```

**功能：** 连接失败原因。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<DisconnectCause>
- ToString

### CONNECT_FAIL_INTERNAL

```cangjie
CONNECT_FAIL_INTERNAL
```

**功能：** 内部错误。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CONNECT_FROM_CAR

```cangjie
CONNECT_FROM_CAR
```

**功能：** 应该从车机侧发起连接。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CONNECT_FROM_KEYBOARD

```cangjie
CONNECT_FROM_KEYBOARD
```

**功能：** 应该从键盘侧发起连接。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### CONNECT_FROM_MOUSE

```cangjie
CONNECT_FROM_MOUSE
```

**功能：** 应该从鼠标侧发起连接。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### TOO_MANY_CONNECTED_DEVICES

```cangjie
TOO_MANY_CONNECTED_DEVICES
```

**功能：** 当前连接数超过上限。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### USER_DISCONNECT

```cangjie
USER_DISCONNECT
```

**功能：** 用户主动断开连接。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(DisconnectCause)

```cangjie
public operator func !=(other: DisconnectCause): Bool
```

**功能：** 对连接失败原因进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[DisconnectCause](#enum-disconnectcause)|是|连接失败原因。|

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

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[DisconnectCause](#enum-disconnectcause)|是|连接失败原因。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果连接失败原因相同，返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回连接失败原因的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|连接失败原因的字符串表示。|