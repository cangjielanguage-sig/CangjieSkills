## class AVPlaybackState

```cangjie
public class AVPlaybackState {
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
    public init()
}
```

**功能：** 媒体播放状态的相关属性。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### var activeItemId

```cangjie
public var activeItemId: ?Int32
```

**功能：** 正在播放的媒体Id。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var bufferedTime

```cangjie
public var bufferedTime: ?Int64
```

**功能：** 缓冲时间。

**类型：** ?Int64

**读写能力：** 可读写

**起始版本：** 19

### var duration

```cangjie
public var duration: ?Int32
```

**功能：** 当前媒体资源的时长。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var extras

```cangjie
public var extras: ?HashMap<String, ValueType>
```

**功能：** 自定义媒体数据。

**类型：** ?HashMap\<String, [ValueType](#enum-valuetype)>

**读写能力：** 可读写

**起始版本：** 19

### var isFavorite

```cangjie
public var isFavorite: ?Bool
```

**功能：** 是否收藏。

**类型：** ?Bool

**读写能力：** 可读写

**起始版本：** 19

### var loopMode

```cangjie
public var loopMode: ?LoopMode
```

**功能：** 循环模式。

**类型：** ?[LoopMode](#enum-loopmode)

**读写能力：** 可读写

**起始版本：** 19

### var maxVolume

```cangjie
public var maxVolume: ?Int32
```

**功能：** 最大音量。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var muted

```cangjie
public var muted: ?Bool
```

**功能：** 当前静音状态，true表示静音。

**类型：** ?Bool

**读写能力：** 可读写

**起始版本：** 19

### var position

```cangjie
public var position: ?PlaybackPosition
```

**功能：** 播放位置。

**类型：** ?[PlaybackPosition](#class-playbackposition)

**读写能力：** 可读写

**起始版本：** 19

### var speed

```cangjie
public var speed: ?Float64
```

**功能：** 播放倍速。

**类型：** ?Float64

**读写能力：** 可读写

**起始版本：** 19

### var state

```cangjie
public var state: ?PlaybackState
```

**功能：** 播放状态。

**类型：** ?[PlaybackState](#enum-playbackstate)

**读写能力：** 可读写

**起始版本：** 19

### var videoHeight

```cangjie
public var videoHeight: ?Int32
```

**功能：** 媒体资源的视频高度，单位为像素（px）。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var videoWidth

```cangjie
public var videoWidth: ?Int32
```

**功能：** 媒体资源的视频宽度，单位为像素（px）。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var volume

```cangjie
public var volume: ?Int32
```

**功能：** 正在播放的媒体音量。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19