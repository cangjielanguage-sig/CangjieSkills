## class AudioHapticPlayer

```cangjie
public class AudioHapticPlayer {}
```

**功能：** 音振播放器，提供音振协同播放功能。在调用[AudioHapticPlayer](#class-audiohapticplayer)的接口前，需要先通过[createPlayer](#func-createplayerint32-audiohapticplayeroptions)创建实例。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

### func isMuted(AudioHapticType)

```cangjie
public func isMuted(hapticType: AudioHapticType): Bool
```

**功能：** 查询该音振类型是否被静音。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hapticType|[AudioHapticType](#enum-audiohaptictype)|是|-|音振类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|查询的音振类型是否被静音。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*

let audiohapticmanager = getAudioHapticManager()
let id = audiohapticmanager.registerSource("/data/11.wav", "/data/11.json")
let player = audiohapticmanager.createPlayer(id)
player.isMuted(AudioHapticType.AUDIO_HAPTIC_TYPE_HAPTIC)
```

### func off(AudioHapticPlayerCallBackType, ?CallbackObject)

```cangjie
public func off(cbType: AudioHapticPlayerCallBackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消监听音频中断事件或流结束事件。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cbType|[AudioHapticPlayerCallBackType](#enum-audiohapticplayercallbacktype)|是|-|要取消订阅事件的类型。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 回调对象。|

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
player.off(AudioHapticPlayerCallBackType.AHP_END_OF_STREAM)
```