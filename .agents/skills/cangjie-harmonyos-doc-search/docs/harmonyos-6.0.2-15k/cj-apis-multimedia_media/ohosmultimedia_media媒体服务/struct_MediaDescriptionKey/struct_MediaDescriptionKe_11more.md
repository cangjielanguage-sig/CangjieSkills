## struct MediaDescriptionKey

```cangjie
public struct MediaDescriptionKey {
    public static const MD_KEY_TRACK_INDEX: String = "track_index"
    public static const MD_KEY_TRACK_TYPE: String = "track_type"
    public static const MD_KEY_CODEC_MIME: String = "codec_mime"
    public static const MD_KEY_DURATION: String = "duration"
    public static const MD_KEY_BITRATE: String = "bitrate"
    public static const MD_KEY_WIDTH: String = "width"
    public static const MD_KEY_HEIGHT: String = "height"
    public static const MD_KEY_FRAME_RATE: String = "frame_rate"
    public static const MD_KEY_AUD_CHANNEL_COUNT: String = "channel_count"
    public static const MD_KEY_AUD_SAMPLE_RATE: String = "sample_rate"
    public static const MD_KEY_AUD_SAMPLE_DEPTH: String = "sample_depth"
    public static const MD_KEY_LANGUAGE: String = "language"
    public static const MD_KEY_TRACK_NAME: String = "track_name"
    public static const MD_KEY_HDR_TYPE: String = "hdr_type"
}
```

**功能：** 媒体信息描述。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### static const MD_KEY_AUD_CHANNEL_COUNT

```cangjie
public static const MD_KEY_AUD_CHANNEL_COUNT: String = "channel_count"
```

**功能：** 表示声道数，其对应键值类型为Int32。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** String

**起始版本：** 19

### static const MD_KEY_AUD_SAMPLE_DEPTH

```cangjie
public static const MD_KEY_AUD_SAMPLE_DEPTH: String = "sample_depth"
```

**功能：** 表示位深，其对应键值类型为Int32，单位为位（bit）。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** String

**起始版本：** 19

### static const MD_KEY_AUD_SAMPLE_RATE

```cangjie
public static const MD_KEY_AUD_SAMPLE_RATE: String = "sample_rate"
```

**功能：** 表示采样率，其对应键值类型为Int32，单位为赫兹（Hz）。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** String

**起始版本：** 19

### static const MD_KEY_BITRATE

```cangjie
public static const MD_KEY_BITRATE: String = "bitrate"
```

**功能：** 表示比特率，其对应键值类型为Int32，单位为比特率（bps）。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** String

**起始版本：** 19

### static const MD_KEY_CODEC_MIME

```cangjie
public static const MD_KEY_CODEC_MIME: String = "codec_mime"
```

**功能：** 表示codec_mime类型，其对应键值类型为String。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** String

**起始版本：** 19

### static const MD_KEY_DURATION

```cangjie
public static const MD_KEY_DURATION: String = "duration"
```

**功能：** 表示媒体时长，其对应键值类型为Int32，单位为毫秒（ms）。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** String

**起始版本：** 19

### static const MD_KEY_FRAME_RATE

```cangjie
public static const MD_KEY_FRAME_RATE: String = "frame_rate"
```

**功能：** 表示视频帧率，其对应键值类型为Float64，单位为每100秒的帧数。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** String

**起始版本：** 19

### static const MD_KEY_HDR_TYPE

```cangjie
public static const MD_KEY_HDR_TYPE: String = "hdr_type"
```

**功能：** 表示视频高度，其对应键值类型为Int32，单位为像素（px）。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** String

**起始版本：** 19

### static const MD_KEY_HEIGHT

```cangjie
public static const MD_KEY_HEIGHT: String = "height"
```

**功能：** 表示视频高度，其对应键值类型为Int32，单位为像素（px）。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** String

**起始版本：** 19

### static const MD_KEY_LANGUAGE

```cangjie
public static const MD_KEY_LANGUAGE: String = "language"
```

**功能：** 表示字幕语言，其对应键值类型为String。

**系统能力：** SystemCapability.Multimedia.Media.Core

**类型：** String

**起始版本：** 19