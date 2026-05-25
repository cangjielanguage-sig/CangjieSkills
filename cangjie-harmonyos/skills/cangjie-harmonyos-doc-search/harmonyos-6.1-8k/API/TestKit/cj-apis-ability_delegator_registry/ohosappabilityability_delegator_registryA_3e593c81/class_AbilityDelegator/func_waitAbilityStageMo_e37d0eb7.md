### func waitAbilityStageMonitor(AbilityStageMonitor, Int64)

```cangjie
public func waitAbilityStageMonitor(monitor: AbilityStageMonitor, timeout!: Int64 = 5000): AbilityStage
```

**功能：** 在指定的超时最大等待时间内，等待并返回与给定[AbilityStageMonitor](#class-abilitystagemonitor)中设置的条件匹配的[AbilityStage](../AbilityKit/cj-apis-app-ability-ability_stage.md#class-abilitystage)对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|monitor|[AbilityStageMonitor](#class-abilitystagemonitor)|是|-|[AbilityStageMonitor](#class-abilitystagemonitor)实例。|
|timeout|Int64|否|5000|**命名参数。** 超时最大等待时间，单位毫秒（ms），默认值为5000毫秒。|

**返回值：**

|类型|说明|
|:----|:----|
|[AbilityStage](../AbilityKit/cj-apis-app-ability-ability_stage.md#class-abilitystage)|返回[AbilityStage](../AbilityKit/cj-apis-app-ability-ability_stage.md#class-abilitystage)对象。|

**异常：**

以下错误码详细介绍请参见[元能力子系统错误码](../AbilityKit/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000050 | Internal error. |
  | 16000100 | Calling WaitAbilityStageMonitor failed. |

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
    let stageMonitor = AbilityStageMonitor("entry", "ohos_app_cangjie_entry.MyAbilityStage")
    spawn {
        let abilityStage = delegator.waitAbilityStageMonitor(stageMonitor, timeout: 2000)
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```