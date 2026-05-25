## enum SendSmsResult

```cangjie
public enum SendSmsResult <: Equatable<SendSmsResult> & ToString {
    | SEND_SMS_SUCCESS
    | SEND_SMS_FAILURE_UNKNOWN
    | SEND_SMS_FAILURE_RADIO_OFF
    | SEND_SMS_FAILURE_SERVICE_UNAVAILABLE
    | ...
}
```

**功能：** 短信发送结果。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**父类型：**

- Equatable\<SendSmsResult>
- ToString

### SEND_SMS_FAILURE_RADIO_OFF

```cangjie
SEND_SMS_FAILURE_RADIO_OFF
```

**功能：** 发送短信失败，原因为调制解调器关机。

**起始版本：** 19

### SEND_SMS_FAILURE_SERVICE_UNAVAILABLE

```cangjie
SEND_SMS_FAILURE_SERVICE_UNAVAILABLE
```

**功能：** 发送短信失败，原因为网络不可用、不支持发送或接收短信。

**起始版本：** 19

### SEND_SMS_FAILURE_UNKNOWN

```cangjie
SEND_SMS_FAILURE_UNKNOWN
```

**功能：** 发送短信失败，原因未知。

**起始版本：** 19

### SEND_SMS_SUCCESS

```cangjie
SEND_SMS_SUCCESS
```

**功能：** 发送短信成功。

**起始版本：** 19

### func !=(SendSmsResult)

```cangjie
public operator func !=(other: SendSmsResult): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SendSmsResult](#enum-sendsmsresult)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值是否不相等。|

### func ==(SendSmsResult)

```cangjie
public operator func ==(other: SendSmsResult): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[SendSmsResult](#enum-sendsmsresult)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值是否相等。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回字符串值。

**系统能力：** SystemCapability.Telephony.SmsMms

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回字符串值。|