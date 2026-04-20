### AVMediaDescription(String, ?String, ?String, ?String, ?ValueType, ?HashMap\<String, ValueType>, ?String, ?String, ?Int32, ?String, ?String, ?String, ?String, ?String, ?AVFileDescriptor, ?AVDataSrcDescriptor, ?String, ?Int64, ?Int64, ?Int64, ?String, ?DisplayTag)

```cangjie
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
```

**功能：** [AVMediaDescription](#class-avmediadescription)构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|assetId|String|是|-|播放列表媒体ID。|
|title|?String|是|-|播放列表媒体标题。|
|subtitle|?String|是|-|播放列表媒体子标题。|
|description|?String|是|-|播放列表媒体描述的文本。|
|mediaImage|?[ValueType](#enum-valuetype)|是|-|播放列表媒体图片像素数据。|
|extras|?HashMap\<String, [ValueType](#enum-valuetype)>|是|-|播放列表媒体额外字段。|
|mediaUri|?String|是|-|播放列表媒体URI。|
|mediaType|?String|是|-|播放列表媒体类型。|
|mediaSize|?Int32|是|-|播放列表媒体的大小。|
|albumTitle|?String|是|-|播放列表媒体专辑标题。|
|albumCoverUri|?String|是|-|播放列表媒体专辑标题URI。|
|lyricContent|?String|是|-|播放列表媒体歌词内容。|
|lyricUri|?String|是|-|播放列表媒体歌词URI。|
|artist|?String|是|-|播放列表媒体专辑作者。|
|fdSrc|?[AVFileDescriptor](../MediaKit/cj-apis-multimedia_media.md#class-avfiledescriptor)|是|-|播放列表媒体本地文件的句柄。|
|dataSrc|?[AVDataSrcDescriptor](../MediaKit/cj-apis-multimedia_media.md#class-avdatasrcdescriptor)|是|-|播放列表数据源描述。|
|drmScheme|?String|是|-|播放列表媒体支持的DRM方案，由uuid表示。|
|duration|?Int64|是|-|播放列表媒体播放时长。|
|startPosition|?Int64|是|-|播放列表媒体起始播放位置。|
|creditsPosition|?Int64|是|-|播放列表媒体的片尾播放位置。|
|appName|?String|是|-|播放列表提供的应用的名字。|
|displayTags|?[DisplayTag](#enum-displaytag)|是|-|媒体资源的金标类型，取值参考[DisplayTag](#enum-displaytag)。|