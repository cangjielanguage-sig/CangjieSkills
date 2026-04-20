## class AVMetadata

```cangjie
public class AVMetadata {
    public AVMetadata(
        public var assetId: String,
        public var title: ?String,
        public var artist: ?String,
        public var author: ?String,
        public var avQueueName: ?String,
        public var avQueueId: ?String,
        public var avQueueImage: ?ValueType,
        public var album: ?String,
        public var writer: ?String,
        public var composer: ?String,
        public var duration: ?Int64,
        public var mediaImage: ?ValueType,
        public var publishDate: ?DateTime,
        public var subtitle: ?String,
        public var description: ?String,
        public var lyric: ?String,
        public var previousAssetId: ?String,
        public var nextAssetId: ?String,
        public var filter: ?Array<ProtocolType>,
        public var drmSchemes: ?Array<String>,
        public var skipIntervals: ?SkipIntervals,
        public var displayTags: ?DisplayTag
    )
    public init(assetId: String)
}
```

**功能：** 媒体元数据的相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### var album

```cangjie
public var album: ?String
```

**功能：** 专辑名称。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var artist

```cangjie
public var artist: ?String
```

**功能：** 艺术家。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var assetId

```cangjie
public var assetId: String
```

**功能：** 媒体ID。歌曲的唯一标识，由应用自定义。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var author

```cangjie
public var author: ?String
```

**功能：** 专辑作者。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var avQueueId

```cangjie
public var avQueueId: ?String
```

**功能：** 歌单（歌曲列表）唯一标识Id。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var avQueueImage

```cangjie
public var avQueueImage: ?ValueType
```

**功能：** 歌单（歌曲列表）封面图，图片的像素数据或者图片路径地址(本地路径或网络路径)。应用通过[setAVMetadata](#func-setavmetadataavmetadata)设置图片数据，当设置的数据类型为[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)时，通过[getAVMetadata](#func-getavmetadata)获取的将为[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)。设置为url图片路径，获取的亦为url图片路径。

**类型：** ?[ValueType](#enum-valuetype)

**读写能力：** 可读写

**起始版本：** 19

### var avQueueName

```cangjie
public var avQueueName: ?String
```

**功能：** 歌单（歌曲列表）名称。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var composer

```cangjie
public var composer: ?String
```

**功能：** 作曲者。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var description

```cangjie
public var description: ?String
```

**功能：** 媒体描述。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var displayTags

```cangjie
public var displayTags: ?DisplayTag
```

**功能：** 媒体资源的金标类型，取值参考DisplayTag。

**类型：** ?[DisplayTag](#enum-displaytag)

**读写能力：** 可读写

**起始版本：** 19

### var drmSchemes

```cangjie
public var drmSchemes: ?Array<String>
```

**功能：** 当前session支持的DRM方案，取值为DRM方案uuid。

**类型：** ?Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### var duration

```cangjie
public var duration: ?Int64
```

**功能：** 媒体时长，单位毫秒（ms）。

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 19

### var filter

```cangjie
public var filter: ?Array<ProtocolType>
```

**功能：** 当前session支持的协议，默认为TYPE_CAST_PLUS_STREAM。具体取值参[ProtocolType](#enum-protocoltype)。

**类型：** ?Array\<[ProtocolType](#enum-protocoltype)>

**读写能力：** 可读写

**起始版本：** 19