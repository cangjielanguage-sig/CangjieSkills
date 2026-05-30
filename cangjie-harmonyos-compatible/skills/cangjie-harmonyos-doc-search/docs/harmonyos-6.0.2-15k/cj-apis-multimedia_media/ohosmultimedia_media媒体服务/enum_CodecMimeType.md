## enum CodecMimeType

```cangjie
public enum CodecMimeType <: ToString & Equatable<CodecMimeType> {
    | VIDEO_H263
    | VIDEO_AVC
    | VIDEO_MPEG2
    | VIDEO_MPEG4
    | VIDEO_VP8
    | AUDIO_AAC
    | AUDIO_VORBIS
    | AUDIO_FLAC
    | VIDEO_HEVC
    | AUDIO_MP3
    | AUDIO_G711MU
    | UNKNOWN
    | ...
}
```

**功能：** Codec MIME类型枚举。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<CodecMimeType>

### AUDIO_AAC

```cangjie
AUDIO_AAC
```

**功能：** 表示音频/mp4a-latm类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### AUDIO_FLAC

```cangjie
AUDIO_FLAC
```

**功能：** 表示音频/flac类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### AUDIO_G711MU

```cangjie
AUDIO_G711MU
```

**功能：** 表示音频/G711-mulaw类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### AUDIO_MP3

```cangjie
AUDIO_MP3
```

**功能：** 表示音频/mpeg类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### AUDIO_VORBIS

```cangjie
AUDIO_VORBIS
```

**功能：** 表示音频/vorbis类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### UNKNOWN

```cangjie
UNKNOWN
```

**功能：** 表示未知Codec MIME类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### VIDEO_AVC

```cangjie
VIDEO_AVC
```

**功能：** 表示视频/avc类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### VIDEO_H263

```cangjie
VIDEO_H263
```

**功能：** 表示视频/h263类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### VIDEO_HEVC

```cangjie
VIDEO_HEVC
```

**功能：** 表示视频/H265类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### VIDEO_MPEG2

```cangjie
VIDEO_MPEG2
```

**功能：** 表示视频/mpeg2类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### VIDEO_MPEG4

```cangjie
VIDEO_MPEG4
```

**功能：** 表示视频/mpeg4类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### VIDEO_VP8

```cangjie
VIDEO_VP8
```

**功能：** 表示视频/vp8类型。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取Codec MIME类型枚举值的字符串表示。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|Codec MIME类型枚举值的字符串表示。|

### func !=(CodecMimeType)

```cangjie
public operator override func !=(that: CodecMimeType): Bool
```

**功能：** 对Codec MIME类型枚举值进行判不等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[CodecMimeType](#enum-codecmimetype)|是|-|Codec MIME类型枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果Codec MIME类型枚举值不等，返回true，否则返回false。|

### func ==(CodecMimeType)

```cangjie
public operator override func ==(that: CodecMimeType): Bool
```

**功能：** 对Codec MIME类型枚举值进行判等。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|that|[CodecMimeType](#enum-codecmimetype)|是|-|Codec MIME类型枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果Codec MIME类型枚举值相等，返回true，否则返回false。|