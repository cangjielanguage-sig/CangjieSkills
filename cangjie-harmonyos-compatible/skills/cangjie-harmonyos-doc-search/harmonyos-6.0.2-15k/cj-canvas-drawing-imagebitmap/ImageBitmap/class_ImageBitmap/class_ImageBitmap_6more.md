## class ImageBitmap

```cangjie
public class ImageBitmap {
    public init(src: String)
    public init(src: String, width: Float64, height: Float64)
    public init(src: String, width: Int64, height: Int64)
    public init(date: PixelMap, unit!: LengthMetricsUnit = LengthMetricsUnit.DEFAULT)
    public init(date: String, unit: LengthMetricsUnit)
}
```

**功能：** ImageBitmap对象可以存储canvas渲染的像素数据。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### prop height

```cangjie
public prop height: Float64
```

**功能：** ImageBitmap的像素高度。默认单位为vp。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### prop width

```cangjie
public prop width: Float64
```

**功能：** ImageBitmap的像素宽度。默认单位为vp。

**类型：** Float64

**读写能力：** 只读

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

### init(String)

```cangjie
public init(src: String)
```

**功能：** 构造一个ImageBitmap类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|图片的数据源支持本地图片。<br>1、string格式用于加载本地图片，例如ImageBitmap("common/images/example.jpg")，type为"entry"和"feature"类型的Module，其图片加载路径的起点为当前Module的ets文件夹，type为"har"和"shared"类型的Module，其图片加载路径的起点为当前构建的"entry"或"feature"类型Module的ets文件夹。type为"har"和"shared"类型的Module中推荐使用ImageSource图片解码方式将资源图片解码为统一的PixelMap加载使用。<br>2、支持本地图片类型：bmp、jpg、png、svg和webp类型。|

### init(String, Float64, Float64)

```cangjie
public init(src: String, _: Float64, _: Float64)
```

**功能：** 构造一个ImageBitmap类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|图片的数据源支持本地图片。<br>1、string格式用于加载本地图片，例如ImageBitmap("common/images/example.jpg")，type为"entry"和"feature"类型的Module，其图片加载路径的起点为当前Module的ets文件夹，type为"har"和"shared"类型的Module，其图片加载路径的起点为当前构建的"entry"或"feature"类型Module的ets文件夹。type为"har"和"shared"类型的Module中推荐使用ImageSource图片解码方式将资源图片解码为统一的PixelMap加载使用。<br>2、支持本地图片类型：bmp、jpg、png、svg和webp类型。|
|width|Float64|是|-|ImageBitmap的像素宽度。|
|height|Float64|是|-|ImageBitmap的像素高度。|

### init(String, Int64, Int64)

```cangjie
public init(src: String, _: Int64, _: Int64)
```

**功能：** 构造一个ImageBitmap类型的对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|String|是|-|图片的数据源支持本地图片。<br>1、string格式用于加载本地图片，例如ImageBitmap("common/images/example.jpg")，type为"entry"和"feature"类型的Module，其图片加载路径的起点为当前Module的ets文件夹，type为"har"和"shared"类型的Module，其图片加载路径的起点为当前构建的"entry"或"feature"类型Module的ets文件夹。type为"har"和"shared"类型的Module中推荐使用ImageSource图片解码方式将资源图片解码为统一的PixelMap加载使用。<br>2、支持本地图片类型：bmp、jpg、png、svg和webp类型。|
|width|Int64|是|-|ImageBitmap的像素宽度。|
|height|Int64|是|-|ImageBitmap的像素高度。|