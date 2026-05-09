### func getCurrentTopAbility()

```cangjie
public func getCurrentTopAbility(): UIAbility
```

**功能：** 获取当前应用顶部[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)|返回[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)实例。|

**异常：**

以下错误码详细介绍请参见[元能力子系统错误码](../AbilityKit/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000050 | Internal error. |
  | 16000100 | Calling GetCurrentTopAbility failed. |

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
    let ability = delegator.getCurrentTopAbility()
    delegator.getAbilityState(ability)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func print(String)

```cangjie
public func print(msg: String): Unit
```

**功能：** 打印日志信息到单元测试终端控制台。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|msg|String|是|-|日志字符串。|

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
    let msg = "msg"
    delegator.print(msg)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func removeAbilityMonitor(AbilityMonitor)

```cangjie
public func removeAbilityMonitor(monitor: AbilityMonitor): Unit
```

**功能：** 删除已经添加的[AbilityMonitor](#class-abilitymonitor)实例。

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
  | 16000100 | Calling RemoveAbilityMonitor failed. |

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
    delegator.removeAbilityMonitor(monitor)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```