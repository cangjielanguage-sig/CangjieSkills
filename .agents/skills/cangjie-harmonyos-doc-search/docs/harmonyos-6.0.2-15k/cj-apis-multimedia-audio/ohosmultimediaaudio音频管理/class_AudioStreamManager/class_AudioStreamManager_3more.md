## class AudioStreamManager

```cangjie
public class AudioStreamManager {}
```

**功能：** 管理音频流。在使用[AudioStreamManager](#class-audiostreammanager)的API前，需要使用[getStreamManager](#func-getstreammanager)获取[AudioStreamManager](#class-audiostreammanager)实例。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func getAudioEffectInfoArray(StreamUsage)

```cangjie
public func getAudioEffectInfoArray(usage: StreamUsage): AudioEffectInfoArray
```

**功能：** 获取当前音效模式的信息，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|usage|[StreamUsage](#enum-streamusage)|是|-|音频流使用类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[AudioEffectInfoArray](#type-audioeffectinfoarray)|返回当前音效模式的信息。|

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
    let arr = smgr.getAudioEffectInfoArray(usage)
} catch (e: BusinessException) {
    Hilog.error(0, "getAudioEffectInfoArray", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getCurrentAudioCapturerInfoArray()

```cangjie
public func getCurrentAudioCapturerInfoArray(): AudioCapturerChangeInfoArray
```

**功能：** 获取当前音频采集器的信息，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioCapturerChangeInfoArray](#type-audiocapturerchangeinfoarray)|返回当前音频采集器信息。|

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
    let instance = getAudioManager()
    let smgr = instance.getStreamManager()
    let usage = StreamUsage.STREAM_USAGE_MUSIC
    let infoarr = smgr.getCurrentAudioCapturerInfoArray()
} catch (e: BusinessException) {
    Hilog.error(0, "getCurrentAudioCapturerInfoArray", "errCode: ${e.code}, errMessage: ${e.message}")
}
```