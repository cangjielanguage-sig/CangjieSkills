### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放音视频录制资源。

释放音视频录制资源之后，该AVRecorder实例不能再进行任何操作。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400105|Service died.|

**示例：**

完整示例参考[prepare](#func-prepareavrecorderconfig)的示例代码。

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

try {
    let avRecorder = createAVRecorder()
    avRecorder.release()
    AppLog.info("release success")
} catch (e: BusinessException) {
    AppLog.info("release exception: ${e}")
}
```

### func reset()

```cangjie
public func reset(): Unit
```

**功能：** 重置音视频录制。

纯音频录制时，需要重新调用[prepare()](#func-prepare)接口才能重新录制。纯视频录制，音视频录制时，需要重新调用[prepare()](#func-prepare)和[getInputSurface()](#func-getinputsurface)接口才能重新录制。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400103|IO error.|
  |5400105|Service died.|

**示例：**

完整示例参考[prepare](#func-prepareavrecorderconfig)的示例代码。

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

try {
    let avRecorder = createAVRecorder()
    // 执行prepare之后，再执行reset
    avRecorder.reset()
    AppLog.info("reset success")
} catch (e: BusinessException) {
    AppLog.info("reset exception: ${e}")
}
```

### func resume()

```cangjie
public func resume(): Unit
```

**功能：** 恢复视频录制。

需要在[pause()](#func-pause)事件成功触发后，才能调用resume方法。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operate not permit.|
  |5400103|IO error.|
  |5400105|Service died.|

**示例：**

完整示例参考[prepare](#func-prepareavrecorderconfig)的示例代码。

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

try {
    let avRecorder = createAVRecorder()
    // 执行prepare、start、pause之后，再执行resume
    avRecorder.resume()
    AppLog.info("resume success")
} catch (e: BusinessException) {
    AppLog.info("resume exception: ${e}")
}
```

### func start()

```cangjie
public func start(): Unit
```

**功能：** 开始视频录制。

纯音频录制需在[prepare()](#func-prepare)事件成功触发后，才能调用start方法。纯视频录制，音视频录制需在[getInputSurface()](#func-getinputsurface)事件成功触发后，才能调用start方法。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operate not permit.|
  |5400103|IO error.|
  |5400105|Service died.|

**示例：**

完整示例参考[prepare](#func-prepareavrecorderconfig)的示例代码。

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

try {
    let avRecorder = createAVRecorder()
    // 执行prepare之后，再执行start
    avRecorder.start()
    AppLog.info("start success")
} catch (e: BusinessException) {
    AppLog.info("start exception: ${e}")
}
```