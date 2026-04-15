### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放当前图像。

> **说明：**
>
> - 在接收另一个图像前必须先释放对应资源。
>
> - 由于图片占用内存较大，所以当Image实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let size = Size(8, 8192)
    let receiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
    let img = receiver.readNextImage()
    img.release()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```