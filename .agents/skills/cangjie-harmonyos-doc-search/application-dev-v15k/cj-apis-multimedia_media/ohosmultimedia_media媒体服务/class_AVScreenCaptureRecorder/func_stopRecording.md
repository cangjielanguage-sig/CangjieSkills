### func stopRecording()

```cangjie
public func stopRecording(): Unit
```

**功能：** 结束录屏。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400103|IO error.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.CoreFileKit.*

let filePath = "/data/storage/el2/base/haps/entry/files/test.mp4"
let file = FileFs.open(filePath, mode: (READ_WRITE.mode | CREATE.mode))
let config = AVScreenCaptureRecordConfig(file.fd, 640, 480)
let scr = createAVScreenCaptureRecorder()
if (let Some(v) <- scr) {
    v.stopRecording()
}
```