### func print(String)

```cangjie
public func print(msg: String): Unit
```

**功能：** 打印日志信息到单元测试终端控制台。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|msg|String|是|-|日志字符串。|

**异常：**

以下错误码详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :--- | :--- |
  | 401| Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.TestKit.*

let delegator = AbilityDelegatorRegistry.getAbilityDelegator()
let msg = "msg"
delegator.print(msg)
```

### func removeAbilityMonitor(AbilityMonitor)

```cangjie
public func removeAbilityMonitor(monitor: AbilityMonitor): Unit
```

**功能：** 删除已经添加的[AbilityMonitor](#class-abilitymonitor)对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|monitor|[AbilityMonitor](#class-abilitymonitor)|是|-|[AbilityMonitor](#class-abilitymonitor)实例。|

**异常：**

以下错误码详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :--- | :--- |
  | 401| Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
  | 16000100 | RemoveAbilityMonitor failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.TestKit.*

let delegator = AbilityDelegatorRegistry.getAbilityDelegator()
let monitor = AbilityMonitor(
    "EntryAbility", moduleName: "entry",
    onAbilityCreate: {ability => delegator.print("onAbilityCreate called, abilityName: ${ability.launchWant.abilityName}")}
)
delegator.removeAbilityMonitor(monitor)
```

### func removeAbilityStageMonitor(AbilityStageMonitor)

```cangjie
public func removeAbilityStageMonitor(stageMonitor: AbilityStageMonitor): Unit
```

**功能：** 删除已经添加的[AbilityStageMonitor](#class-abilitystagemonitor)对象。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|stageMonitor|[AbilityStageMonitor](#class-abilitystagemonitor)|是|-|[AbilityStageMonitor](#class-abilitystagemonitor)实例。|

**异常：**

以下错误码详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :--- | :--- |
  | 401| Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
  | 16000100 | RemoveAbilityStageMonitor failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.TestKit.*

let delegator = AbilityDelegatorRegistry.getAbilityDelegator()
let monitor = AbilityStageMonitor("entry", "ohos_app_cangjie_entry.MyAbilityStage")
delegator.removeAbilityStageMonitor(monitor)
```