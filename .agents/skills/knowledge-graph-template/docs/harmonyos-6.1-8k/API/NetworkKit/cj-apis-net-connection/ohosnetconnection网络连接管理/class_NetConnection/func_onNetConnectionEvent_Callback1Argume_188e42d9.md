### func on(NetConnectionEvent, Callback1Argument\<NetConnectionPropertyInfo>)

```cangjie
public func on(event: NetConnectionEvent, callback: Callback1Argument<NetConnectionPropertyInfo>): Unit
```

**功能：** 订阅网络连接信息变化事件。此接口要在register接口调用前调用，不需要网络状态变化回调通知时，使用unregister取消订阅默认网络状态变化的通知。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[NetConnectionEvent](#enum-netconnectionevent)|是|-|网络连接事件类型，仅支持NetConnectionPropertiesChange事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[NetConnectionPropertyInfo](#class-netconnectionpropertyinfo)>|是|-|回调函数，获取网络连接属性信息。|

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

// 定义NetConnectionPropertiesChangeCb类
class NetConnectionPropertiesChangeCb <: Callback1Argument<NetConnectionPropertyInfo> {
    let callback_: (NetConnectionPropertyInfo)->Unit
    public init(callback: (NetConnectionPropertyInfo)->Unit) {callback_ = callback}
    public func invoke(err: ?BusinessException, val: NetConnectionPropertyInfo): Unit {
        callback_(val)
    }
}

try {
    let netConn = createNetConnection()
    netConn.register()

    let netConnectionPropertiesChangeCallBack = NetConnectionPropertiesChangeCb(
        {
            info => Hilog.info(0, "net_connection test",
                "onNetConnectionPropertiesChange handle is ${info.netHandle.netId}, props is ")
        })
    netConn.on(NetConnectionEvent.NetConnectionPropertiesChange, netConnectionPropertiesChangeCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```