### func translate(Float32, Float32)

```cangjie
public func translate(x: Float32, y: Float32): Unit
```

**功能：** 根据输入的坐标对图片进行位置变换。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|区域横坐标。|
|y|Float32|是|-|区域纵坐标。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let pixelMap = imageSourceApi.createPixelMap()
let translateX: Float32 = 50.0
let translateY: Float32 = 10.0
pixelMap.translate(translateX, translateY)
```

### func writeBufferToPixels(Array\<UInt8>)

```cangjie
public func writeBufferToPixels(src: Array<UInt8>): Unit
```

**功能：** 读取缓冲区中的图片数据，结果写入PixelMap中。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|Array\<UInt8>|是|-|图像像素数据。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let pixelMap = imageSourceApi.createPixelMap()
let color: Array<UInt8> = Array<UInt8>(96, {i => UInt8(i)}) //96为需要创建的像素buffer大小，取值为：height * width *4
pixelMap.writeBufferToPixels(color)
```

### func writePixels(PositionArea)

```cangjie
public func writePixels(area: PositionArea): Unit
```

**功能：** 将PixelMap写入指定区域内。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|area|[PositionArea](#struct-positionarea)|是|-|区域，根据区域写入。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let pixelMap = imageSourceApi.createPixelMap()
let area: PositionArea = PositionArea(
    Array<UInt8>(8, {i => UInt8(i)}),
    0,
    8,
    Region(Size(height: 1, width: 2), 0, 0)
)
pixelMap.writePixels(area)
```