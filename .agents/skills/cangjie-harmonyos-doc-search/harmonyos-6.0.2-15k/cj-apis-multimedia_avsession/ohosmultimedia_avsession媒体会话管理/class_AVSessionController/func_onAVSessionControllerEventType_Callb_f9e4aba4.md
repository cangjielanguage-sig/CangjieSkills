### func on(AVSessionControllerEventType, Callback2Argument\<String, HashMap\<String, ValueType>>)

```cangjie
public func on(eventType: AVSessionControllerEventType, callback: Callback2Argument<String, HashMap<String, ValueType>>): Unit
```

**功能：** 媒体控制器设置会话自定义事件变化的监听器。使用callback回调。当前仅支持EVENT_SESSION_EVENT_CHANGE。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionControllerEventType](#enum-avsessioncontrollereventtype)|是|-|事件回调类型，支持事件EVENT_SESSION_EVENT_CHANGE：当会话事件变化时，触发该事件。|
|callback|[Callback2Argument](../BasicServicesKit/cj-apis-base.md#class-callback2argument)\<String, HashMap\<String, [ValueType](#enum-valuetype)>>|是|-|回调函数，sessionEvent为变化的会话事件名，args为事件的参数。|

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
import std.collection.HashMap

// 此处代码可添加在依赖项定义中
class SessionEventChangeCallback <: Callback2Argument<String, HashMap<String, ValueType>> {
    SessionEventChangeCallback(let f: (String, HashMap<String, ValueType>) -> Unit) {}

    public func invoke(sessionEvent: String, args: HashMap<String, ValueType>): Unit {
        f(sessionEvent, args)
    }
}

let ctx = Global.getStageContext() // 需获取Context应用上下文，详见本文使用说明
let avSession = createAVSession(ctx, "tag", AVSessionType.SESSION_TYPE_AUDIO)
let controller = avSession.getController()
let callback = SessionEventChangeCallback({
    sessionEvent: String, args: HashMap<String, ValueType> =>
        AppLog.info("ConnectionState is ${sessionEvent.toString()}")
})
controller.on(AVSessionControllerEventType.EVENT_SESSION_EVENT_CHANGE , callback)
```