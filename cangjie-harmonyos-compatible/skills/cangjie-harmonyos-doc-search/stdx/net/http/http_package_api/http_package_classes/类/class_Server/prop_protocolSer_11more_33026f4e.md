### prop protocolServiceFactory

```cangjie
public prop protocolServiceFactory: ProtocolServiceFactory
```

功能：获取协议服务工厂，服务协议工厂会生成每个协议所需的服务实例。

类型：[ProtocolServiceFactory](http_package_interfaces.md#interface-protocolservicefactory)

### prop readHeaderTimeout

```cangjie
public prop readHeaderTimeout: Duration
```

功能：获取服务器设定的读取请求头的超时时间。

类型：Duration

### prop readTimeout

```cangjie
public prop readTimeout: Duration
```

功能：获取服务器设定的读取整个请求的超时时间。

类型：Duration

### prop servicePoolConfig

```cangjie
public prop servicePoolConfig: ServicePoolConfig
```

功能：获取协程池配置实例。

类型：[ServicePoolConfig](http_package_structs.md#struct-servicepoolconfig)

### prop transportConfig

```cangjie
public prop transportConfig: TransportConfig
```

功能：获取服务器设定的传输层配置。

类型：[TransportConfig](http_package_structs.md#struct-transportconfig)

### prop writeTimeout

```cangjie
public prop writeTimeout: Duration
```

功能：获取服务器设定的写响应的超时时间。

类型：Duration

### func afterBind(() -> Unit)

```cangjie
public func afterBind(f: ()-> Unit): Unit
```

功能：注册服务器启动时的回调函数，服务内部 ServerSocket 实例 bind 之后，accept 之前将调用该函数。重复调用将覆盖之前注册的函数。

参数：

- f: () -> Unit - 回调函数，入参为空，返回值为 Unit 类型。

### func close()

```cangjie
public func close(): Unit
```

功能：关闭服务器，服务器关闭后将不再对请求进行读取与处理，重复关闭将只有第一次生效（包括 close 和 closeGracefully）。

### func closeGracefully()

```cangjie
public func closeGracefully(): Unit
```

功能：关闭服务器，服务器关闭后将不再对请求进行读取，当前正在进行处理的服务器待处理结束后进行关闭。

### func getTlsConfig()

```cangjie
public func getTlsConfig(): ?TlsServerConfig
```

功能：获取服务器设定的 TLS 层配置。

返回值：

- ?[TlsServerConfig](../../tls/tls_package_api/tls_package_structs.md#struct-tlsserverconfig) - 服务端设定的 TLS 层配置，如果没有设置则返回 None。

### func onShutdown(() -> Unit)

```cangjie
public func onShutdown(f: () -> Unit): Unit
```

功能：注册服务器关闭时的回调函数，服务器关闭时将调用该回调函数，重复调用将覆盖之前注册的函数。

参数：

- f: () -> Unit - 回调函数，入参为空，返回值为 Unit 类型。