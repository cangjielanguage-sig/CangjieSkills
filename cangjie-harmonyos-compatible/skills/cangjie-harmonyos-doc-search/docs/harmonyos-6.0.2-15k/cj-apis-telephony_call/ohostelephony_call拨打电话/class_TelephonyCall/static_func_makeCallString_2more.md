### static func makeCall(String)

```cangjie
public static func makeCall(phoneNumber: String): Unit
```

**功能：** 跳转到拨号界面，并显示待拨出的号码。后台调用需要申请ohos.permission.START_ABILITIES_FROM_BACKGROUND权限。

**系统能力：** SystemCapability.Applications.Contacts

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|phoneNumber|String|是|-|电话号码。|

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
import ohos.ability.UIAbilityContext

TelephonyCall.makeCall("138xxxxxxxx")
```

### static func makeCall(UIAbilityContext, String)

```cangjie
public static func makeCall(context: UIAbilityContext, phoneNumber: String): Unit
```

**功能：** 跳转到拨号界面，并显示待拨出的号码。后台调用需要申请ohos.permission.START_ABILITIES_FROM_BACKGROUND权限。

**系统能力：** SystemCapability.Applications.Contacts

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext)|是|-|应用上下文Context。|
|phoneNumber|String|是|-|电话号码。|

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
import ohos.ability.UIAbilityContext

var ctx = Option<UIAbilityContext>.None

TelephonyCall.makeCall(ctx.getOrThrow(), "138xxxxxxxx")
```