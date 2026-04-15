### func modifyImageProperty(PropertyKey, String)

```cangjie
public func modifyImageProperty(key: PropertyKey, value: String): Unit
```

**功能：** 通过指定的键修改图片属性的值。

该接口仅支持JPEG、PNG、HEIF和WEBP（不同硬件设备支持情况不同）文件，且需要包含Exif信息。

> **说明：**
>
> 调用modifyImageProperty修改属性会改变属性字节长度，使用buffer创建的ImageSource调用modifyImageProperty会导致buffer内容覆盖，目前buffer创建的ImageSource不支持调用此接口，请改用fd或path创建的ImageSource。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[PropertyKey](#enum-propertykey)|是|-|图片属性名。|
|value|String|是|-|属性值。|

**异常：**

- BusinessException：对应错误码如下表，详见[Image错误码](./cj-errorcode-image.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 62980104 | Failed to initialize the internal object. |
  | 62980110 | The image source data is incorrect. |
  | 62980115 | Parameter error.Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
  | 62980123 | The image does not support EXIF decoding. |
  | 62980133 | The EXIF data is out of range. |
  | 62980135 | The EXIF value is invalid. |
  | 62980146 | The EXIF data failed to be written to the file. |

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
    imageSourceApi.modifyImageProperty(PropertyKey.ImageLength, "200")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放ImageSource实例。

> **说明：**
>
> 由于图片占用内存较大，所以当ImageSource实例使用完成后，应主动调用该方法，及时释放内存。释放时应确保后续不再使用该实例。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

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
    let data: Array<UInt8> = Array<UInt8>(112, repeat: 0)
    let sourceOptions: SourceOptions = SourceOptions(120)
    let imageSourceApi: ImageSource = createImageSource(data, sourceOptions)  // 请替换为正确的图片源，参考本文使用说明。
    imageSourceApi.release()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```