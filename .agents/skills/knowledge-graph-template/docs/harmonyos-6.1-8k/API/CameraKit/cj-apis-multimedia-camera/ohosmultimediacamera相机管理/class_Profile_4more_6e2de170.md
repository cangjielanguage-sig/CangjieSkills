## class Profile

```cangjie
public open class Profile {
    public let format: CameraFormat
    public let size: Size
}
```

**功能：** 相机配置信息项。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let format

```cangjie
public let format: CameraFormat
```

**功能：** 输出格式。

**类型：** [CameraFormat](#enum-cameraformat)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let size

```cangjie
public let size: Size
```

**功能：** 分辨率。

设置的是相机的分辨率宽度和高度，而非实际输出图像的宽度和高度。

**类型：** [Size](#class-size)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

## class Rect

```cangjie
public class Rect {
    public var topLeftX: Float64
    public var topLeftY: Float64
    public var width: Float64
    public var height: Float64
}
```

**功能：** 矩形定义，返回的检测点坐标系以设备充电口在右侧时的横向设备方向为基准。该坐标系左上角为（0，0），右下角为（1，1），其中（topLeftX，topLeftY）表示矩形区域的左上角坐标，width和height分别表示矩形区域的宽和高。因此在实际使用中根据业务诉求需要裁剪或者选择人脸区域时，必须将矩形区域的x坐标和y坐标分别乘以实际相机输出流的宽和高，即可得到裁剪后的人脸矩形区域。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var height

```cangjie
public var height: Float64
```

**功能：** 矩形高，相对值，范围[0.0, 1.0]。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var topLeftX

```cangjie
public var topLeftX: Float64
```

**功能：** 矩形区域左上角x坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var topLeftY

```cangjie
public var topLeftY: Float64
```

**功能：** 矩形区域左上角y坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var width

```cangjie
public var width: Float64
```

**功能：** 矩形宽，相对值，范围[0.0, 1.0]。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

## class Size

```cangjie
public class Size {
    public var width: UInt32
    public var height: UInt32
}
```

**功能：** 尺寸参数。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var height

```cangjie
public var height: UInt32
```

**功能：** 图像尺寸高(像素)。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var width

```cangjie
public var width: UInt32
```

**功能：** 图像尺寸宽(像素)。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

## class SmoothZoomInfo

```cangjie
public class SmoothZoomInfo {
    public var duration: Int32
}
```

**功能：** 平滑变焦参数信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var duration

```cangjie
public var duration: Int32
```

**功能：** 平滑变焦总时长，单位ms。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22