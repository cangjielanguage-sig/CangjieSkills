## class AbilityStageMonitor

```cangjie
public class AbilityStageMonitor {
    public var moduleName: String
    public var srcEntrance: String
    public init(
        moduleName: String,
        srcEntrance: String
    )
}
```

**功能：** [AbilityStageMonitor](#class-abilitystagemonitor)模块提供用于匹配满足指定条件的受监视的[AbilityStage](../AbilityKit/cj-apis-app-ability-ability_stage.md#class-abilitystage)对象的方法。最近匹配的[AbilityStage](../AbilityKit/cj-apis-app-ability-ability_stage.md#class-abilitystage)对象将保存在[AbilityStageMonitor](#class-abilitystagemonitor)中。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var moduleName

```cangjie
public var moduleName: String
```

**功能：** 要监视的abilityStage的模块名。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### var srcEntrance

```cangjie
public var srcEntrance: String
```

**功能：** 要监视的abilityStage的源路径。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### init(String, String)

```cangjie
public init(
    moduleName: String,
    srcEntrance: String
)
```

**功能：** 构造一个[AbilityStageMonitor](#class-abilitystagemonitor)对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|moduleName|String|是|-|要监视的abilityStage的模块名。|
|srcEntrance|String|是|-|要监视的abilityStage的源路径。|

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