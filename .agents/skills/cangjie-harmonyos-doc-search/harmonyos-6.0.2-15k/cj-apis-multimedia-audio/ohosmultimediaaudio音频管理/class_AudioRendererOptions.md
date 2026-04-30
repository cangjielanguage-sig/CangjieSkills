## class AudioRendererOptions

```cangjie
public class AudioRendererOptions {
    public AudioRendererOptions(rendererInfo: AudioRendererInfo, streamInfo: AudioStreamInfo,
        privacyType!: AudioPrivacyType = PRIVACY_TYPE_PUBLIC)
}
```

**功能：** 音频渲染器选项信息。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### prop privacyType

```cangjie
public mut prop privacyType: AudioPrivacyType
```

**功能：** 表示音频流是否可以被其他应用录制。

**类型：** [AudioPrivacyType](#enum-audioprivacytype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### prop rendererInfo

```cangjie
public mut prop rendererInfo: AudioRendererInfo
```

**功能：** 音频渲染器信息。

**类型：** [AudioRendererInfo](#class-audiorendererinfo)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### prop streamInfo

```cangjie
public mut prop streamInfo: AudioStreamInfo
```

**功能：** 表示音频流信息。

**类型：** [AudioStreamInfo](#class-audiostreaminfo)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

### AudioRendererOptions(AudioRendererInfo, AudioStreamInfo, AudioPrivacyType)

```cangjie
public AudioRendererOptions(rendererInfo: AudioRendererInfo, streamInfo: AudioStreamInfo,
    privacyType!: AudioPrivacyType = PRIVACY_TYPE_PUBLIC)
```

**功能：** 构造[AudioRendererOptions](#class-audiorendereroptions)。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rendererInfo|[AudioRendererInfo](#class-audiorendererinfo)|是|-|表示音频流信息。|
|streamInfo|[AudioStreamInfo](#class-audiostreaminfo)|是|-|表示渲染器信息。|
|privacyType|[AudioPrivacyType](#enum-audioprivacytype)|否|PRIVACY_TYPE_PUBLIC| **命名参数。** 表示音频流是否可以被其他应用录制，默认值为0。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

let rendererInfo = AudioRendererInfo(StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, 0)
let streamInfo = AudioStreamInfo(
    AudioChannel.CHANNEL_1,
    AudioEncodingType.ENCODING_TYPE_RAW,
    AudioSampleFormat.SAMPLE_FORMAT_S16LE,
    AudioSamplingRate.SAMPLE_RATE_48000
)
let options = AudioRendererOptions(rendererInfo, streamInfo)
```