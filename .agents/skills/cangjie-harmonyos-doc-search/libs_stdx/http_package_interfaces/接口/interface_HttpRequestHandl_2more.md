## interface HttpRequestHandler

```cangjie
public interface HttpRequestHandler {
    func handle(ctx: HttpContext): Unit
}
```

功能：Http request 处理器。

http server 端通过 handler 处理来自客户端的 http request；在 handler 中用户可以获取 http request 的详细信息，包括 header、body；在 handler 中，用户可以构造 http response，包括 header、body，并且可以直接发送 response 给客户端，也可交由 server 发送。

用户在构建 http server 时，需手动通过 server 的 [HttpRequestDistributor](http_package_interfaces.md#interface-httprequestdistributor) 注册一个或多个 handler，当一个客户端 http request 被接收，distributor 按照 request 中 url 的 path 分发给对应的 handler 处理。

> **注意：**
>
> 应用程序应注意 DNS 重绑定攻击，即在 handler 的处理逻辑中对 request 中的 Host 请求头的值进行合法性校验，校验该值是否为此应用程序所认可的权威主机名。

### func handle(HttpContext)

```cangjie
func handle(ctx: HttpContext): Unit
```

功能：处理 Http 请求。

参数：

- ctx: [HttpContext](http_package_classes.md#class-httpcontext) - Http 请求上下文。

## interface ProtocolServiceFactory

```cangjie
public interface ProtocolServiceFactory {
    func create(protocol: Protocol, socket: StreamingSocket): ProtocolService
}
```

功能：Http 服务实例工厂，用于生成 `ProtocolService` 实例。

[ServerBuilder](http_package_classes.md#class-serverbuilder) 提供默认的实现。默认实现可用于生成 HTTP/1.1、HTTP/2 的 `ProtocolService` 实例。

### func create(Protocol, StreamingSocket)

```cangjie
func create(protocol: Protocol, socket: StreamingSocket): ProtocolService
```

功能：根据协议创建协议服务实例。

参数：

- protocol: [Protocol](http_package_enums.md#enum-protocol) - 协议版本，如  [HTTP1_0](./http_package_enums.md#enum-protocol)、 [HTTP1_1](./http_package_enums.md#enum-protocol)、 [HTTP2_0](./http_package_enums.md#enum-protocol)。
- socket: StreamingSocket - 来自客户端的套接字。

返回值：

- ProtocolService - 协议服务实例。