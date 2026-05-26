# ohos.image（图片处理）

本模块提供图片处理效果，包括通过属性创建PixelMap、读取图像像素数据、读取区域内的图片数据等。

## 导入模块

```cangjie
import kit.ImageKit.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func CreateIncrementalSource(Array\<UInt8>, SourceOptions)

```cangjie
public func CreateIncrementalSource(buf: Array<UInt8>, options!: SourceOptions = SourceOptions()): ImageSource
```

**功能：** 通过缓冲区以增量的方式创建图片源实例，IncrementalSource不支持读写Exif信息。

以增量方式创建的图片源实例ImageSource，仅支持使用以下功能。

- 获取图片信息：指定序号-[getImageInfo](#func-getimageinfouint32)、直接获取-[getImageInfo](#func-getimageinfo)
- 获取图片中给定索引处图像的指定属性键的值：[getImageProperty](#func-getimagepropertypropertykey-imagepropertyoptions)
- 批量获取图片中的指定属性键的值：[getImageProperties](#func-getimagepropertiesarraypropertykey)
- 更新增量数据：[updateData](#func-updatedataarrayuint8-bool-uint32-uint32)
- 创建PixelMap对象：通过图片解码参数创建-[createPixelMap](#func-createpixelmapdecodingoptions)
- 释放图片源实例：[release](#func-release-1)

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buf|Array\<UInt8>|是|-|增量数据， 这个参数实际不生效。|
|options|[SourceOptions](#struct-sourceoptions)|否|SourceOptions()| **命名参数。** 图片属性，包括图片序号与默认属性值。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageSource](#class-imagesource)|返回图片源。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let buf = Array<UInt8>(1, repeat: 0)
let imageSource = CreateIncrementalSource(buf)
```

## func createImageCreator(Int32, Int32, Int32, Int32)

```cangjie
public func createImageCreator(width: Int32, height: Int32, format: Int32, capacity: Int32): ImageCreator
```

**功能：** 创建ImageCreator实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Int32|是|-|图像的默认宽度。|
|height|Int32|是|-|图像的默认高度。|
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

var imageCreator = createImageCreator(8192, 8, 4, 8)
```