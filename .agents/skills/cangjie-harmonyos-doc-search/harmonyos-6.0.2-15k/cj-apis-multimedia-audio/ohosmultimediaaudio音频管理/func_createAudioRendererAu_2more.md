## func createAudioRenderer(AudioRendererOptions)

```cangjie
public func createAudioRenderer(options: AudioRendererOptions): AudioRenderer
```

**功能：** 获取音频渲染器。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[AudioRendererOptions](#class-audiorendereroptions)|是|-|配置渲染器。|

**返回值：**

|类型|说明|
|:----|:----|
|[AudioRenderer](#class-audiorenderer)|成功将返回音频渲染器对象，异常将返回error对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800301|Create AudioRenderer failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

try {
    let rendererInfo = AudioRendererInfo(
    StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, 0)
    let streamInfo = AudioStreamInfo(
        AudioChannel.CHANNEL_1,
        AudioEncodingType.ENCODING_TYPE_RAW,
        AudioSampleFormat.SAMPLE_FORMAT_S16LE,
        AudioSamplingRate.SAMPLE_RATE_44100)
    let options = AudioRendererOptions(rendererInfo, streamInfo)
    let audioRenderer = createAudioRenderer(options)
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

## func getAudioManager()

```cangjie
public func getAudioManager(): AudioManager
```

**功能：** 获取音频管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioManager](#class-audiomanager)|音频管理对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800301|Create AudioManager failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

try {
    let audioManager: AudioManager = getAudioManager()
} catch (e: BusinessException) {
    Hilog.error(0, "getAudioManager", "errCode: ${e.code}, errMessage: ${e.message}")
}
```