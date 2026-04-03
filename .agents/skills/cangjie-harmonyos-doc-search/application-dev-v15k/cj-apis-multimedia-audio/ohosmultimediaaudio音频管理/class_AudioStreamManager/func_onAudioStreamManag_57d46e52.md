### func on(AudioStreamManagerCallbackType, Callback1Argument\<AudioRendererChangeInfoArray>)

```cangjie
public func on(`type`: AudioStreamManagerCallbackType, callback: Callback1Argument<AudioRendererChangeInfoArray>): Unit
```

**功能：** 监听音频渲染器更改事件（当音频播放流状态变化、设备变化时触发），使用callback方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioStreamManagerCallbackType](#enum-audiostreammanagercallbacktype)|是|-|监听事件，固定为：'RENDERER_CHANGE'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AudioRendererChangeInfoArray](#type-audiorendererchangeinfoarray)>|是|-|回调函数，返回当前音频渲染器信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800301|System error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

// 此处代码可添加在依赖项定义中
class Callback <: Callback1Argument<AudioRendererChangeInfoArray> {
    public func invoke(arg: AudioRendererChangeInfoArray) {
        AppLog.info("callback: ${arg.size}")
    }
}

try {
    let instance = getAudioManager()
    let smgr = instance.getStreamManager()
    var cb1 = Callback()
    smgr.on(AudioStreamManagerCallbackType.RENDERER_CHANGE, cb1)
    smgr.off(AudioStreamManagerCallbackType.RENDERER_CHANGE)
} catch (e: BusinessException) {
    Hilog.error(0, "StreamManager:on/off", "errCode: ${e.code}, errMessage: ${e.message}")
}
```