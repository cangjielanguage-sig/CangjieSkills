### func off(AudioStreamManagerCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: AudioStreamManagerCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消监听事件。

**系统能力：** 与\`type\`取值有关，详见[AudioStreamManagerCallbackType](#enum-audiostreammanagercallbacktype)

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioStreamManagerCallbackType](#enum-audiostreammanagercallbacktype)|是|-|监听事件。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |6800101|Invalid parameter.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

// 此处代码可添加在依赖项定义中
class Callback <: Callback1Argument<AudioCapturerChangeInfoArray> {
    public func invoke(arg: AudioCapturerChangeInfoArray) {
        AppLog.info("callback: ${arg[0].streamId}")
    }
}

try {
    let instance = getAudioManager()
    let smgr = instance.getStreamManager()
    var cb1 = Callback()
    smgr.on(AudioStreamManagerCallbackType.CAPTURER_CHANGE, cb1)
    smgr.off(AudioStreamManagerCallbackType.CAPTURER_CHANGE)
} catch (e: BusinessException) {
    Hilog.error(0, "StreamManager:on/off", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func on(AudioStreamManagerCallbackType, Callback1Argument\<AudioCapturerChangeInfoArray>)

```cangjie
public func on(`type`: AudioStreamManagerCallbackType, callback: Callback1Argument<AudioCapturerChangeInfoArray>): Unit
```

**功能：** 监听音频采集器更改事件（当音频录制流状态变化、设备变化时触发），使用callback方式返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioStreamManagerCallbackType](#enum-audiostreammanagercallbacktype)|是|-|监听事件，固定为：'CAPTURER_CHANGE'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AudioCapturerChangeInfoArray](#type-audiocapturerchangeinfoarray)>|是|-|回调函数，返回当前音频采集器信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800301|System error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

// 此处代码可添加在依赖项定义中
class Callback <: Callback1Argument<AudioCapturerChangeInfoArray> {
    public func invoke(arg: AudioCapturerChangeInfoArray) {
        AppLog.info("callback: ${arg[0].streamId}")
    }
}

try {
    let instance = getAudioManager()
    let smgr = instance.getStreamManager()
    var cb1 = Callback()
    smgr.on(AudioStreamManagerCallbackType.CAPTURER_CHANGE, cb1)
    smgr.off(AudioStreamManagerCallbackType.CAPTURER_CHANGE)
} catch (e: BusinessException) {
    Hilog.error(0, "StreamManager:on/off", "errCode: ${e.code}, errMessage: ${e.message}")
}
```