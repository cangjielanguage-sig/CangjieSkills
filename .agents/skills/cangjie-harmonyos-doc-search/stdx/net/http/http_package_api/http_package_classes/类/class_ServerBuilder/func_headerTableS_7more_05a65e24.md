### func headerTableSize(UInt32)

```cangjie
public func headerTableSize(size: UInt32): ServerBuilder
```

功能：设置服务端 HTTP/2 Hpack 动态表的初始值，默认值为 4096。

参数：

- size: UInt32 - 本端对响应头编码时使用的最大 `table size`

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func httpKeepAliveTimeout(Duration)

```cangjie
public func httpKeepAliveTimeout(timeout: Duration): ServerBuilder
```

功能：HTTP/1.1 专用，设定服务端连接保活时长，该时长内客户端未再次发送请求，服务端将关闭长连接，默认不进行限制。

参数：

- timeout: Duration - 设定保持长连接的超时时间，如果传入负的 Duration 将被替换为 Duration.Zero。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func initialWindowSize(UInt32)

```cangjie
public func initialWindowSize(size: UInt32): ServerBuilder
```

功能：HTTP/2 专用，设置当前服务器上每个流的接收报文的初始流量窗口大小，默认值为 65535。取值范围为 0 至 2^31 - 1。

参数：

- size: UInt32 - 本端一个 stream 上接收报文的初始流量窗口大小。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func listener(ServerSocket)

```cangjie
public func listener(listener: ServerSocket): ServerBuilder
```

功能：服务端调用此函数对指定 socket 进行绑定监听。

参数：

- listener: ServerSocket - 所绑定的 socket。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func logger(Logger)

```cangjie
public func logger(logger: Logger): ServerBuilder
```

功能：设定服务器的 logger，默认 logger 级别为 INFO，logger 内容将写入 Console.stdout。

参数：

- logger: [Logger](../../../log/log_package_api/log_package_classes.md#class-logger) - 需要是线程安全的，默认使用内置线程安全 logger。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func maxConcurrentStreams(UInt32)

```cangjie
public func maxConcurrentStreams(size: UInt32): ServerBuilder
```

功能：HTTP/2 专用，设置本端同时处理的最大请求数量，限制对端并发发送请求的数量，默认值为 100。

参数：

- size: UInt32 - 本端同时处理的最大请求数量。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func maxFrameSize(UInt32)

```cangjie
public func maxFrameSize(size: UInt32): ServerBuilder
```

功能：HTTP/2 专用，设置本端接收的一个帧的最大长度，用来限制对端发送帧的长度，默认值为 16384. 取值范围为 2^14 至 2^24 - 1。

参数：

- size: UInt32 - 本端接收的一个帧的最大长度。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。