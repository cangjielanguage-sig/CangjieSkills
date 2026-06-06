### func waitAbilityStageMonitor(AbilityStageMonitor, Int64)

```cangjie
public func waitAbilityStageMonitor(stageMonitor: AbilityStageMonitor, timeout: Int64): AbilityStage
```

**功能：** 等待并返回与给定[AbilityStageMonitor](#class-abilitystagemonitor)中设置的条件匹配的[AbilityStage](../AbilityKit/cj-apis-ability.md#class-abilitystage)对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|stageMonitor|[AbilityStageMonitor](#class-abilitystagemonitor)|是|-|[AbilityStageMonitor](#class-abilitystagemonitor)实例。|
|timeout|Int64|是|-|超时最大等待时间，以毫秒（ms）为单位。|

**返回值：**

|类型|说明|
|:----|:----|
|[AbilityStage](../AbilityKit/cj-apis-ability.md#class-abilitystage)|返回[AbilityStage](../AbilityKit/cj-apis-ability.md#class-abilitystage)对象。|

**异常：**

以下错误码详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :--- | :--- |
  | 401| Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
  | 16000100 | WaitAbilityStageMonitor failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.TestKit.*

let delegator = AbilityDelegatorRegistry.getAbilityDelegator()
let stageMonitor = AbilityStageMonitor("entry", "ohos_app_cangjie_entry.MyAbilityStage")
spawn {
    let abilityStage = delegator.waitAbilityStageMonitor(stageMonitor, 2000)
}
```