## func createEffect(PixelMap)

```cangjie
public func createEffect(source: PixelMap): ?Filter
```

**功能：** 通过传入的PixelMap创建Filter实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|source|[PixelMap](../ImageKit/cj-apis-image.md#class-pixelmap)|是|-|image模块创建的PixelMap实例。可通过图片解码或直接创建获得。|

**返回值：**

|类型|说明|
|:----|:----|
|?[Filter](#class-filter)|返回不带任何效果的Filter链表的头节点，失败时返回None。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkGraphics2D.*
import kit.ImageKit.*

let color = Array<UInt8>(16, repeat: 0)
let opts = InitializationOptions(editable: true, pixelFormat: RGBA_8888, size: Size(height: 2, width: 2), alphaType: PREMUL)
var map: PixelMap = createPixelMap(color, opts)
let imagesource = createImageSource("data/storage/el2/base/haps/entry/files/test.jpg")
map = imagesource.createPixelMap()
let headFilter = createEffect(map)
```

## class Color

```cangjie
public class Color {}
```

**功能：** 颜色类，用于保存取色的结果。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 19

### let alpha

```cangjie
public let alpha: Int32
```

**功能：** 透明通道分量值，取值范围[0x0, 0xFF]。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let blue

```cangjie
public let blue: Int32
```

**功能：** 蓝色分量值，取值范围[0x0, 0xFF]。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let green

```cangjie
public let green: Int32
```

**功能：** 绿色分量值，取值范围[0x0, 0xFF]。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let red

```cangjie
public let red: Int32
```

**功能：** 红色分量值，取值范围[0x0, 0xFF]。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19