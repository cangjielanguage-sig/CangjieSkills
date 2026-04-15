### func getDelayTimeList()

```cangjie
public func getDelayTimeList(): Array<Int32>
```

**功能：** 获取图像延迟时间数组。此接口仅用于gif图片和webp图片。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Int32>|返回延迟时间数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
  | 62980102 | Failed to malloc memory. |
  | 62980104 | Failed to initialize the internal object. |
  | 62980110 | The image source data is incorrect. |
  | 62980111 | The image source data is incomplete. |
  | 62980115 | Invalid image parameter. |
  | 62980116 | Failed to decode the image. |
  | 62980118 | Failed to create the image plugin. |
  | 62980122 | Failed to decode the image header. |
  | 62980149 | Invalid MIME type for the image source. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
    let sourceOptions: SourceOptions = SourceOptions(120)
    let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)  // 请替换为正确的图片源，参考本文使用说明。
    let list = imageSourceApi.getDelayTimeList()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getFrameCount()

```cangjie
public func getFrameCount(): UInt32
```

**功能：** 获取图像帧数。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回图像帧数。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980096 | The operation failed. Possible cause: 1.Image upload exception. 2. Decoding process exception. 3. Insufficient memory. |
  | 62980104 | Failed to initialize the internal object. |
  | 62980111 | The image source data is incomplete. |
  | 62980112 | The image format does not match. |
  | 62980113 | Unknown image format. The image data provided is not in a recognized or supported format, or it may be occorrupted. |
  | 62980115 | Invalid image parameter. |
  | 62980116 | Failed to decode the image. |
  | 62980118 | Failed to create the image plugin. |
  | 62980122 | Failed to decode the image header. |
  | 62980137 | Invalid media operation. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ImageKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
    let sourceOptions: SourceOptions = SourceOptions(120)
    let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)  // 请替换为正确的图片源，参考本文使用说明。
    let count = imageSourceApi.getFrameCount()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```