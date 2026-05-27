## class Image

```cangjie
public class Image {}
```

**功能：** 提供基本的图像操作，包括获取图像信息、读写图像数据。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

### prop clipRect

```cangjie
public prop clipRect: Region
```

**功能：** 要裁剪的图像区域。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** [Region](#struct-region)

**读写能力：** 只读

**起始版本：** 12

### prop format

```cangjie
public prop format: Int32
```

**功能：** 图像格式，参考[PixelMapFormat](#enum-pixelmapformat)。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### prop size

```cangjie
public prop size: Size
```

**功能：** 图像大小。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** [Size](#struct-size)

**读写能力：** 只读

**起始版本：** 12

### prop timestamp

```cangjie
public prop timestamp: Int64
```

**功能：** 图像时间戳。时间戳以纳秒为单位，通常是单调递增的。时间戳的具体含义和基准取决于图像的生产者，在相机预览/拍照场景，生产者就是相机。来自不同生产者的图像的时间戳可能有不同的含义和基准，因此可能无法进行比较。如果要获取某张照片的生成时间，可以通过[getImageProperty](#func-getimagepropertypropertykey-imagepropertyoptions)接口读取相关的EXIF信息。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Int64

**读写能力：** 只读

**起始版本：** 19

### func Release()<sup>(deprecated)</sup>

```cangjie
public func Release(): Unit
```

**功能：** 释放当前图像。

> **注意：**
>
> 从API version 19版本开始废弃不再维护，可使用[release](#func-release)替代。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let imageCreator = createImageCreator(8192, 8, 4, 8)
let img = imageCreator.dequeueImage()
img.Release()
```

### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放当前图像。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let imageCreator = createImageCreator(8192, 8, 4, 8)
let img = imageCreator.dequeueImage()
img.release()
```

### func getComponent(ComponentType)

```cangjie
public func getComponent(componentType: ComponentType): Component
```

**功能：** 根据图像的组件类型从图像中获取组件缓存返回结果。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|componentType|[ComponentType](#enum-componenttype)|是|-|图像的组件类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[Component](#struct-component)|返回组件缓冲区。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let imageCreator = createImageCreator(8192, 8, 4, 8)
let img = imageCreator.dequeueImage()
let component: Component = img.getComponent(ComponentType.JPEG)
```