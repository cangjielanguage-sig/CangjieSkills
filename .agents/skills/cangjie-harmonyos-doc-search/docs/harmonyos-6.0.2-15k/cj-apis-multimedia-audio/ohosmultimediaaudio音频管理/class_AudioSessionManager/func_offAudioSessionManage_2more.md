### func off(AudioSessionManagerCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: AudioSessionManagerCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消监听事件。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioSessionManagerCallbackType](#enum-audiosessionmanagercallbacktype)|是|-|监听事件类型。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

class SessionManagerCallback <: Callback1Argument<AudioSessionDeactivatedEvent> {
    public invoke(event: AudioSessionDeactivatedEvent) {
        AppLog.info("invoke success")
    }
}

let instance = getAudioManager()
let smgr = instance.getSessionManager()
let callback = SessionManagerCallback()
smgr.on(AudioSessionManagerCallbackType.AudioSessionDeactivated, callback)

// 指定删除某个回调
smgr.off(AudioSessionManagerCallbackType.AudioSessionDeactivated, callback)
// 删除全部回调
smgr.off(AudioSessionManagerCallbackType.AudioSessionDeactivated)
```

### func on(AudioSessionManagerCallbackType, Callback1Argument\<AudioSessionDeactivatedEvent>)

```cangjie
public func on(`type`: AudioSessionManagerCallbackType, callback: Callback1Argument\<AudioSessionDeactivatedEvent>): Unit
```

**功能：** 监听音频会话停用事件（当音频会话停用时触发），使用callback方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioSessionManagerCallbackType](#enum-audiosessionmanagercallbacktype)|是|-|监听事件。|
|callback|?[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AudioSessionDeactivatedEvent](#class-audiosessiondeactivatedevent)>|否|None| 回调函数, 返回音频会话停用原因。|

**异常：**

- IllegalArgumentException:

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |The type is not supported yet.|`type`仅支持传入AudioSessionManagerCallbackType.AudioSessionDeactivated|检查传入的`type`是否满足要求|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

class SessionManagerCallback <: Callback1Argument<AudioSessionDeactivatedEvent> {
    public invoke(event: AudioSessionDeactivatedEvent) {
        AppLog.info("invoke success")
    }
}

try {
    let instance = getAudioManager()
    let smgr = instance.getSessionManager()
    let callback = SessionManagerCallback()
    smgr.on(AudioSessionManagerCallbackType.AudioSessionDeactivated, callback)
} catch (e: BusinessException) {
    Hilog.error(0, "on", "errCode: ${e.code}, errMessage: ${e.message}")
}
```