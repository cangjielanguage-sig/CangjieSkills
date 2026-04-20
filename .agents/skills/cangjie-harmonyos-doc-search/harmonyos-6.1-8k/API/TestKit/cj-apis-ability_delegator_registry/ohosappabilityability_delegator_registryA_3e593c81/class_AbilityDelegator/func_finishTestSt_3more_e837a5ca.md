### func finishTest(String, Int64)

```cangjie
public func finishTest(msg: String, code: Int64): Unit
```

**功能：** 结束测试并打印日志信息到单元测试终端控制台。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|msg|String|是|-|日志字符串。|
|code|Int64|是|-|日志码。|

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
    delegator.finishTest(msg, 0)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getAbilityState(UIAbility)

```cangjie
public func getAbilityState(ability: UIAbility): AbilityLifecycleState
```

**功能：** 获取指定ability的生命周期状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ability|[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)|是|-|指定[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[AbilityLifecycleState](#enum-abilitylifecyclestate)|指定ability的生命周期状态。|

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

### func getAppContext()

```cangjie
public func getAppContext(): Context
```

**功能：** 获取应用Context。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Context](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)|应用Context。|

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
    let context = delegator.getAppContext()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```