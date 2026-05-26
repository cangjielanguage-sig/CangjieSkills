### var lyric

```cangjie
public var lyric: ?String
```

**功能：** 媒体歌词内容。应用需将歌词内容拼接为一个字符串传入。字符串长度需小于等于40960字节。说明： 系统支持简单版的LRC格式（Simple LRC format）的歌词文本内容。当传入的歌词内容不规范（如出现重复的时间戳等），将导致解析失败以及在系统中显示异常。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var mediaImage

```cangjie
public var mediaImage: ?ValueType
```

**功能：** 图片的像素数据或者图片路径地址(本地路径或网络路径)。应用通过[setAVMetadata](#func-setavmetadataavmetadata)设置图片数据，当设置的数据类型为[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)时，通过[getAVMetadata](#func-getavmetadata)获取的将为[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)。设置为url图片路径，获取的亦为url图片路径。

**类型：** ?[ValueType](#enum-valuetype)

**读写能力：** 可读写

**起始版本：** 19

### var nextAssetId

```cangjie
public var nextAssetId: ?String
```

**功能：** 下一首媒体ID。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var previousAssetId

```cangjie
public var previousAssetId: ?String
```

**功能：** 上一首媒体ID。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var publishDate

```cangjie
public var publishDate: ?DateTime
```

**功能：** 发行日期。

**类型：** ?DateTime

**读写能力：** 可读写

**起始版本：** 19

### var skipIntervals

```cangjie
public var skipIntervals: ?SkipIntervals
```

**功能：** 快进快退支持的时间间隔，默认为SECONDS_15，即15秒。

**类型：** ?[SkipIntervals](#enum-skipintervals)

**读写能力：** 可读写

**起始版本：** 19

### var subtitle

```cangjie
public var subtitle: ?String
```

**功能：** 子标题。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var title

```cangjie
public var title: ?String
```

**功能：** 标题。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var writer

```cangjie
public var writer: ?String
```

**功能：** 词作者。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19