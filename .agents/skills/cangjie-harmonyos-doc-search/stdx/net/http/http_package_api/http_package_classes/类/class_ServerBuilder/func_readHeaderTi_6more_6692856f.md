### func readHeaderTimeout(Duration)

```cangjie
public func readHeaderTimeout(timeout: Duration): ServerBuilder
```

功能：设定服务端读取客户端发送一个请求的请求头最大时长，超过该时长将不再进行读取并关闭连接，默认不进行限制。

参数：

- timeout: Duration - 设定的读请求头超时时间，如果传入负的 Duration 将被替换为 Duration.Zero。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func readTimeout(Duration)

```cangjie
public func readTimeout(timeout: Duration): ServerBuilder
```

功能：设定服务端读取一个请求的最大时长，超过该时长将不再进行读取并关闭连接，默认不进行限制。

参数：

- timeout: Duration - 设定读请求的超时时间，如果传入时间为负值将被替换为 Duration.Zero。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func servicePoolConfig(ServicePoolConfig)

```cangjie
public func servicePoolConfig(cfg: ServicePoolConfig): ServerBuilder
```

功能：服务过程中使用的协程池相关设置，具体说明见 [ServicePoolConfig](http_package_structs.md#struct-servicepoolconfig) 结构体。

参数：

- cfg: [ServicePoolConfig](http_package_structs.md#struct-servicepoolconfig) - 协程池相关设置。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func tlsConfig(TlsServerConfig)

```cangjie
public func tlsConfig(config: TlsServerConfig): ServerBuilder
```

功能：设置 TLS 层配置，默认不对其进行设置。

参数：

- config: [TlsServerConfig](../../tls/tls_package_api/tls_package_structs.md#struct-tlsserverconfig) - 设定支持 tls 服务所需要的配置信息。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func transportConfig(TransportConfig)

```cangjie
public func transportConfig(config: TransportConfig): ServerBuilder
```

功能：设置传输层配置，默认配置详见 [TransportConfig](http_package_structs.md#struct-transportconfig) 结构体说明。

参数：

- config: [TransportConfig](http_package_structs.md#struct-transportconfig) - 设定的传输层配置信息。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。

### func writeTimeout(Duration)

```cangjie
public func writeTimeout(timeout: Duration): ServerBuilder
```

功能：设定服务端发送一个响应的最大时长，超过该时长将不再进行写入并关闭连接，默认不进行限制。

参数：

- timeout: Duration - 设定写响应的超时时间，如果传入时间为负值将被替换为 Duration.Zero。

返回值：

- [ServerBuilder](http_package_classes.md#class-serverbuilder) - 当前 [ServerBuilder](http_package_classes.md#class-serverbuilder) 的引用。