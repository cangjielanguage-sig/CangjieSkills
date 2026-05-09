### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放图片打包实例。

> **说明：**
>
> 由于图片占用内存较大，所以当ImagePacker实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImagePacker

**起始版本：** 22

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let imagePacker = createImagePacker()
    imagePacker.release()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```