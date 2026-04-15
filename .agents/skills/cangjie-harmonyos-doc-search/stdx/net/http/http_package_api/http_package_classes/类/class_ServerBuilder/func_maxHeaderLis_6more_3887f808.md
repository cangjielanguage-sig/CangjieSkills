### func maxHeaderListSize(UInt32)

```cangjie
public func maxHeaderListSize(size: UInt32): ServerBuilder
```

功能：获取客户端支持的 HTTP/2 最大头部（Header）大小。这个大小指的是响应头部中所有头部字段（Header Field）的最大允许长度之和，其中包括所有字段名称（name）的长度、字段值（value）的长度以及每个字段自动添加的伪头开销（通常每个字段会有 32 字节的开销，这包括了 HTTP/2 协议本身为头部字段添加的伪头部信息）。默认情况下，这个最大长度被设置为 UInt32.Max。

参数：

- size: UInt32 - 本端接收的报文头最大长度。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func maxRequestBodySize(Int64)

```cangjie
public func maxRequestBodySize(size: Int64): ServerBuilder
```

功能：设置服务端允许客户端发送单个请求的请求体最大长度，请求体长度超过该值时，将返回状态码为 413 的响应。默认值为 2M。仅对于 HTTP/1.1 且未设置 "Transfer-Encoding: chunked" 的请求生效。

参数：

- size: Int64 - 设定允许接收请求的请求体大小最大值，值为 0 代表不作限制。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

异常：

- IllegalArgumentException - 当入参 size < 0 时，抛出异常。

### func maxRequestHeaderSize(Int64)

```cangjie
public func maxRequestHeaderSize(size: Int64): ServerBuilder
```

功能：设定服务端允许客户端发送单个请求的请求头最大长度，请求头长度超过该值时，将返回状态码为 431 的响应；仅对 HTTP/1.1 生效，HTTP/2 中有专门的配置 maxHeaderListSize。

参数：

- size: Int64 - 设定允许接收请求的请求头大小最大值，值为 0 代表不作限制。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

异常：

- IllegalArgumentException - 当入参 size < 0 时，抛出异常。

### func onShutdown(() -> Unit)

```cangjie
public func onShutdown(f: () -> Unit): ServerBuilder
```

功能：注册服务器关闭时的回调函数，服务器关闭时将调用该回调函数，重复调用将覆盖之前注册的函数。

参数：

- f: () ->Unit - 回调函数，入参为空，返回值为 Unit 类型。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func port(UInt16)

```cangjie
public func port(port: UInt16): ServerBuilder
```

功能：设置服务端监听端口，若 listener 被设定，此值被忽略。

参数：

- port: UInt16 - 端口值。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func protocolServiceFactory(ProtocolServiceFactory)

```cangjie
public func protocolServiceFactory(factory: ProtocolServiceFactory): ServerBuilder
```

功能：设置协议服务工厂，服务协议工厂会生成每个协议所需的服务实例，不设置时使用默认工厂。

参数：

- factory: [ProtocolServiceFactory](http_package_interfaces.md#interface-protocolservicefactory) - 自定义工厂实例。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。