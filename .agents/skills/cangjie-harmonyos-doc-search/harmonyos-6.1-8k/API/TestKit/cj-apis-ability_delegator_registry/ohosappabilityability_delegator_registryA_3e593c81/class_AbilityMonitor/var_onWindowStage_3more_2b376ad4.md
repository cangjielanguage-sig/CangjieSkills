### var onWindowStageDestroy

```cangjie
public var onWindowStageDestroy:?(UIAbility) -> Unit
```

**功能：** 当WindowStage被销毁前，触发该回调函数。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability))->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var onWindowStageRestore

```cangjie
public var onWindowStageRestore:?(UIAbility) -> Unit
```

**功能：** 当UIAbility跨端迁移时，目标端UIAbility恢复页面栈时，触发该回调函数。

**类型：** ?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability))->Unit

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### init(String, String, ?(UIAbility) -> Unit, ?(UIAbility) -> Unit, ?(UIAbility) -> Unit, ?(UIAbility) -> Unit, ?(UIAbility) -> Unit, ?(UIAbility) -> Unit, ?(UIAbility) -> Unit)

```cangjie
public init(
    abilityName: String,
    moduleName!: String = "",
    onAbilityCreate!: ?(UIAbility) -> Unit = None,
    onAbilityForeground!: ?(UIAbility) -> Unit = None,
    onAbilityBackground!: ?(UIAbility) -> Unit = None,
    onAbilityDestroy!: ?(UIAbility) -> Unit = None,
    onWindowStageCreate!: ?(UIAbility) -> Unit = None,
    onWindowStageRestore!: ?(UIAbility) -> Unit = None,
    onWindowStageDestroy!: ?(UIAbility) -> Unit = None
)
```

**功能：** 构造一个[AbilityMonitor](#class-abilitymonitor)对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|abilityName|String|是|-|被监听的UIAbility对象名称。|
|moduleName|String|否|""| **命名参数。** 被监听的UIAbility对象所属模块名称。|
|onAbilityCreate|?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)) -> Unit|否|None| **命名参数。** UIAbility对象被创建时，触发该回调函数。|
|onAbilityForeground|?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)) -> Unit|否|None| **命名参数。** UIAbility对象状态变成前台时，触发该回调函数。|
|onAbilityBackground|?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)) -> Unit|否|None| **命名参数。** UIAbility对象状态变成后台时，触发该回调函数。|
|onAbilityDestroy|?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)) -> Unit|否|None| **命名参数。** UIAbility对象被销毁前，触发该回调函数。|
|onWindowStageCreate|?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)) -> Unit|否|None| **命名参数。** 当WindowStage实例被创建时，触发该回调函数。|
|onWindowStageRestore|?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)) -> Unit|否|None| **命名参数。** 当UIAbility跨端迁移时，目标端UIAbility恢复页面栈时，触发该回调函数。|
|onWindowStageDestroy|?([UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)) -> Unit|否|None| **命名参数。** 当WindowStage被销毁前，触发该回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.TestKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let delegator = AbilityDelegatorRegistry.getAbilityDelegator()
    let monitor = AbilityMonitor(
        "EntryAbility", moduleName: "entry",
        onAbilityCreate: {ability => delegator.print("onAbilityCreate called, abilityName: ${ability.launchWant.abilityName}")}
    )
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```