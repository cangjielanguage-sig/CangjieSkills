### func on(AVSessionControllerEventType, Callback2Argument\<ConnectionState, OutputDeviceInfo>)

```cangjie
public func on(eventType: AVSessionControllerEventType, callback: Callback2Argument<ConnectionState, OutputDeviceInfo>): Unit
```

**功能：** 设置播放设备变化的监听事件。使用callback回调。当前仅支持EVENT_OUTPUT_DEVICE_CHANGE。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionControllerEventType](#enum-avsessioncontrollereventtype)|是|-|事件回调类型，支持事件为EVENT_OUTPUT_DEVICE_CHANGE ：当播放设备变化时，触发该事件。|
|callback|[Callback2Argument](../BasicServicesKit/cj-apis-base.md#class-callback2argument)\<[ConnectionState](#enum-connectionstate), [OutputDeviceInfo](#class-outputdeviceinfo)>|是|-|回调函数，参数device是设备相关信息。|

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
class OutputDeviceChangeCallback <: Callback2Argument<ConnectionState, OutputDeviceInfo> {
    OutputDeviceChangeCallback(let f: (ConnectionState, OutputDeviceInfo) -> Unit) {}

    public func invoke(arg1: ConnectionState, arg2: OutputDeviceInfo): Unit {
        f(arg1, arg2)
    }
}

let ctx = Global.getStageContext() // 需获取Context应用上下文，详见本文使用说明
let avSession = createAVSession(ctx, "tag", AVSessionType.SESSION_TYPE_AUDIO)
let controller = avSession.getController()
let callback = OutputDeviceChangeCallback({
    p1: ConnectionState, p2: OutputDeviceInfo =>
        AppLog.info("ConnectionState is ${p1}")
})
controller.on(AVSessionControllerEventType.EVENT_OUTPUT_DEVICE_CHANGE, callback)
```