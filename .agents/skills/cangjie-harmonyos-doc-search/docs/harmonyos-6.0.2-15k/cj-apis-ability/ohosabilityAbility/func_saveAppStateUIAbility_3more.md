## func saveAppState(?UIAbilityContext)

```cangjie
public func saveAppState(context!: ?UIAbilityContext = None): Bool
```

**功能：** 保存当前App状态，可以配合[ErrorManager](#class-errormanager)相关接口使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|?[UIAbilityContext](#class-uiabilitycontext)|否|None| **命名参数。** 需要保存状态的Ability所对应的context。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：保存成功，false：保存失败。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

AppLog.info("saveAppState")
saveAppState()
```

## func setRestartWant(Want)

```cangjie
public func setRestartWant(want: Want): Unit
```

**功能：** 设置下次恢复主动拉起场景下的Ability。该Ability必须为当前包下的Ability。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](#class-want)|是|-|通过设置Want中"bundleName"和"abilityName"字段来指定恢复重启的Ability。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let want = Want(bundleName: "com.example.apprecoverytest", abilityName: "EntryAbility")
setRestartWant(want)
```

## func trigger(WantAgent, TriggerInfo, (CompleteData) -> Unit)

```cangjie
public func trigger(agent: WantAgent, triggerInfo: TriggerInfo,
    callback!: (CompleteData) -> Unit = {_: CompleteData => ()}): Unit
```

**功能：** 主动激发WantAgent实例（callback形式）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|agent|[WantAgent](#class-wantagent)|是|-|WantAgent对象。|
|triggerInfo|[TriggerInfo](#class-triggerinfo)|是|-|TriggerInfo对象。|
|callback|([CompleteData](#class-completedata))->Unit|否|{ _: CompleteData =>() }| **命名参数。** 主动激发WantAgent实例的回调方法。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let wantAgentInfo = WantAgentInfo(
    wants: [Want(deviceId: "deviceId", bundleName: "com.example.myapplication",
    abilityName: "EntryAbility")], actionType: START_ABILITIES,
    requestCode: 0, actionFlags: [UPDATE_PRESENT_FLAG])
let wantAgent = getWantAgent(wantAgentInfo)
let triggerInfo = TriggerInfo(code: 2)
let callback = {
    value: CompleteData =>
    AppLog.info("wantAgentTrigger: ${value.want.deviceId}")
    AppLog.info("wantAgentTrigger: ${value.want.bundleName}")
    AppLog.info("wantAgentTrigger: ${value.want.parameters}")
    AppLog.info("wantAgentTrigger: ${value.finalCode}")
    AppLog.info("wantAgentTrigger: ${value.finalData}")
}
trigger(wantAgent, triggerInfo, callback: callback)
```