# ohos.effect_kit（图像效果）

图像效果提供处理图像的一些基础能力，包括对当前图像的亮度调节、模糊化、灰度调节、智能取色等。

## 导入模块

```cangjie
import kit.ArkGraphics2D.*
```

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func createColorPicker(PixelMap, ?Array\<Float64>)

```cangjie
public func createColorPicker(source: PixelMap, region!: ?Array<Float64> = None): ?ColorPicker
```

**功能：** 通过传入的PixelMap创建ColorPicker实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|image模块创建的PixelMap实例。可通过图片解码或直接创建获得。|
|region|?Array\<Float64>|否|None| **命名参数。** 指定图片的取色区域。默认为None。数组元素个数为4，取值范围为[0.0, 1.0]，数组元素分别表示图片区域的左、上、右、下位置，图片最左侧和最上侧对应位置0.0，最右侧和最下侧对应位置1.0。数组第三个元素需大于第一个元素，第四个元素需大于第二个元素。|

**返回值：**

|类型|说明|
|:----|:----|
|?[ColorPicker](#class-colorpicker)|返回创建的ColorPicker实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

**示例1：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*
import kit.ImageKit.*

let color = Array<UInt8>(16, repeat: 0)
let opts = InitializationOptions(editable: true, pixelFormat: RGBA_8888,
    size: Size(height: 2, width: 2), alphaType: PREMUL)
var map: PixelMap = createPixelMap(color, opts)
let imagesource = createImageSource("data/storage/el2/base/haps/entry/files/test.jpg")
map = imagesource.createPixelMap()
let colorPicker = createColorPicker(map)
```

**示例2：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*
import kit.ImageKit.*

let color = Array<UInt8>(16, repeat: 0)
let opts = InitializationOptions(editable: true, pixelFormat: RGBA_8888,
    size: Size(height: 2, width: 2), alphaType: PREMUL)
var map: PixelMap = createPixelMap(color, opts)
let imagesource = createImageSource("data/storage/el2/base/haps/entry/files/test.jpg")
map = imagesource.createPixelMap()
let colorPicker = createColorPicker(map, region: Some([0.0, 0.0, 0.1, 0.1]))
```