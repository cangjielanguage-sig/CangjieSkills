## class LoopObserver

```cangjie
public class LoopObserver {
    public LoopObserver(let onLoopTimeOut!: ?(Int64) -> Unit = None)
}
```

**功能：** 定义异常监听，可以作为[ErrorManager.on](#static-func-onstring-int64-loopobserver)的入参监听当前应用主线程事件处理事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

### LoopObserver(?(Int64) -> Unit)

```cangjie
public LoopObserver(let onLoopTimeOut!: ?(Int64) -> Unit = None)
```

**功能：** LoopObserver类构造函数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|onLoopTimeOut|?(Int64)->Unit|否|None| **命名参数。** 应用主线程处理事件超时的回调，回调函数的参数是主线程消息实际执行时间（单位：毫秒）。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

try {
    let loopObserver = LoopObserver(onLoopTimeOut: {
        timeout =>
            AppLog.info("onLoopTimeOut timeout:  ${timeout}")
        })
    ErrorManager.on("loopObserver", 2, loopObserver)
} catch (e: BusinessException) {
    AppLog.error("error: ${e}")
}
```

## class OnReleaseCallback

```cangjie
public class OnReleaseCallback <: Callback1Argument<String> {
    public OnReleaseCallback(let callback: (String) -> Unit)
}
```

**功能：** 注册通用组件服务端Stub（桩）断开监听通知的回调函数类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**父类型：**

- [Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<String>

### OnReleaseCallback((String) -> Unit)

```cangjie
public OnReleaseCallback(let callback: (String) -> Unit)
```

**功能：** OnReleaseCallback的主构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(String)->Unit|是|-|用于传递释放消息的回调函数。|

### func invoke(String)

```cangjie
public func invoke(arg1: String)
```

**功能：** 触发回调函数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg1|String|是|-|用于传递释放消息。|

## class OnRemoteStateChangeCallback

```cangjie
public class OnRemoteStateChangeCallback <: Callback1Argument<String> {
    public OnRemoteStateChangeCallback(let callback: (String) -> Unit)
}
```

**功能：** 注册协同场景下跨设备组件状态变化监听通知的回调函数类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**父类型：**

- [Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<String>

### OnRemoteStateChangeCallback((String) -> Unit)

```cangjie
public OnRemoteStateChangeCallback(let callback: (String) -> Unit)
```

**功能：** OnRemoteStateChangeCallback的主构造器。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|(String)->Unit|是|-|释放消息的回调函数。|

### func invoke(String)

```cangjie
public func invoke(arg1: String)
```

**功能：** 触发回调函数。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg1|String|是|-|用于传递释放消息。|