## enum CameraEvents

```cangjie
public enum CameraEvents {
    | CameraError
    | CameraStatus
    | FoldStatusChange
    | TorchStatusChange
    | FrameStart
    | FrameEnd
    | CaptureStartWithInfo
    | FrameShutter
    | CaptureEnd
    | FrameShutterEnd
    | CaptureReady
    | EstimatedCaptureDuration
    | MetadataObjectsAvailable
    | FocusStateChange
    | SmoothZoomInfoAvailable
    | ...
}
```

**功能：** 监听事件名。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- Equatable\<CameraEvents>

### CameraError

```cangjie
CameraError
```

**功能：** 错误事件。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CameraStatus

```cangjie
CameraStatus
```

**功能：** 相机的状态变化。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CaptureEnd

```cangjie
CaptureEnd
```

**功能：** 拍照结束。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CaptureReady

```cangjie
CaptureReady
```

**功能：** 可拍下一张。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### CaptureStartWithInfo

```cangjie
CaptureStartWithInfo
```

**功能：** 拍照开始。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### EstimatedCaptureDuration

```cangjie
EstimatedCaptureDuration
```

**功能：** 预估的拍照时间。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FocusStateChange

```cangjie
FocusStateChange
```

**功能：** 相机聚焦的状态变化。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FoldStatusChange

```cangjie
FoldStatusChange
```

**功能：** 折叠设备折叠状态发生变化。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FrameEnd

```cangjie
FrameEnd
```

**功能：** 预览帧结束。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FrameShutter

```cangjie
FrameShutter
```

**功能：** 拍照帧输出捕获。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FrameShutterEnd

```cangjie
FrameShutterEnd
```

**功能：** 拍照曝光结束。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### FrameStart

```cangjie
FrameStart
```

**功能：** 预览帧启动。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### MetadataObjectsAvailable

```cangjie
MetadataObjectsAvailable
```

**功能：** 检测到metadata对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### SmoothZoomInfoAvailable

```cangjie
SmoothZoomInfoAvailable
```

**功能：** 相机平滑变焦的状态变化。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### TorchStatusChange

```cangjie
TorchStatusChange
```

**功能：** 手电筒状态变化。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func !=(CameraEvents)

```cangjie
public operator func !=(other: CameraEvents): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraEvents](#enum-cameraevents)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true表示不相等，false表示相等。|