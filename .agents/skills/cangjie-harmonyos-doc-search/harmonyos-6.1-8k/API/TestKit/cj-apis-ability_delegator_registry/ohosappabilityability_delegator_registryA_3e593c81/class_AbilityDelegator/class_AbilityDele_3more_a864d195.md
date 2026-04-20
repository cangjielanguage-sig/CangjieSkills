## class AbilityDelegator

```cangjie
public class AbilityDelegator {}
```

**功能：** AbilityDelegator用于创建并管理一个[AbilityMonitor](#class-abilitymonitor)对象（该对象用于监视指定[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)生命周期状态的变更），包括对[AbilityMonitor](#class-abilitymonitor)实例的添加、删除，等待[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)到达OnCreate生命周期、设置等待时间、获取指定Ability的生命周期状态、获取当前应用顶部[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)、启动指定[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)等。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### func addAbilityMonitor(AbilityMonitor)

```cangjie
public func addAbilityMonitor(monitor: AbilityMonitor): Unit
```

**功能：** 添加[AbilityMonitor](#class-abilitymonitor)实例。不支持多线程并发调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|monitor|[AbilityMonitor](#class-abilitymonitor)|是|-|[AbilityMonitor](#class-abilitymonitor)实例。|

**异常：**

以下错误码详细介绍请参见[元能力子系统错误码](../AbilityKit/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000100 | Calling AddAbilityMonitor failed. |

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
    let monitor = AbilityMonitor(
            "EntryAbility", moduleName: "entry",
            onAbilityCreate: {ability => delegator.print("onAbilityCreate called, abilityName: ${ability.launchWant.abilityName}")}
    )
    delegator.addAbilityMonitor(monitor)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func addAbilityStageMonitor(AbilityStageMonitor)

```cangjie
public func addAbilityStageMonitor(monitor: AbilityStageMonitor): Unit
```

**功能：** 添加一个[AbilityStageMonitor](#class-abilitystagemonitor)对象，用于监视指定[AbilityStage](../AbilityKit/cj-apis-app-ability-ability_stage.md#class-abilitystage)的生命周期状态更改。

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
  | 16000100 | Calling AddAbilityStageMonitor failed. |

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
    delegator.addAbilityStageMonitor(monitor)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```