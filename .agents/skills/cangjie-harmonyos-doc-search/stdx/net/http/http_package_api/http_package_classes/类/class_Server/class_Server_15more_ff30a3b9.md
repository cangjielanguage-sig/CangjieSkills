## class Server

```cangjie
public class Server
```

功能：提供 HTTP 服务的 [Server](http_package_classes.md#class-server) 类。

> **说明：**
>
> - 启动服务，在指定地址及端口等待用户连接、服务用户的 http request；
> - 关闭服务，包括关闭所有已有连接；
> - 提供注册处理 http request 的 handler 的机制，根据注册信息分发 request 到相应的 handler；
> - 提供 tls 证书热机制；
> - 提供 shutdown 回调机制；
> - 通过 [Logger](../../../log/log_package_api/log_package_classes.md#class-logger).level 开启、关闭日志打印，包括按照用户要求打印相应级别的日志；
> - [Server](http_package_classes.md#class-server) 文档中未明确说明支持版本的配置，在 HTTP/1.1 与 HTTP/2 都会生效。

### prop addr

```cangjie
public prop addr: String
```

功能：获取服务端监听地址。

类型：String

### prop distributor

```cangjie
public prop distributor: HttpRequestDistributor
```

功能：获取请求分发器，请求分发器会根据 url 将请求分发给对应的 handler。

类型：[HttpRequestDistributor](http_package_interfaces.md#interface-httprequestdistributor)

### prop enableConnectProtocol

```cangjie
public prop enableConnectProtocol: Bool
```

功能：HTTP/2 专用，用来限制对端发送的报文是否支持通过 connect 方法升级协议，true 表示支持。

类型：Bool

### prop headerTableSize

```cangjie
public prop headerTableSize: UInt32
```

功能：获取服务端 HTTP/2 Hpack 动态表的初始值，默认值为 4096。

类型：UInt32

### prop httpKeepAliveTimeout

```cangjie
public prop httpKeepAliveTimeout: Duration
```

功能：HTTP/1.1 专用，获取服务器设定的保持长连接的超时时间。

类型：Duration

### prop initialWindowSize

```cangjie
public prop initialWindowSize: UInt32
```

功能：HTTP/2 专用，用来限制对端发送的报文 stream 初始流量窗口大小。默认值为 65535 ，取值范围为 0 至 2^31 - 1。

类型：UInt32

### prop listener

```cangjie
public prop listener: ServerSocket
```

功能：获取服务器绑定 socket。

类型：ServerSocket

### prop logger

```cangjie
public prop logger: Logger
```

功能：获取服务器日志记录器，设置 logger.level 将立即生效，记录器应该是线程安全的。

类型：[Logger](../../../log/log_package_api/log_package_classes.md#class-logger)

### prop maxConcurrentStreams

```cangjie
public prop maxConcurrentStreams: UInt32
```

功能：HTTP/2 专用，用来限制连接同时处理的最大请求数量。

类型：UInt32

### prop maxFrameSize

```cangjie
public prop maxFrameSize: UInt32
```

功能：HTTP/2 专用，用来限制对端发送的报文一个帧的最大长度。默认值为 16384. 取值范围为 2^14 至 2^24 - 1。

类型：UInt32

### prop maxHeaderListSize

```cangjie
public prop maxHeaderListSize: UInt32
```

功能：获取客户端支持的 HTTP/2 最大头部（Header）大小。这个大小指的是响应头部中所有头部字段（Header Field）的最大允许长度之和，其中包括所有字段名称（name）的长度、字段值（value）的长度以及每个字段自动添加的伪头开销（通常每个字段会有 32 字节的开销，这包括了 HTTP/2 协议本身为头部字段添加的伪头部信息）。默认情况下，这个最大长度被设置为 UInt32.Max。

类型：UInt32

### prop maxRequestBodySize

```cangjie
public prop maxRequestBodySize: Int64
```

功能：获取服务器设定的读取请求的请求体最大值，仅对于 HTTP/1.1 且未设置 "Transfer-Encoding: chunked" 的请求生效。

类型：Int64

### prop maxRequestHeaderSize

```cangjie
public prop maxRequestHeaderSize: Int64
```

功能：获取服务器设定的读取请求的请求头最大值。仅对 HTTP/1.1 生效，HTTP/2 中有专门的配置 maxHeaderListSize。

类型：Int64

### prop port

```cangjie
public prop port: UInt16
```

功能：获取服务端监听端口。

类型：UInt16