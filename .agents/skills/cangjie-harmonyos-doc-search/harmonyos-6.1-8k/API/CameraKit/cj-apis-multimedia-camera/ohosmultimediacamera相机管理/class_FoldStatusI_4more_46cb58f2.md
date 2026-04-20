## class FoldStatusInfo

```cangjie
public class FoldStatusInfo {
    public let supportedCameras: Array<CameraDevice>
    public let foldStatus: FoldStatus
}
```

**功能：** 相机管理器回调返回的接口实例，表示折叠机折叠状态信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let foldStatus

```cangjie
public let foldStatus: FoldStatus
```

**功能：** 折叠屏折叠状态。

**类型：** [FoldStatus](#enum-foldstatus)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let supportedCameras

```cangjie
public let supportedCameras: Array<CameraDevice>
```

**功能：** 当前折叠状态所支持的相机信息列表。

**类型：** Array\<[CameraDevice](#class-cameradevice)>

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

## class FrameRateRange

```cangjie
public class FrameRateRange {
    public let min: Int32
    public let max: Int32
}
```

**功能：** 帧率范围。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let max

```cangjie
public let max: Int32
```

**功能：** 最大帧率，单位：fps。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let min

```cangjie
public let min: Int32
```

**功能：** 最小帧率，单位：fps。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

## class FrameShutterEndInfo

```cangjie
public class FrameShutterEndInfo {
    public var captureId: Int32
}
```

**功能：** 拍照曝光结束信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var captureId

```cangjie
public var captureId: Int32
```

**功能：** 拍照的ID。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

## class FrameShutterInfo

```cangjie
public class FrameShutterInfo {
    public var captureId: Int32
    public var timestamp: Int64
}
```

**功能：** 拍照帧输出信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var captureId

```cangjie
public var captureId: Int32
```

**功能：** 拍照的ID。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var timestamp

```cangjie
public var timestamp: Int64
```

**功能：** 快门时间戳，单位毫秒。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22