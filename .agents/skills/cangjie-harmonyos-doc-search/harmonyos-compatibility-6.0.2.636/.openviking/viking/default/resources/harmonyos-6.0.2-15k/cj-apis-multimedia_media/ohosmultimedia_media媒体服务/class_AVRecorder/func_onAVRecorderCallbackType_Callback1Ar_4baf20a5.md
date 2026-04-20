### func on(AVRecorderCallbackType, Callback1Argument\<BusinessException>)

```cangjie
public func on(`type`: AVRecorderCallbackType, callback: Callback1Argument<BusinessException>): Unit
```

**功能：** 订阅AVRecorder的错误事件，该事件仅用于错误提示，不需要用户停止播控动作。如果此时[AVRecorderState](#enum-avrecorderstate)也切至error状态，用户需要通过[reset()](#func-reset)或者[release()](#func-release)退出录制操作。

用户只能订阅一个错误事件的回调方法，当用户重复订阅时，以最后一次订阅的回调接口为准。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVRecorderCallbackType](#enum-avrecordercallbacktype)|是|-|录制错误事件回调类型AVRECORDER_ERROR。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<BusinessException>|是|-|录制错误事件回调方法。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied. |
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |
  |801|Capability not supported. |
  |5400101|No memory. |
  |5400102|Operation not allowed. |
  |5400103|IO error. |
  |5400104|Time out.|
  |5400105|Service died.|
  |5400106|Unsupported format.|
  |5400107|Audio interrupted. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

// 此处代码可添加在依赖项定义中
class ErrorCallback <: Callback1Argument<BusinessException> {
    public static var invoked = false

    public func invoke(exception: BusinessException) {
        AppLog.info("case avRecorder.on(AVError) called, errMessage is ${exception.message}")
        invoked = true
    }
}

let avRecorder = createAVRecorder()
avRecorder.on(AVRECORDER_ERROR, ErrorCallback())
```