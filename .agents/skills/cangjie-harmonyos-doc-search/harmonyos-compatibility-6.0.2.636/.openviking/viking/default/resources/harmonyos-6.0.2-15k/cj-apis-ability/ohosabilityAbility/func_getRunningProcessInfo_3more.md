## func getRunningProcessInformation()

```cangjie
public func getRunningProcessInformation(): Array<ProcessInformation>
```

**功能：** 获取当前运行进程的有关信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[ProcessInformation](#class-processinformation)>| 返回有关运行进程的信息，可进行错误处理或其他自定义处理。|

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

let pInfos = getRunningProcessInformation()
AppLog.info("pInfoNum = ${pInfos.size}")
for (pInfo in pInfos) {
    AppLog.info("pid = ${pInfo.pid}, uid=${pInfo.uid}, procName=${pInfo.processName}, state=${pInfo.state}, appCloneIndex=${pInfo.appCloneIndex}")
    AppLog.info("bundleNameNum = ${pInfo.bundleNames.size}")
    for (name in pInfo.bundleNames) {
        AppLog.info("bundleName = ${name}")
    }
}
```

## func getStageContext(UIAbilityContext)

```cangjie
public func getStageContext(abilityContext: UIAbilityContext): StageContext
```

**功能：** 将UIAbility上下文转换成StageContext类型，StageContext是CPointer\<Unit> 类型的别名。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|abilityContext|[UIAbilityContext](#class-uiabilitycontext)|是|仓颉上下文信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext)|StageContext是CPointer\<Unit> 类型的别名。|

## func getUid(WantAgent)

```cangjie
public func getUid(agent: WantAgent): Int32
```

**功能：** 获取WantAgent实例的用户ID。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|agent|[WantAgent](#class-wantagent)|是|WantAgent对象。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|获取WantAgent实例的用户ID。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000007|Service busy. There are concurrent tasks. Try again later.|
  |16000151|Invalid wantagent object.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let wantAgentInfo = WantAgentInfo(
    wants: [Want(bundleName: "com.example.myapplication", abilityName: "EntryAbility")],
    actionType: START_ABILITIES, requestCode: 0, actionFlags: [UPDATE_PRESENT_FLAG])
let wantAgent = getWantAgent(wantAgentInfo)
let uid = getUid(wantAgent)
AppLog.info("uid is ${uid}")
```