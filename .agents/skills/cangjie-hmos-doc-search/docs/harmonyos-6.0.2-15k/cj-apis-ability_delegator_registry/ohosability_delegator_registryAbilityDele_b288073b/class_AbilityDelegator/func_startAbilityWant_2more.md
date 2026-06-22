### func startAbility(Want)

```cangjie
public func startAbility(want: Want): Future<Unit>
```

**功能：** 启动指定[UIAbility](../../../cj-apis-ability/.overview.md)。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](../../../cj-apis-ability/.overview.md)|是|-|启动[UIAbility](../../../cj-apis-ability/.overview.md)参数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.TestKit.*

let delegator = AbilityDelegatorRegistry.getAbilityDelegator()
let want = Want(bundleName: "com.example.myapplication", abilityName: "EntryAbility")
delegator.startAbility(want).get()
```

### func waitAbilityMonitor(AbilityMonitor)

```cangjie
public func waitAbilityMonitor(monitor: AbilityMonitor): UIAbility
```

**功能：** 等待与[AbilityMonitor](#class-abilitymonitor)实例匹配的[UIAbility](../../../cj-apis-ability/.overview.md)到达[onCreate](../../../cj-apis-ability/.overview.md)生命周期，并返回[UIAbility](../../../cj-apis-ability/.overview.md)实例。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|monitor|[AbilityMonitor](#class-abilitymonitor)|是|-|[AbilityMonitor](#class-abilitymonitor)实例。|

**返回值：**

|类型|说明|
|:----|:----|
|[UIAbility](../../../cj-apis-ability/.overview.md)|返回[UIAbility](../../../cj-apis-ability/.overview.md)实例。|

**异常：**

以下错误码详细介绍请参见[通用错误码](../../../cj-errorcode-universal/cj-errorcode-universal.md)和[元能力子系统错误码](../../../cj-errorcode-ability/cj-errorcode-ability.md)。

  | 错误码ID | 错误信息 |
  | :--- | :--- |
  | 401| Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
  | 16000100 | WaitAbilityMonitor failed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.TestKit.*

let delegator = AbilityDelegatorRegistry.getAbilityDelegator()
let monitor = AbilityMonitor("EntryAbility", moduleName: "entry",
    onAbilityCreate: {ability => delegator.print("call onAbilityCreate success!")}
)
spawn {
    let ability = delegator.waitAbilityMonitor(monitor)
}
```