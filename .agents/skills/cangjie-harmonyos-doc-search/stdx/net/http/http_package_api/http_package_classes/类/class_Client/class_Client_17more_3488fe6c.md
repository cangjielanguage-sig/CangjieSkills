## class Client

```cangjie
public class Client
```

功能：发送 Http request、随时关闭等。用户可以通过 Client 实例发送 HTTP/1.1 或 HTTP/2 请求。

> **说明：**
>
> [Client](http_package_classes.md#class-client) 文档中未明确说明支持版本的配置，在 HTTP/1.1 与 HTTP/2 都会生效。

### prop autoRedirect

```cangjie
public prop autoRedirect: Bool
```

功能：客户端是否会自动进行重定向，304 状态码默认不重定向。

类型：Bool

### prop connector

```cangjie
public prop connector: (SocketAddress) -> StreamingSocket
```

功能：客户端调用此函数获取到服务器的连接。

类型：(SocketAddress) -> StreamingSocket

### prop cookieJar

```cangjie
public prop cookieJar: ?CookieJar
```

功能：用于存储客户端所有 [Cookie](http_package_classes.md#class-cookie)，如果配置为 None，则不会启用 [Cookie](http_package_classes.md#class-cookie)。

类型：?[CookieJar](http_package_interfaces.md#interface-cookiejar)

### prop enablePush

```cangjie
public prop enablePush: Bool
```

功能：客户端 HTTP/2 是否支持服务器推送，默认值为 true。

类型：Bool

### prop headerTableSize

```cangjie
public prop headerTableSize: UInt32
```

功能：获取客户端 HTTP/2 Hpack 动态表的初始值，默认值为 4096。

类型：UInt32

### prop httpProxy

```cangjie
public prop httpProxy: String
```

功能：获取客户端 http 代理，默认使用系统环境变量 http_proxy 的值，用字符串表示，格式为：`"http://host:port"`，例如：`"http://192.168.1.1:80"`。

类型：String

### prop httpsProxy

```cangjie
public prop httpsProxy: String
```

功能：获取客户端 https 代理，默认使用系统环境变量 https_proxy 的值，用字符串表示，格式为：`"http://host:port"`，例如：`"http://192.168.1.1:443"`。

类型：String

### prop initialWindowSize

```cangjie
public prop initialWindowSize: UInt32
```

功能：获取客户端 HTTP/2 流控窗口初始值，默认值为 65535 ，取值范围为 0 至 2^31 - 1。

类型：UInt32

### prop logger

```cangjie
public prop logger: Logger
```

功能：获取客户端日志记录器，设置 logger.level 将立即生效，记录器应该是线程安全的。

类型：[Logger](../../../log/log_package_api/log_package_classes.md#class-logger)

### prop maxConcurrentStreams

```cangjie
public prop maxConcurrentStreams: UInt32
```

功能：获取客户端 HTTP/2 初始最大并发流数量，默认值为 2^31 - 1。

类型：UInt32

### prop maxFrameSize

```cangjie
public prop maxFrameSize: UInt32
```

功能：获取客户端 HTTP/2 初始最大帧大小。默认值为 16384. 取值范围为 2^14 至 2^24 - 1。

类型：UInt32

### prop maxHeaderListSize

```cangjie
public prop maxHeaderListSize: UInt32
```

功能：获取客户端支持的 HTTP/2 最大头部（Header）大小。这个大小指的是响应头部中所有头部字段（Header Field）的最大允许长度之和，其中包括所有字段名称（name）的长度、字段值（value）的长度以及每个字段自动添加的伪头开销（通常每个字段会有 32 字节的开销，这包括了 HTTP/2 协议本身为头部字段添加的伪头部信息）。默认情况下，这个最大长度被设置为 UInt32.Max。

类型：UInt32

### prop poolSize

```cangjie
public prop poolSize: Int64
```

功能：配置 HTTP/1.1 客户端使用的连接池的大小，亦可表示对同一个主机（host:port）同时存在的连接数的最大值。

类型：Int64

### prop readTimeout

```cangjie
public prop readTimeout: Duration
```

功能：获取客户端设定的读取整个响应的超时时间，默认值为 15 秒。

类型：Duration

### prop writeTimeout

```cangjie
public prop writeTimeout: Duration
```

功能：获取客户端设定的写请求的超时时间，默认值为 15 秒。

类型：Duration

### func close()

```cangjie
public func close(): Unit
```

功能：关闭客户端建立的所有连接，调用后不能继续发送请求。