## class ClientBuilder

```cangjie
public class ClientBuilder {
    public init()
}
```

功能：用于 [Client](http_package_classes.md#class-client) 实例的构建，[Client](http_package_classes.md#class-client) 没有公开的构造函数，用户只能通过 [ClientBuilder](http_package_classes.md#class-clientbuilder) 得到 [Client](http_package_classes.md#class-client) 实例。[ClientBuilder](http_package_classes.md#class-clientbuilder) 文档中未明确说明支持版本的配置，在 HTTP/1.1 与 HTTP/2 都会生效。

> **说明：**
>
> 该类提供了一系列配置参数的函数，配置完成后调用 [build](./http_package_classes.md#func-build) 函数构造出 [Client](./http_package_classes.md#class-client) 实例。配置函数中说明了参数的取值范围，但配置函数本身不做参数合法性校验，[build](./http_package_classes.md#func-build) 时统一进行校验。

### init()

```cangjie
public init()
```

功能：创建新的 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例。

### func autoRedirect(Bool)

```cangjie
public func autoRedirect(auto: Bool): ClientBuilder
```

功能：配置客户端是否会自动进行重定向。重定向会请求 Location 头的资源，协议规定，Location 只能包含一个 URI 引用 Location = URI-reference，详见 [RFC 9110 10.2.2.](https://httpwg.org/specs/rfc9110.html#rfc.section.10.2.2)。304 状态码默认不重定向。

参数：

- auto: Bool - 默认值为 true，即开启自动重定向。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func build()

```cangjie
public func build(): Client
```

功能：构造 [Client](http_package_classes.md#class-client) 实例。

此处会对各参数的值进行检查，如果取值非法，将抛出异常。各参数的取值范围详见设置参数相关的函数。

返回值：

- [Client](http_package_classes.md#class-client) - 用当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例中的配置构建的 [Client](http_package_classes.md#class-client) 实例。

异常：

- IllegalArgumentException - 配置项有非法参数时抛出此异常。

### func connector((SocketAddress) -> StreamingSocket)

```cangjie
public func connector(c: (SocketAddress) -> StreamingSocket): ClientBuilder
```

功能：客户端调用此函数获取到服务器的连接。

参数：

- c: (SocketAddress) ->StreamingSocket - 入参为 SocketAddress 实例，返回值类型为 StreamingSocket 的函数类型。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func cookieJar(?CookieJar)

```cangjie
public func cookieJar(cookieJar: ?CookieJar): ClientBuilder
```

功能：用于存储客户端所有 [Cookie](http_package_classes.md#class-cookie)。

参数：

- cookieJar: ?[CookieJar](http_package_interfaces.md#interface-cookiejar) - 默认使用一个空的 [CookieJar](http_package_interfaces.md#interface-cookiejar)，如果配置为 None 则不会启用 [Cookie](http_package_classes.md#class-cookie)。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func enablePush(Bool)

```cangjie
public func enablePush(enable: Bool): ClientBuilder
```

功能：配置客户端 HTTP/2 是否支持服务器推送。

参数：

- enable: Bool - 默认值 true。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。