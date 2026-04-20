### func scale(Float32, Float32)

```cangjie
public func scale(x: Float32, y: Float32): Unit
```

**功能：** 根据输入的宽高对图片进行缩放。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|宽度的缩放倍数。|
|y|Float32|是|-|高度的缩放倍数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed|
  |501|Resource Unavailable|

### func scale(Float32, Float32, AntiAliasingLevel)

```cangjie
public func scale(x: Float32, y: Float32, level: AntiAliasingLevel): Unit
```

**功能：** 根据输入的宽高对图片进行缩放。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|x|Float32|是|-|宽度的缩放倍数。|
|y|Float32|是|-|高度的缩放倍数。|
|level|[AntiAliasingLevel](#enum-antialiasinglevel)|是|-|采用的缩放算法。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed|
  |501|Resource Unavailable|

### func setColorSpace(ColorSpaceManager)

```cangjie
public func setColorSpace(colorSpace: ColorSpaceManager): Unit
```

**功能：** 设置图像广色域信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorSpace|[ColorSpaceManager](../ArkGraphics2D/cj-apis-color_manager.md#class-colorspacemanager)|是|-|图像广色域信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980111|If the operation invalid.|
  |62980115|If the image parameter invalid.|

### func toSdr()

```cangjie
public func toSdr(): Unit
```

**功能：** 将HDR的图像内容转换为SDR的图像内容。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |62980137|Invalid image operation.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let imagesource = createImageSource("xxx.jpg")
let pixelMap = imagesource.createPixelMap(
    options: DecodingOptions(desiredDynamicRange: DecodingDynamicRange.AUTO))
pixelMap.toSdr()
```