## class AudioStreamInfo

```cangjie
public class AudioStreamInfo {
    public AudioStreamInfo(channels: AudioChannel, encodingType: AudioEncodingType, sampleFormat: AudioSampleFormat,
        samplingRate: AudioSamplingRate, channelLayout!: AudioChannelLayout = AudioChannelLayout.CH_LAYOUT_UNKNOWN)
}
```

**功能：** 音频流信息。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### prop channelLayout

```cangjie
public mut prop channelLayout: AudioChannelLayout
```

**功能：** 音频声道布局，默认值为0x0。

**类型：** [AudioChannelLayout](#enum-audiochannellayout)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### prop channels

```cangjie
public mut prop channels: AudioChannel
```

**功能：** 音频文件的通道数。

**类型：** [AudioChannel](#enum-audiochannel)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### prop encodingType

```cangjie
public mut prop encodingType: AudioEncodingType
```

**功能：** 音频编码格式。

**类型：** [AudioEncodingType](#enum-audioencodingtype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### prop sampleFormat

```cangjie
public mut prop sampleFormat: AudioSampleFormat
```

**功能：** 音频采样格式。

**类型：** [AudioSampleFormat](#enum-audiosampleformat)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### prop samplingRate

```cangjie
public mut prop samplingRate: AudioSamplingRate
```

**功能：** 音频文件的采样率。

**类型：** [AudioSamplingRate](#enum-audiosamplingrate)

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### AudioStreamInfo(AudioChannel, AudioEncodingType, AudioSampleFormat, AudioSamplingRate, AudioChannelLayout)

```cangjie
public AudioStreamInfo(channels: AudioChannel, encodingType: AudioEncodingType, sampleFormat: AudioSampleFormat,
    samplingRate: AudioSamplingRate, channelLayout!: AudioChannelLayout = AudioChannelLayout.CH_LAYOUT_UNKNOWN)
```

**功能：** 创建[AudioStreamInfo](#class-audiostreaminfo)实例。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|channels|[AudioChannel](#enum-audiochannel)|是|-|音频文件的通道数。|
|encodingType|[AudioEncodingType](#enum-audioencodingtype)|是|-|音频编码格式。|
|sampleFormat|[AudioSampleFormat](#enum-audiosampleformat)|是|-|音频采样格式。|
|samplingRate|[AudioSamplingRate](#enum-audiosamplingrate)|是|-|音频文件的采样率。|
|channelLayout|[AudioChannelLayout](#enum-audiochannellayout)|否|AudioChannelLayout.CH_LAYOUT_UNKNOWN| **命名参数。** 音频声道布局，默认值为0x0。|