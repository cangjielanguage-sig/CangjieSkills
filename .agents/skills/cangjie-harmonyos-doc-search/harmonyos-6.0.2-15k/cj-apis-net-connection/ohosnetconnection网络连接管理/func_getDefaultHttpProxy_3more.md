## func getDefaultHttpProxy()

```cangjie
public func getDefaultHttpProxy(): HttpProxy
```

**功能：** 获取网络默认的代理配置信息。 如果设置了全局代理，则会返回全局代理配置信息。如果进程使用setAppNet绑定到指定NetHandle对应的网络，则返回NetHandle对应网络的代理配置信息。在其它情况下，将返回默认网络的代理配置信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[HttpProxy](#class-httpproxy)|返回网络默认的代理配置信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[网络连接管理错误码](../../errorcodes/cj-errorcode-net-connection.md)。

  |错误码ID|错误信息|
  |:---|:---|
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
    let proxy = getDefaultHttpProxy()
    Hilog.info(0, "test", "proxy: ${proxy.host ?? ""} ${proxy.port ?? 0}")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "getDefaultHttpProxy failed: ${e.code} ${e.message}")
}
```

## func getDefaultNet()

```cangjie
public func getDefaultNet(): NetHandle
```

**功能：** 获取默认激活的数据网络。可以使用getNetCapabilities去获取网络的类型、拥有的能力等信息。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[NetHandle](#class-nethandle)|返回默认激活的数据网络。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[网络连接管理错误码](../../errorcodes/cj-errorcode-net-connection.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error.|
  |2100002|Operation failed. Cannot connect to service.|
  |2100003|System internal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let netHandle = getDefaultNet()
```

## func getNetCapabilities(NetHandle)

```cangjie
public func getNetCapabilities(netHandle: NetHandle): NetCapabilities
```

**功能：** 获取netHandle对应的网络的能力信息。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|netHandle|[NetHandle](#class-nethandle)|是|-|数据网络的句柄。|

**返回值：**

|类型|说明|
|:----|:----|
|[NetCapabilities](#class-netcapabilities)|返回网络的能力信息。|

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
    let netCapabilities = getNetCapabilities(netHandle)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "getNetCapabilities failed: ${e.code} ${e.message}")
}
```