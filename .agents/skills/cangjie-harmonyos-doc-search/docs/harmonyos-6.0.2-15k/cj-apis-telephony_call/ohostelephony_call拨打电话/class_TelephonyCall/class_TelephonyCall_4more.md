## class TelephonyCall

```cangjie
public class TelephonyCall {}
```

**功能：** 拨打电话类，提供呼叫管理功能，包括拨打电话、跳转到拨号界面、获取通话状态、格式化电话号码等接口。

**起始版本：** 12

### static func formatPhoneNumber(String, NumberFormatOptions)

```cangjie
public static func formatPhoneNumber(phoneNumber: String,
    options!: NumberFormatOptions = NumberFormatOptions("CN")): String
```

**功能：** 格式化电话号码，可设置格式化参数。

电话号码格式化后为标准数字字串，例如：“138 xxxx xxxx”、“0755 xxxx xxxx”。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|phoneNumber|String|是|-|电话号码。|
|options|[NumberFormatOptions](#class-numberformatoptions)|否|NumberFormatOptions("CN")| **命名参数。** 格式化参数，如国家码。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回格式化电话号码的结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |8300001|Invalid parameter value.|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300999|Unknown error code.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let result = TelephonyCall.formatPhoneNumber("138xxxxxxxx", options: NumberFormatOptions("CN"))
```

### static func formatPhoneNumberToE164(String, String)

```cangjie
public static func formatPhoneNumberToE164(phoneNumber: String, countryCode: String): String
```

**功能：** 将电话号码格式化为E.164表示形式。

待格式化的电话号码需要与传入的国家码相匹配，如中国电话号码需要传入国家码CN，否则格式化后的电话号码为null。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|phoneNumber|String|是|-|电话号码。|
|countryCode|String|是|-|国家码，支持所有国家码，如：中国（CN）。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回将电话号码格式化为E.164表示形式的结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[电话子系统错误码](../../errorcodes/cj-errorcode-telephony.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |8300001|Invalid parameter value.|
  |8300002|Operation failed. Cannot connect to service.|
  |8300003|System internal error.|
  |8300999|Unknown error code.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let result = TelephonyCall.formatPhoneNumberToE164("138xxxxxxxx", "CN")
```

### static func getCallState()

```cangjie
public static func getCallState(): CallState
```

**功能：** 获取当前通话状态。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[CallState](#enum-callstate)|返回获取到的通话状态。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let result: CallState = TelephonyCall.getCallState()
```