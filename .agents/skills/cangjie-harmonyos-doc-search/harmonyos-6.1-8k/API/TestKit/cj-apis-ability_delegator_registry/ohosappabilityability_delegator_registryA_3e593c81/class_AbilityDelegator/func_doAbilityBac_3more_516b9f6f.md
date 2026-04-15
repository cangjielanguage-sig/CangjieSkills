### func doAbilityBackground(UIAbility)

```cangjie
public func doAbilityBackground(ability: UIAbility): Unit
```

**功能：** 调度指定[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)生命周期状态到Background状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ability|[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)|是|-|指定[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)对象。|

**异常：**

以下错误码详细介绍请参见[元能力子系统错误码](../AbilityKit/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000100 | Calling DoAbilityBackground failed. |

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
    delegator.doAbilityBackground(ability)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func doAbilityForeground(UIAbility)

```cangjie
public func doAbilityForeground(ability: UIAbility): Unit
```

**功能：** 调度指定[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)生命周期状态到Foreground状态。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ability|[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)|是|-|指定[UIAbility](../AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)对象。|

**异常：**

以下错误码详细介绍请参见[元能力子系统错误码](../AbilityKit/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 16000100 | Calling DoAbilityForeground failed. |

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
    delegator.doAbilityForeground(ability)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func executeShellCommand(String, Int64)

```cangjie
public func executeShellCommand(cmd: String, timeoutSecs!: Int64 = 0): ShellCmdResult
```

**功能：** 指定超时时间，并执行指定的shell命令。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cmd|String|是|-|Shell命令字符串。|
|timeoutSecs|Int64|否|0|**命名参数。** 设定命令超时时间，单位秒（s）。|

**返回值：**

|类型|说明|
|:----|:----|
|[ShellCmdResult](#class-shellcmdresult)|返回Shell命令执行结果[ShellCmdResult](#class-shellcmdresult)对象。|

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
    let cmd = "cmd"
    delegator.executeShellCommand(cmd, timeoutSecs: 2)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```