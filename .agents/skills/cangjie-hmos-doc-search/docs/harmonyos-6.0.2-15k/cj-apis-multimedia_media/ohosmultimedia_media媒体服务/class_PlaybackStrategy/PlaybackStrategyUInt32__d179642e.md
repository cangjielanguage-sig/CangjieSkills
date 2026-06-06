### PlaybackStrategy(UInt32, UInt32, UInt32, Bool, ?MediaType, String, String)

```cangjie
public PlaybackStrategy(
    public var preferredWidth!: UInt32 = 0,
    public var preferredHeight!: UInt32 = 0,
    public var preferredBufferDuration!: UInt32 = 0,
    public var preferredHdr!: Bool = false,
    public var mutedMediaType!: ?MediaType = None, // will pass 3 to C
    public var preferredAudioLanguage!: String = "",
    public var preferredSubtitleLanguage!: String = ""
)
```

**功能：** 创建PlaybackStrategy对象。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|preferredWidth|UInt32|否|0| **命名参数。** 播放策略首选宽度。|
|preferredHeight|UInt32|否|0| **命名参数。** 播放策略首选高度。|
|preferredBufferDuration|UInt32|否|0| **命名参数。** 播放策略首选缓冲持续时间，单位s，取值范围1-20。|
|preferredHdr|Bool|否|false| **命名参数。** 播放策略true是hdr，false非hdr，默认非hdr。|
|mutedMediaType|?[MediaType](#enum-mediatype)|否|None| **命名参数。** 静音播放的媒体类型，仅支持设置MediaType.MEDIA_TYPE_AUD。|
|preferredAudioLanguage|String|否|""| **命名参数。** 播放策略首选音轨语言。dash场景下应用可按需设置。非dash场景暂不支持，建议缺省。|
|preferredSubtitleLanguage|String|否|""| **命名参数。** 播放策略首选字幕语言。dash场景下应用可按需设置。非dash场景暂不支持，建议缺省。|