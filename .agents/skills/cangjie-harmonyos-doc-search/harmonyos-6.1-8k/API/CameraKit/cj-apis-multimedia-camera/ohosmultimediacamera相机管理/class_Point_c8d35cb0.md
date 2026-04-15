## class Point

```cangjie
public class Point {
    public var x: Float64
    public var y: Float64
    public init(x: Float64, y: Float64)
}
```

**功能：** 点坐标用于对焦和曝光配置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var x

```cangjie
public var x: Float64
```

**功能：** 点的x坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### var y

```cangjie
public var y: Float64
```

**功能：** 点的y坐标。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### init(Float64, Float64)

```cangjie
public init(x: Float64, y: Float64)
```

**功能：** 创建Point对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float64|是|-|点的x坐标。|
|y|Float64|是|-|点的y坐标。|