## class Image

```cangjie
public class Image {}
```

**功能：** Image类，用于获取图像内容。

> **说明：**
>
> - 调用[readNextImage](#func-readnextimage)和[readLatestImage](#func-readlatestimage)接口时会返回Image实例。
>
> - Image的属性仅支持在创建时初始化，后续无法再修改，且它的属性不对图像内容产生实际影响，请以图片生产者写入的属性为准，即以向[ImageReceiver](#class-imagereceiver)发送图片数据的发送方实际写入的内容为准。
>
> - 由于图片占用内存较大，所以当Image实例使用完成后，应主动调用[release](#func-release)方法及时释放内存。释放时应确保后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### prop clipRect

```cangjie
public prop clipRect: Region
```

**功能：** 要裁剪的图像区域。

**类型：** [Region](#class-region)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |

### prop format

```cangjie
public prop format: Int32
```

**功能：** 图像格式，参考[PixelMapFormat](#enum-pixelmapformat)。

**类型：** Int32

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.Core

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

**功能：** 图像大小。如果image对象所存储的是相机预览流数据，即YUV图像数据，那么获取到的size中的宽高分别对应YUV图像的宽高； 如果image对象所存储的是相机拍照流数据，即JPEG图像，由于已经是编码后的文件，size中的宽等于JPEG文件大小，高等于1。image对象所存储的数据是预览流还是拍照流，取决于应用将receiver中的surfaceId传给相机的previewOutput还是captureOutput。

**类型：** [Size](#class-size)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |

### func getComponent(ComponentType)

```cangjie
public func getComponent(componentType: ComponentType): Component
```

**功能：** 根据图像的组件类型从图像中获取组件缓存。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|componentType|[ComponentType](#enum-componenttype)|是|-|图像的组件类型。（目前仅支持 ComponentType:Jpeg，实际返回格式由生产者决定，如相机）。|

**返回值：**

|类型|说明|
|:----|:----|
|[Component](#class-component)|返回组件缓冲区。|

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
    let receiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
    let img = receiver.readNextImage()
    let component : Component = img.getComponent(ComponentType.Jpeg)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```