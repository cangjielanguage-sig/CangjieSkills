## class Filter

```cangjie
public class Filter <: RemoteDataLite {}
```

**功能：** 图像效果类，用于将指定的效果添加到输入图像中。在调用Filter的方法前，需要先通过[createEffect](#func-createeffectpixelmap)创建一个Filter实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### func blur(Float32)

```cangjie
public func blur(radius: Float32): Filter
```

**功能：** 将模糊效果添加到效果链表中，结果返回效果链表的头节点。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|radius|Float32|是|-|模糊半径，单位是像素。模糊效果与所设置的值成正比，值越大效果越明显。|

**返回值：**

|类型|说明|
|:----|:----|
|[Filter](#class-filter)|返回已添加的图像效果。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*
import kit.ImageKit.*

let colors: Array<UInt8> = Array<UInt8>(96, repeat: 0)
let pixelMap = createPixelMap(colors,
    InitializationOptions(editable: true, pixelFormat: RGBA_8888, size: Size(height: 4, width: 6)))
let imageSource = createImageSource("test.jpg")
let originMap  = imageSource.createPixelMap()

let filter = createEffect(originMap)
if (let Some(v) <- filter) {
    let map = v.blur(Float32(5.0))
}
```

### func brightness(Float32)

```cangjie
public func brightness(bright: Float32): Filter
```

**功能：** 将高亮效果添加到效果链表中，结果返回效果链表的头节点。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bright|Float32|是|-|高亮程度，取值范围在0.0-1.0之间，取值为0.0时图像保持不变。不在范围内则抛出异常。|

**返回值：**

|类型|说明|
|:----|:----|
|[Filter](#class-filter)|返回已添加的图像效果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*
import kit.ImageKit.*

let colors: Array<UInt8> = Array<UInt8>(96, repeat: 0)
let pixelMap = createPixelMap(colors,
    InitializationOptions(editable: true, pixelFormat: RGBA_8888, size: Size(height: 4, width: 6)))
let imageSource = createImageSource("test.jpg")
let originMap  = imageSource.createPixelMap()

let filter = createEffect(originMap)
if (let Some(v) <- filter) {
    let map = v.brightness(0.5)
}
```

### func getEffectPixelMap()

```cangjie
public func getEffectPixelMap(): PixelMap
```

**功能：** 获取已添加链表效果的源图像的PixelMap。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|返回已添加链表效果的源图像的PixelMap。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*
import kit.ImageKit.*

let colors: Array<UInt8> = Array<UInt8>(96, repeat: 0)
let pixelMap = createPixelMap(colors,
    InitializationOptions(editable: true, pixelFormat: RGBA_8888, size: Size(height: 4, width: 6)))
let imageSource = createImageSource("test.jpg")
let originMap  = imageSource.createPixelMap()

let filter = createEffect(originMap)
if (let Some(v) <- filter) {
    let map = v.getEffectPixelMap()
}
```