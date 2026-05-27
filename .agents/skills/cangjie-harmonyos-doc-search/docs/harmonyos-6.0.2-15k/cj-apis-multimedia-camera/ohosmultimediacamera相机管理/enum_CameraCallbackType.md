## enum CameraCallbackType

```cangjie
public enum CameraCallbackType <: ToString & Equatable<CameraCallbackType> {
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

**起始版本：** 19

**父类型：**

- ToString
- Equatable\<CameraCallbackType>

### CameraError

```cangjie
CameraError
```

**功能：** 错误事件。

**起始版本：** 19

### CameraStatus

```cangjie
CameraStatus
```

**功能：** 相机的状态变化。

**起始版本：** 19

### CaptureEnd

```cangjie
CaptureEnd
```

**功能：** 拍照结束。

**起始版本：** 19

### CaptureReady

```cangjie
CaptureReady
```

**功能：** 可拍下一张。

**起始版本：** 19

### CaptureStartWithInfo

```cangjie
CaptureStartWithInfo
```

**功能：** 拍照开始。

**起始版本：** 19

### EstimatedCaptureDuration

```cangjie
EstimatedCaptureDuration
```

**功能：** 预估的拍照时间。

**起始版本：** 19

### FocusStateChange

```cangjie
FocusStateChange
```

**功能：** 相机聚焦的状态变化。

**起始版本：** 19

### FoldStatusChange

```cangjie
FoldStatusChange
```

**功能：** 折叠设备折叠状态发生变化。

**起始版本：** 19

### FrameEnd

```cangjie
FrameEnd
```

**功能：** 预览帧结束。

**起始版本：** 19

### FrameShutter

```cangjie
FrameShutter
```

**功能：** 拍照帧输出捕获。

**起始版本：** 19

### FrameShutterEnd

```cangjie
FrameShutterEnd
```

**功能：** 拍照曝光结束。

**起始版本：** 19

### FrameStart

```cangjie
FrameStart
```

**功能：** 预览帧启动。

**起始版本：** 19

### MetadataObjectsAvailable

```cangjie
MetadataObjectsAvailable
```

**功能：** 检测到metadata对象。

**起始版本：** 19

### SmoothZoomInfoAvailable

```cangjie
SmoothZoomInfoAvailable
```

**功能：** 相机平滑变焦的状态变化。

**起始版本：** 19

### TorchStatusChange

```cangjie
TorchStatusChange
```

**功能：** 手电筒状态变化。

**起始版本：** 19

### func !=(CameraCallbackType)

```cangjie
public operator func !=(other: CameraCallbackType): Bool
```

**功能：** 判断两个枚举值是否不相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraCallbackType](#enum-cameracallbacktype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值不相等返回true，否则返回false。|

### func ==(CameraCallbackType)

```cangjie
public operator func ==(other: CameraCallbackType): Bool
```

**功能：** 判断两个枚举值是否相等。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[CameraCallbackType](#enum-cameracallbacktype)|是|-|另一个枚举值。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|两个枚举值相等返回true，否则返回false。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 获取枚举的值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|枚举的说明。|