### static func makeCall(String)

```cangjie
public static func makeCall(phoneNumber: String): Unit
```

**功能：** 跳转到拨号界面，并显示待拨出的号码。后台调用需要申请ohos.permission.START_ABILITIES_FROM_BACKGROUND权限。

> **说明：**
>
> 该接口为预埋接口，当前功能受限，推荐使用双参接口[makeCall](#static-func-makecalluiabilitycontext-string)。

**系统能力：** SystemCapability.Applications.Contacts

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|phoneNumber|String|是|-|电话号码。|

**异常：**

- BusinessException：对应错误码如下表，详见[电话子系统错误码](./cj-errorcode-telephony.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 8300001 | Invalid parameter value. |
  | 8300002 | Operation failed. Cannot connect to service. |
  | 8300003 | System internal error. |
  | 8300999 | Unknown error code. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TelephonyKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    Call.makeCall("138xxxxxxxx")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### static func makeCall(UIAbilityContext, String)

```cangjie
public static func makeCall(context: UIAbilityContext, phoneNumber: String): Unit
```

**功能：** 跳转到拨号界面，并显示待拨出的号码。后台调用需要申请ohos.permission.START_ABILITIES_FROM_BACKGROUND权限。

**系统能力：** SystemCapability.Applications.Contacts

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiabilitycontext)|是|-|应用上下文Context。|
|phoneNumber|String|是|-|电话号码。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 8300001 | Invalid parameter value. |
  | 8300002 | Operation failed. Cannot connect to service. |
  | 8300003 | System internal error. |
  | 8300999 | Unknown error code. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TelephonyKit.*
import ohos.app.ability.ui_ability.UIAbilityContext
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    Call.makeCall(Global.abilityContext, "138xxxxxxxx")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```