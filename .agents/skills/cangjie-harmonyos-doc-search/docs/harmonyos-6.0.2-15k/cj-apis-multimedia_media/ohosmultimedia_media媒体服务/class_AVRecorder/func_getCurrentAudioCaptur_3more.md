### func getCurrentAudioCapturerInfo()

```cangjie
public func getCurrentAudioCapturerInfo(): audio.AudioCapturerChangeInfo
```

**功能：** 获取当前音频采集参数。

在[prepare()](#func-prepare)成功触发后，才能调用此方法。在[stop()](#func-stop)成功触发后，调用此方法会报错。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[audio](../AudioKit/cj-apis-multimedia-audio.md).[AudioCapturerChangeInfo](../AudioKit/cj-apis-multimedia-audio.md#class-audiocapturerchangeinfo)|音频采集参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operation not allowed.|
  |5400103|I/O error.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*

let avRecorder = createAVRecorder()
avRecorder.getCurrentAudioCapturerInfo()
```

### func getInputSurface()

```cangjie
public func getInputSurface(): String
```

**功能：** 获得录制需要的surface。此surface提供给调用者，调用者从此surface中获取surfaceBuffer，填入相应的视频数据。

应当注意，填入的视频数据需要携带时间戳（单位ns）和buffersize。时间戳的起始时间请以系统启动时间为基准。

需在[prepare()](#func-prepare)事件成功触发后，才能调用getInputSurface方法。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|获取的surface的Id。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operate not permit.|
  |5400103|IO error.|
  |5400105|Service died.|

**示例：**

完整示例参考[prepare](#func-prepareavrecorderconfig)的示例代码。

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.*

try {
    let avRecorder = createAVRecorder()
    // 需在prepare执行成功之后，调用此接口
    let surfaceId = avRecorder.getInputSurface()
    AppLog.info("surfaceId:  ${surfaceId}")
} catch (e: BusinessException) {
    AppLog.info("getInputSurface exception: ${e}")
}
```

### func off(AVRecorderCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: AVRecorderCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅AVRecorder状态变化的事件。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVRecorderCallbackType](#enum-avrecordercallbacktype)|是|-|录音配置变化的回调类型。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 事件的回调方法。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*

let avRecorder = createAVRecorder()
avRecorder.off(AVRECORDER_ERROR)
```