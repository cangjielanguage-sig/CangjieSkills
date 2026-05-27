### func grayscale()

```cangjie
public func grayscale(): Filter
```

**功能：** 将灰度效果添加到效果链表中，结果返回效果链表的头节点。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

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
    let map = v.grayscale().getEffectPixelMap()
}
```

### func invert()

```cangjie
public func invert(): Filter
```

**功能：** 将反转效果添加到效果链表中，结果返回效果链表的头节点。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

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
    let map = v.invert()
}
```

### func setColorMatrix(Array\<Float32>)

```cangjie
public func setColorMatrix(colorMatrix: Array<Float32>): Filter
```

**功能：** 将自定义效果添加到效果链表中，结果返回效果链表的头节点。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorMatrix|Array\<Float32>|是|-|自定义颜色矩阵。 <br>用于创建效果滤镜的 5x4 大小的矩阵, 矩阵元素取值范围为[0.0, 1.0], 0.0和1.0代表的是矩阵中对应位置的颜色通道的权重，0.0代表该颜色通道不参与计算，1.0代表该颜色通道参与计算并保持原始权重。|

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
let colorMatrix:Array<Float32> = [
        0.2126,0.7152,0.0722,0.0,0.0,
        0.2126,0.7152,0.0722,0.0,0.0,
        0.2126,0.7152,0.0722,0.0,0.0,
        0.0,0.0,0.0,1.0,0.0
        ];
if (let Some(v) <- filter) {
    let map1 = v.setColorMatrix(colorMatrix).getEffectPixelMap()
}
```