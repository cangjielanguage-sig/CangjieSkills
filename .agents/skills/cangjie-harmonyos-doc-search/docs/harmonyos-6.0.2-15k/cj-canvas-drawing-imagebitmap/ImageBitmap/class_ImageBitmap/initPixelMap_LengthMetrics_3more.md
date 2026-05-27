### init(PixelMap, LengthMetricsUnit)

```cangjie
public init(date: PixelMap, unit!: LengthMetricsUnit = LengthMetricsUnit.DEFAULT)
```

**功能：** 构造一个ImageBitmap类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|date|[PixelMap](../apis/ImageKit/cj-apis-image.md#class-pixelmap)|是|-|图片的数据源支持PixelMap对象。|
|unit|[LengthMetricsUnit](./cj-common-types.md#enum-lengthmetricsunit)|否|LengthMetricsUnit.DEFAULT| **命名参数。** 用来配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](./cj-canvas-drawing-canvasrenderingcontext2d.md#class-canvasrenderingcontext2d)。|

### init(String, LengthMetricsUnit)

```cangjie
public init(date: String, unit: LengthMetricsUnit)
```

**功能：** 构造一个ImageBitmap类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|date|String|是|-|图片的数据源支持本地图片。<br>1、string格式用于加载本地图片，例如ImageBitmap("common/images/example.jpg")，type为"entry"和"feature"类型的Module，其图片加载路径的起点为当前Module的ets文件夹，type为"har"和"shared"类型的Module，其图片加载路径的起点为当前构建的"entry"或"feature"类型Module的ets文件夹。type为"har"和"shared"类型的Module中推荐使用ImageSource图片解码方式将资源图片解码为统一的PixelMap加载使用。<br>2、支持本地图片类型：bmp、jpg、png、svg和webp类型。|
|unit|[LengthMetricsUnit](./cj-common-types.md#enum-lengthmetricsunit)|是|-|用来配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](./cj-canvas-drawing-canvasrenderingcontext2d.md#class-canvasrenderingcontext2d)。|

### func close()

```cangjie
public func close(): Unit
```

**功能：** 释放ImageBitmap对象相关联的所有图形资源，并将ImageBitmap对象的宽高置为0。close示例代码同创建ImageBitmap代码。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 19