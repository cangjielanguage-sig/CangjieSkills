### func getTrackDescription()

```cangjie
public func getTrackDescription(): Array<MediaDescription>
```

**功能：** 获取音视频轨道信息，可以在prepared/playing/paused状态调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[MediaDescription](#type-mediadescription)>|音视频轨道信息。|

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
    let player = createAVPlayer()
    let mediaDescription = player.getTrackDescription()
    AppLog.info("mediaDescription.size = ${mediaDescription.size}")
    var index = 0
    for (item in mediaDescription) {
        AppLog.info("mediaDescription[${index}]")
        for ((key, value) in item) {
            AppLog.info("key = ${key}")
            match (value) {
                case INT(v) => AppLog.info("value = Int32(${v})")
                case INT64(v) => AppLog.info("value = Int64(${v})")
                case DOUBLE(v) => AppLog.info("value = Float64(${v})")
                case STRING(v) => AppLog.info("value = String(${v})")
                case _ => throw IllegalArgumentException("The type is not supported.")
            }
        }
        index++
    }
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

### func off(AVPlayerCallbackType, CallbackObject)

```cangjie
public func off(`type`: AVPlayerCallbackType, callback: CallbackObject): Unit
```

**功能：** 取消订阅AVPlayer相关监听事件的指定回调函数。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVPlayerCallbackType](#enum-avplayercallbacktype)|是|-|AVPlayer相关监听事件。|
|callback|[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|是|-|取消的回调函数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class StateChangeCallback <: OnAVPlayerStateChangeHandle {
    public init() {}
    public open func invoke(state: AVPlayerState, reason: StateChangeReason): Unit {
        match (state) {
            case Idle =>
                AppLog.info("Idle")
            case Initialized =>
                AppLog.info("Initialized")
            case Prepared =>
                AppLog.info("Prepared")
            case Playing =>
                AppLog.info("Playing")
            case Paused =>
                AppLog.info("Paused")
            case Completed =>
                AppLog.info("Completed")
            case Stopped =>
                AppLog.info("Stopped")
            case Released =>
                AppLog.info("Released")
            case _ =>
                AppLog.info('other state')
        }
    }
}

let callback = StateChangeCallback()
let player = createAVPlayer()
try {
    player.off(AVPlayerCallbackType.StateChange, callback)
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

### func off(AVPlayerCallbackType)

```cangjie
public func off(`type`: AVPlayerCallbackType): Unit
```

**功能：** 取消订阅AVPlayer相关监听事件的所有回调函数。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVPlayerCallbackType](#enum-avplayercallbacktype)|是|-|AVPlayer相关监听事件。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.*

try {
    let player = createAVPlayer()
    player.off(AVPlayerCallbackType.StateChange)
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```