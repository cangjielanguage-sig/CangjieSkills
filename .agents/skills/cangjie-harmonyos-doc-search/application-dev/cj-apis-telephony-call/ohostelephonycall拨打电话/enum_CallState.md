## enum CallState

```cangjie
public enum CallState <: Equatable<CallState> & ToString {
    | CallStateUnknown
    | CallStateIdle
    | CallStateRinging
    | CallStateOffhook
    | CallStateAnswered
    | ...
}
```

**功能：** 通话状态码。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

**父类型：**

- Equatable\<CallState>
- ToString

### CallStateAnswered

```cangjie
CallStateAnswered
```

**功能：** 表示来电已经接听。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

### CallStateIdle

```cangjie
CallStateIdle
```

**功能：** 表示没有正在进行的呼叫。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

### CallStateOffhook

```cangjie
CallStateOffhook
```

**功能：** 表示至少有一个呼叫处于拨号、通话中或呼叫保持状态，并且没有新的来电振铃或等待。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

### CallStateRinging

```cangjie
CallStateRinging
```

**功能：** 表示来电正在振铃或等待。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

### CallStateUnknown

```cangjie
CallStateUnknown
```

**功能：** 无效状态，当获取呼叫状态失败时返回。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

### func !=(CallState)

```cangjie
public operator func !=(other: CallState): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CallState](#enum-callstate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CallState)

```cangjie
public operator func ==(other: CallState): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CallState](#enum-callstate)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|