### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放ImageReceiver实例。

> **说明：**
>
> 由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

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
    var receiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
    receiver.release()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readLatestImage()

```cangjie
public func readLatestImage(): Image
```

**功能：** 从ImageReceiver读取最新的图片。

> **注意：** 
> 
> - 此接口需要在[on](#func-onreceivetype-callback0argument)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](#class-image)对象使用完毕后需要调用[release](#func-release-1)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Image](#class-image)|返回最新图片。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    let size = Size(8, 8192)
    let receiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
    let image = receiver.readLatestImage()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func readNextImage()

```cangjie
public func readNextImage(): Image
```

**功能：** 从ImageReceiver读取下一张图片。

> **注意：** 
> 
> - 此接口需要在[on](#func-onreceivetype-callback0argument)回调触发后调用，才能正常的接收到数据。且此接口返回的[Image](#class-image)对象使用完毕后需要调用[release](#func-release-1)方法释放，释放后才可以继续接收新的数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Image](#class-image)|返回下一张图片。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    let size = Size(8, 8192)
    let receiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
    let image = receiver.readNextImage()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```