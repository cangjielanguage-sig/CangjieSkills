### func getMainColor()

```cangjie
public func getMainColor(): ?Color
```

**功能：** 读取图像主色的颜色值，结果写入[Color](#class-color)里。

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
    let color = p.getMainColor()
    if (let Some(v) <- color) {
        Hilog.info(0,"test","color alpha ${v.alpha} red is ${v.red}, green ${v.green}, blue ${v.blue}, ")
    }
}
```

### func getTopProportionColors(Float64)

```cangjie
public func getTopProportionColors(colorCount: Float64): Array<?Color>
```

**功能：** 读取图像占比靠前的颜色值，个数由colorCount指定，结果写入[Color](#class-color)的数组里。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|colorCount|Float64|是|-|需要取主色的个数，取值范围为[1.0, 10.0]，向下取整。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<?[Color](#class-color)>|?Color数组，即图像占比前colorCount的颜色值数组，按占比排序。当实际读取的特征色个数小于colorCount时，数组大小为实际特征色个数。取色失败或取色个数小于1返回[None]。取色个数大于10视为取前10个。|

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

let picker = createColorPicker(originMap)
if (let Some(p) <- picker) {
    let colors = p.getTopProportionColors(13.1)
}
```

### func isBlackOrWhiteOrGrayColor(UInt32)

```cangjie
public func isBlackOrWhiteOrGrayColor(color: UInt32): Bool
```

**功能：** 判断颜色color是否为黑白灰颜色，返回true或false。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|color|UInt32|是|-|需要判断是否黑白灰色的颜色值，取值范围[0x0, 0xFFFFFFFF]。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果此颜色为黑白灰颜色，则返回true；否则返回false。|

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
    let ret = p.isBlackOrWhiteOrGrayColor(0xFFFFFFF)
    Hilog.info(0,"test","isBlackOrWhiteOrGrayColor ${ret}")
}
```