## class NumberFormatOptions

```cangjie
public class NumberFormatOptions {
    public let countryCode: String
    public init(countryCode: String)
}
```

**功能：** 格式化号码的可选参数。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 12

### let countryCode

```cangjie
public let countryCode: String
```

**功能：** 国家码，支持所有国家的国家码，如：CN（中国）。默认为：CN。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### init(String)

```cangjie
public init(countryCode: String)
```

**功能：** 用于创建NumberFormatOptions实例的构造函数。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|countryCode|String|是|-|国家码，支持所有国家的国家码，如：CN（中国）。默认为：CN。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let op = NumberFormatOptions("CN")
```

## enum CallState

```cangjie
public enum CallState {
    | CALL_STATE_UNKNOWN
    | CALL_STATE_IDLE
    | CALL_STATE_RINGING
    | CALL_STATE_OFFHOOK
    | CALL_STATE_ANSWERED
    | ...
}
```

**功能：** 通话状态码。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 12

### CALL_STATE_ANSWERED

```cangjie
CALL_STATE_ANSWERED
```

**功能：** 表示来电已经接听。

**起始版本：** 19

### CALL_STATE_IDLE

```cangjie
CALL_STATE_IDLE
```

**功能：** 表示没有正在进行的呼叫。

**起始版本：** 12

### CALL_STATE_OFFHOOK

```cangjie
CALL_STATE_OFFHOOK
```

**功能：** 表示至少有一个呼叫处于拨号、通话中或呼叫保持状态，并且没有新的来电振铃或等待。

**起始版本：** 12

### CALL_STATE_RINGING

```cangjie
CALL_STATE_RINGING
```

**功能：** 表示来电正在振铃或等待。

**起始版本：** 12

### CALL_STATE_UNKNOWN

```cangjie
CALL_STATE_UNKNOWN
```

**功能：** 无效状态，当获取呼叫状态失败时返回。

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): Int32
```

**功能：** 获取枚举类型对应的数值。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Int32|枚举类型对应的数值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let i = CallState.CALL_STATE_IDLE.getValue()
```

## enum EmergencyNumberOptions

```cangjie
public enum EmergencyNumberOptions {
    | SLOT_ID_ONE
    | SLOT_ID_TWO
    | ...
}
```

**功能：** 函数isEmergencyPhoneNumber的可选参数。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 12

### SLOT_ID_ONE

```cangjie
SLOT_ID_ONE
```

**功能：** 卡槽1。

**起始版本：** 12

### SLOT_ID_TWO

```cangjie
SLOT_ID_TWO
```

**功能：** 卡槽2。

**起始版本：** 12