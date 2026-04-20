## func getAllNets()

```cangjie
public func getAllNets(): Array<NetHandle>
```

**功能：** 获取所有处于连接状态的网络列表。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[NetHandle](#class-nethandle)>|返回激活的数据网络列表。|

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

let netHandles = getAllNets()
```

## func getAppNet()

```cangjie
public func getAppNet(): NetHandle
```

**功能：** 绑定App到指定网络，绑定后的App只能通过指定网络访问外网。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[NetHandle](#class-nethandle)|返回APP绑定的数据网络。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[网络连接管理错误码](../../errorcodes/cj-errorcode-net-connection.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |2100002|Operation failed. Cannot connect to service.|
  |2100003|System internal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let netHandle = getAppNet()
```

## func getConnectionProperties(NetHandle)

```cangjie
public func getConnectionProperties(netHandle: NetHandle): ConnectionProperties
```

**功能：** 获取netHandle对应的网络的连接信息。

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
|[ConnectionProperties](#class-connectionproperties)|返回网络的连接信息。|

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
    let connectionProperties = getConnectionProperties(netHandle)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "getConnectionProperties failed: ${e.code} ${e.message}")
}
```