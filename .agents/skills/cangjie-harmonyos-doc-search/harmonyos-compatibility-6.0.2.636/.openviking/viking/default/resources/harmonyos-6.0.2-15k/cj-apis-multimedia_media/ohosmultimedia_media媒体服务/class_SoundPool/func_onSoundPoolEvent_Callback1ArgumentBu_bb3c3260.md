### func on(SoundPoolEvent, Callback1Argument\<BusinessException>)

```cangjie
public func on(eventType: SoundPoolEvent, callback: Callback1Argument<BusinessException>): Unit
```

**功能：** 监听[SoundPool](#class-soundpool)的错误事件，该事件仅用于错误提示。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[SoundPoolEvent](#enum-soundpoolevent)|是|-| 填SoundPoolEvent.EventError，soundPool事件状态。用户操作和系统都会触发此事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)>|是|-|错误事件回调方法：使用播放器的过程中发生错误，会提供错误码ID和错误信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Invalid Parameter.|
  |801|Unsupport Capability.|
  |5400101|No Memory.|
  |5400102|Operation Not Allowed.|
  |5400103|IO Error.|
  |5400105|Service Died.|

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