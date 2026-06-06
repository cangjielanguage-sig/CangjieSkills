# ohos.multimedia.audio（音频管理）

音频管理模块提供管理音频的一些基础能力，包括对音频音量、音频设备的管理，以及对音频数据的采集和渲染等。

该模块提供以下音频相关的常用功能：

- [AudioManager](#class-audiomanager)：音频管理。
- [AudioCapturer](#class-audiocapturer)：音频采集，用于录制PCM音频数据。
- [AudioRenderer](#class-audiorenderer)：音频渲染，用于播放PCM（Pulse Code Modulation）音频数据。

## 导入模块

```cangjie
import kit.AudioKit.*
```

## 权限列表

ohos.permission.ACCESS_NOTIFICATION_POLICY

ohos.permission.MANAGE_AUDIO_CONFIG

ohos.permission.MICROPHONE

ohos.permission.MODIFY_AUDIO_SETTINGS

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## const DEFAULT_INTERRUPT_GROUP_ID

```cangjie
public const DEFAULT_INTERRUPT_GROUP_ID: Int32 = 1
```

**功能：** 默认音频中断组id。

**类型：** Int32

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

## const DEFAULT_VOLUME_GROUP_ID

```cangjie
public const DEFAULT_VOLUME_GROUP_ID: Int32 = 1
```

**功能：** 默认音量组id。

**类型：** Int32

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

## func createAudioCapturer(AudioCapturerOptions)

```cangjie
public func createAudioCapturer(options: AudioCapturerOptions): AudioCapturer
```

**功能：** 获取音频采集器。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**需要权限：** ohos.permission.MICROPHONE

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[AudioCapturerOptions](#class-audiocaptureroptions)|是|-|配置音频采集器。|

**返回值：**

|类型|说明|
|:----|:----|
|[AudioCapturer](#class-audiocapturer)|成功将返回音频采集器对象，异常将返回error对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800301|Create AudioCapturer failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

try {
    let streamInfo = AudioStreamInfo(AudioChannel.CHANNEL_2, AudioEncodingType.ENCODING_TYPE_RAW,
    AudioSampleFormat.SAMPLE_FORMAT_S16LE, AudioSamplingRate.SAMPLE_RATE_44100)
    let capturerInfo = AudioCapturerInfo(SourceType.SOURCE_TYPE_VOICE_RECOGNITION, 0)
    let options = AudioCapturerOptions(capturerInfo, streamInfo)
    let audioCapturer = createAudioCapturer(options)
} catch (e: BusinessException) {
    Hilog.error(0, "createAudioCapturer", "errCode: ${e.code}, errMessage: ${e.message}")
}
```