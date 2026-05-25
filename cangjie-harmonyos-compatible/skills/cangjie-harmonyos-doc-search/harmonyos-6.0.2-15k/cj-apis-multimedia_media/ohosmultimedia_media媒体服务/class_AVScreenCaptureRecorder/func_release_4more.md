### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放录屏。

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
    v.release()
}
```

### func setMicEnabled(Bool)

```cangjie
public func setMicEnabled(enable: Bool): Unit
```

**功能：** 设置麦克风开关。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|enable|Bool|是|-|麦克风开关控制，true代表麦克风打开，false代表麦克风关闭。|

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
    v.setMicEnabled(true)
}
```

### func skipPrivacyMode(Array\<UInt64>)

```cangjie
public func skipPrivacyMode(windowIDsVec: Array<UInt64>): Unit
```

**功能：** 录屏时，应用可对本应用的隐私窗口做安全豁免。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|windowIDsVec|Array\<UInt64>|是|-|需要豁免隐私的窗口列表，包括主窗口id和子窗口id，窗口属性获取方法可以参考窗口API引用。|

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
    v.skipPrivacyMode([0])
}
```

### func startRecording()

```cangjie
public func startRecording(): Unit
```

**功能：** 开始录屏。

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
    v.startRecording()
}
```