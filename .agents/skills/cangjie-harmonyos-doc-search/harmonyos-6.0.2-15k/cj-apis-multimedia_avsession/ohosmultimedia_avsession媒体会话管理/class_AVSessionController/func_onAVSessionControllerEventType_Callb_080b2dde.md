### func on(AVSessionControllerEventType, Callback1Argument\<AVControlCommandType>)

```cangjie
public func on(eventType: AVSessionControllerEventType, callback: Callback1Argument<AVControlCommandType>): Unit
```

**功能：** 会话支持的有效命令变化监听事件。使用callback回调。当前仅支持EVENT_VALID_COMMAND_CHANGE。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionControllerEventType](#enum-avsessioncontrollereventtype)|是|-|事件回调类型，支持事件EVENT_VALID_COMMAND_CHANGE：当检测到会话的合法命令发生改变时，触发该事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AVControlCommandType](#enum-avcontrolcommandtype)>|是|-|回调函数。参数commands是有效命令的集合。|

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
class VaildCommandChangeCallback <: Callback1Argument<AVControlCommandType> {
    VaildCommandChangeCallback(let f: (AVControlCommandType) -> Unit) {}

    public func invoke(arg1: AVControlCommandType): Unit {
        f(arg1)
    }
}

let ctx = Global.getStageContext() // 需获取Context应用上下文，详见本文使用说明
let avSession = createAVSession(ctx, "tag", AVSessionType.SESSION_TYPE_AUDIO)
let controller = avSession.getController()
try {
    let callback = VaildCommandChangeCallback({
        p: AVControlCommandType =>
        let status = match(p) {
            case SESSION_CMD_INVALID =>  "invalid "
            case SESSION_CMD_PLAY => "play"
            case SESSION_CMD_PAUSE => "pause"
            case SESSION_CMD_STOP =>  "stop "
            case SESSION_CMD_PLAY_NEXT =>  "playNext "
            case SESSION_CMD_PLAY_PREVIOUS =>  "playPrevious "
            case SESSION_CMD_FAST_FORWARD =>  "fastForward "
            case SESSION_CMD_REWIND =>  "rewind "
            case SESSION_CMD_SEEK =>  "seek "
            case SESSION_CMD_SET_SPEED =>  "setSpeed "
            case SESSION_CMD_SET_LOOP_MODE =>  "setLoopMode "
            case SESSION_CMD_TOGGLE_FAVORITE =>  "toggleFavorite "
            case SESSION_CMD_PLAY_FROM_ASSETID =>  "playFromAssetId "
            case SESSION_CMD_AVCALL_ANSWER =>  "answer "
            case SESSION_CMD_AVCALL_HANG_UP =>  "hangUp "
            case SESSION_CMD_AVCALL_TOGGLE_CALL_MUTE =>  "toggleCallMute "
            case _ => throw IllegalArgumentException("The type is not supported.")
        }
        AppLog.info("callback1 excute: ${status}")
    })
    controller.on(AVSessionControllerEventType.EVENT_VALID_COMMAND_CHANGE, callback)
} catch (e: BusinessException) {
    AppLog.info("error code is ${e.code}, error message is ${e.message}")
}
```