### AVPlaybackState(?PlaybackState, ?Float64, ?PlaybackPosition, ?Int64, ?LoopMode, ?Bool, ?Int32, ?Int32, ?Int32, ?Bool, ?Int32, ?Int32, ?Int32, ?HashMap\<String, ValueType>)

```cangjie
public AVPlaybackState(
    public var state: ?PlaybackState,
    public var speed: ?Float64,
    public var position: ?PlaybackPosition,
    public var bufferedTime: ?Int64,
    public var loopMode: ?LoopMode,
    public var isFavorite: ?Bool,
    public var activeItemId: ?Int32,
    public var volume: ?Int32,
    public var maxVolume: ?Int32,
    public var muted: ?Bool,
    public var duration: ?Int32,
    public var videoWidth: ?Int32,
    public var videoHeight: ?Int32,
    public var extras: ?HashMap<String, ValueType>
)
```

**功能：** [AVPlaybackState](#class-avplaybackstate)构造函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|state|?[PlaybackState](#enum-playbackstate)|是|-|播放状态。|
|speed|?Float64|是|-|播放倍速。|
|position|?[PlaybackPosition](#class-playbackposition)|是|-|播放位置。|
|bufferedTime|?Int64|是|-|缓冲时间。|
|loopMode|?[LoopMode](#enum-loopmode)|是|-|循环模式。|
|isFavorite|?Bool|是|-|是否收藏。|
|activeItemId|?Int32|是|-|正在播放的媒体Id。|
|volume|?Int32|是|-|正在播放的媒体音量。|
|maxVolume|?Int32|是|-|最大音量。|
|muted|?Bool|是|-|当前静音状态，true表示静音。|
|duration|?Int32|是|-|当前媒体资源的时长。|
|videoWidth|?Int32|是|-|媒体资源的视频宽度，单位为像素（px）。|
|videoHeight|?Int32|是|-|媒体资源的视频高度，单位为像素（px）。|
|extras|?HashMap\<String, [ValueType](#enum-valuetype)>|是|-|自定义媒体数据。|

### init()

```cangjie
public init()
```

**功能：** [AVPlaybackState](#class-avplaybackstate)构造函数。

**起始版本：** 19