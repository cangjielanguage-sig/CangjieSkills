## class PixelMap

```cangjie
public class PixelMap {}
```

**功能：** 图像像素类，用于读取或写入图像数据以及获取图像信息。在调用PixelMap的方法前，需要先通过[createPixelMap](#func-createpixelmaparrayuint8-initializationoptions)创建一个PixelMap实例。目前pixelmap序列化大小最大128MB，超过会送显失败。大小计算方式为(宽\*高\*每像素占用字节数)。

PixelMap支持通过worker跨线程调用。当PixelMap通过Worker跨线程后，原线程的PixelMap的所有接口均不能调用，否则将报错501服务器不具备完成请求的功能。

在调用PixelMap的方法前，需要先通过[createPixelMap](#func-createpixelmaparrayuint8-initializationoptions)构建一个PixelMap对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### prop isEditable

```cangjie
public prop isEditable: Bool
```

**功能：** 设定图像像素是否可被编辑。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### prop isStrideAlignment

```cangjie
public prop isStrideAlignment: Bool
```

**功能：** 设定图像内存是否为DMA内存。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Bool

**读写能力：** 只读

**起始版本：** 12

### func Release()<sup>(deprecated)</sup>

```cangjie
public func Release(): Unit
```

**功能：** 释放PixelMap对象。

> **注意：**
>
> 从API version 19版本开始废弃不再维护，可使用[release](#func-release-5)替代。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let pixelMap = imageSourceApi.createPixelMap()
pixelMap.Release()
```

### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放PixelMap对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)
let pixelMap = imageSourceApi.createPixelMap()
pixelMap.release()
```

### func applyColorSpace(ColorSpaceManager)

```cangjie
public func applyColorSpace(colorSpace: ColorSpaceManager): Unit
```

**功能：** 根据输入的目标色彩空间对图像像素颜色进行色彩空间转换。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorSpace|[ColorSpaceManager](../ArkGraphics2D/cj-apis-color_manager.md#class-colorspacemanager)|是|-|目标色彩空间，支持SRGB、DCI_P3、DISPLAY_P3、ADOBE_RGB_1998。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|The parameter check failed.|
  |62980104|Failed to initialize the internal object.|
  |62980108|Failed to convert the color space.|
  |62980115|Invalid image parameter.|