## class PlaybackStrategy

```cangjie
public class PlaybackStrategy {
    public PlaybackStrategy(
        public var preferredWidth!: UInt32 = 0,
        public var preferredHeight!: UInt32 = 0,
        public var preferredBufferDuration!: UInt32 = 0,
        public var preferredHdr!: Bool = false,
        public var mutedMediaType!: ?MediaType = None, // will pass 3 to C
        public var preferredAudioLanguage!: String = "",
        public var preferredSubtitleLanguage!: String = ""
    )
}
```

**功能：** 播放策略。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### var mutedMediaType

```cangjie
public var mutedMediaType: ?MediaType = None
```

**功能：** 静音播放的媒体类型，仅支持设置MediaType.MEDIA_TYPE_AUD。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** ?[MediaType](#enum-mediatype)

**读写能力：** 可读写

**起始版本：** 19

### var preferredAudioLanguage

```cangjie
public var preferredAudioLanguage: String = ""
```

**功能：** 播放策略首选音轨语言。dash场景下应用可按需设置。非dash场景暂不支持，建议缺省。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var preferredBufferDuration

```cangjie
public var preferredBufferDuration: UInt32 = 0
```

**功能：** 播放策略首选缓冲持续时间，单位s，取值范围1-20。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var preferredHdr

```cangjie
public var preferredHdr: Bool = false
```

**功能：** 播放策略，true是hdr，false非hdr，默认非hdr。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** Bool

**读写能力：** 可读写

**起始版本：** 19

### var preferredHeight

```cangjie
public var preferredHeight: UInt32 = 0
```

**功能：** 播放策略首选高度。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var preferredSubtitleLanguage

```cangjie
public var preferredSubtitleLanguage: String = ""
```

**功能：** 播放策略首选字幕语言。dash场景下应用可按需设置。非dash场景暂不支持，建议缺省。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var preferredWidth

```cangjie
public var preferredWidth: UInt32 = 0
```

**功能：** 播放策略首选宽度。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19