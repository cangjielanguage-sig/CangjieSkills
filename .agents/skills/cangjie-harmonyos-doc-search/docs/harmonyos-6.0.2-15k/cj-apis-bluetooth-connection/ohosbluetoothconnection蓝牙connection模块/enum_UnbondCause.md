## enum UnbondCause

```cangjie
public enum UnbondCause <: Equatable<UnbondCause> & ToString {
    | USER_REMOVED
    | REMOTE_DEVICE_DOWN
    | AUTH_FAILURE
    | AUTH_REJECTED
    | INTERNAL_ERROR
    | ...
}
```

**功能：** 配对失败原因。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**父类型：**

- Equatable\<UnbondCause>
- ToString

### AUTH_FAILURE

```cangjie
AUTH_FAILURE
```

**功能：** PIN码错误。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### AUTH_REJECTED

```cangjie
AUTH_REJECTED
```

**功能：** 远端设备鉴权拒绝。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### INTERNAL_ERROR

```cangjie
INTERNAL_ERROR
```

**功能：** 内部错误。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### REMOTE_DEVICE_DOWN

```cangjie
REMOTE_DEVICE_DOWN
```

**功能：** 远端设备关闭。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### USER_REMOVED

```cangjie
USER_REMOVED
```

**功能：** 用户主动移除设备。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

### func !=(UnbondCause)

```cangjie
public operator func !=(other: UnbondCause): Bool
```

**功能：** 对配对失败原因进行判不等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[UnbondCause](#enum-unbondcause)|是|配对失败原因。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个配对失败原因不同返回 true，否则返回 false。|

### func ==(UnbondCause)

```cangjie
public operator func ==(other: UnbondCause): Bool
```

**功能：** 对配对失败原因进行判等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|other|[UnbondCause](#enum-unbondcause)|是|配对失败原因。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果配对失败原因相同返回 true，否则返回 false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回配对失败原因的字符串表示。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|配对失败原因的字符串表示。|