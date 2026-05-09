### func on(NetConnectionEvent, Callback0Argument)

```cangjie
public func on(event: NetConnectionEvent, callback: Callback0Argument): Unit
```

**功能：** 订阅网络不可用事件。此接口要在register接口调用前调用，不需要网络状态变化回调通知时，使用unregister取消订阅默认网络状态变化的通知。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[NetConnectionEvent](#enum-netconnectionevent)|是|-|网络连接事件类型，仅支持NetUnavailable事件。|
|callback|[Callback0Argument](../arkinterop/cj-api-callback_invoke.md#class-callback0argument)|是|-|回调函数，无返回结果。|

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

// 定义NetUnavailableCb类
class NetUnavailableCb <: Callback0Argument {
    let callback_: ()->Unit
    public init(callback: ()->Unit) {callback_ = callback}
    public func invoke(err: ?BusinessException): Unit {
        callback_()
    }
}

try {
    let netConn = createNetConnection()
    netConn.register()

    let netUnAvailableCallBack = NetUnavailableCb({=> Hilog.info(0, "net_connection test", "onNetUnavailable")})
    netConn.on(NetConnectionEvent.NetUnavailable, netUnAvailableCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func register()

```cangjie
public func register(): Unit
```

**功能：** 订阅指定网络状态变化的通知。如需监听特定事件，确保调用on监听事件后再调用register进行注册。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[网络连接管理错误码](./cj-errorcode-net-connection.md)和[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 2100002 | Failed to connect to the service. |
  | 2100003 | System internal error. |
  | 2101008 | The callback already exists. |
  | 2101022 | The number of requests exceeded the maximum allowed. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let netCon: NetConnection = createNetConnection()
    netCon.register()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func unregister()

```cangjie
public func unregister(): Unit
```

**功能：** 取消订阅默认网络状态变化的通知。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[网络连接管理错误码](./cj-errorcode-net-connection.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 2100002 | Failed to connect to the service. |
  | 2100003 | System internal error. |
  | 2101007 | The callback does not exist. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let netCon: NetConnection = createNetConnection()
    netCon.register()
    netCon.unregister()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```