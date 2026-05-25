### func on(NetConnectionEvent, Callback1Argument\<NetCapabilityInfo>)

```cangjie
public func on(event: NetConnectionEvent, callback: Callback1Argument<NetCapabilityInfo>): Unit
```

**功能：** 订阅网络能力变化事件。此接口要在register接口调用前调用，不需要网络状态变化回调通知时，使用unregister取消订阅默认网络状态变化的通知。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[NetConnectionEvent](#enum-netconnectionevent)|是|-|网络连接事件类型，仅支持NetCapabilitiesChange事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[NetCapabilityInfo](#class-netcapabilityinfo)>|是|-|回调函数，返回数据网络句柄（netHandle）和网络的能力信息（netCap）。|

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

// 定义NetCapabilitiesChangeCb类
class NetCapabilitiesChangeCb <: Callback1Argument<NetCapabilityInfo> {
    let callback_: (NetCapabilityInfo)->Unit
    public init(callback: (NetCapabilityInfo)->Unit) {callback_ = callback}
    public func invoke(err: ?BusinessException, val: NetCapabilityInfo): Unit {
        callback_(val)
    }
}

try {
    let netConn = createNetConnection()
    netConn.register()

    let netCapabilitiesChangeCallBack = NetCapabilitiesChangeCb(
        {
            info => Hilog.info(0, "net_connection test",
                "onNetCapabilitiesChange handle is ${info.netHandle.netId}, props is ")
        })
    netConn.on(NetConnectionEvent.NetCapabilitiesChange, netCapabilitiesChangeCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```