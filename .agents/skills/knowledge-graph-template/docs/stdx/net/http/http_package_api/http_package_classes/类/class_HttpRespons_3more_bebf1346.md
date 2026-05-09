## class HttpResponsePusher

```cangjie
public class HttpResponsePusher
```

功能：HTTP/2 服务器推送。

> **说明：**
>
> 如果服务器收到请求后，认为客户端后续还需要某些关联资源，可以将其提前推送到客户端；
> 服务端推送包括推送请求和推送响应；
> 启用服务端推送需要先调用 push 函数发送推送请求，并向服务器注册该请求对应的 handler，用以生成推送响应；
> 客户端可设置拒绝服务端推送；
> 不允许嵌套推送，即不允许在推送请求对应的 handler 中再次推送。嵌套推送情况下，服务端将不执行推送，并打印日志进行提示。

### static func getPusher(HttpContext)

```cangjie
public static func getPusher(ctx: HttpContext): ?HttpResponsePusher
```

功能：获取 [HttpResponsePusher](http_package_classes.md#class-httpresponsepusher) 实例，如果客户端拒绝推送，将返回 None。

参数：

- ctx: [HttpContext](#class-httpcontext) - Http 请求上下文。

返回值：

- ?[HttpResponsePusher](http_package_classes.md#class-httpresponsepusher) - 获得的 [HttpResponsePusher](http_package_classes.md#class-httpresponsepusher)。

### func push(String, String, HttpHeaders)

```cangjie
public func push(path: String, method: String, header: HttpHeaders): Unit
```

功能：向客户端发送推送请求，path 为请求地址，method 为请求方法，header 为请求头。

参数：

- path: String - 推送的请求地址。
- method: String - 推送的请求方法。
- header: [HttpHeaders](#class-httpheaders) - 推送的请求头。

## class HttpResponseWriter

```cangjie
public class HttpResponseWriter {
    public HttpResponseWriter(let ctx: HttpContext)
}
```

功能：HTTP response 消息体 Writer，支持用户控制消息体的发送过程。

> **说明：**
>
> 第一次调用 write 函数时，将立即发送 header 和通过参数传入的 body，此后每次调用 write，发送通过参数传入的 body。
> 对于 HTTP/1.1，如果设置了 transfer-encoding: chunked，用户每调用一次 write，将发送一个 chunk。
> 对于 HTTP/2，用户每调用一次 write，将把指定数据封装并发出。

### HttpResponseWriter(HttpContext)

```cangjie
public HttpResponseWriter(let ctx: HttpContext)
```

功能：构造一个 [HttpResponseWriter](http_package_classes.md#class-httpresponsewriter) 实例。

参数：

- ctx: [HttpContext](#class-httpcontext) - Http 请求上下文。

### func write(Array\<Byte>)

```cangjie
public func write(buf: Array<Byte>): Unit
```

功能：发送 buf 中数据到客户端。

参数：

- buf: Array\<Byte> - 要发送的数据。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 请求方法为 "HEAD" 或响应状态码为 "1XX\204\304"。
- [HttpException](http_package_exceptions.md#class-httpexception) - 连接关闭。
- [HttpException](http_package_exceptions.md#class-httpexception) - response 协议版本为 HTTP/1.0。
- [HttpException](http_package_exceptions.md#class-httpexception) - 响应连接已升级为 [WebSocket](http_package_classes.md#class-websocket)。

## class NotFoundHandler

```cangjie
public class NotFoundHandler <: HttpRequestHandler
```

功能：便捷的 Http 请求处理器，`404 Not Found` 处理器。

父类型：

- [HttpRequestHandler](http_package_interfaces.md#interface-httprequesthandler)

### func handle(HttpContext)

```cangjie
public func handle(ctx: HttpContext): Unit
```

功能：处理 Http 请求，回复 404 响应。

参数：

- ctx: [HttpContext](http_package_classes.md#class-httpcontext) - Http 请求上下文。