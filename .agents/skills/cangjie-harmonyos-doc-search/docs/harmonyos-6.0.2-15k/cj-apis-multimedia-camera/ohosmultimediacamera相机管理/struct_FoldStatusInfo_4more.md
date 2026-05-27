## struct FoldStatusInfo

```cangjie
public struct FoldStatusInfo {
    public let supportedCameras: Array<CameraDevice>
    public let foldStatus: FoldStatus
    public init(supportedCameras: Array<CameraDevice>, foldStatus: FoldStatus)
}
```

**功能：** 相机管理器回调返回的接口实例，表示折叠机折叠状态信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### let foldStatus

```cangjie
public let foldStatus: FoldStatus
```

**功能：** 折叠屏折叠状态。

**类型：** [FoldStatus](#enum-foldstatus)

**读写能力：** 只读

**起始版本：** 19

### let supportedCameras

```cangjie
public let supportedCameras: Array<CameraDevice>
```

**功能：** 当前折叠状态所支持的相机信息列表。

**类型：** Array\<[CameraDevice](#class-cameradevice)>

**读写能力：** 只读

**起始版本：** 19

### init(Array\<CameraDevice>, FoldStatus)

```cangjie
public init(supportedCameras: Array<CameraDevice>, foldStatus: FoldStatus)
```

**功能：** 创建FoldStatusInfo对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|supportedCameras|Array\<[CameraDevice](#class-cameradevice)>|是|-|当前折叠状态所支持的相机信息列表。|
|foldStatus|[FoldStatus](#enum-foldstatus)|是|-|折叠屏折叠状态。|

## struct FrameRateRange

```cangjie
public struct FrameRateRange {
    public let min: Int32
    public let max: Int32
}
```

**功能：** 帧率范围。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### let max

```cangjie
public let max: Int32
```

**功能：** 最大帧率。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let min

```cangjie
public let min: Int32
```

**功能：** 最小帧率。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

## struct FrameShutterEndInfo

```cangjie
public struct FrameShutterEndInfo {
    public var captureId: Int32
}
```

**功能：** 拍照曝光结束信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### var captureId

```cangjie
public var captureId: Int32
```

**功能：** 拍照的ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

## struct FrameShutterInfo

```cangjie
public struct FrameShutterInfo {
    public var captureId: Int32
    public var timestamp: UInt64
}
```

**功能：** 拍照帧输出信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### var captureId

```cangjie
public var captureId: Int32
```

**功能：** 拍照的ID。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### var timestamp

```cangjie
public var timestamp: UInt64
```

**功能：** 快门时间戳。

**类型：** UInt64

**读写能力：** 可读写

**起始版本：** 19