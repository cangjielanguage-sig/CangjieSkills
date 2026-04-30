## func hasDefaultNet()

```cangjie
public func hasDefaultNet(): Bool
```

**功能：** 检查默认数据网络是否被激活，返回接口，如果被激活则返回true。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|默认数据网络被激活返回true。|

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

let hasDefault = hasDefaultNet()
```

## func isDefaultNetMetered()

```cangjie
public func isDefaultNetMetered(): Bool
```

**功能：** 检查当前网络上的数据流量使用是否被计量。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|当前网络上的数据流量使用被计量，则返回true，否则返回false。|

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

let isMetered = isDefaultNetMetered()
```

## func reportNetConnected(NetHandle)

```cangjie
public func reportNetConnected(netHandle: NetHandle): Unit
```

**功能：** 向网络管理报告网络处于可用状态。

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
reportNetConnected(handle)
```