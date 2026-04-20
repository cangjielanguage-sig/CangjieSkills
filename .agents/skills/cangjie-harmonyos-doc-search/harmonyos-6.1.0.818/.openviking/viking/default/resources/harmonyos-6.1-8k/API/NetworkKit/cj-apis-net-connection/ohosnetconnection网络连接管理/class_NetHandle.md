## class NetHandle

```cangjie
public class NetHandle {
    public var netId: Int32
}
```

**功能：** 数据网络的句柄。

在调用NetHandle的方法之前，需要先获取NetHandle对象。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### var netId

```cangjie
public var netId: Int32
```

**功能：** 网络ID，取值为0代表没有默认网络，其余取值必须大于等于100。

**类型：** Int32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

### func getAddressByName(String)

```cangjie
public func getAddressByName(host: String): NetAddress
```

**功能：** 使用当前NetHandle对应的网络解析主机名获取到的第一个IP地址。

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
|[NetAddress](#class-netaddress)|返回第一个IP地址。|

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

    let address = handle.getAddressByName("localhost")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getAddressesByName(String)

```cangjie
public func getAddressesByName(host: String): Array<NetAddress>
```

**功能：** 使用当前NetHandle对应的网络解析主机名获取到的所有IP地址。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|host|String|是|-|需要解析的主机名。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[NetAddress](#class-netaddress)>|需要解析的主机名。例如："www.example.com"。|

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

    let addresses = handle.getAddressesByName("localhost")
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```