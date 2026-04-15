### func noProxy()

```cangjie
public func noProxy(): ClientBuilder
```

功能：调用此函数后，客户端不使用任何代理。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func poolSize(Int64)

```cangjie
public func poolSize(size: Int64): ClientBuilder
```

功能：配置 HTTP/1.1 客户端使用的连接池的大小，亦可表示对同一个主机（host:port）同时存在的连接数的最大值。

参数：

- size: Int64 - 默认 10，poolSize 需要大于 0。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) - 如果传参小于等于 0，则会抛出该异常。

### func readTimeout(Duration)

```cangjie
public func readTimeout(timeout: Duration): ClientBuilder
```

功能：设定客户端读取一个响应的最大时长。

参数：

- timeout: Duration - 默认 15s，Duration.Max 代表不限制，如果传入负的 Duration 将被替换为 Duration.Zero。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func tlsConfig(TlsClientConfig)

```cangjie
public func tlsConfig(config: TlsClientConfig): ClientBuilder
```

功能：设置 TLS 层配置，默认不对其进行设置。

参数：

- config: [TlsClientConfig](../../tls/tls_package_api/tls_package_structs.md#struct-tlsclientconfig) - 设定支持 tls 客户端需要的配置信息。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。

### func writeTimeout(Duration)

```cangjie
public func writeTimeout(timeout: Duration): ClientBuilder
```

功能：设定客户端发送一个请求的最大时长。

参数：

- timeout: Duration - 默认 15 秒，Duration.Max 代表不限制，如果传入负的 Duration 将被替换为 Duration.Zero。

返回值：

- [ClientBuilder](http_package_classes.md#class-clientbuilder) - 当前 [ClientBuilder](http_package_classes.md#class-clientbuilder) 实例的引用。