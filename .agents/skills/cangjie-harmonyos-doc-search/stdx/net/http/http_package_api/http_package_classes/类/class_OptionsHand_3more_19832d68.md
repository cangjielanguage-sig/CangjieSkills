## class OptionsHandler

```cangjie
public class OptionsHandler <: HttpRequestHandler
```

功能：便捷的 Http 处理器，用于处理 OPTIONS 请求。固定返回 "Allow: OPTIONS，GET，HEAD，POST，PUT，DELETE" 响应头。

父类型：

- [HttpRequestHandler](http_package_interfaces.md#interface-httprequesthandler)

### func handle(HttpContext)

```cangjie
public func handle(ctx: HttpContext): Unit
```

功能：处理 Http OPTIONS 请求。

参数：

- ctx: [HttpContext](http_package_classes.md#class-httpcontext) - Http 请求上下文。

## class ProtocolService

```cangjie
public abstract class ProtocolService
```

功能：Http 协议服务实例，为单个客户端连接提供 Http 服务，包括对客户端 request 报文的解析、 request 的分发处理、 response 的发送等。

## class RedirectHandler

```cangjie
public class RedirectHandler <: HttpRequestHandler {
    public init(url: String, code: UInt16)
}
```

功能：便捷的 Http 处理器，用于回复重定向响应。

父类型：

- [HttpRequestHandler](http_package_interfaces.md#interface-httprequesthandler)

### init(String, UInt16)

```cangjie
public init(url: String, code: UInt16)
```

功能：[RedirectHandler](http_package_classes.md#class-redirecthandler) 的构造函数。

参数：

- url: String - 重定向响应中 Location 头部的 url。
- code: UInt16 - 重定向响应的响应码。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - url 为空或响应码不是除 304 以外的 3XX 状态码时抛出异常。

### func handle(HttpContext)

```cangjie
public func handle(ctx: HttpContext): Unit
```

功能：处理 Http 请求，回复重定向响应。

参数：

- ctx: [HttpContext](http_package_classes.md#class-httpcontext) - Http 请求上下文。