## func enableAppRecovery(RestartFlag, SaveOccasionFlag, SaveModeFlag)

```cangjie
public func enableAppRecovery(restart!: RestartFlag = ALWAYS_RESTART,
    saveOccasion!: SaveOccasionFlag = SAVE_WHEN_ERROR, saveMode!: SaveModeFlag = SAVE_WITH_FILE): Unit
```

**功能：** 使能应用恢复功能，参数按顺序填入。该接口调用后，应用从启动器启动时第一个Ability支持恢复。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|restart|[RestartFlag](#enum-restartflag)|否|ALWAYS_RESTART| **命名参数。** 发生对应故障时是否重启。|
|saveOccasion|[SaveOccasionFlag](#enum-saveoccasionflag)|否|SAVE_WHEN_ERROR| **命名参数。** 状态保存时机。|
|saveMode|[SaveModeFlag](#enum-savemodeflag)|否|SAVE_WITH_FILE| **命名参数。** 状态保存方式。|

**示例：**

<!-- compile -->

```cangjie
// ability_stage.cj

import ohos.base.*
import kit.AbilityKit.*

class MyAbilityStage <: AbilityStage {
    public override func onCreate(): Unit {
        AppLog.info("MyAbilityStage onCreated.")
        enableAppRecovery()
    }
}
```

## func equal(WantAgent, WantAgent)

```cangjie
public func equal(agent: WantAgent, otherAgent: WantAgent): Bool
```

**功能：** 判断两个WantAgent实例是否相等，以此来判断是否是来自同一应用的相同操作。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|agent|[WantAgent](#class-wantagent)|是|WantAgent对象。|
|otherAgent|[WantAgent](#class-wantagent)|是|WantAgent对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示两个WantAgent实例相等，false表示两个WantAgent实例不相等。|

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

let wantAgentInfo1 = WantAgentInfo(
    wants: [Want(deviceId: "deviceId", bundleName: "com.example.myapplication",
    abilityName: "EntryAbility")], actionType: START_ABILITIES, requestCode: 0,
    actionFlags: [UPDATE_PRESENT_FLAG])
let wantAgent1 = getWantAgent(wantAgentInfo1)
let wantAgentInfo2 = WantAgentInfo(
    wants: [Want(deviceId: "deviceId", bundleName: "com.example.myapplication",
    abilityName: "EntryAbility")], actionType: START_ABILITIES, requestCode: 0,
    actionFlags: [UPDATE_PRESENT_FLAG])
let wantAgent2 = getWantAgent(wantAgentInfo2)
let isEqual = equal(wantAgent1, wantAgent2)
AppLog.info("isEqual is ${isEqual}")
```

## func getAppMemorySize()

```cangjie
public func getAppMemorySize(): Int32
```

**功能：** 获取当前应用程序可以使用的内存的值。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int32|获取当前应用程序可以使用的内存的值，可根据此值进行错误处理或其他自定义处理，单位是M。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16000050|Internal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let value = getAppMemorySize()
AppLog.info("getAppMemorySize = ${value}")
```