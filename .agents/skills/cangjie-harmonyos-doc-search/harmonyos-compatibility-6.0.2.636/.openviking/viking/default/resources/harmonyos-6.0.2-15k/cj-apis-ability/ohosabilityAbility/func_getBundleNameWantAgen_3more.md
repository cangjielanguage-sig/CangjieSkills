## func getBundleName(WantAgent)

```cangjie
public func getBundleName(agent: WantAgent): String
```

**功能：** 获取WantAgent实例的包名。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|agent|[WantAgent](#class-wantagent)|是|WantAgent对象。|

**返回值：**

|类型|说明|
|:----|:----|
|String|获取WantAgent实例的包名。|

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
let boundleName = getBundleName(wantAgent)
AppLog.info("boundleName is ${boundleName}")
```

## func getNapiValue(CPointer\<Unit>, StageContext)

```cangjie
public func getNapiValue(env: CPointer<Unit>, context: StageContext): CPointer<Unit>
```

**功能：** 根据上下文环境获取napi_value。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|env| CPointer\<Unit> |是|环境指针。|
|context| [StageContext](../../arkinterop/cj-apis-ark_interop_helper.md#type-stagecontext) |是|上下文信息。|

**返回值：**

|类型|说明|
|:----|:----|
|CPointer\<Unit> | 返回napi_value信息。|

## func getOperationType(WantAgent)

```cangjie
public func getOperationType(agent: WantAgent): OperationType
```

**功能：** 获取一个WantAgent的[OperationType](#enum-operationtype)信息。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填| 说明|
|:---|:---|:---|:---|
|agent|[WantAgent](#class-wantagent)|是|WantAgent对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[OperationType](#enum-operationtype)|返回获取OperationType的结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000007|Service busy. There are concurrent tasks. Try again later.|
  |16000015|Service timeout.|
  |16000151|Invalid wantagent object.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let wantAgentInfo = WantAgentInfo(
    wants: [Want(deviceId: "deviceId", bundleName: "com.example.myapplication", abilityName: "EntryAbility")],
    actionType: OperationType.START_ABILITY, requestCode: 0, actionFlags: [UPDATE_PRESENT_FLAG])
let wantAgent = getWantAgent(wantAgentInfo)
let opType = getOperationType(wantAgent)
AppLog.info("OperationType is ${opType}")
```