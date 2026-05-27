### func off(CallerType, OnRemoteStateChangeCallback)

```cangjie
public func off(onType: CallerType, callback: OnRemoteStateChangeCallback): Unit
```

**功能：** 取消注册通用组件服务端Stub（桩）断开监听通知。预留能力，当前暂未支持。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onType|[CallerType](#enum-callertype)|是|-|监听releaseCall事件。|
|callback|[OnRemoteStateChangeCallback](#class-onremotestatechangecallback)|是|-|回调函数，返回off回调结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

### func off(CallerType)

```cangjie
public func off(onType: CallerType): Unit
```

**功能：** 取消注册通用组件服务端Stub（桩）断开监听通知。预留能力，当前暂未支持。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onType|[CallerType](#enum-callertype)|是|-|监听releaseCall事件。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

### func on(CallerType, OnReleaseCallback)

```cangjie
public func on(onType: CallerType, callback: OnReleaseCallback): Unit
```

**功能：** 注册通用组件服务端Stub（桩）断开监听通知。使用callback异步回调。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onType|[CallerType](#enum-callertype)|是|-|监听releaseCall事件。|
|callback|[OnReleaseCallback](#class-onreleasecallback)|是|-|回调函数，返回on回调结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16200001|The caller has been released.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let uiAbilityContext = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let want = Want(bundleName: "com.example.myservice", moduleName: 'entry',
    abilityName: "EntryAbility", parameters: ##"{"ohos.aafwk.param.callAbilityToForeground":true}"##) // parameters是一个json格式的字符串
let caller = uiAbilityContext.startAbilityByCall(want)
caller.on(RELEASE,
    OnReleaseCallback({str => AppLog.info("On Release CallBack is called: ${str}.")}))
```