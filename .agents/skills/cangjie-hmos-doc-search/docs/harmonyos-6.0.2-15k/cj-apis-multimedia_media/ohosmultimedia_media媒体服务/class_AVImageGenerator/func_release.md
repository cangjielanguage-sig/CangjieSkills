### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放资源。

**系统能力：** SystemCapability.Multimedia.Media.AVImageGenerator

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operation not allowed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.*

try {
    let timeUs = 0
    let queryOption = AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC
    let param = PixelMapParams(300, 300)
    let generator = createAVImageGenerator()
    let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
    let rawFd = abilityContext.resourceManager.getRawFd("demo.mp4")
    generator.fdSrc = AVFileDescriptor(rawFd.fd, rawFd.offset, rawFd.length)
    generator.release()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```