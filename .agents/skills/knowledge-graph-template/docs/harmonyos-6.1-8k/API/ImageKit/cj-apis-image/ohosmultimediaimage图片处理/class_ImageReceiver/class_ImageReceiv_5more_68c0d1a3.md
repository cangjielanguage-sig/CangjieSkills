## class ImageReceiver

```cangjie
public class ImageReceiver {}
```

**功能：** 图像接收类，用于获取组件surface id，接收最新的图片和读取下一张图片，以及释放ImageReceiver实例。

> **说明：**
>
> - ImageReceiver作为图片的接收方、消费者，它的参数属性实际上不会对接收到的图片产生影响。图片属性的配置应在发送方、生产者进行，如相机预览流[createPreviewOutput](../CameraKit/cj-apis-multimedia-camera.md#func-createpreviewoutputprofile-string)。
>
> - 在调用以下方法前需要先通过[createImageReceiver](#func-createimagereceiversize-imageformat-int32)创建ImageReceiver实例。
>
> - 由于图片占用内存较大，所以当ImageReceiver实例使用完成后，应主动调用[release](#func-release-2)方法及时释放内存。释放时应确保后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

### prop capacity

```cangjie
public prop capacity: Int32
```

**功能：** 同时访问的图像数。该参数仅作为期望值，实际capacity由设备硬件决定。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |

### prop format

```cangjie
public prop format: ImageFormat
```

**功能：** 图像格式，取值为[ImageFormat](#enum-imageformat)常量（目前仅支持 ImageFormat:Jpeg，实际返回格式由生产者决定，如相机）。

**类型：** [ImageFormat](#enum-imageformat)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |

### prop size

```cangjie
public prop size: Size
```

**功能：** 图片大小。该参数不会影响接收到的图片大小，实际返回大小由生产者决定，如相机。

**类型：** [Size](#class-size)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |

### func getReceivingSurfaceId()

```cangjie
public func getReceivingSurfaceId(): String
```

**功能：** 用于获取一个surface id供Camera或其他组件使用。

**系统能力：** SystemCapability.Multimedia.Image.ImageReceiver

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|返回surface id。|

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
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let size = Size(8, 8192)
    var receiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
    let id: String = receiver.getReceivingSurfaceId()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```