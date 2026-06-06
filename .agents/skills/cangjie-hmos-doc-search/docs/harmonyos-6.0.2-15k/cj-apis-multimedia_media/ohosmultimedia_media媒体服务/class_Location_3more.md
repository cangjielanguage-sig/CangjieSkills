## class Location

```cangjie
public class Location {}
```

**功能：** 视频录制的地理位置。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

### var latitude

```cangjie
public var latitude: Float64
```

**功能：** 地理位置的纬度。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var longitude

```cangjie
public var longitude: Float64
```

**功能：** 地理位置的经度。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

## class MediaSource

```cangjie
public class MediaSource {}
```

**功能：** 媒体数据信息，通过[createMediaSourceWithUrl](#func-createmediasourcewithurlstring-hashmapstring-string)获取。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

## class OnAVRecorderStateChangeHandler

```cangjie
public class OnAVRecorderStateChangeHandler {
    public var state: AVRecorderState
    public var stateChangeReason: StateChangeReason
    public init(
        state: AVRecorderState,
        reason: StateChangeReason
    )
}
```

**功能：** 状态机切换事件回调方法类。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

### var state

```cangjie
public var state: AVRecorderState
```

**功能：** 当前播放状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** [AVRecorderState](#enum-avrecorderstate)

**读写能力：** 可读写

**起始版本：** 19

### var stateChangeReason

```cangjie
public var stateChangeReason: StateChangeReason
```

**功能：** 当前播放状态切换的原因。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**类型：** [StateChangeReason](#enum-statechangereason)

**读写能力：** 可读写

**起始版本：** 19

### init(AVRecorderState, StateChangeReason)

```cangjie
public init(state: AVRecorderState, reason: StateChangeReason)
```

**功能：** 构造OnAVRecorderStateChangeHandler实例。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|state|[AVRecorderState](#enum-avrecorderstate)|是|-|当前播放状态。|
|reason|[StateChangeReason](#enum-statechangereason)|是|-|当前播放状态的切换原因。|