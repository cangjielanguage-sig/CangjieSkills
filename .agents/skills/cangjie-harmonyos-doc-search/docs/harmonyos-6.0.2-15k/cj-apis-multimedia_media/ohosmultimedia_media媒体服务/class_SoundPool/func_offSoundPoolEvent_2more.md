### func off(SoundPoolEvent)

```cangjie
public func off(eventType: SoundPoolEvent): Unit
```

**功能：** 取消监听音频池的事件。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[SoundPoolEvent](#enum-soundpoolevent)|是|-|soundPool事件状态。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.AudioKit.*

let audioRendererInfo: AudioRendererInfo = AudioRendererInfo(STREAM_USAGE_MUSIC, 0)
let soundpool = createSoundPool(5, audioRendererInfo)
if (let Some(v) <- soundpool) {
    v.off(PlayFinished)
}
```

### func on(SoundPoolEvent, Callback1Argument\<Int32>)

```cangjie
public func on(eventType: SoundPoolEvent, callback: Callback1Argument<Int32>): Unit
```

**功能：** 音频池资源加载完成监听。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[SoundPoolEvent](#enum-soundpoolevent)|是|-|填SoundPoolEvent.LoadCompleted，soundPool事件状态。对应的ID加载完成会触发此回调。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Int32>|是|-|对应资源加载完成的资源ID。|

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
public class LoadCallback <: Callback1Argument<Int32> {
    public LoadCallback(let function: (Int32) -> Unit) {}

    public func invoke(arg1: Int32): Unit {
        function(arg1)
    }
}

let audioRendererInfo: AudioRendererInfo = AudioRendererInfo(STREAM_USAGE_MUSIC, 0)
let soundpool = createSoundPool(5, audioRendererInfo)

func testloadcallback(): Unit {
    if (let Some(v) <- soundpool) {
        let callback = LoadCallback({
            p: Int32 => AppLog.info("loadComplete soundId ${p}")
        })
        v.on(LoadCompleted, callback)
    }
}

if (let Some(v) <- soundpool) {
    testloadcallback()
    let file = FileFs.open("/data/storage/el2/base/support_fast_01.mp3", mode: READ_ONLY.mode)
    var uri: String = ""
    uri = "fd://" + file
        .fd
        .toString()
    let soundId = v.load(uri)
}
```