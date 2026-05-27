## class AVMetadata

```cangjie
public class AVMetadata {}
```

**功能：** 音视频元数据，包含各个元数据字段。在[AVRecorderConfig](#class-avrecorderconfig)中使用时未声明为当前版本只读的参数可以作为使用[AVRecorder](#class-avrecorder)录制时的入参。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 19

### var album

```cangjie
public var album: ?String = None
```

**功能：** 专辑的标题。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var albumArtist

```cangjie
public var albumArtist: ?String = None
```

**功能：** 专辑的艺术家。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var artist

```cangjie
public var artist: ?String = None
```

**功能：** 媒体资源的艺术家。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var author

```cangjie
public var author: ?String = None
```

**功能：** 媒体资源的作者。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var composer

```cangjie
public var composer: ?String = None
```

**功能：** 媒体资源的作曲家。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var customInfo

```cangjie
public var customInfo: ?HashMap<String, String> = None
```

**功能：** 从moov.meta.list 获取的自定义参数键值映射。

**类型：** ?HashMap\<String, String>

**读写能力：** 可读写

**起始版本：** 19

### var dateTime

```cangjie
public var dateTime: ?String = None
```

**功能：** 媒体资源的创建时间。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var dateTimeFormat

```cangjie
public var dateTimeFormat: ?String = None
```

**功能：** 媒体资源的创建时间，按YYYY-MM-DD HH:mm:ss格式输出。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var duration

```cangjie
public var duration: ?String = None
```

**功能：** 媒体资源的时长。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var genre

```cangjie
public var genre: ?String = None
```

**功能：** 媒体资源的类型或体裁。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var hasAudio

```cangjie
public var hasAudio: ?String = None
```

**功能：** 媒体资源是否包含音频。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var hasVideo

```cangjie
public var hasVideo: ?String = None
```

**功能：** 媒体资源是否包含视频。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var hdrType

```cangjie
public var hdrType: ?HdrType = None
```

**功能：** 媒体资源的HDR类型。当前版本为只读成员变量。

**类型：** ?[HdrType](#enum-hdrtype)

**读写能力：** 可读写

**起始版本：** 19

### var location

```cangjie
public var location: ?Location = None
```

**功能：** 视频的地理位置信息。

**类型：** ?[Location](#class-location)

**读写能力：** 可读写

**起始版本：** 19

### var mimeType

```cangjie
public var mimeType: ?String = None
```

**功能：** 媒体资源的mime类型。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var sampleRate

```cangjie
public var sampleRate: ?String = None
```

**功能：** 音频的采样率，单位为赫兹（Hz）。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var title

```cangjie
public var title: ?String = None
```

**功能：** 媒体资源的标题。当前版本为只读成员变量。当前版本为只读成员变量。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19