### UPGRADE_REQUIRED

```cangjie
UPGRADE_REQUIRED
```

**功能：** 服务器拒绝使用当前协议执行请求，但在客户端升级到其他协议后可能愿意这样做。 服务端发送带有Upgrade(en-US)字段的426响应 来表明它所需的协议。

**起始版本：** 12

### USE_PROXY

```cangjie
USE_PROXY
```

**功能：** 使用代理。

**起始版本：** 12

### VARIANT_ALSO_NEGOTIATES

```cangjie
VARIANT_ALSO_NEGOTIATES
```

**功能：** 服务器存在内部配置错误：所选的变体资源被配置为参与透明内容协商本身，因此不是协商过程中的适当终点。

**起始版本：** 12

### VERSION

```cangjie
VERSION
```

**功能：** 服务器请求的HTTP协议的版本。

**起始版本：** 12

### static func parse(UInt32)

```cangjie
public static func parse(code: UInt32): ResponseCode
```

**功能：** 获取状态码对应。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|code|UInt32|是|-|状态码的数值。|

**返回值：**

|类型|说明|
|:----|:----|
|[ResponseCode](#enum-responsecode)|返回的响应码。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let code = ResponseCode.parse(200)
```

### func getValue()

```cangjie
public func getValue(): UInt32
```

**功能：** 获取ResponseCode枚举对应的数值。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|UInt32|返回ResponseCode枚举对应的数值。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let code = ResponseCode.OK.getValue()
```