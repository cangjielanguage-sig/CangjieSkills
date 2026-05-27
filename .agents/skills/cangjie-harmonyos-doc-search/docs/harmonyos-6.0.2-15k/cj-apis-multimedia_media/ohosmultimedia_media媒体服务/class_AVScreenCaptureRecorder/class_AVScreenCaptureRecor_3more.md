## class AVScreenCaptureRecorder

```cangjie
public class AVScreenCaptureRecorder {}
```

**功能：** 屏幕录制管理类，用于进行屏幕录制。在调用AVScreenCaptureRecorder的方法前，需要先通过[createAVScreenCaptureRecorder()](#func-createavscreencapturerecorder)创建一个AVScreenCaptureRecorder实例。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

### func initialize(AVScreenCaptureRecordConfig)

```cangjie
public func initialize(config: AVScreenCaptureRecordConfig): Unit
```

**功能：** 设置录屏参数。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|config|[AVScreenCaptureRecordConfig](#class-avscreencapturerecordconfig)|是|-|设置录屏参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.|
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
    v.initialize(config)
}
```

### func off(ProfileCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: ProfileCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅连接管理回调事件。用户可以指定填入状态切换或填入错误的回调方法来取消订阅。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[ProfileCallbackType](#enum-profilecallbacktype)|是|-|连接管理回调事件。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 连接管理回调方法。|

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
    {val: AVScreenCaptureStateCode => AppLog.info("off state change")})
if (let Some(v) <- scr) {
    v.off(ProfileCallbackType.CONNECTION_STATE_CHANGE, callback: callback)
}
```