### func getCurrentAudioRendererInfoArray()

```cangjie
public func getCurrentAudioRendererInfoArray(): AudioRendererChangeInfoArray
```

**功能：** 获取当前音频渲染器的信息，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioRendererChangeInfoArray](#type-audiorendererchangeinfoarray)|返回当前音频采集器信息。|

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

try {
    let streamMgr: AudioStreamManager = getAudioManager().getStreamManager()
    let renderChangInfos: AudioRendererChangeInfoArray = streamMgr.getCurrentAudioRendererInfoArray()
    for (renderChangInfo in renderChangInfos) {
        let streamId: Int32 = renderChangInfo.streamId
        let rendererInfo: AudioRendererInfo = renderChangInfo.rendererInfo
        let usage: StreamUsage = rendererInfo.usage
        let rendererFlags: Int32 = rendererInfo.rendererFlags
        let descs: AudioDeviceDescriptors = renderChangInfo.deviceDescriptors
    }
} catch (e: BusinessException) {
    Hilog.error(0, "getCurrentAudioRendererInfoArray", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func isActive(AudioVolumeType)

```cangjie
public func isActive(volumeType: AudioVolumeType): Bool
```

**功能：** 获取指定音频流是否为活跃状态，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|volumeType|[AudioVolumeType](#enum-audiovolumetype)|是|-|音频流类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回流的活跃状态，true为活跃，false为不活跃。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |6800101|Invalid parameter.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

try {
    let instance = getAudioManager()
    let smgr = instance.getStreamManager()
    let usage = StreamUsage.STREAM_USAGE_MUSIC
    let typ = AudioVolumeType.RINGTONE
    let isactive = smgr.isActive(typ)
} catch (e: BusinessException) {
    Hilog.error(0, "isActive", "errCode: ${e.code}, errMessage: ${e.message}")
}
```