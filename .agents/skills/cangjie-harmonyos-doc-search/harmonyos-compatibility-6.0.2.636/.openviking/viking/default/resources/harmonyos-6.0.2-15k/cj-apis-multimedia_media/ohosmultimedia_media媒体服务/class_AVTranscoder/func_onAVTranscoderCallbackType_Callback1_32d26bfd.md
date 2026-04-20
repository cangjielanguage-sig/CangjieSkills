### func on(AVTranscoderCallbackType, Callback1Argument\<BusinessException>)

```cangjie
public func on(`type`: AVTranscoderCallbackType, callback: Callback1Argument<BusinessException>): Unit
```

**功能：** 注册[AVtranscoder](#class-avtranscoder)的错误事件，该事件仅用于错误提示。如果AVTranscoder上报error事件，用户需要通过[release()](#func-release)退出转码操作。用户只能订阅一个错误事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVTranscoder

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVTranscoderCallbackType](#enum-avtranscodercallbacktype)|是|-|转码错误事件回调类型ERROR。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)>|是|-|转码错误事件回调方法。|

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

class ErrCallBack <: Callback1Argument<BusinessException> {
    let callback_: (BusinessException)->Unit
    public init(callback: (BusinessException)->Unit) {callback_ = callback}
    public open func invoke(err: BusinessException): Unit {
        callback_(err)
    }
}

try {
    let avTranscoder = createAVTranscoder()
    let errCallBack = ErrCallBack({ val: BusinessException => AppLog.info("ErrCallBack") })
    avTranscoder.on(AVTranscoderCallbackType.Error, errCallBack)
} catch (e: BusinessException) {
    AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
}
```