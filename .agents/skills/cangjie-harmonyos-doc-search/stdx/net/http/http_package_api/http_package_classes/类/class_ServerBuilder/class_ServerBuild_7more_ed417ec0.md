## class ServerBuilder

```cangjie
public class ServerBuilder {
    public init()
}
```

功能：提供 [Server](http_package_classes.md#class-server) 实例构建器。

支持通过如下参数构造一个 Http [Server](http_package_classes.md#class-server)：

- 地址、端口；
- 线程安全的 logger；
- [HttpRequestDistributor](http_package_interfaces.md#interface-httprequestdistributor)，用于注册 handler、分发 request；
- HTTP/2 的 settings；
- shutdown 回调；
- transport：listener、连接及其配置；
- protocol service：http 协议解析服务；

除地址端口、shutdown 回调外，均提供默认实现，用户在构造 server 过程中可不指定其他构建参数。
[ServerBuilder](http_package_classes.md#class-serverbuilder) 文档中未明确说明支持版本的配置，在 HTTP/1.1 与 HTTP/2 都会生效。

> **说明：**
>
> 该类提供了一系列配置参数的函数，配置完成后调用 [build](./http_package_classes.md#func-build-3) 函数构造出 [Server](./http_package_classes.md#class-server) 实例。配置函数中说明了参数的取值范围，但配置函数本身不做参数合法性校验，[build](./http_package_classes.md#func-build-3) 时统一进行校验。

### init()

```cangjie
public init()
```

功能：创建 [ServerBuilder](http_package_classes.md#class-serverbuilder) 实例。

### func addr(String)

```cangjie
public func addr(addr: String): ServerBuilder
```

功能：设置服务端监听地址，若 listener 被设定，此值被忽略。

格式需符合 IPAddress 中相关规定。

参数：

- addr: String - 地址值。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func afterBind(()->Unit)

```cangjie
public func afterBind(f: ()->Unit): ServerBuilder
```

功能：注册服务器启动时的回调函数，服务内部 ServerSocket 实例 bind 之后，accept 之前将调用该函数。重复调用将覆盖之前注册的函数。

参数：

- f: () ->Unit - 回调函数，入参为空，返回值为 Unit 类型。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func build()

```cangjie
public func build(): Server
```

功能：根据设置的参数构建 [Server](http_package_classes.md#class-server) 实例。

此处会对各参数的值进行检查，如果取值非法，将抛出异常。各参数的取值范围详见设置参数相关的函数。

返回值：

- [Server](http_package_classes.md#class-server) - 生成的 [Server](http_package_classes.md#class-server) 实例。

异常：

- IllegalArgumentException - 当设置的参数非法时，抛出异常。
- IllegalFormatException 格式错误时，抛出异常。

### func distributor(HttpRequestDistributor)

```cangjie
public func distributor(distributor: HttpRequestDistributor): ServerBuilder
```

功能：设置请求分发器，请求分发器会根据 url 将请求分发给对应的 handler。不设置时使用默认请求分发器。

参数：

- distributor: [HttpRequestDistributor](http_package_interfaces.md#interface-httprequestdistributor) - 自定义请求分发器实例。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func enableConnectProtocol(Bool)

```cangjie
public func enableConnectProtocol(flag: Bool): ServerBuilder
```

功能：HTTP/2 专用，设置本端是否接收 CONNECT 请求，默认 false。

参数：

- flag: Bool - 本端是否接收 CONNECT 请求。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。