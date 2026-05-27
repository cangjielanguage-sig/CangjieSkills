### func headerTableSize(UInt32)

```cangjie
public func headerTableSize(size: UInt32): ClientBuilder
```

功能：配置客户端 HTTP/2 Hpack 动态表初始值。

参数：

- size: UInt32 - 默认值 4096。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func httpProxy(String)

```cangjie
public func httpProxy(addr: String): ClientBuilder
```

功能：设置客户端 http 代理，默认使用系统环境变量 http_proxy 的值。

参数：

- addr: String - 格式为：`"http://host:port"`，例如：`"http://192.168.1.1:80"`。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func httpsProxy(String)

```cangjie
public func httpsProxy(addr: String): ClientBuilder
```

功能：设置客户端 https 代理，默认使用系统环境变量 https_proxy 的值。

参数：

- addr: String - 格式为：`"http://host:port"`，例如：`"http://192.168.1.1:443"`。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func initialWindowSize(UInt32)

```cangjie
public func initialWindowSize(size: UInt32): ClientBuilder
```

功能：配置客户端 HTTP/2 流控窗口初始值。

参数：

- size: UInt32 - 默认值 65535 ， 取值范围为 0 至 2^31 - 1。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func logger(Logger)

```cangjie
public func logger(logger: Logger): ClientBuilder
```

功能：设定客户端的 logger，默认 logger 级别为 INFO，logger 内容将写入 Console.stdout。

参数：

- logger: [Logger](../../../log/log_package_api/log_package_classes.md#class-logger) - 需要是线程安全的，默认使用内置线程安全 logger。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func maxConcurrentStreams(UInt32)

```cangjie
public func maxConcurrentStreams(size: UInt32): ClientBuilder
```

功能：配置客户端 HTTP/2 初始最大并发流数量。

参数：

- size: UInt32 - 默认值为 2^31 - 1。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func maxFrameSize(UInt32)

```cangjie
public func maxFrameSize(size: UInt32): ClientBuilder
```

功能：配置客户端 HTTP/2 初始最大帧大小。

参数：

- size: UInt32 - 默认值为 16384。取值范围为 2^14 至 2^24 - 1。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func maxHeaderListSize(UInt32)

```cangjie
public func maxHeaderListSize(size: UInt32): ClientBuilder
```

功能：获取客户端支持的 HTTP/2 最大头部（Header）大小。这个大小指的是响应头部中所有头部字段（Header Field）的最大允许长度之和，其中包括所有字段名称（name）的长度、字段值（value）的长度以及每个字段自动添加的伪头开销（通常每个字段会有 32 字节的开销，这包括了 HTTP/2 协议本身为头部字段添加的伪头部信息）。默认情况下，这个最大长度被设置为 UInt32.Max。

参数：

- size: UInt32 - 客户端接收的 HTTP/2 响应 headers 最大长度。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。