### func prepare(AVRecorderConfig)

```cangjie
public func prepare(config: AVRecorderConfig): Unit
```

**功能：** 进行音视频录制的参数设置。

**需要权限：** ohos.permission.MICROPHONE

不涉及音频录制时，可以不需要获ohos.permission.MICROPHONE权限。

使用相机视频录制还需要与相机模块配合，相机模块接口的使用详情见[相机管理](../CameraKit/cj-apis-multimedia-camera.md)。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|config|[AVRecorderConfig](#class-avrecorderconfig)|是|-|配置音视频录制的相关参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|
  |5400102|Operate not permit.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.AudioKit.*
import kit.CoreFileKit.*
import ohos.base.*

let avRecorder = createAVRecorder()
let avRecorderProfile = AVRecorderProfile(
    ContainerFormatType.CFT_MPEG_4,
    audioBitrate: 48000,
    audioChannels: 2,
    audioCodec: CodecMimeType.AUDIO_AAC,
    audioSampleRate: 48000,
    videoBitrate: 2000000,
    videoCodec: CodecMimeType.VIDEO_AVC,
    videoFrameWidth: 640,
    videoFrameHeight: 480,
    videoFrameRate: 30
)
let context = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let applicationContext = context.getApplicationContext() // add
let filePath2: String = context.filesDirectory + '/example00.mp3'
let audioFile = FileFs.open(
    filePath2,
    mode: (READ_WRITE.mode | OpenMode
        .CREATE
        .mode)
)
let fileFd: Int32 = audioFile.fd
let url: String = 'fd://' + fileFd.toString()

let avRecorderConfig = AVRecorderConfig(
    avRecorderProfile,
    url,
    audioSourceType: AudioSourceType.AUDIO_SOURCE_TYPE_MIC
)
try {
    avRecorder.prepare(avRecorderConfig)
} catch (e: BusinessException) {
    AppLog.info("error is ${e}")
}
```