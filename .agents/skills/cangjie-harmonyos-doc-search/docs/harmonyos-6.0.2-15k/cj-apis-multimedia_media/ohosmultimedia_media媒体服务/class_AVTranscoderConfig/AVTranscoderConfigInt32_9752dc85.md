### AVTranscoderConfig(Int32, ?CodecMimeType, ?ContainerFormatType, Int32, ?CodecMimeType, Int32, Int32)

```cangjie
public AVTranscoderConfig(
    public var audioBitrate!: Int32 = 48000,
    public var audioCodec!: ?CodecMimeType = None,
    public var fileFormat!: ?ContainerFormatType,
    public var videoBitrate!: Int32 = -1,
    public var videoCodec!: ?CodecMimeType = None,
    public var videoFrameWidth!: Int32 = -1,
    public var videoFrameHeight!: Int32 = -1
)
```

**功能：** 构造AVTranscoderConfig对象

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|audioBitrate|Int32|否|48000|输出音频的码率，单位为比特率（bps）。用户不设置，则默认设置为48Kbps。|
|audioCodec|CodecMimeType|否|None|输出音频的编码格式，当前仅支持AAC。|
|fileFormat|ContainerFormatType|是|-|输出视频文件的封装格式，当前视频文件仅支持MP4。|
|videoBitrate|Int32|否|-1|输出视频的码率，单位为比特率（bps）。用户不设置，则默认码率按输出视频的分辨率设置，[240p，480P]默认码率值为1Mbps，(480P,720P]默认码率值为2Mbps，(720P,1080P]默认码率值为4Mbps，1080P及以上默认值为8Mbps。|
|videoCodec|CodecMimeType|否|None|输出视频的编码格式，当前仅支持AVC和HEVC。|
|videoFrameWidth|Int32|否|-1|输出视频帧的宽，单位为像素（px）。用户不设置，则默认设置为源视频帧的宽。|
|videoFrameHeight|Int32|否|-1|输出视频帧的高，单位为像素（px）。用户不设置，则默认设置为源视频帧的高。|