## func createImageSource(String)

```cangjie
public func createImageSource(uri: String): ImageSource
```

**功能：** 通过传入的uri创建ImageSource实例。

> **说明：**
>
> 由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](#func-release-3)方法及时释放内存。释放时应确保后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|图片路径，当前仅支持应用沙箱路径。</br>当前支持格式有：.jpg .png .gif .bmp .webp .dng .heic（不同硬件设备支持情况不同） [.svg](#svg标签说明) .ico。 |

**返回值：**

|类型|说明|
|:----|:----|
|[ImageSource](#class-imagesource)|返回ImageSource类实例。|

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
    let path: String = "../test.jpg"
    let imageSourceApi: ImageSource = createImageSource(path)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func createImageSource(String, SourceOptions)

```cangjie
public func createImageSource(uri: String, options: SourceOptions): ImageSource
```

**功能：** 通过传入的uri创建ImageSource实例。

> **说明：**
>
> 由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](#func-release-3)方法及时释放内存。释放时应确保后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|uri|String|是|-|图片路径，当前仅支持应用沙箱路径。</br>当前支持格式有：.jpg .png .gif .bmp .webp .dng .heic（不同硬件设备支持情况不同） [.svg](#svg标签说明) .ico。|
|options|[SourceOptions](#class-sourceoptions)|是|-|图片属性，包括图片像素密度、像素格式和图片尺寸。|

**返回值：**

|类型|说明|
|:----|:----|
|[ImageSource](#class-imagesource)|返回ImageSource类实例。|

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
    let sourceOptions: SourceOptions = SourceOptions(120)
    let imageSource: ImageSource = createImageSource("test.png", sourceOptions)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```