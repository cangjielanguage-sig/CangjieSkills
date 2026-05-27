## class ImageCreator

```cangjie
public class ImageCreator {}
```

**功能：** 图像创建模块，用于请求图像原生数据区域，并开放给应用编译原生图像数据的能力。 在调用以下方法前需要先创建ImageCreator实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**起始版本：** 12

### prop capacity

```cangjie
public prop capacity: Int32
```

**功能：** 同时访问的图像数。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### prop format

```cangjie
public prop format: Int32
```

**功能：** 图像格式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### func Release()<sup>(deprecated)</sup>

```cangjie
public func Release(): Unit
```

**功能：** 释放当前图像。

> **注意：**
>
> 从API version 19版本开始废弃不再维护，可使用[release](#func-release-1)替代。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let imageCreator = createImageCreator(8192, 8, 4, 8)
imageCreator.Release()
```

### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放当前图像。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

let imageCreator = createImageCreator(8192, 8, 4, 8)
imageCreator.release()
```

### func dequeueImage()

```cangjie
public func dequeueImage(): Image
```

**功能：** 从空闲队列中获取buffer图片，用于绘制UI内容。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[Image](#class-image)|用于返回最新图片。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

var imageCreator = createImageCreator(8192, 8, 4, 8)
var image = imageCreator.dequeueImage()
```

### func queueImage(Image)

```cangjie
public func queueImage(image: Image): Unit
```

**功能：** 将绘制好的图片放入Dirty队列。

**系统能力：** SystemCapability.Multimedia.Image.ImageCreator

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|image|[Image](#class-image)|是|-|绘制好的buffer图像。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

var imageCreator = createImageCreator(8192, 8, 4, 8)
var image = imageCreator.dequeueImage()
imageCreator.queueImage(image)
```