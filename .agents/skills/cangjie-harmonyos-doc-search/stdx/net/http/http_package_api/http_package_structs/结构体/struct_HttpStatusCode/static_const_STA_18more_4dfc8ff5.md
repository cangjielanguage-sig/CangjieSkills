### static const STATUS_ACCEPTED

```cangjie
public static const STATUS_ACCEPTED: UInt16 = 202
```

功能：服务器已接受请求，但尚未处理。

类型：UInt16

### static const STATUS_ALREADY_REPORTED

```cangjie
public static const STATUS_ALREADY_REPORTED: UInt16 = 208
```

功能：消息体将是一个 XML 消息。

类型：UInt16

### static const STATUS_BAD_GATEWAY

```cangjie
public static const STATUS_BAD_GATEWAY: UInt16 = 502
```

功能：作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。

类型：UInt16

### static const STATUS_BAD_REQUEST

```cangjie
public static const STATUS_BAD_REQUEST: UInt16 = 400
```

功能：语义有误，当前请求无法被服务器理解；或请求参数有误。

类型：UInt16

### static const STATUS_CONFLICT

```cangjie
public static const STATUS_CONFLICT: UInt16 = 409
```

功能：由于和被请求的资源的当前状态之间存在冲突，请求无法完成。

类型：UInt16

### static const STATUS_CONTINUE

```cangjie
public static const STATUS_CONTINUE: UInt16 = 100
```

功能：这个临时响应是用来通知客户端它的部分请求已经被服务器接收，且仍未被拒绝。

类型：UInt16

> **说明：**
>
> 客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。
> 服务器必须在请求完成后向客户端发送一个最终响应。

### static const STATUS_CREATED

```cangjie
public static const STATUS_CREATED: UInt16 = 201
```

功能：请求已经被实现，而且有一个新的资源已经依据请求的需要而建立，且其 URI 已经随 Location 头信息返回。

类型：UInt16

### static const STATUS_EARLY_HINTS

```cangjie
public static const STATUS_EARLY_HINTS: UInt16 = 103
```

功能：提前预加载 (css、js) 文档。

类型：UInt16

### static const STATUS_EXPECTATION_FAILED

```cangjie
public static const STATUS_EXPECTATION_FAILED: UInt16 = 417
```

功能：服务器无法满足 Expect 的请求头信息。

类型：UInt16

### static const STATUS_FAILED_DEPENDENCY

```cangjie
public static const STATUS_FAILED_DEPENDENCY: UInt16 = 424
```

功能：由于之前的某个请求发生的错误，导致当前请求失败。

类型：UInt16

### static const STATUS_FORBIDDEN

```cangjie
public static const STATUS_FORBIDDEN: UInt16 = 403
```

功能：服务器已经理解请求，但是拒绝执行。

类型：UInt16

### static const STATUS_FOUND

```cangjie
public static const STATUS_FOUND: UInt16 = 302
```

功能：临时移动。

类型：UInt16

> **说明：**
>
> 请求的资源已被临时的移动到新 URI，客户端应当继续向原有地址发送以后的请求。

### static const STATUS_GATEWAY_TIMEOUT

```cangjie
public static const STATUS_GATEWAY_TIMEOUT: UInt16 = 504
```

功能：从上游服务器（URI 标识出的服务器，例如 HTTP、FTP、LDAP）或者辅助服务器（例如 DNS）收到响应超时。

类型：UInt16

### static const STATUS_GONE

```cangjie
public static const STATUS_GONE: UInt16 = 410
```

功能：被请求的资源在服务器上已经不再可用，而且没有任何已知的转发地址。

类型：UInt16

### static const STATUS_HTTP_VERSION_NOT_SUPPORTED

```cangjie
public static const STATUS_HTTP_VERSION_NOT_SUPPORTED: UInt16 = 505
```

功能：服务器不支持，或者拒绝支持在请求中使用的 HTTP 版本。

类型：UInt16

### static const STATUS_IM_USED

```cangjie
public static const STATUS_IM_USED: UInt16 = 226
```

功能：服务器已完成对资源的请求，并且响应是应用于当前实例的一个或多个实例操作的结果的表示。

类型：UInt16

### static const STATUS_INSUFFICIENT_STORAGE

```cangjie
public static const STATUS_INSUFFICIENT_STORAGE: UInt16 = 507
```

功能：服务器无法存储完成请求所必须的内容。

类型：UInt16

### static const STATUS_INTERNAL_SERVER_ERROR

```cangjie
public static const STATUS_INTERNAL_SERVER_ERROR: UInt16 = 500
```

功能：服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。

类型：UInt16