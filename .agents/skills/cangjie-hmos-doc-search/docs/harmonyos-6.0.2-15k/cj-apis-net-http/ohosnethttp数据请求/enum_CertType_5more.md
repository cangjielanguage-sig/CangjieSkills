## enum CertType

```cangjie
public enum CertType {
    | PEM
    | DER
    | P12
    | ...
}
```

**功能：** 证书类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### DER

```cangjie
DER
```

**功能：** 证书类型DER。

**起始版本：** 12

### P12

```cangjie
P12
```

**功能：** 证书类型P12。

**起始版本：** 12

### PEM

```cangjie
PEM
```

**功能：** 证书类型PEM。

**起始版本：** 12

## enum HttpData

```cangjie
public enum HttpData <: ToString {
    | STRING_DATA(String)
    | ARRAY_DATA(Array<Byte>)
    | ...
}
```

**功能：** HTTP的数据。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**父类型：**

- ToString

### ARRAY_DATA(Array\<Byte>)

```cangjie
ARRAY_DATA(Array<Byte>)
```

**功能：** 二进制数组。

**起始版本：** 12

### STRING_DATA(String)

```cangjie
STRING_DATA(String)
```

**功能：** 字符串。

**起始版本：** 12

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回字符串形式的[HttpData](#enum-httpdata)。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回字符串形式的[HttpData](#enum-httpdata)。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let httpData = HttpData.STRING_DATA("data to send")
AppLog.info(httpData.toString())
```

## enum HttpDataType

```cangjie
public enum HttpDataType {
    | STRING
    | ARRAY_BUFFER
    | ...
}
```

**功能：** HTTP的数据类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### ARRAY_BUFFER

```cangjie
ARRAY_BUFFER
```

**功能：** 二进制数组类型。

**起始版本：** 12

### STRING

```cangjie
STRING
```

**功能：** 字符串类型。

**起始版本：** 12

## enum HttpProtocol

```cangjie
public enum HttpProtocol {
    | HTTP1_1
    | HTTP2
    | HTTP3
    | ...
}
```

**功能：** HTTP协议版本。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### HTTP1_1

```cangjie
HTTP1_1
```

**功能：** 协议HTTP/1.1。

**起始版本：** 12

### HTTP2

```cangjie
HTTP2
```

**功能：** 协议HTTP/2。

**起始版本：** 12

### HTTP3

```cangjie
HTTP3
```

**功能：** 协议HTTP/3，若系统或服务器不支持，则使用低版本的HTTP协议请求。仅对HTTPS的URL生效，HTTP则会请求失败。

**起始版本：** 12

## enum RequestMethod

```cangjie
public enum RequestMethod {
    | OPTIONS
    | GET
    | HEAD
    | POST
    | PUT
    | DELETE
    | TRACE
    | CONNECT
    | ...
}
```

**功能：** HTTP请求方法。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### CONNECT

```cangjie
CONNECT
```

**功能：** HTTP请求CONNECT。

**起始版本：** 12

### DELETE

```cangjie
DELETE
```

**功能：** HTTP请求DELETE。

**起始版本：** 12

### GET

```cangjie
GET
```

**功能：** HTTP请求GET。

**起始版本：** 12

### HEAD

```cangjie
HEAD
```

**功能：** HTTP请求HEAD。

**起始版本：** 12

### OPTIONS

```cangjie
OPTIONS
```

**功能：** HTTP请求OPTIONS。

**起始版本：** 12

### POST

```cangjie
POST
```

**功能：** HTTP请求POST。

**起始版本：** 12

### PUT

```cangjie
PUT
```

**功能：** HTTP请求PUT。

**起始版本：** 12

### TRACE

```cangjie
TRACE
```

**功能：** HTTP请求TRACE。

**起始版本：** 12

### func getValue()

```cangjie
public func getValue(): String
```

**功能：** 获取RequestMethod枚举对应的字符串。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回RequestMethod枚举对应的字符串。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*

let getMethod = RequestMethod.GET.getValue()
```