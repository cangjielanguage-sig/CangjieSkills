### func stop(Int32)

```cangjie
public func stop(streamID: Int32): Unit
```

**功能：** 停止streamID对应的音频播放。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|streamID|Int32|是|-|音频流ID，通过play方法获取。|

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
    v.stop(streamId)
}
```

### func unload(Int32)

```cangjie
public func unload(soundID: Int32): Unit
```

**功能：** 卸载音频资源。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|soundID|Int32|是|-|资源ID，通过load方法获取。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operation not allowed.|
  |5400103|I/O error.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.AudioKit.*
import kit.CoreFileKit.*

let audioRendererInfo: AudioRendererInfo = AudioRendererInfo(STREAM_USAGE_MUSIC, 0)
let soundpool = createSoundPool(5, audioRendererInfo)

if (let Some(v) <- soundpool) {
    let file = FileFs.open("/data/storage/el2/base/support_fast_01.mp3", mode: READ_ONLY.mode)
    var uri: String = ""
    uri = "fd://" + file
        .fd
        .toString()
    let soundId = v.load(uri)
    v.unload(soundId)
}
```