## enum CallState

```cangjie
public enum CallState <: Equatable<CallState> & ToString {
    | CALL_STATE_IDLE
    | CALL_STATE_INCOMING
    | CALL_STATE_ACTIVE
    | CALL_STATE_DIALING
    | CALL_STATE_WAITING
    | CALL_STATE_HOLDING
    | CALL_STATE_DISCONNECTING
    | ...
}
```

**功能：** 表示通话状态的枚举。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**父类型：**

- Equatable\<[CallState](#enum-callstate)>
- ToString

### CALL_STATE_ACTIVE

```cangjie
CALL_STATE_ACTIVE
```

**功能：** 接通。

**起始版本：** 19

### CALL_STATE_DIALING

```cangjie
CALL_STATE_DIALING
```

**功能：** 响铃。

**起始版本：** 19

### CALL_STATE_DISCONNECTING

```cangjie
CALL_STATE_DISCONNECTING
```

**功能：** 挂断。

**起始版本：** 19

### CALL_STATE_HOLDING

```cangjie
CALL_STATE_HOLDING
```

**功能：** 保持。

**起始版本：** 19

### CALL_STATE_IDLE

```cangjie
CALL_STATE_IDLE
```

**功能：** 空闲状态。

**起始版本：** 19

### CALL_STATE_INCOMING

```cangjie
CALL_STATE_INCOMING
```

**功能：** 来电。

**起始版本：** 19

### CALL_STATE_WAITING

```cangjie
CALL_STATE_WAITING
```

**功能：** 等待接通。

**起始版本：** 19

### func !=(CallState)

```cangjie
public operator func !=(other: CallState): Bool
```

**功能：** 判断两个枚举值是否不等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CallState](#enum-callstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值不等，返回true, 否则返回false。|

### func ==(CallState)

```cangjie
public operator func ==(other: CallState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CallState](#enum-callstate)|是|-|待比较的另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果两个枚举值相等，返回true, 否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取通话状态枚举的字符串表示。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|通话状态枚举的字符串表示。|