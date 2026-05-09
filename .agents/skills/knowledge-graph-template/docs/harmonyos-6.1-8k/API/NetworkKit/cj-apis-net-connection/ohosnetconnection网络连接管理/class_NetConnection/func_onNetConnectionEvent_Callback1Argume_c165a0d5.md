### func on(NetConnectionEvent, Callback1Argument\<NetBlockStatusInfo>)

```cangjie
public func on(event: NetConnectionEvent, callback: Callback1Argument<NetBlockStatusInfo>): Unit
```

**功能：** 订阅网络阻塞状态事件。此接口需要在调用register接口之前调用。若无需接收网络状态变化的回调通知，应使用unregister取消订阅默认的网络状态变化通知。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[NetConnectionEvent](#enum-netconnectionevent)|是|-|网络连接事件类型，仅支持NetBlockStatusChange事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[NetBlockStatusInfo](#class-netblockstatusinfo)>|是|-|回调函数，获取网络阻塞状态信息。|

**异常：**

- BusinessException：对应错误码如下表，详见[网络连接管理错误码](./cj-errorcode-net-connection.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 2100001 | Invalid parameter value. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.NetworkKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException
import ohos.callback_invoke.*

// 定义NetBlockStatusChangeCb类
class NetBlockStatusChangeCb <: Callback1Argument<NetBlockStatusInfo> {
    let callback_: (NetBlockStatusInfo)->Unit
    public init(callback: (NetBlockStatusInfo)->Unit) {callback_ = callback}
    public func invoke(err: ?BusinessException, val: NetBlockStatusInfo): Unit {
        callback_(val)
    }
}

try {
    let netConn = createNetConnection()
    netConn.register()

    let netBlockStatusChangeCallBack = NetBlockStatusChangeCb(
        {
            info => Hilog.info(0, "net_connection test",
                "onNetBlockStatusChange handle is ${info.netHandle.netId}, block is ${info.blocked}")
        })
    netConn.on(NetConnectionEvent.NetBlockStatusChange, netBlockStatusChangeCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```