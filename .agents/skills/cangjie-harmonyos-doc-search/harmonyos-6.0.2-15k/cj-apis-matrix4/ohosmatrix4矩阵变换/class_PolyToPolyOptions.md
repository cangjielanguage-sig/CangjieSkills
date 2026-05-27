## class PolyToPolyOptions

```cangjie
public class PolyToPolyOptions {
    public let src: Array<Point>
    public let srcIndex: Int32
    public let dst: Array<Point>
    public let dstIndex: Int32
    public let pointCount: Int32
    public init(
        src!: Array<Point>,
        srcIndex!: Int32 = 0,
        dst!: Array<Point>,
        dstIndex!: Int32 = 0,
        pointCount!: Int32 = Int32(src.size) / 2
    )
}
```

**功能：** 表示一个多边形的顶点坐标映射到另外一个多边形的顶点坐标。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let src

```cangjie
public let src: Array<Point>
```

**功能：** 表示源点坐标。

**类型：** Array\<[Point](#class-point)>

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let srcIndex

```cangjie
public let srcIndex: Int32
```

**功能：** 表示源点坐标起始索引。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let dst

```cangjie
public let dst: Array<Point>
```

**功能：** 表示目标点坐标。

**类型：** Array\<[Point](#class-point)>

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let dstIndex

```cangjie
public let dstIndex: Int32
```

**功能：** 表示目标坐标起始索引。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### let pointCount

```cangjie
public let pointCount: Int32
```

**功能：** 表示使用到的点数量。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

### init(Array\<Point>, Int32, Array\<Point>, Int32, Int32)

```cangjie
public init(
    src!: Array<Point>,
    srcIndex!: Int32 = 0,
    dst!: Array<Point>,
    dstIndex!: Int32 = 0,
    pointCount!: Int32 = Int32(src.size) / 2
)
```

**功能：** PolyToPolyOptions构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|Array\<[Point](#class-point)>|是|-| **命名参数。** 源点坐标。|
|srcIndex|Int32|否|0| **命名参数。** 源点坐标起始索引。<br>取值范围：[0, +∞)|
|dst|Array\<[Point](#class-point)>|是|-| **命名参数。** 目标点坐标。|
|dstIndex|Int32|否|0| **命名参数。** 目标坐标起始索引。<br>取值范围：[0, +∞)|
|pointCount|Int32|否|Int32(src.size) / 2| **命名参数。** 使用到的点数量。<br>取值范围：[0, +∞)|