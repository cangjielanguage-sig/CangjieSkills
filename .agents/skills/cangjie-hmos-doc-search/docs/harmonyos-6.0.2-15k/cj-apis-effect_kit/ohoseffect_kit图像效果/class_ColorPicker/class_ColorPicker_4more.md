## class ColorPicker

```cangjie
public class ColorPicker {}
```

**功能：** 取色类，用于从一张图像数据中获取它的主要颜色。在调用ColorPicker的方法前，需要先通过[createColorPicker](#func-createcolorpickerpixelmap-arrayfloat64)创建一个ColorPicker实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### func getAverageColor()

```cangjie
public func getAverageColor(): ?Color
```

**功能：** 读取图像平均的颜色值，结果写入[Color](#class-color)里。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|?[Color](#class-color)|Color实例，即图像平均的颜色值，失败时返回None。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*
import kit.ImageKit.*
import ohos.hilog.Hilog

let colors: Array<UInt8> = Array<UInt8>(96, repeat: 0)
let pixelMap = createPixelMap(colors,
    InitializationOptions(editable: true, pixelFormat: RGBA_8888, size: Size(height: 4, width: 6)))
let imageSource = createImageSource("test.jpg")
let originMap  = imageSource.createPixelMap()

let picker = createColorPicker(originMap, region: Some([0.0,0.0,0.1,0.1]))
if (let Some(p) <- picker) {
    let color = p.getAverageColor()
    if (let Some(v) <- color) {
        Hilog.info(0,"test","color alpha ${v.alpha} red is ${v.red}, green ${v.green}, blue ${v.blue}, ")
    }
}
```

### func getHighestSaturationColor()

```cangjie
public func getHighestSaturationColor(): ?Color
```

**功能：** 读取图像饱和度最高的颜色值，结果写入[Color](#class-color)里。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|?[Color](#class-color)|Color实例，即图像饱和度最高的颜色值，失败时返回None。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*
import kit.ImageKit.*
import ohos.hilog.Hilog

let colors: Array<UInt8> = Array<UInt8>(96, repeat: 0)
let pixelMap = createPixelMap(colors,
    InitializationOptions(editable: true, pixelFormat: RGBA_8888, size: Size(height: 4, width: 6)))
let imageSource = createImageSource("test.jpg")
let originMap  = imageSource.createPixelMap()

let picker = createColorPicker(originMap, region: Some([0.0,0.0,0.1,0.1]))
if (let Some(p) <- picker) {
    let color = p.getHighestSaturationColor()
    if (let Some(v) <- color) {
        Hilog.info(0,"test","color alpha ${v.alpha} red is ${v.red}, green ${v.green}, blue ${v.blue}, ")
    }
}
```

### func getLargestProportionColor()

```cangjie
public func getLargestProportionColor(): ?Color
```

**功能：** 读取图像占比最多的颜色值，结果写入[Color](#class-color)里。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|?[Color](#class-color)|Color实例，即图像饱和度最高的颜色值，失败时返回None。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*
import kit.ImageKit.*
import ohos.hilog.Hilog

let colors: Array<UInt8> = Array<UInt8>(96, repeat: 0)
let pixelMap = createPixelMap(colors,
    InitializationOptions(editable: true, pixelFormat: RGBA_8888, size: Size(height: 4, width: 6)))
let imageSource = createImageSource("test.jpg")
let originMap  = imageSource.createPixelMap()

let picker = createColorPicker(originMap, region: Some([0.0,0.0,0.1,0.1]))
if (let Some(p) <- picker) {
    let color = p.getLargestProportionColor()
    if (let Some(v) <- color) {
        Hilog.info(0,"test","color alpha ${v.alpha} red is ${v.red}, green ${v.green}, blue ${v.blue}, ")
    }
}
```