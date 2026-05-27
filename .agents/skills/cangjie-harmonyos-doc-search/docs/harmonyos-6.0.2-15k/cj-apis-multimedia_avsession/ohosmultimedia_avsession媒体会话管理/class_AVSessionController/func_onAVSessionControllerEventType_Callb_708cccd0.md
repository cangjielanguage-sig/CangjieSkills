### func on(AVSessionControllerEventType, Callback1Argument\<Bool>)

```cangjie
public func on(eventType: AVSessionControllerEventType, callback: Callback1Argument<Bool>): Unit
```

**功能：** 会话的激活状态的监听事件。使用callback回调，当前仅支持EVENT_ACTIVE_STATE_CHANGE。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionControllerEventType](#enum-avsessioncontrollereventtype)|是|-|事件回调类型，支持事件EVENT_ACTIVE_STATE_CHANGE：当检测到会话的激活状态发生改变时，触发该事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Bool>|是|-|回调函数。参数isActive表示会话是否被激活。true表示被激活，false表示禁用。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600103|The session controller does not exist.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AVSessionKit.*
import ohos.ability.getStageContext

// 此处代码可添加在依赖项定义中
class ActiveStateChangeCallback <: Callback1Argument<Bool> {
    ActiveStateChangeCallback(let f: (Bool) -> Unit) {}

    public func invoke(arg1: Bool): Unit {
        f(arg1)
    }
}

let ctx = Global.getStageContext() // 需获取Context应用上下文，详见本文使用说明
let avSession = createAVSession(ctx, "tag", AVSessionType.SESSION_TYPE_AUDIO)
let controller = avSession.getController()
try {
    let callback = ActiveStateChangeCallback({
        p: Bool => AppLog.info("callback1 excute: ${p}")
    })
    controller.on(AVSessionControllerEventType.EVENT_ACTIVE_STATE_CHANGE, callback)
} catch (e: BusinessException) {
    AppLog.info("error code is ${e.code}, error message is ${e.message}")
}
```