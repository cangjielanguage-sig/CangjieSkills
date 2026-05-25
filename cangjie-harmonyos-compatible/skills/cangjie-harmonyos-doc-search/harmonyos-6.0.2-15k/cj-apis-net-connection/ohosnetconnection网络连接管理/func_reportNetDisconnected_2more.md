## func reportNetDisconnected(NetHandle)

```cangjie
public func reportNetDisconnected(netHandle: NetHandle): Unit
```

**功能：** 向网络管理报告网络处于不可用状态。

**需要权限：** ohos.permission.GET_NETWORK_INFO 和 ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|netHandle|[NetHandle](#class-nethandle)|是|-|数据网络的句柄，参考[NetHandle](#class-nethandle)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[网络连接管理错误码](../../errorcodes/cj-errorcode-net-connection.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error.|
  |2100001|Invalid parameter value.|
  |2100002|Operation failed. Cannot connect to service.|
  |2100003|System internal error.|
  |2101006|the net id is not found.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let handle = getDefaultNet()
reportNetDisconnected(handle)
```

## func setAppNet(NetHandle)

```cangjie
public func setAppNet(netHandle: NetHandle): Unit
```

**功能：** 绑定App到指定网络，绑定后的App只能通过指定网络访问外网。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|netHandle|[NetHandle](#class-nethandle)|是|-|数据网络的句柄。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[网络连接管理错误码](../../errorcodes/cj-errorcode-net-connection.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error.|
  |2100001|Invalid parameter value.|
  |2100002|Operation failed. Cannot connect to service.|
  |2100003|System internal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import kit.PerformanceAnalysisKit.*

try {
    let netHandle = getDefaultNet()
    setAppNet(netHandle)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "setAppNet failed: ${e.code} ${e.message}")
}
```