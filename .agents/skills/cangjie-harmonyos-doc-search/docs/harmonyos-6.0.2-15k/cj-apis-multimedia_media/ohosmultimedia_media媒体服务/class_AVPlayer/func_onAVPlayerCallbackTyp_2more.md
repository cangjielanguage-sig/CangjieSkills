### func on(AVPlayerCallbackType, OnTrackChangeHandler)

```cangjie
public func on(`type`: AVPlayerCallbackType, callback: OnTrackChangeHandler): Unit
```

**功能：** 订阅获取轨道变更的事件，当播放的轨道变更时，会通过订阅的回调方法通知用户。用户只能订阅一个轨道变更事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVPlayerCallbackType](#enum-avplayercallbacktype)|是|-|事件回调类型，支持的事件为：[TrackChange](#trackchange)。|
|callback|[OnTrackChangeHandler](#type-ontrackchangehandler)|是|-|取消轨道变更事件的回调方法。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class TrackChangeCallback <: OnTrackChangeHandler {
    public init() {}
    public open func invoke(index: Int32, isSelect: Bool): Unit {
        AppLog.info("index: ${index}, isSelect: ${isSelect}")
    }
}

let callback = TrackChangeCallback()
let player = createAVPlayer()
player.on(AVPlayerCallbackType.TrackChange, callback)
```

### func on(AVPlayerCallbackType, Callback1Argument\<Array\<MediaDescription>>)

```cangjie
public func on(`type`: AVPlayerCallbackType, callback: Callback1Argument<Array<MediaDescription>>): Unit
```

**功能：** 订阅获取轨道信息更新的事件，当播放的轨道有更新时，会通过订阅的回调方法通知用户。用户只能订阅一个轨道变更事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVPlayerCallbackType](#enum-avplayercallbacktype)|是|-|事件回调类型，支持的事件为：[TrackInfoUpdate](#trackinfoupdate)。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<[MediaDescription](#type-mediadescription)>>|是|-|轨道信息更新事件回调方法。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class TrackInfoUpdateCallback <: Callback1Argument<Array<MediaDescription>> {
    public init() {}
    public open func invoke(info: Array<MediaDescription>): Unit {
        AppLog.info("TrackInfoUpdate called")
    }
}

let callback = TrackInfoUpdateCallback()
let player = createAVPlayer()
player.on(AVPlayerCallbackType.TrackInfoUpdate, callback)
```