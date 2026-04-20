## func requestEnableNotification()

```cangjie
public func requestEnableNotification(): Unit
```

**功能：** 应用请求通知使能。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NotificationKit.*

try {
    requestEnableNotification()
    AppLog.info("requestEnableNotification success")
} catch (e: Exception) {
    AppLog.info("requestEnableNotification fail because ${e}")
}
```

## func requestEnableNotification(UIAbilityContext)

```cangjie
public func requestEnableNotification(context: UIAbilityContext): Unit
```

**功能：** 应用请求通知使能模态弹窗。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[UIAbilityContext](../AbilityKit/cj-apis-ability.md#class-uiabilitycontext)|是|-|通知弹窗绑定Ability的上下文。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.*
import kit.NotificationKit.*
import kit.AbilityKit.*
import kit.ArkUI.*

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.")
        spawn {
            AppLog.info("enable notification")
            let globalAbilityContext = this.context
            requestEnableNotification(globalAbilityContext)
            AppLog.info("enable notification success")
        }
        AppLog.info("MainAbility OnCreated end.")
    }
}
```

## func setBadgeNumber(Int32)

```cangjie
public func setBadgeNumber(badgeNumber: Int32): Unit
```

**功能：** 设定角标个数，在应用的桌面图标上呈现。

**系统能力：** SystemCapability.Notification.Notification

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|badgeNumber|Int32|是|-|角标个数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通知管理错误码](../../errorcodes/cj-errorcode-notification.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1600001|Internal error.|
  |1600002|Marshalling or unmarshalling error.|
  |1600003|Failed to connect service.|
  |1600012|No memory space.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NotificationKit.*

let badgeNumber: Int32 = 10
try {
    setBadgeNumber(badgeNumber)
    AppLog.info("setBadgeNumber success")
} catch (e: Exception) {
    AppLog.info("call setBadgeNumber fail because ${e}")
}
```