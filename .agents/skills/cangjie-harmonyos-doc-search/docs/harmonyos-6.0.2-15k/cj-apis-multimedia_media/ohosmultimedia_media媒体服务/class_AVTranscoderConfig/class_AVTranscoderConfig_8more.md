## class AVTranscoderConfig

```cangjie
public class AVTranscoderConfig {
    public AVTranscoderConfig(
        public var audioBitrate!: Int32 = 48000,
        public var audioCodec!: ?CodecMimeType = None,
        public var fileFormat!: ?ContainerFormatType,
        public var videoBitrate!: Int32 = -1,
        public var videoCodec!: ?CodecMimeType = None,
        public var videoFrameWidth!: Int32 = -1,
        public var videoFrameHeight!: Int32 = -1
    ) {}
}
```

**功能：** 表示视频转码的参数设置。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

### var audioBitrate

```cangjie
public var audioBitrate: Int32 = 48000
```

**功能：** 输出音频的码率，单位为比特率（bps）。用户不设置，则默认设置为48Kbps。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 20

### var audioCodec

```cangjie
public var audioCodec: ?CodecMimeType = None
```

**功能：** 输出音频的编码格式，当前仅支持AAC。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**类型：** [CodecMimeType](#enum-codecmimetype)

**读写能力：** 可读写

**起始版本：** 20

### var fileFormat

```cangjie
public var fileFormat: ?ContainerFormatType
```

**功能：** 输出视频文件的封装格式，当前视频文件仅支持MP4。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**类型：** [ContainerFormatType](#enum-containerformattype)

**读写能力：** 可读写

**起始版本：** 20

### var videoBitrate

```cangjie
public var videoBitrate: Int32 = -1
```

**功能：** 输出视频的码率，单位为比特率（bps）。用户不设置，则默认码率按输出视频的分辨率设置，[240p，480P]默认码率值为1Mbps，(480P,720P]默认码率值为2Mbps，(720P,1080P]默认码率值为4Mbps，1080P及以上默认值为8Mbps。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 20

### var videoCodec

```cangjie
public var videoCodec: ?CodecMimeType = None
```

**功能：** 输出视频的编码格式，当前仅支持AVC和HEVC。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**类型：** [CodecMimeType](#enum-codecmimetype)

**读写能力：** 可读写

**起始版本：** 20

### var videoFrameWidth

```cangjie
public var videoFrameWidth: Int32 = -1
```

**功能：** 输出视频帧的宽，单位为像素（px）。用户不设置，则默认设置为源视频帧的宽。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 20

### var videoFrameHeight

```cangjie
public var videoFrameHeight: Int32 = -1
```

**功能：** 输出视频帧的高，单位为像素（px）。用户不设置，则默认设置为源视频帧的高。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 20