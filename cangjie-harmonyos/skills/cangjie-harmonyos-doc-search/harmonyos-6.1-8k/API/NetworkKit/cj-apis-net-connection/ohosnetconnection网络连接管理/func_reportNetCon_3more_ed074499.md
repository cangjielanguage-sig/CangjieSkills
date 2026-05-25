## func reportNetConnected(NetHandle)

```cangjie
public func reportNetConnected(netHandle: NetHandle): Unit
```

**功能：** 向网络管理报告网络处于可用状态。

**需要权限：** ohos.permission.GET_NETWORK_INFO & ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|netHandle|[NetHandle](#class-nethandle)|是|-|数据网络的句柄，参考[NetHandle](#class-nethandle)。|

**异常：**

- BusinessException：对应错误码如下表，详见[网络连接管理错误码](./cj-errorcode-net-connection.md)和[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 2100001 | Invalid parameter value. |
  | 2100002 | Failed to connect to the service. |
  | 2100003 | System internal error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let handle = getDefaultNet()
    reportNetConnected(handle)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func reportNetDisconnected(NetHandle)

```cangjie
public func reportNetDisconnected(netHandle: NetHandle): Unit
```

**功能：** 向网络管理上报网络处于不可用状态。

**需要权限：** ohos.permission.GET_NETWORK_INFO & ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|netHandle|[NetHandle](#class-nethandle)|是|-|数据网络的句柄，参考[NetHandle](#class-nethandle)。|

**异常：**

- BusinessException：对应错误码如下表，详见[网络连接管理错误码](./cj-errorcode-net-connection.md)和[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 2100001 | Invalid parameter value. |
  | 2100002 | Failed to connect to the service. |
  | 2100003 | System internal error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let handle = getDefaultNet()
    reportNetDisconnected(handle)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func setAppNet(NetHandle)

```cangjie
public func setAppNet(netHandle: NetHandle): Unit
```

**功能：** 将App绑定到特定的网络，绑定后App只能通过netHandle对应的网络访问网络。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|netHandle|[NetHandle](#class-nethandle)|是|-|数据网络的句柄。|

**异常：**

- BusinessException：对应错误码如下表，详见[网络连接管理错误码](./cj-errorcode-net-connection.md)和[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 2100001 | Invalid parameter value. |
  | 2100002 | Failed to connect to the service. |
  | 2100003 | System internal error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import kit.PerformanceAnalysisKit.*
import ohos.business_exception.*

try {
    let netHandle = getDefaultNet()
    setAppNet(netHandle)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "setAppNet failed: ${e.code} ${e.message}")
}
```