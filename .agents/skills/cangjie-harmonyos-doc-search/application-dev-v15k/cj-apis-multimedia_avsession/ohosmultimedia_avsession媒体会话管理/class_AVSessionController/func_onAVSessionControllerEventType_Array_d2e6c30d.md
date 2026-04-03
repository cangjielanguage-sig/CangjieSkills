### func on(AVSessionControllerEventType, Array\<KeyOfCallMetadata>, Callback1Argument\<CallMetadata>)

```cangjie
public func on(eventType: AVSessionControllerEventType, filter: Array<KeyOfCallMetadata>, callback: Callback1Argument<CallMetadata>): Unit
```

**功能：** 设置通话元数据变化的监听事件。使用callback回调。当前仅支持EVENT_AVCALL_META_DATA_CHANGE。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionControllerEventType](#enum-avsessioncontrollereventtype)|是|-|事件回调类型，支持事件EVENT_AVCALL_META_DATA_CHANGE：当通话元数据变化时，触发该事件。|
|filter|Array\<[KeyOfCallMetadata](#enum-keyofcallmetadata)>|是|-|Array\<[KeyOfCallMetadata](#enum-keyofcallmetadata)>表示关注Array中的字段变化。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[CallMetadata](#class-callmetadata)>|是|-|回调函数，参数state是变化后的播放状态。|

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
class CallMetaDataChangeCallback <: Callback1Argument<CallMetadata> {
    CallMetaDataChangeCallback(let f: (CallMetadata) -> Unit) {}

    public func invoke(args1: CallMetadata): Unit {
        f(args1)
    }
}

let ctx = Global.getStageContext() // 需获取Context应用上下文，详见本文使用说明
let avSession = createAVSession(ctx, "tag", AVSessionType.SESSION_TYPE_AUDIO)
let controller = avSession.getController()
let callback = CallMetaDataChangeCallback({
    p: CallMetadata =>
        let name = match(p.name) {
            case Some(v) => v
            case None => throw Exception("")
        }
        AppLog.info("on metadataChange name: ${name}")
})
controller.on(AVSessionControllerEventType.EVENT_AVCALL_META_DATA_CHANGE, [KeyOfCallMetadata.KEY_OF_CALLMETADATA_AVATAR], callback)
```