## class PixelMap

```cangjie
public class PixelMap {}
```

**功能：** 图像像素类，用于读取或写入图像数据以及获取图像信息。在调用PixelMap的方法前，需要先通过[createPixelMap](#func-createpixelmaparrayuint8-initializationoptions)创建一个PixelMap实例。目前pixelmap序列化大小最大128MB，超过会送显失败。大小计算方式为(宽\*高\*每像素占用字节数)。

在调用PixelMap的方法前，需要先通过[createPixelMap](#func-createpixelmaparrayuint8-initializationoptions)构建一个PixelMap对象。

图片使用的内存往往较大，在PixelMap对象使用完成后，应主动调用[release](#func-release-4)方法及时释放内存。释放时应确保后续不再使用该对象。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

### prop isEditable

```cangjie
public prop isEditable: Bool
```

**功能：**  图像像素是否可被编辑。true表示可被编辑，false表示不可被编辑。为false时，图像的渲染和传输性能更好。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |

### prop isStrideAlignment

```cangjie
public prop isStrideAlignment: Bool
```

**功能：** 图像的行数据是否已进行内存对齐。true表示已进行内存对齐，每行数据的末尾可能有空白字节填充以满足对齐要求；false表示未进行内存对齐，每行数据紧密排列，末尾无空白字节填充。

**类型：** Bool

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |

### func applyColorSpace(ColorSpaceManager)

```cangjie
public func applyColorSpace(targetColorSpace: ColorSpaceManager): Unit
```

**功能：** 根据输入的目标色彩空间对图像像素颜色进行色彩空间转换。

**系统能力：** SystemCapability.Multimedia.Image.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|targetColorSpace|[ColorSpaceManager](../ArkGraphics2D/cj-apis-color_manager.md#class-colorspacemanager)|是|-|目标色彩空间，支持Srgb、DciP3、DisplayP3、AdobeRgb1998。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |
  | 62980108 | Failed to convert the color space. |
  | 62980115 | Invalid image parameter. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import kit.ArkGraphics2D.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
    let sourceOptions: SourceOptions = SourceOptions(120)
    let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)  // 请替换为正确的图片源，参考本文使用说明。
    let pixelMap = imageSourceApi.createPixelMap()
    let colorSpaceManager = create(Srgb)
    pixelMap.applyColorSpace(colorSpaceManager)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```