## class FuncHandler

```cangjie
public class FuncHandler <: HttpRequestHandler {
    public FuncHandler(let handler: (HttpContext) -> Unit)
}
```

功能：[HttpRequestHandler](http_package_interfaces.md#interface-httprequesthandler) 接口包装类，把单个函数包装成 [HttpRequestHandler](http_package_interfaces.md#interface-httprequesthandler)。

父类型：

- [HttpRequestHandler](http_package_interfaces.md#interface-httprequesthandler)

### FuncHandler((HttpContext) -> Unit)

```cangjie
public FuncHandler(let handler: (HttpContext) -> Unit)
```

功能：[FuncHandler](http_package_classes.md#class-funchandler) 的构造函数。

参数：

- handler: ([HttpContext](http_package_classes.md#class-httpcontext)) -> Unit - 是调用 handle 的处理函数。

### func handle(HttpContext)

```cangjie
public func handle(ctx: HttpContext): Unit
```

功能：处理 Http 请求。

参数：

- ctx: [HttpContext](http_package_classes.md#class-httpcontext) - Http 请求上下文。

## class HttpContext

```cangjie
public class HttpContext
```

功能：Http 请求上下文，作为 [HttpRequestHandler](http_package_interfaces.md#interface-httprequesthandler).handle 函数的参数在服务端使用。

### prop clientCertificate

```cangjie
public prop clientCertificate: ?Array<X509Certificate>
```

功能：获取 Http 客户端证书。

类型：?Array\<[X509Certificate](../../../crypto/x509/x509_package_api/x509_package_classes.md#class-x509certificate)>

### prop request

```cangjie
public prop request: HttpRequest
```

功能：获取 Http 请求。

类型：[HttpRequest](http_package_classes.md#class-httprequest)

### prop responseBuilder

```cangjie
public prop responseBuilder: HttpResponseBuilder
```

功能：获取 Http 响应构建器。

类型：[HttpResponseBuilder](http_package_classes.md#class-httpresponsebuilder)

### func isClosed()

```cangjie
public func isClosed(): Bool
```

功能：使用 HTTP/1.1 协议时，判断 socket 是否已关闭；使用 HTTP/2 协议时，判断 HTTP/2 流是否已关闭。

返回值：

- Bool - 如果 HTTP/1.1 的 socket 或 HTTP/2 的流已关闭，返回 true，否则返回 false。