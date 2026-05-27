### func stop()

```cangjie
public func stop(): Unit
```

**功能：** 停止视频录制。

需要在[start()](#func-start)或[pause()](#func-pause)事件成功触发后，才能调用stop方法。

纯音频录制时，需要重新调用[prepare()](#func-prepare)接口才能重新录制。纯视频录制，音视频录制时，需要重新调用[prepare()](#func-prepare)和[getInputSurface()](#func-getinputsurface)接口才能重新录制。

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
    // 执行start或pause成功之后，再执行stop
    avRecorder.stop()
    AppLog.info("stop success")
} catch (e: BusinessException) {
    AppLog.info("stop exception: ${e}")
}
```

### func updateRotation(Int32)

```cangjie
public func updateRotation(rotation: Int32): Unit
```

**功能：** 更新视频旋转角度。

当且仅当[prepare()](#func-prepare)事件成功触发后，且在[start()](#func-start)之前，才能调用updateRotation方法。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rotation|Int32|是|-|旋转角度，取值仅支持0、90、180、270度。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|
  |5400102|Operation not allowed.|
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
    // 执行prepare之后、start之前，执行updateRotation
    avRecorder.updateRotation(90)
    AppLog.info("updateRotation success")
} catch (e: BusinessException) {
    AppLog.info("updateRotation exception: ${e}")
}
```