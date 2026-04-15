### func updateData(Array\<UInt8>, Bool, UInt32, UInt32)

```cangjie
public func updateData(buf: Array<UInt8>, isFinished: Bool, offset: UInt32, length: UInt32): Unit
```

**功能：** 更新增量数据。

**系统能力：** SystemCapability.Multimedia.Image.ImageSource

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|buf|Array\<UInt8>|是|-|存放增量数据的buffer。|
|isFinished|Bool|是|-|true表示数据更新完成，当前buffer内存放最后一段数据；false表示数据还未更新完成，需要继续更新。|
|offset|UInt32|是|-|即当前buffer中的数据首地址，相对于整个图片文件首地址的偏移量。单位：字节。|
|length|UInt32|是|-|当前buffer的长度。单位：字节。|

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
    let testPng = Array<UInt8>(16500, repeat: 0)
    let bufferSize = 5000
    var offset = 0
    var isFinished = false
    while (offset < testPng.size) {
        var oneStep = testPng.slice(offset, min(bufferSize, testPng.size - offset))
        if (oneStep.size < bufferSize) {
            isFinished = true
        }
        imageSourceApi.updateData(oneStep, isFinished, 0, UInt32(oneStep.size))
        offset = offset + oneStep.size
    }
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```