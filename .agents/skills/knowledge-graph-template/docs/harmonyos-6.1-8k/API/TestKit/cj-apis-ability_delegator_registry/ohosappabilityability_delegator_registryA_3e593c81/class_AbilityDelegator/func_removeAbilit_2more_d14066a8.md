### func removeAbilityStageMonitor(AbilityStageMonitor)

```cangjie
public func removeAbilityStageMonitor(monitor: AbilityStageMonitor): Unit
```

**功能：** 从应用程序内存中删除指定的AbilityStageMonitor对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|monitor|[AbilityStageMonitor](#class-abilitystagemonitor)|是|-|[AbilityStageMonitor](#class-abilitystagemonitor)实例。|

**异常：**

以下错误码详细介绍请参见[元能力子系统错误码](../AbilityKit/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000100 | Calling RemoveAbilityStageMonitor failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let delegator = AbilityDelegatorRegistry.getAbilityDelegator()
    let monitor = AbilityStageMonitor("entry", "ohos_app_cangjie_entry.MyAbilityStage")
    delegator.removeAbilityStageMonitor(monitor)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func startAbility(Want)

```cangjie
public func startAbility(want: Want): Unit
```

**功能：** 启动指定[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](../AbilityKit/cj-apis-app-ability-want.md#class-want)|是|-|启动[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)参数。|

**异常：**

以下错误码详细介绍请参见[元能力子系统错误码](../AbilityKit/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000001 | The specified ability does not exist. |
  | 16000002 | Incorrect ability type. |
  | 16000004 | Cannot start an invisible component. |
  | 16000005 | The specified process does not have the permission. |
  | 16000006 | Cross-user operations are not allowed. |
  | 16000008 | The crowdtesting application expires. |
  | 16000009 | An ability cannot be started or stopped in Wukong mode. |
  | 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
  | 16000011 | The context does not exist. |
  | 16000012 | The application is controlled. |
  | 16000013 | The application is controlled by EDM. |
  | 16000050 | Internal error. |
  | 16000053 | The ability is not on the top of the UI. |
  | 16000055 | Installation-free timed out. |
  | 16200001 | The caller has been released. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*
import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let delegator = AbilityDelegatorRegistry.getAbilityDelegator()
    let want = Want(bundleName: "com.example.myapplication", abilityName: "EntryAbility")
    delegator.startAbility(want)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```