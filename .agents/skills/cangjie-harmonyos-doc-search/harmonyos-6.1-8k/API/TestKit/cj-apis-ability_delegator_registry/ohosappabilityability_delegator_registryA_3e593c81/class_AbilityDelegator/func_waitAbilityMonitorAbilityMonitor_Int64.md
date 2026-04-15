### func waitAbilityMonitor(AbilityMonitor, Int64)

```cangjie
public func waitAbilityMonitor(monitor: AbilityMonitor, timeout!: Int64 = 5000): UIAbility
```

**功能：** 设置等待时间，并等待与[AbilityMonitor](#class-abilitymonitor)实例匹配的[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)到达[onCreate](../AbilityKit/cj-apis-app-ability-ui_ability.md#func-oncreatewant-launchparam)生命周期，并返回[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)实例。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|monitor|[AbilityMonitor](#class-abilitymonitor)|是|-|[AbilityMonitor](#class-abilitymonitor)实例。|
|timeout|Int64|否|5000|**命名参数。** 最大等待时间，单位毫秒（ms），默认值为5000毫秒。   |

**返回值：**

|类型|说明|
|:----|:----|
|[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)|返回[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)实例。|

**异常：**

以下错误码详细介绍请参见[元能力子系统错误码](../AbilityKit/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000050 | Internal error. |
  | 16000100 | Calling WaitAbilityMonitor failed. |

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
    let monitor = AbilityMonitor("EntryAbility", moduleName: "entry",
        onAbilityCreate: {ability => delegator.print("call onAbilityCreate success!")}
    )
    spawn {
        let ability = delegator.waitAbilityMonitor(monitor)
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```