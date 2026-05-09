### static const STATUS_PAYMENT_REQUIRED

```cangjie
public static const STATUS_PAYMENT_REQUIRED: UInt16 = 402
```

功能：为了将来可能的需求而预留的状态码。

类型：UInt16

### static const STATUS_PERMANENT_REDIRECT

```cangjie
public static const STATUS_PERMANENT_REDIRECT: UInt16 = 308
```

功能：请求和所有将来的请求应该使用另一个 URI。

类型：UInt16

### static const STATUS_PRECONDITION_FAILED

```cangjie
public static const STATUS_PRECONDITION_FAILED: UInt16 = 412
```

功能：服务器在验证在请求的头字段中给出先决条件时，没能满足其中的一个或多个。

类型：UInt16

### static const STATUS_PRECONDITION_REQUIRED

```cangjie
public static const STATUS_PRECONDITION_REQUIRED: UInt16 = 428
```

功能：客户端发送 HTTP 请求时，必须要满足的一些预设条件。

类型：UInt16

### static const STATUS_PROCESSING

```cangjie
public static const STATUS_PROCESSING: UInt16 = 102
```

功能：处理将被继续执行。

类型：UInt16

### static const STATUS_PROXY_AUTH_REQUIRED

```cangjie
public static const STATUS_PROXY_AUTH_REQUIRED: UInt16 = 407
```

功能：必须在代理服务器上进行身份验证。

类型：UInt16

### static const STATUS_REQUESTED_RANGE_NOT_SATISFIABLE

```cangjie
public static const STATUS_REQUESTED_RANGE_NOT_SATISFIABLE: UInt16 = 416
```

功能：客户端请求的范围无效。

类型：UInt16

> **说明：**
>
> 请求中包含了 `Range` 请求头，并且 `Range` 中指定的任何数据范围都与当前资源的可用范围不重合；
> 同时请求中又没有定义 `If-Range` 请求头。

### static const STATUS_REQUEST_CONTENT_TOO_LARGE

```cangjie
public static const STATUS_REQUEST_CONTENT_TOO_LARGE: UInt16 = 413
```

功能：请求提交的实体数据大小超过了服务器愿意或者能够处理的范围。

类型：UInt16

### static const STATUS_REQUEST_HEADER_FIELDS_TOO_LARGE

```cangjie
public static const STATUS_REQUEST_HEADER_FIELDS_TOO_LARGE: UInt16 = 431
```

功能：请求头字段太大。

类型：UInt16

### static const STATUS_REQUEST_TIMEOUT

```cangjie
public static const STATUS_REQUEST_TIMEOUT: UInt16 = 408
```

功能：请求超时。客户端没有在服务器预备等待的时间内完成一个请求的发送。

类型：UInt16

### static const STATUS_REQUEST_URI_TOO_LONG

```cangjie
public static const STATUS_REQUEST_URI_TOO_LONG: UInt16 = 414
```

功能：求的 URI 长度超过了服务器能够解释的长度。

类型：UInt16

### static const STATUS_RESET_CONTENT

```cangjie
public static const STATUS_RESET_CONTENT: UInt16 = 205
```

功能：服务器成功处理了请求，且没有返回任何内容，希望请求者重置文档视图。

类型：UInt16

### static const STATUS_SEE_OTHER

```cangjie
public static const STATUS_SEE_OTHER: UInt16 = 303
```

功能：对应当前请求的响应可以在另一个 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 上被找到，而且客户端应当采用 GET 的方式访问那个资源。

类型：UInt16

### static const STATUS_SERVICE_UNAVAILABLE

```cangjie
public static const STATUS_SERVICE_UNAVAILABLE: UInt16 = 503
```

功能：临时的服务器维护或者过载。

类型：UInt16

### static const STATUS_SWITCHING_PROTOCOLS

```cangjie
public static const STATUS_SWITCHING_PROTOCOLS: UInt16 = 101
```

功能：服务器已经理解了客户端的请求，并将通过 Upgrade 消息头通知客户端采用不同的协议来完成这个请求。

类型：UInt16

> **说明：**
>
> 在发送完这个响应最后的空行后，服务器将会切换到在 Upgrade 消息头中定义的那些协议。

### static const STATUS_TEAPOT

```cangjie
public static const STATUS_TEAPOT: UInt16 = 418
```

功能：服务端无法处理请求，一个愚弄客户端的状态码，被称为“我是茶壶”错误码，不应被认真对待。

类型：UInt16

### static const STATUS_TEMPORARY_REDIRECT

```cangjie
public static const STATUS_TEMPORARY_REDIRECT: UInt16 = 307
```

功能：临时重定向。

类型：UInt16