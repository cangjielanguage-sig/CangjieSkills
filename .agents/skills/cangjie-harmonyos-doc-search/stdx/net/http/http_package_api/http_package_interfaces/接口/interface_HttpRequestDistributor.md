## interface HttpRequestDistributor

```cangjie
public interface HttpRequestDistributor {
    func register(path: String, handler: HttpRequestHandler): Unit
    func register(path: String, handler: (HttpContext) -> Unit): Unit
    func distribute(path: String): HttpRequestHandler
}
```

功能：Http request 分发器接口，将一个 request 按照 url 中的 path 分发给对应的 [HttpRequestHandler](http_package_interfaces.md#interface-httprequesthandler) 处理。

> **说明：**
>
> 本实现提供一个默认的 [HttpRequestDistributor](http_package_interfaces.md#interface-httprequestdistributor)，该 distributor 非线程安全。
> 且只能在启动 server 前 register，启动后再次 register，结果未定义。
> 如果用户希望在启动 server 后还能够 register，需要自己提供一个线程安全的 [HttpRequestDistributor](http_package_interfaces.md#interface-httprequestdistributor) 实现。

### func distribute(String)

```cangjie
func distribute(path: String): HttpRequestHandler
```

功能：分发请求处理器，未找到对应请求处理器时，将返回 [NotFoundHandler](http_package_classes.md#class-notfoundhandler) 以返回 404 状态码。

参数：

- path: String - 请求路径。

返回值：

- [HttpRequestHandler](http_package_interfaces.md#interface-httprequesthandler) - 返回请求处理器。

### func register(String, (HttpContext) -> Unit)

```cangjie
func register(path: String, handler: (HttpContext) -> Unit): Unit
```

功能：注册请求处理器。

参数：

- path: String - 请求路径。
- handler: ([HttpContext](http_package_classes.md#class-httpcontext)) ->Unit - 请求处理函数。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 请求路径已注册请求处理器。

### func register(String, HttpRequestHandler)

```cangjie
func register(path: String, handler: HttpRequestHandler): Unit
```

功能：注册请求处理器。

参数：

- path: String - 请求路径。
- handler: [HttpRequestHandler](http_package_interfaces.md#interface-httprequesthandler) - 请求处理器。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 请求路径已注册请求处理器。