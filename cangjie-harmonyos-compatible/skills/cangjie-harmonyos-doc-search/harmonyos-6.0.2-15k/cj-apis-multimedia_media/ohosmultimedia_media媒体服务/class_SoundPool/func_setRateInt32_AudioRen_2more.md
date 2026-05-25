### func setRate(Int32, AudioRendererRate)

```cangjie
public func setRate(streamID: Int32, rate: AudioRendererRate): Unit
```

**功能：** 设置音频流的播放速率。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|streamID|Int32|是|-|音频流ID，通过play方法获取。|
|rate|[AudioRendererRate](../AudioKit/cj-apis-multimedia-audio.md#enum-audiorendererrate)|是|-|音频rate相关参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.|
  |5400102|Operation not allowed.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.AudioKit.*

let audioRendererInfo: AudioRendererInfo = AudioRendererInfo(STREAM_USAGE_MUSIC, 0)
let soundpool = createSoundPool(5, audioRendererInfo)
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let resMgr = abilityContext.resourceManager
let rawfd = resMgr.getRawFd("01.mp3")
if (let Some(v) <- soundpool) {
    let playparams = PlayParameters(loop: 1i32, rate: RENDER_RATE_DOUBLE, leftVolume: 0.2)
    let soundId = v.load(rawfd.fd, rawfd.offset, rawfd.length)
    let streamId = v.play(soundId, params: playparams)
    v.setRate(streamId, RENDER_RATE_DOUBLE)
}
```

### func setVolume(Int32, Float32, Float32)

```cangjie
public func setVolume(streamID: Int32, leftVolume: Float32, rightVolume: Float32): Unit
```

**功能：** 设置音频流的播放音量。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|streamID|Int32|是|-|音频流ID，通过play方法获取。|
|leftVolume|Float32|是|-|左声道音量，设置范围为0.0-1.0之间。|
|rightVolume|Float32|是|-|右声道音量，当前右声道设置无效，以左声道为准。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.|
  |5400102|Operation not allowed.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.AudioKit.*

let audioRendererInfo: AudioRendererInfo = AudioRendererInfo(STREAM_USAGE_MUSIC, 0)
let soundpool = createSoundPool(5, audioRendererInfo)
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let resMgr = abilityContext.resourceManager
let rawfd = resMgr.getRawFd("01.mp3")
if (let Some(v) <- soundpool) {
    let playparams = PlayParameters(loop: 1i32, rate: RENDER_RATE_DOUBLE, leftVolume: 0.2)
    let soundId = v.load(rawfd.fd, rawfd.offset, rawfd.length)
    let streamId = v.play(soundId, params: playparams)
    v.setVolume(streamId, 0.2, 0.5)
}
```