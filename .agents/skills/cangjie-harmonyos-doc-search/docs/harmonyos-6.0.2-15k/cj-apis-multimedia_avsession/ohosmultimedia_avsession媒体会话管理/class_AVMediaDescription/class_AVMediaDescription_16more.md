## class AVMediaDescription

```cangjie
public class AVMediaDescription {
    public AVMediaDescription(
        public var assetId: String,
        public var title: ?String,
        public var subtitle: ?String,
        public var description: ?String,
        public var mediaImage: ?ValueType,
        public var extras: ?HashMap<String, ValueType>,
        public var mediaUri: ?String,
        public var mediaType: ?String,
        public var mediaSize: ?Int32,
        public var albumTitle: ?String,
        public var albumCoverUri: ?String,
        public var lyricContent: ?String,
        public var lyricUri: ?String,
        public var artist: ?String,
        public var fdSrc: ?AVFileDescriptor,
        public var dataSrc: ?AVDataSrcDescriptor,
        public var drmScheme: ?String,
        public var duration: ?Int64,
        public var startPosition: ?Int64,
        public var creditsPosition: ?Int64,
        public var appName: ?String,
        public var displayTags: ?DisplayTag
    )
    public init(assetId: String)
}
```

**功能：** 播放列表媒体元数据的相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### var albumCoverUri

```cangjie
public var albumCoverUri: ?String
```

**功能：** 播放列表媒体专辑标题URI。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var albumTitle

```cangjie
public var albumTitle: ?String
```

**功能：** 播放列表媒体专辑标题。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var appName

```cangjie
public var appName: ?String
```

**功能：** 播放列表提供的应用的名字。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var artist

```cangjie
public var artist: ?String
```

**功能：** 播放列表媒体专辑作者。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var assetId

```cangjie
public var assetId: String
```

**功能：** 播放列表媒体ID。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var creditsPosition

```cangjie
public var creditsPosition: ?Int64
```

**功能：** 播放列表媒体的片尾播放位置。

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 19

### var dataSrc

```cangjie
public var dataSrc: ?AVDataSrcDescriptor
```

**功能：** 播放列表数据源描述。

**类型：** ?[AVDataSrcDescriptor](../MediaKit/cj-apis-multimedia_media.md#class-avdatasrcdescriptor)

**读写能力：** 可读写

**起始版本：** 19

### var description

```cangjie
public var description: ?String
```

**功能：** 播放列表媒体描述的文本。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var displayTags

```cangjie
public var displayTags: ?DisplayTag
```

**功能：** 媒体资源的金标类型，取值参考[DisplayTag](#enum-displaytag)。

**类型：** ?[DisplayTag](#enum-displaytag)

**读写能力：** 可读写

**起始版本：** 19

### var drmScheme

```cangjie
public var drmScheme: ?String
```

**功能：** 播放列表媒体支持的DRM方案，由uuid表示。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var duration

```cangjie
public var duration: ?Int64
```

**功能：** 播放列表媒体播放时长。

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 19

### var extras

```cangjie
public var extras: ?HashMap<String, ValueType>
```

**功能：** 播放列表媒体额外字段。

**类型：** ?HashMap\<String, [ValueType](#enum-valuetype)>

**读写能力：** 可读写

**起始版本：** 19

### var fdSrc

```cangjie
public var fdSrc: ?AVFileDescriptor
```

**功能：** 播放列表媒体本地文件的句柄。

**类型：** ?[AVFileDescriptor](../MediaKit/cj-apis-multimedia_media.md#class-avfiledescriptor)

**读写能力：** 可读写

**起始版本：** 19

### var lyricContent

```cangjie
public var lyricContent: ?String
```

**功能：** 播放列表媒体歌词内容。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var lyricUri

```cangjie
public var lyricUri: ?String
```

**功能：** 播放列表媒体歌词URI。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19