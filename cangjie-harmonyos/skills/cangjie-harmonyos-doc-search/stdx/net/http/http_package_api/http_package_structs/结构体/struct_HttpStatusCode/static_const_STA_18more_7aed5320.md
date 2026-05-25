### static const STATUS_LENGTH_REQUIRED

```cangjie
public static const STATUS_LENGTH_REQUIRED: UInt16 = 411
```

功能：服务器拒绝在没有定义 Content-Length 头的情况下接受请求。

类型：UInt16

### static const STATUS_LOCKED

```cangjie
public static const STATUS_LOCKED: UInt16 = 423
```

功能：当前资源被锁定。

类型：UInt16

### static const STATUS_LOOP_DETECTED

```cangjie
public static const STATUS_LOOP_DETECTED: UInt16 = 508
```

功能：服务器在处理请求时检测到无限递归。

类型：UInt16

### static const STATUS_METHOD_NOT_ALLOWED

```cangjie
public static const STATUS_METHOD_NOT_ALLOWED: UInt16 = 405
```

功能：请求行中指定的请求函数不能被用于请求响应的资源。

类型：UInt16

### static const STATUS_MISDIRECTED_REQUEST

```cangjie
public static const STATUS_MISDIRECTED_REQUEST: UInt16 = 421
```

功能：请求被指向到无法生成响应的服务器。

类型：UInt16

### static const STATUS_MOVED_PERMANENTLY

```cangjie
public static const STATUS_MOVED_PERMANENTLY: UInt16 = 301
```

功能：永久移动。

类型：UInt16

> **说明：**
>
> 请求的资源已被永久的移动到新 URI，返回信息会包括新的 URI，浏览器会自动定向到新 URI。

### static const STATUS_MULTIPLE_CHOICES

```cangjie
public static const STATUS_MULTIPLE_CHOICES: UInt16 = 300
```

功能：被请求的资源有一系列可供选择的回馈信息，每个都有自己特定的地址和浏览器驱动的商议信息。

类型：UInt16

> **说明：**
>
> 用户或浏览器能够自行选择一个首选的地址进行重定向。

### static const STATUS_MULTI_STATUS

```cangjie
public static const STATUS_MULTI_STATUS: UInt16 = 207
```

功能：DAV 绑定的成员已经在（多状态）响应之前的部分被列举，且未被再次包含。

类型：UInt16

### static const STATUS_NETWORK_AUTHENTICATION_REQUIRED

```cangjie
public static const STATUS_NETWORK_AUTHENTICATION_REQUIRED: UInt16 = 511
```

功能：要求网络认证。

类型：UInt16

### static const STATUS_NON_AUTHORITATIVE_INFO

```cangjie
public static const STATUS_NON_AUTHORITATIVE_INFO: UInt16 = 203
```

功能：服务器已成功处理了请求。

类型：UInt16

> **说明：**
>
> 返回的实体头部元信息不是在原始服务器上有效的确定集合，而是来自本地或者第三方的拷贝。

### static const STATUS_NOT_ACCEPTABLE

```cangjie
public static const STATUS_NOT_ACCEPTABLE: UInt16 = 406
```

功能：请求的资源的内容特性无法满足请求头中的条件，因而无法生成响应实体。

类型：UInt16

### static const STATUS_NOT_EXTENDED

```cangjie
public static const STATUS_NOT_EXTENDED: UInt16 = 510
```

功能：获取资源所需要的策略并没有被满足。

类型：UInt16

### static const STATUS_NOT_FOUND

```cangjie
public static const STATUS_NOT_FOUND: UInt16 = 404
```

功能：请求失败，请求所希望得到的资源未被在服务器上发现。

类型：UInt16

### static const STATUS_NOT_IMPLEMENTED

```cangjie
public static const STATUS_NOT_IMPLEMENTED: UInt16 = 501
```

功能：服务器不支持当前请求所需要的某个功能。

类型：UInt16

### static const STATUS_NOT_MODIFIED

```cangjie
public static const STATUS_NOT_MODIFIED: UInt16 = 304
```

功能：请求的资源未修改，服务器返回此状态码时，不会返回任何资源。

类型：UInt16

> **说明：**
>
> 客户端通常会缓存访问过的资源，通过提供一个头信息指出客户端希望只返回在指定日期之后修改的资源。

### static const STATUS_NO_CONTENT

```cangjie
public static const STATUS_NO_CONTENT: UInt16 = 204
```

功能：服务器成功处理，但未返回内容。

类型：UInt16

### static const STATUS_OK

```cangjie
public static const STATUS_OK: UInt16 = 200
```

功能：请求已经成功，请求所希望的响应头或数据体将随此响应返回。

类型：UInt16

### static const STATUS_PARTIAL_CONTENT

```cangjie
public static const STATUS_PARTIAL_CONTENT: UInt16 = 206
```

功能：服务器已经成功处理了部分 GET 请求。

类型：UInt16