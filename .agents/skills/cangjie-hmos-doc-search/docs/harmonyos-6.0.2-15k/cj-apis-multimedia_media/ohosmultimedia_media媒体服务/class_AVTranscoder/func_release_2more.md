### func release()

```cangjie
public func release(): Unit
```

**功能：** 释放视频转码资源。释放视频转码资源之后，该AVTranscoder实例不能再进行任何操作。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400101|No memory.|
  |5400102|Operation not allowed.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.BusinessException

try {
    let avTranscoder = createAVTranscoder()
    avTranscoder.release()
} catch (e: BusinessException) {
    AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
}
```

### func on(AVTranscoderCallbackType, Callback1Argument\<Int32>)

```cangjie
public func on(`type`: AVTranscoderCallbackType, callback: Callback1Argument<Int32>): Unit
```

**功能：** 注册转码进度更新事件，并通过注册的回调方法通知用户。用户只能注册一个进度更新事件的回调方法，当用户重复注册时，以最后一次注册的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVTranscoderCallbackType](#enum-avtranscodercallbacktype)|是|-|进度更新事件回调类型ProgressUpdate。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Int32>|是|-|进度更新事件回调方法，val: Int32，表示当前转码进度。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400101|No memory. |

- IllegalArgumentException：

  |错误信息|可能原因|处理步骤|
  |:---|:---|:---|
  |The parameter check failed.|参数校验错误。|请检查传入的参数是否正确。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*
import ohos.base.BusinessException

class UpdateCallBack <: Callback1Argument<Int32> {
    let callback_: (Int32)->Unit
    public init(callback: (Int32)->Unit) {callback_ = callback}
    public open func invoke(val: Int32): Unit {
        callback_(val)
    }
}

try {
    let avTranscoder = createAVTranscoder()
    let updateCallBack = UpdateCallBack({ val: Int32 => AppLog.info("UpdateCallBack ${val}")})
    avTranscoder.on(AVTranscoderCallbackType.ProgressUpdate, updateCallBack)
} catch (e: BusinessException) {
    AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
}
```