### func setPixelMap(PixelMap)

```cangjie
public func setPixelMap(pixelMap: PixelMap): Unit
```

**功能：** 将当前传入[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)对象绘制在画布上。setPixelMap示例同[getPixelMap](#func-getpixelmapint64-int64-int64-int64)。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|pixelMap|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)|是|-|包含像素值的PixelMap对象。<br>初始值：None。|

### func setTransform(Float64, Float64, Float64, Float64, Float64, Float64)

```cangjie
public func setTransform(
    scaleX: Float64,
    skewX: Float64,
    skewY: Float64,
    scaleY: Float64,
    translateX: Float64,
    translateY: Float64
): Unit
```

**功能：** 对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|scaleX|Float64|是|-|指定水平缩放值。|
|skewX|Float64|是|-|指定水平倾斜值。|
|skewY|Float64|是|-|指定垂直倾斜值。|
|scaleY|Float64|是|-|指定垂直缩放值。|
|translateX|Float64|是|-|指定水平移动值。<br>默认单位：vp。|
|translateY|Float64|是|-|指定垂直移动值。<br>默认单位：vp。|

### func setTransform(Matrix2D)

```cangjie
public func setTransform(matrix: Matrix2D): Unit
```

**功能：** 以Matrix2D对象为模板重置现有的变换矩阵并创建新的变换矩阵。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|matrix|[Matrix2D](./cj-canvas-drawing-matrix2d.md#class-matrix2d)|是|-| 变换矩阵。|

### func shadowBlur(Float64)

```cangjie
public func shadowBlur(blur: Float64): Unit
```

**功能：** 设置绘制阴影时的模糊级别，值越大越模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|blur|Float64|是|-|设置绘制阴影时的模糊级别，值越大越模糊，精度为float，取值范围≥0。<br>初始值：0.0。 <br>单位：px。<br>shadowBlur取值不支持负数，负数按异常值处理，异常值按默认值处理。|

### func shadowBlur(Int64)

```cangjie
public func shadowBlur(offset: Int64): Unit
```

**功能：** 设置绘制阴影时的模糊级别，值越大越模糊。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|offset|Int64|是|-|设置绘制阴影时的模糊级别，值越大越模糊，精度为float，取值范围≥0。<br>初始值：0。 <br>单位：px。<br>shadowBlur取值不支持负数，负数按异常值处理，异常值按默认值处理|

### func shadowColor(ResourceColor)

```cangjie
public func shadowColor(color: ResourceColor): Unit
```

**功能：** 设置绘制阴影时的阴影颜色。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|[ResourceColor](./cj-common-types.md#interface-resourcecolor)|是|-|设置绘制阴影时的阴影颜色。|