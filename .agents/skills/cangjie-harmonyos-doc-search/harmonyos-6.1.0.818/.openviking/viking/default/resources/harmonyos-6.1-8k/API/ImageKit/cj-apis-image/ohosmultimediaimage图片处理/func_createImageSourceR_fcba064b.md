## func createImageSource(RawFileDescriptor, SourceOptions)

```cangjie
public func createImageSource(rawfile: RawFileDescriptor, options!: SourceOptions = SourceOptions(0)): ImageSource
```

**功能：** 通过图像资源文件的RawFileDescriptor创建ImageSource实例。

> **说明：**
>
> 由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用[release](#func-release-3)方法及时释放内存。释放时应确保后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rawfile|[RawFileDescriptor](../LocalizationKit/cj-apis-raw_file_descriptor.md#class-rawfiledescriptor)|是|-|图像资源文件的RawFileDescriptor。|
|options|[SourceOptions](#class-sourceoptions)|否|SourceOptions(0)| **命名参数。** 图片属性，包括图片像素密度、像素格式和图片尺寸。|

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
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException
import ohos.resource_manager.ResourceManager

let resourceManager = Global.abilityContext.resourceManager // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
try {
    let rawfd = resourceManager.getRawFd("test.png")
    createImageSource(rawfd)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "error code: ${e.code}, message: ${e.message}.", "")
}
```