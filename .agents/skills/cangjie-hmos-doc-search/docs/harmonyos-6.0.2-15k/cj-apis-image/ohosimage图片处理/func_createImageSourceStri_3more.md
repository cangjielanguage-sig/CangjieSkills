## func createImageSource(String, SourceOptions)

```cangjie
public func createImageSource(uri: String, options: SourceOptions): ImageSource
```

**功能：** 通过传入的URI创建图片源实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|图片路径，当前仅支持应用沙箱路径。</br>当前支持格式有：.jpg .png .gif .bmp .webp RAW [SVG](#svg标签说明)。|
|options|[SourceOptions](#struct-sourceoptions)|是|-|图片属性，包括图片序号与默认属性值。|

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

let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSource: ImageSource = createImageSource("test.png", sourceOptions)
```

## func createImageSource(Int32)

```cangjie
public func createImageSource(fd: Int32): ImageSource
```

**功能：** 通过传入文件描述符来创建图片源实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|文件描述符fd。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageSource](#class-imagesource)|返回ImageSource类实例。|

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

let imageSourceApi: ImageSource = createImageSource(0)
```

## func createImageSource(Int32, SourceOptions)

```cangjie
public func createImageSource(fd: Int32, options: SourceOptions): ImageSource
```

**功能：** 通过传入文件描述符来创建图片源实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|文件描述符fd。|
|options|[SourceOptions](#struct-sourceoptions)|是|-|图片属性，包括图片序号与默认属性值。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageSource](#class-imagesource)|返回ImageSource类实例。|

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

let sourceOptions: SourceOptions = SourceOptions(sourceDensity: 120)
let imageSource: ImageSource = createImageSource(0, sourceOptions)
```