### func on(AudioHapticPlayerCallBackType, Callback0Argument)

```cangjie
public func on(cbType: AudioHapticPlayerCallBackType, callback: Callback0Argument): Unit
```

**功能：** 监听音频中断事件（当音频焦点发生变化时触发），使用callback方式返回结果。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cbType|[AudioHapticPlayerCallBackType](#enum-audiohapticplayercallbacktype)|是|-|事件回调类型，值必须为AHP_AUDIO_INTERRRUPT。|
|callback|[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)|是|-|回调函数，返回播放中断时，应用接收的中断事件信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*

// 此处代码可添加在依赖项定义中
class EndOfStreamListener <: Callback0Argument {
    public func invoke() {
        AppLog.error("endofstream called")
    }
}

let audiohapticmanager = getAudioHapticManager()
let id = audiohapticmanager.registerSource("/data/11.wav", "/data/11.json")
let player = audiohapticmanager.createPlayer(id)
player.on(AudioHapticPlayerCallBackType.AHP_END_OF_STREAM, EndOfStreamListener())
```

### func on(AudioHapticPlayerCallBackType, Callback1Argument\<InterruptEvent>)

```cangjie
public func on(cbType: AudioHapticPlayerCallBackType, callback: Callback1Argument<InterruptEvent>): Unit
```

**功能：** 监听音频中断事件（当音频焦点发生变化时触发），使用callback方式返回结果。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cbType|[AudioHapticPlayerCallBackType](#enum-audiohapticplayercallbacktype)|是|-|事件回调类型，值必须为AHP_AUDIO_INTERRRUPT。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[InterruptEvent](cj-apis-multimedia-audio.md#class-interruptevent)>|是|-|回调函数，返回播放中断时，应用接收的中断事件信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*

// 此处代码可添加在依赖项定义中
class InterruptListener <: Callback1Argument<InterruptEvent> {
    public func invoke(evt: InterruptEvent) {
        AppLog.error("interrupt called")
        AppLog.error(evt.hintType)
        AppLog.error(evt.eventType)
        AppLog.error(evt.forceType)
    }
}

let audiohapticmanager = getAudioHapticManager()
let id = audiohapticmanager.registerSource("/data/11.wav", "/data/11.json")
let player = audiohapticmanager.createPlayer(id)
player.on(AudioHapticPlayerCallBackType.AHP_AUDIO_INTERRRUPT, InterruptListener())
```

### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放音振播放器。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400105|Service died.|

### func start()

```cangjie
public func start(): Unit
```

**功能：** 开始播放。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operate not permit.|
  |5400103|IO error.|
  |5400105|Service died.|