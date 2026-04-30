### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放音频池实例。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.AudioKit.*

let audioRendererInfo: AudioRendererInfo = AudioRendererInfo(STREAM_USAGE_MUSIC, 0)
let soundpool = createSoundPool(5, audioRendererInfo)
if (let Some(v) <- soundpool) {
    v.release()
}
```

### func setLoop(Int32, Int32)

```cangjie
public func setLoop(streamID: Int32, loop: Int32): Unit
```

**功能：** 设置循环模式。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|streamID|Int32|是|-|音频流ID，通过play方法获取。|
|loop|Int32|是|-|设置循环的次数，0为默认1次，-1为一直循环。|

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
    v.setLoop(streamId, 2i32)
}
```

### func setPriority(Int32, Int32)

```cangjie
public func setPriority(streamID: Int32, priority: Int32): Unit
```

**功能：** 设置音频流优先级。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|streamID|Int32|是|-|音频流ID，通过play方法获取。|
|priority|Int32|是|-|优先级，0表示最低优先级。|

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
    v.setPriority(streamId, 1)
}
```