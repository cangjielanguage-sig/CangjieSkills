### func on(SoundPoolEvent, Callback0Argument)

```cangjie
public func on(eventType: SoundPoolEvent, callback: Callback0Argument): Unit
```

**功能：** 音频池资源播放完成监听。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[SoundPoolEvent](#enum-soundpoolevent)|是|-|填SoundPoolEvent.PlayFinished，soundPool事件状态。音频流播放完成会触发此回调。|
|callback|[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)|是|-||

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*
import kit.AudioKit.*
import kit.CoreFileKit.*

// 此处代码可添加在依赖项定义中
public class PlayCallback <: Callback0Argument {
    public PlayCallback(public let function: () -> Unit) {}

    public func invoke(): Unit {
        function()
    }
}

let audioRendererInfo: AudioRendererInfo = AudioRendererInfo(STREAM_USAGE_MUSIC, 0)
let soundpool = createSoundPool(5, audioRendererInfo)

func testplaycallback(): Unit {
    if (let Some(v) <- soundpool) {
        let callback = PlayCallback({
            => AppLog.info("playfinished success!")
        })
        v.on(PlayFinished, callback)
    }
}

if (let Some(v) <- soundpool) {
    testplaycallback()
    let playparams = PlayParameters(loop: 1i32, rate: RENDER_RATE_DOUBLE, leftVolume: 0.2)
    let file = FileFs.open("/data/storage/el2/base/support_fast_01.mp3", mode: READ_ONLY.mode)
    var uri: String = ""
    uri = "fd://" + file
        .fd
        .toString()
    let soundId = v.load(uri)
    let streamId = v.play(soundId, params: playparams)
}
```