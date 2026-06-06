## struct Point

```cangjie
public struct Point {
    public var x: Float32
    public var y: Float32
    public init(x: Float32, y: Float32)
}
```

**功能：** 点坐标用于对焦、曝光配置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### var x

```cangjie
public var x: Float32
```

**功能：** 点的x坐标。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### var y

```cangjie
public var y: Float32
```

**功能：** 点的y坐标。

**类型：** Float32

**读写能力：** 可读写

**起始版本：** 19

### init(Float32, Float32)

```cangjie
public init(x: Float32, y: Float32)
```

**功能：** 创建Point对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|点的x坐标。|
|y|Float32|是|-|点的y坐标。|

## struct Rect

```cangjie
public struct Rect {
    public var topLeftX: Float64
    public var topLeftY: Float64
    public var width: Float64
    public var height: Float64
}
```

**功能：** 矩形定义。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### var height

```cangjie
public var height: Float64
```

**功能：** 矩形高，相对值，范围[0.0, 1.0]。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var topLeftX

```cangjie
public var topLeftX: Float64
```

**功能：** 矩形区域左上角x坐标。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var topLeftY

```cangjie
public var topLeftY: Float64
```

**功能：** 矩形区域左上角y坐标。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

### var width

```cangjie
public var width: Float64
```

**功能：** 矩形宽，相对值，范围[0.0, 1.0]。

**类型：** Float64

**读写能力：** 可读写

**起始版本：** 19

## struct Size

```cangjie
public struct Size {
    public var width: UInt32
    public var height: UInt32
}
```

**功能：** 输出能力查询。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### var height

```cangjie
public var height: UInt32
```

**功能：** 图像尺寸高(像素)。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

### var width

```cangjie
public var width: UInt32
```

**功能：** 图像尺寸宽(像素)。

**类型：** UInt32

**读写能力：** 可读写

**起始版本：** 19

## struct SmoothZoomInfo

```cangjie
public struct SmoothZoomInfo {
    public SmoothZoomInfo(public var duration: Int32)
}
```

**功能：** 平滑变焦参数信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### var duration

```cangjie
public var duration: Int32
```

**功能：** 平滑变焦总时长，单位ms。

**类型：** Int32

**读写能力：** 可读写

**起始版本：** 19

### SmoothZoomInfo(Int32)

```cangjie
public SmoothZoomInfo(public var duration: Int32)
```

**功能：** 创建SmoothZoomInfo对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|Int32|是|-|平滑变焦总时长，单位ms。|