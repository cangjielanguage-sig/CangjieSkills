### AVMetadata(String, ?String, ?String, ?String, ?String, ?String, ?ValueType, ?String, ?String, ?String, ?Int64, ?ValueType, ?DateTime, ?String, ?String, ?String, ?String, ?String, ?Array\<ProtocolType>, ?Array\<String>, ?SkipIntervals, ?DisplayTag)

```cangjie
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
```

**功能：** [AVMetadata](#class-avmetadata)构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|assetId|String|是|-|媒体ID。歌曲的唯一标识，由应用自定义。|
|title|?String|是|-|标题。|
|artist|?String|是|-|艺术家。|
|author|?String|是|-|专辑作者。|
|avQueueName|?String|是|-|歌单（歌曲列表）名称。|
|avQueueId|?String|是|-|歌单（歌曲列表）唯一标识Id。|
|avQueueImage|?[ValueType](#enum-valuetype)|是|-|歌单（歌曲列表）封面图，图片的像素数据或者图片路径地址(本地路径或网络路径)。应用通过[setAVMetadata](#func-setavmetadataavmetadata)设置图片数据，当设置的数据类型为[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)时，通过[getAVMetadata](#func-getavmetadata)获取的将为[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)。设置为url图片路径，获取的亦为url图片路径。|
|album|?String|是|-|专辑名称。|
|writer|?String|是|-|词作者。|
|composer|?String|是|-|作曲者。|
|duration|?Int64|是|-|媒体时长，单位毫秒（ms）。|
|mediaImage|?[ValueType](#enum-valuetype)|是|-|图片的像素数据或者图片路径地址(本地路径或网络路径)。应用通过[setAVMetadata](#func-setavmetadataavmetadata)设置图片数据，当设置的数据类型为[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)时，通过[getAVMetadata](#func-getavmetadata)获取的将为[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)。设置为url图片路径，获取的亦为url图片路径。|
|publishDate|?DateTime|是|-|发行日期。|
|subtitle|?String|是|-|子标题。|
|description|?String|是|-|媒体描述。|
|lyric|?String|是|-|媒体歌词内容。应用需将歌词内容拼接为一个字符串传入。字符串长度需小于等于40960字节。说明： 系统支持简单版的LRC格式（Simple LRC format）的歌词文本内容。当传入的歌词内容不规范（如出现重复的时间戳等），将导致解析失败以及在系统中显示异常。|
|previousAssetId|?String|是|-|上一首媒体ID。|
|nextAssetId|?String|是|-|下一首媒体ID。|
|filter|?Array\<[ProtocolType](#enum-protocoltype)>|是|-|当前session支持的协议，默认为TYPE_CAST_PLUS_STREAM。具体取值参[ProtocolType](#enum-protocoltype)。|
|drmSchemes|?Array\<String>|是|-|当前session支持的DRM方案，取值为DRM方案uuid。|
|skipIntervals|?[SkipIntervals](#enum-skipintervals)|是|-|快进快退支持的时间间隔，默认为SECONDS_15，即15秒。|
|displayTags|?[DisplayTag](#enum-displaytag)|是|-|媒体资源的金标类型，取值参考DisplayTag。|