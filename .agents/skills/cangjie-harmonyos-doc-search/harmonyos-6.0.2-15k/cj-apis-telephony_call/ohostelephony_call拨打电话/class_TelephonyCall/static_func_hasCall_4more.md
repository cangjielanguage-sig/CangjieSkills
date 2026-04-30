### static func hasCall()

```cangjie
public static func hasCall(): Bool
```

**功能：** 判断是否存在通话。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回判断是否存在通话。返回true表示当前存在通话，false表示当前不存在通话。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let result: Bool = TelephonyCall.hasCall()
```

### static func hasVoiceCapability()

```cangjie
public static func hasVoiceCapability(): Bool
```

**功能：** 检查当前设备是否具备语音通话能力。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回判断是否具备语音通话能力。返回true表示设备具备语音通话能力，返回false表示设备不具备语音通话能力。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.TelephonyKit.*

let result: Bool = TelephonyCall.hasVoiceCapability()
```

### static func isEmergencyPhoneNumber(String, EmergencyNumberOptions)

```cangjie
public static func isEmergencyPhoneNumber(phoneNumber: String, options: EmergencyNumberOptions): Bool
```

**功能：** 根据电话号码参数，判断是否是紧急电话号码。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|phoneNumber|String|是|-|电话号码。|
|options|[EmergencyNumberOptions](#enum-emergencynumberoptions)|是|-|电话号码参数。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回判断是否是紧急电话号码的结果。返回true表示是紧急电话号码，返回false表示不是紧急电话号码。|

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

let result = TelephonyCall.isEmergencyPhoneNumber("138xxxxxxxx", EmergencyNumberOptions.SLOT_ID_ONE)
```

### static func isEmergencyPhoneNumber(String)

```cangjie
public static func isEmergencyPhoneNumber(phoneNumber: String): Bool
```

**功能：** 判断是否是紧急电话号码。

**系统能力：** SystemCapability.Telephony.CallManager

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|phoneNumber|String|是|-|电话号码。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回判断是否是紧急电话号码的结果。返回true表示是紧急电话号码，返回false表示不是紧急电话号码。|

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

let result: Bool = TelephonyCall.isEmergencyPhoneNumber("138xxxxxxxx")
```