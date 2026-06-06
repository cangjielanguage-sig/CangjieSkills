## class NetHandle

```cangjie
public class NetHandle <: ToString {
    public NetHandle(public let netId: Int32)
}
```

**功能：** 数据网络的句柄。在调用NetHandle的方法之前，需要先获取NetHandle对象。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**父类型：**

- ToString

### let netId

```cangjie
public let netId: Int32
```

**功能：** 网络ID，取值为0代表没有默认网络，其余取值必须大于等于100。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 12

### NetHandle(Int32)

```cangjie
public NetHandle(public let netId: Int32)
```

**功能：** 构造NetHandle实例。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|netId|Int32|是|-|网络ID，取值为0代表没有默认网络，其余取值必须大于等于100。|

### func getAddressByName(String)

```cangjie
public func getAddressByName(host: String): NetAddress
```

**功能：** 使用对应网络解析主机名以获取第一个IP地址。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|host|String|是|-|需要解析的主机名。|

**返回值：**

|类型|说明|
|:----|:----|
|[NetAddress](#class-netaddress)|返回第一个IP地址。|

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

let handle = getDefaultNet()
let address = handle.getAddressByName("localhost")
```

### func getAddressesByName(String)

```cangjie
public func getAddressesByName(host: String): Array<NetAddress>
```

**功能：** 使用对应网络解析主机名以获取所有IP地址。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|host|String|是|-|需要解析的主机名。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[NetAddress](#class-netaddress)>|返回所有IP地址。|

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

let handle = getDefaultNet()
let addresses = handle.getAddressesByName("localhost")
```

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回字符串形式的NetHandle。

**系统能力：** SystemCapability.Communication.NetManager.Core

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回字符串形式的[NetHandle](#class-nethandle)。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let handle = getDefaultNet()

AppLog.info(handle.toString())
```