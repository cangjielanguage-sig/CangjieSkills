### func play(Int32, ?PlayParameters)

```cangjie
public func play(soundID: Int32, params!: ?PlayParameters = None): Int32
```

**功能：** 播放音频资源。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|soundID|Int32|是|-|资源ID，通过load方法获取。|
|params|?[PlayParameters](#struct-playparameters)|否|None| **命名参数。** play播放相关参数的设置。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|获取回调的音频流ID，有效值大于0。|

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
import ohos.base.*
import kit.AudioKit.*

// 此处代码可添加在依赖项定义中
public class ErrorCallback <: Callback1Argument<BusinessException> {
    public ErrorCallback(public let function: (BusinessException) -> Unit) {}

    public func invoke(value: BusinessException): Unit {
        function(value)
    }
}

let audioRendererInfo: AudioRendererInfo = AudioRendererInfo(STREAM_USAGE_MUSIC, 0)
let soundpool = createSoundPool(5, audioRendererInfo)
func testerrorcallback(): Unit {
    if (let Some(v) <- soundpool) {
        let callback = ErrorCallback(
            {
                p: BusinessException => AppLog.info("error code is ${p.toString()}!")
            })
        v.on(EventError, callback)
    }
}
let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let resMgr = abilityContext.resourceManager
let rawfd = resMgr.getRawFd("01.mp3")
if (let Some(v) <- soundpool) {
    testerrorcallback()
    let playparams = PlayParameters(loop: 1i32, rate: RENDER_RATE_DOUBLE, leftVolume: 0.2)
    let id = v.load(rawfd.fd, rawfd.offset, rawfd.length)
    let streamId = v.play(id, params: playparams)
}
```