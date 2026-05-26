### func on(AVTranscoderCallbackType, Callback0Argument)

```cangjie
public func on(`type`: AVTranscoderCallbackType, callback: Callback0Argument): Unit
```

**功能：** 注册转码完成事件，并通过注册的回调方法通知用户。用户只能注册一个转码完成事件的回调方法，当用户重复注册时，以最后一次注册的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVTranscoderCallbackType](#enum-avtranscodercallbacktype)|是|-|转码完成事件回调类型Complete。|
|callback|[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)|是|-|转码完成事件回调方法。|

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

class CompleteCallBack <: Callback0Argument {
    let callback_: ()->Unit
    public init(callback: ()->Unit) {callback_ = callback}
    public open func invoke(): Unit {
        callback_()
    }
}

try {
    let avTranscoder = createAVTranscoder()
    let completeCallBack = CompleteCallBack({=> AppLog.info("CompleteCallBack")})
    avTranscoder.on(AVTranscoderCallbackType.Complete, completeCallBack)
} catch (e: BusinessException) {
    AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
}
```

### func off(AVTranscoderCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: AVTranscoderCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消视频转码回调事件。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVTranscoderCallbackType](#enum-avtranscodercallbacktype)|是|-|转码事件回调类型。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None|转码回调方法。|

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

try {
    let avTranscoder = createAVTranscoder()
    avTranscoder.off(AVTranscoderCallbackType.Complete)
    avTranscoder.off(AVTranscoderCallbackType.ProgressUpdate)
    avTranscoder.off(AVTranscoderCallbackType.Error)
} catch (e: BusinessException) {
    AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
}
```