### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放资源。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Media错误码](./cj-errorcode-multimedia-media.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 5400101 | No memory. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.LocalizationKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.BusinessException

try {
    let timeUs = 0
    let queryOption = AVImageQueryOptions.AvImageQueryNextSync
    let param = PixelMapParams(width: 300, height: 300)
    let generator = createAVImageGenerator()
    let abilityContext = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let rawFd = abilityContext.resourceManager.getRawFd("trailer.mp4")
    generator.fdSrc = AVFileDescriptor(rawFd.fd, offset:rawFd.offset, length:rawFd.length)
    let pic = generator.fetchFrameByTime(timeUs, queryOption, param)
    generator.release()
} catch (e: BusinessException) {
    Hilog.error(0, "AppLogCj", e.message)
}
```