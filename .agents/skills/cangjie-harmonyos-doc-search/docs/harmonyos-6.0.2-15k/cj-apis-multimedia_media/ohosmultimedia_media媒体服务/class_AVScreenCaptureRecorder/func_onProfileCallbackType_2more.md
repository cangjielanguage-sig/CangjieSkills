### func on(ProfileCallbackType, Callback1Argument\<AVScreenCaptureStateCode>)

```cangjie
public func on(`type`: ProfileCallbackType, callback: Callback1Argument<AVScreenCaptureStateCode>): Unit
```

**功能：** 订阅录屏状态切换的事件，当状态发生的时候，会通过订阅的回调通知用户。用户只能订阅一个状态切换的回调方法，重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ProfileCallbackType](#enum-profilecallbacktype)|是|-|状态切换事件回调类型，支持的事件：'stateChange'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AVScreenCaptureStateCode](#enum-avscreencapturestatecode)>|是|-|状态切换事件回调方法，AVScreenCaptureStateCode表示切换到的状态。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.CoreFileKit.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class MyCallbackObject <: Callback1Argument<AVScreenCaptureStateCode> {
    let callback_: (AVScreenCaptureStateCode) -> Unit
    public init(callback: (AVScreenCaptureStateCode) -> Unit) {callback_ = callback}
    public open func invoke(val: AVScreenCaptureStateCode): Unit {
        callback_(val)
    }
}

let filePath = "/data/storage/el2/base/haps/entry/files/test.mp4"
let file = FileFs.open(filePath, mode: (READ_WRITE.mode | CREATE.mode))
let config = AVScreenCaptureRecordConfig(file.fd, 640, 480)
let scr = createAVScreenCaptureRecorder()
let callback = MyCallbackObject(
    {val: AVScreenCaptureStateCode => AppLog.info("on state change")})
if (let Some(v) <- scr) {
    v.on(ProfileCallbackType.CONNECTION_STATE_CHANGE, callback)
}
```

### func on(ProfileCallbackType, Callback1Argument\<BusinessException>)

```cangjie
public func on(`type`: ProfileCallbackType, callback: Callback1Argument<BusinessException>): Unit
```

**功能：** 订阅AVScreenCaptureRecorder的错误事件，用户可以根据应用自身逻辑对错误事件进行处理。用户只能订阅一个错误事件的回调方法，重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ProfileCallbackType](#enum-profilecallbacktype)|是|-|错误事件回调类型，支持的事件：'error'。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)>|是|-|录屏错误事件回调方法。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|permission denied.|
  |5400103|IO error.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.*
import kit.CoreFileKit.*

// 此处代码可添加在依赖项定义中
class ErrorCallback <: Callback1Argument<BusinessException> {
    public static var invoked = false

    public func invoke(exception: BusinessException) {
        AppLog.info("[multimedia_camera | Error Callback]: exception: ${exception.message}")

        invoked = true
    }
}

let filePath = "/data/storage/el2/base/haps/entry/files/test.mp4"
let scr = createAVScreenCaptureRecorder()
let callback = ErrorCallback()
if (let Some(v) <- scr) {
    v.on(ProfileCallbackType.CONNECTION_ERROR, callback)
}
```