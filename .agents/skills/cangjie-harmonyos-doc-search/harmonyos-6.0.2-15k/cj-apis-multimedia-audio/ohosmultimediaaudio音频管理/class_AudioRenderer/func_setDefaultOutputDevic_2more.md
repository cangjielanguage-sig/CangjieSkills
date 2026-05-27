### func setDefaultOutputDevice(DeviceType)

```cangjie
public func setDefaultOutputDevice(deviceType: DeviceType): Unit
```

**功能：** 设置默认本机内置发声设备。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceType|[DeviceType](#enum-devicetype)|是|-|设备类型。只支持：EARPIECE（听筒）、SPEAKER（扬声器）和DEFAULT（系统默认设备）。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800103|Unsupported state.|
  |6800301|System error.|

- IllegalArgumentException:

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |The type is not supported yet.|传入不支持的[DeviceType](#enum-devicetype)类型|检查传入[DeviceType](#enum-devicetype)类型是否满足要求|

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
    try {
        audioRenderer.setDefaultOutputDevice(DeviceType.SPEAKER)
    } catch (e: BusinessException) {
        Hilog.error(0, "setDefaultOutputDevice", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func setInterruptMode(InterruptMode)

```cangjie
public func setInterruptMode(mode: InterruptMode): Unit
```

**功能：** 设置应用的焦点模型。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[InterruptMode](#enum-interruptmode)|是|-|焦点模型。|

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
    let rendererInfo = AudioRendererInfo(
    StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, 0)
    let streamInfo = AudioStreamInfo(
        AudioChannel.CHANNEL_1,
        AudioEncodingType.ENCODING_TYPE_RAW,
        AudioSampleFormat.SAMPLE_FORMAT_S16LE,
        AudioSamplingRate.SAMPLE_RATE_44100)
    let options = AudioRendererOptions(rendererInfo, streamInfo)
    let audioRenderer = createAudioRenderer(options)
    try {
        audioRenderer.setInterruptMode(InterruptMode.SHARE_MODE)
    } catch (e: BusinessException) {
        Hilog.error(0, "setInterruptMode", "errCode: ${e.code}, errMessage: ${e.message}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioRenderer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```