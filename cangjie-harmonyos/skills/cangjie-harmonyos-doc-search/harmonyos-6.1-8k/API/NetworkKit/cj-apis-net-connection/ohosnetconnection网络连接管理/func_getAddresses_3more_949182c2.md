## func getAddressesByName(String)

```cangjie
public func getAddressesByName(host: String): Array<NetAddress>
```

**功能：** 使用对应网络解析主机名以获取所有IP地址。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|host|String|是|-|需要解析的主机名。例如："www.example.com"。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[NetAddress](#class-netaddress)>|返回所有IP地址。|

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
    let addresses = getAddressesByName("localhost")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func getAllNets()

```cangjie
public func getAllNets(): Array<NetHandle>
```

**功能：** 获取所有处于连接状态的网络列表。

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[NetHandle](#class-nethandle)>|返回处于激活状态的数据网络列表。|

**异常：**

- BusinessException：对应错误码如下表，详见[网络连接管理错误码](./cj-errorcode-net-connection.md)和[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
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
    let netHandles = getAllNets()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## func getAppNet()

```cangjie
public func getAppNet(): NetHandle
```

**功能：** 获取App绑定的网络信息。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[NetHandle](#class-nethandle)|返回App绑定的网络信息。|

**异常：**

- BusinessException：对应错误码如下表，详见[网络连接管理错误码](./cj-errorcode-net-connection.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
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
    let netHandle = getAppNet()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```