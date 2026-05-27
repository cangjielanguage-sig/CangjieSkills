## class AVRecorderProfile

```cangjie
public class AVRecorderProfile {
    public AVRecorderProfile(
        public var fileFormat: ContainerFormatType,
        public var audioBitrate!: ?Int32 = None,
        public var audioChannels!: ?Int32 = None,
        public var audioCodec!: ?CodecMimeType = None,
        public var audioSampleRate!: ?Int32 = None,
        public var videoBitrate!: ?Int32 = None,
        public var videoCodec!: ?CodecMimeType = None,
        public var videoFrameWidth!: ?Int32 = None,
        public var videoFrameHeight!: ?Int32 = None,
        public var videoFrameRate!: ?Int32 = None,
        public var isHdr!: ?Bool = false,
        public var enableTemporalScale!: ?Bool = false
    )
}
```

**功能：** 音视频录制的配置文件。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

### var audioBitrate

```cangjie
public var audioBitrate: ?Int32 = None
```

**功能：** 音频编码比特率，选择音频录制时必填。

支持范围：

- AAC编码格式支持比特率范围[32000 - 500000]。
- G711-mulaw编码格式支持比特率范围[64000 - 64000]。
- MP3编码格式支持范围[8000, 16000, 32000, 40000, 48000, 56000, 64000, 80000, 96000, 112000, 128000, 160000, 192000, 224000, 256000, 320000]。

当使用MP3编码格式时，采样率和比特率的映射关系：

- 采样率使用16K以下时，对应比特率范围为[8kbps - 64kbps]。
- 采样率使用16K~32K时对应的比特率范围为[8kbps - 160kbps]。
- 采样率使用32K以上时对应的比特率范围为[32kbps - 320kbps]。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var audioChannels

```cangjie
public var audioChannels: ?Int32 = None
```

**功能：** 音频采集声道数，选择音频录制时必填。

- AAC编码格式支持范围[1 - 8]。
- G711-mulaw编码格式支持范围[1 - 1]。
- MP3编码格式支持范围[1 - 2]。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var audioCodec

```cangjie
public var audioCodec: ?CodecMimeType = None
```

**功能：** 音频编码格式，选择音频录制时必填。当前支持AUDIO_AAC，AUDIO_MP3，AUDIO_G711MU。

**类型：** ?[CodecMimeType](#enum-codecmimetype)

**读写能力：** 可读写

**起始版本：** 19

### var audioSampleRate

```cangjie
public var audioSampleRate: ?Int32 = None
```

**功能：** 音频采样率，选择音频录制时必填。

支持范围：

- AAC编码支持采样率范围[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000, 64000, 88200, 96000]。
- G711-mulaw编码支持采样率范围[8000 - 8000]。
- MP3编码支持采样率范围[8000, 11025, 12000, 16000, 22050, 24000, 32000, 44100, 48000]。
- 可变比特率模式，码率仅作参考。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var enableTemporalScale

```cangjie
public var enableTemporalScale: ?Bool = false
```

**功能：** 视频录制是否支持时域分层编码功能，选择视频录制时选填，enableTemporalScale默认为false。设置为true时，编码输出的码流中部分帧可以支持跳过不编码。

**类型：** ?Bool

**读写能力：** 可读写

**起始版本：** 19

### var fileFormat

```cangjie
public var fileFormat: ContainerFormatType
```

**功能：** 文件的容器格式，必要参数。当前支持MP4、M4A、MP3、WAV封装格式，不支持在MP4封装格式下使用AUDIO_MP3编码格式。

**类型：** [ContainerFormatType](#enum-containerformattype)

**读写能力：** 可读写

**起始版本：** 19

### var isHdr

```cangjie
public var isHdr: ?Bool = false
```

**功能：** HDR编码，选择视频录制时选填，isHdr默认为false，对应编码格式没有要求，isHdr为true时，对应的编码格式必须为video/hevc。

**类型：** ?Bool

**读写能力：** 可读写

**起始版本：** 19

### var videoBitrate

```cangjie
public var videoBitrate: ?Int32 = None
```

**功能：** 视频编码比特率，选择视频录制时必填，支持范围[10000 - 100000000]。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19