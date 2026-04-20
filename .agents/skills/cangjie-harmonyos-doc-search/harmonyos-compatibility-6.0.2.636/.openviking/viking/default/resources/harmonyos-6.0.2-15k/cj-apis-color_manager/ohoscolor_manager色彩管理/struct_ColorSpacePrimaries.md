## struct ColorSpacePrimaries

```cangjie
public struct ColorSpacePrimaries {
    public ColorSpacePrimaries(
        public let redX!: Float32,
        public let redY!: Float32,
        public let greenX!: Float32,
        public let greenY!: Float32,
        public let blueX!: Float32,
        public let blueY!: Float32,
        public let whitePointX!: Float32,
        public let whitePointY!: Float32
    )
}
```

**功能：** 色域标准三原色（红、绿、蓝）和白色，使用(x, y)表示其在色彩空间中的位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 12

### let blueX

```cangjie
public let blueX: Float32
```

**功能：** 标准蓝色在色彩空间的x坐标值。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### let blueY

```cangjie
public let blueY: Float32
```

**功能：** 标准蓝色在色彩空间的y坐标值。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### let greenX

```cangjie
public let greenX: Float32
```

**功能：** 标准绿色在色彩空间的x坐标值。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### let greenY

```cangjie
public let greenY: Float32
```

**功能：** 标准绿色在色彩空间的y坐标值。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### let redX

```cangjie
public let redX: Float32
```

**功能：** 标准红色在色彩空间的x坐标值。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### let redY

```cangjie
public let redY: Float32
```

**功能：** 标准红色在色彩空间的y坐标值。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### let whitePointX

```cangjie
public let whitePointX: Float32
```

**功能：** 标准白色在色彩空间的x坐标值。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### let whitePointY

```cangjie
public let whitePointY: Float32
```

**功能：** 标准白色在色彩空间的y坐标值。

**类型：** Float32

**读写能力：** 只读

**起始版本：** 12

### ColorSpacePrimaries(Float32, Float32, Float32, Float32, Float32, Float32, Float32, Float32)

```cangjie
public ColorSpacePrimaries(
    public let redX!: Float32,
    public let redY!: Float32,
    public let greenX!: Float32,
    public let greenY!: Float32,
    public let blueX!: Float32,
    public let blueY!: Float32,
    public let whitePointX!: Float32,
    public let whitePointY!: Float32
)
```

**功能：** ColorSpacePrimaries的主构造函数。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|redX|Float32|是|-| **命名参数。** 标准红色在色彩空间的x坐标值。|
|redY|Float32|是|-| **命名参数。** 标准红色在色彩空间的y坐标值。|
|greenX|Float32|是|-| **命名参数。** 标准绿色在色彩空间的x坐标值。|
|greenY|Float32|是|-| **命名参数。** 标准绿色在色彩空间的y坐标值。|
|blueX|Float32|是|-| **命名参数。** 标准蓝色在色彩空间的x坐标值。|
|blueY|Float32|是|-| **命名参数。** 标准蓝色在色彩空间的y坐标值。|
|whitePointX|Float32|是|-| **命名参数。** 标准白色在色彩空间的x坐标值。|
|whitePointY|Float32|是|-| **命名参数。** 标准白色在色彩空间的y坐标值。|