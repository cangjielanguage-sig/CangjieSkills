## func createImageCreator(Size, Int32, Int32)

```cangjie
public func createImageCreator(size: Size, format: Int32, capacity: Int32): ImageCreator
```

**功能：** 创建ImageCreator实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|size|[Size](#struct-size)|是|-|图像的默认大小。|
|format|Int32|是|-|图像格式，如YCBCR_422_SP，JPEG。|
|capacity|Int32|是|-|同时访问的最大图像数。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageCreator](#class-imagecreator)|返回ImageCreator实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let size = Size(height: 8192, width: 8)
let imageCreator = createImageCreator(size, 4, 8)
```

## func createImagePacker()

```cangjie
public func createImagePacker(): ImagePacker
```

**功能：** 创建ImagePacker实例。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[ImagePacker](#class-imagepacker)|返回ImagePacker实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let imagePacker: ImagePacker = createImagePacker()
```

## func createImageReceiver(Int32, Int32, ImageFormat, Int32)

```cangjie
public func createImageReceiver(width: Int32, height: Int32, format: ImageFormat, capacity: Int32): ImageReceiver
```

**功能：** 通过宽、高、图片格式、容量创建ImageReceiver实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Int32|是|-|图像的默认宽度。|
|height|Int32|是|-|图像的默认高度。|
|format|[ImageFormat](#enum-imageformat)|是|-|图像格式，取值为[ImageFormat](#enum-imageformat)常量（目前仅支持ImageFormat:JPEG）。|
|capacity|Int32|是|-|同时访问的最大图像数。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageReceiver](#class-imagereceiver)|如果操作成功，则返回ImageReceiver实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let receiver: ImageReceiver = createImageReceiver(8192, 8, ImageFormat.JPEG, 8)
```

## func createImageSource(String)

```cangjie
public func createImageSource(uri: String): ImageSource
```

**功能：** 通过传入的URI创建图片源实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|图片路径，当前仅支持应用沙箱路径。</br>当前支持格式有：.jpg .png .gif .bmp .webp RAW [SVG](#svg标签说明)。 |

**返回值：**

|类型|说明|
|:----|:----|
|[ImageSource](#class-imagesource)|返回ImageSource类实例|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Image错误码](../../errorcodes/cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :------- | :--------------------------------------------|
  | 62980104 | Image initialization abnormal.      |
  | 62980115 | Invalid image parameter.            |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let path: String = "../test.jpg"
let imageSourceApi: ImageSource = createImageSource(path)
```