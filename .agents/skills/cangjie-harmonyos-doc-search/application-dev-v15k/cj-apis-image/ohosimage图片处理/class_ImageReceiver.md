## class ImageReceiver

```cangjie
public class ImageReceiver {}
```

**功能：** 图像接收类，用于获取组件surface id，接收最新的图片和读取下一张图片，以及释放ImageReceiver实例。

在调用以下方法前需要先创建ImageReceiver实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

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
public prop format: ImageFormat
```

**功能：** 图像格式。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** [ImageFormat](#enum-imageformat)

**读写能力：** 只读

**起始版本：** 12

### prop size

```cangjie
public prop size: Size
```

**功能：** 图片大小。

**系统能力：** SystemCapability.Multimedia.Image.Core

**类型：** [Size](#struct-size)

**读写能力：** 只读

**起始版本：** 12

### func Release()<sup>(deprecated)</sup>

```cangjie
public func Release(): Unit
```

**功能：** 释放当前图像接收类。

> **注意：**
>
> 从API version 19版本开始废弃不再维护，可使用[release](#func-release-3)替代。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

var receiver = createImageReceiver(8192, 8, ImageFormat.JPEG, 8)
receiver.Release()
```

### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放当前图像接收类。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

var receiver = createImageReceiver(8192, 8, ImageFormat.JPEG, 8)
receiver.release()
```

### func getReceivingSurfaceId()

```cangjie
public func getReceivingSurfaceId(): String
```

**功能：** 用于获取一个surface id供Camera或其他组件使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回surface id。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*

var receiver = createImageReceiver(8192, 8, ImageFormat.JPEG, 8)
let id: String = receiver.getReceivingSurfaceId()
```