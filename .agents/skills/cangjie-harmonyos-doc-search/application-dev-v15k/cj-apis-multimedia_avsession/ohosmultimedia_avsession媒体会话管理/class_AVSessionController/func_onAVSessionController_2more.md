### func on(AVSessionControllerEventType, Callback1Argument\<HashMap\<String, ValueType>>)

```cangjie
public func on(eventType: AVSessionControllerEventType, callback: Callback1Argument<HashMap<String, ValueType>>): Unit
```

**功能：** 媒体控制器设置自定义媒体数据包事件变化的监听器。使用callback回调。当前支持EVENT_EXTRAS_CHANGE。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionControllerEventType](#enum-avsessioncontrollereventtype)|是|-|事件回调类型，支持事件EVENT_EXTRAS_CHANGE ：当媒体提供方设置自定义媒体数据包时，触发该事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<HashMap\<String, [ValueType](#enum-valuetype)>>|是|-|回调函数，extras为媒体提供方新设置的自定义媒体数据包，该自定义媒体数据包与[dispatchSessionEvent](#func-dispatchsessioneventstring-hashmapstring-valuetype)方法设置的数据包完全一致。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600103|The session controller does not exist.|

### func on(AVSessionControllerEventType, Callback1Argument\<AVQueueItem>)

```cangjie
public func on(eventType: AVSessionControllerEventType, callback: Callback1Argument<AVQueueItem>): Unit
```

**功能：** 媒体控制器设置会话自定义播放列表变化的监听器。使用callback回调。当前仅支持EVENT_QUEUE_ITEMS_CHANGE。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionControllerEventType](#enum-avsessioncontrollereventtype)|是|-|事件回调类型，支持事件EVENT_QUEUE_ITEMS_CHANGE：当session修改播放列表时，触发该事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AVQueueItem](#class-avqueueitem)>|是|-|回调函数，items为变化的播放列表。|

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
class QueueItemChangeCallback <: Callback1Argument<AVQueueItem> {
    QueueItemChangeCallback(let f: (AVQueueItem) -> Unit) {}

    public func invoke(arg1: AVQueueItem): Unit {
        f(arg1)
    }
}

let ctx = Global.getStageContext() // 需获取Context应用上下文，详见本文使用说明
let avSession = createAVSession(ctx, "tag", AVSessionType.SESSION_TYPE_AUDIO)
let controller = avSession.getController()
try {
    let callback = QueueItemChangeCallback({
        p: AVQueueItem =>
        let status = match(p) {
            case itemId => "0"
            case description => "description"
        }
        AppLog.info("callback1 excute: ${status}")
    })
    controller.on(AVSessionControllerEventType.EVENT_QUEUE_ITEMS_CHANGE, callback)
} catch (e: BusinessException) {
    AppLog.info("error code is ${e.code}, error message is ${e.message}")
}
```