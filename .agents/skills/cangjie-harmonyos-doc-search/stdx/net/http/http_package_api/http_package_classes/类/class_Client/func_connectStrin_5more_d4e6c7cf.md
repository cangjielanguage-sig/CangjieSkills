### func connect(String, HttpHeaders, Protocol)

```cangjie
public func connect(url: String, header!: HttpHeaders = HttpHeaders(), version!: Protocol = HTTP1_1): (HttpResponse, ?StreamingSocket)
```

功能：发送 CONNECT 请求与服务器建立隧道，返回建连成功后的连接，连接由用户负责关闭。服务器返回 2xx 表示建连成功，否则建连失败（不支持自动重定向，3xx 也视为失败）。

参数：

- url: String - 请求的 url。
- header!: [HttpHeaders](http_package_classes.md#class-httpheaders) - 请求头，默认为空请求头。
- version!: [Protocol](http_package_enums.md#enum-protocol) - 请求的协议，默认为 [HTTP1_1](./http_package_enums.md#enum-protocol)。

返回值：

- ([HttpResponse](http_package_classes.md#class-httpresponse), ?StreamingSocket) - 返回元组类型，其中 [HttpResponse](http_package_classes.md#class-httpresponse) 实例表示服务器返回的响应体，Option\<StreamingSocket> 实例表示请求成功时返回 headers 之后连接。

异常：

- [UrlSyntaxException](../../../encoding/url/url_package_api/url_package_exceptions.md#class-urlsyntaxexception) - 当参数 url 不符合 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 解析规范时，抛出异常。
- IllegalArgumentException - 当被编码的字符不符合 UTF-8 的字节序列规则时，抛出异常。
- 其余同 func send。

### func delete(String)

```cangjie
public func delete(url: String): HttpResponse
```

功能：请求方法为 DELETE 的便捷请求函数。

参数：

- url: String - 请求的 url。

返回值：

- [HttpResponse](http_package_classes.md#class-httpresponse) - 服务端返回的响应。

异常：

- [UrlSyntaxException](../../../encoding/url/url_package_api/url_package_exceptions.md#class-urlsyntaxexception) - 当参数 url 不符合 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 解析规范时，抛出异常。
- IllegalArgumentException - 当被编码的字符不符合 UTF-8 的字节序列规则时，抛出异常。
- 其余同 func send。

### func get(String)

```cangjie
public func get(url: String): HttpResponse
```

功能：请求方法为 GET 的便捷请求函数。

参数：

- url: String - 请求的 url。

返回值：

- [HttpResponse](http_package_classes.md#class-httpresponse) - 服务端返回的响应。

异常：

- [UrlSyntaxException](../../../encoding/url/url_package_api/url_package_exceptions.md#class-urlsyntaxexception) - 当参数 url 不符合 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 解析规范时，抛出异常。
- IllegalArgumentException - 当被编码的字符不符合 UTF-8 的字节序列规则时，抛出异常。
- 其余同 func send。

### func getTlsConfig()

```cangjie
public func getTlsConfig(): ?TlsClientConfig
```

功能：获取客户端设定的 TLS 层配置。

返回值：

- ?[TlsClientConfig](../../tls/tls_package_api/tls_package_structs.md#struct-tlsclientconfig) - 客户端设定的 TLS 层配置，如果没有设置则返回 None。

### func head(String)

```cangjie
public func head(url: String): HttpResponse
```

功能：请求方法为 HEAD 的便捷请求函数。

参数：

- url: String - 请求的 url。

返回值：

- [HttpResponse](http_package_classes.md#class-httpresponse) - 服务端返回的响应。

异常：

- [UrlSyntaxException](../../../encoding/url/url_package_api/url_package_exceptions.md#class-urlsyntaxexception) - 当参数 url 不符合 [URL](../../../encoding/url/url_package_api/url_package_classes.md#class-url) 解析规范时，抛出异常。
- IllegalArgumentException - 当被编码的字符不符合 UTF-8 的字节序列规则时，抛出异常。
- 其余同 func send。