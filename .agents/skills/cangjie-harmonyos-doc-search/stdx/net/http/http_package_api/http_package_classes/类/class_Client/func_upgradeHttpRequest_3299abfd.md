### func upgrade(HttpRequest)

```cangjie
public func upgrade(req: HttpRequest): (HttpResponse, ?StreamingSocket)
```

功能：发送请求并升级协议，用户设置请求头，返回升级后的连接（如果升级成功），连接由用户负责关闭。

> **说明：**
>
> - 服务器返回 101 表示升级成功，获取到了 StreamingSocket；
> - 必选请求头：
>     - Upgrade:  protocol-name ["/" protocol-version]；
>     - Connection: Upgrade（在请求头包含 Upgrade 字段时会自动添加）；
> - 不支持 HTTP/1.0、HTTP/2；
> - 不支持 HTTP/1.1 CONNECT 方法的 [HttpRequest](http_package_classes.md#class-httprequest)。

参数：

- req: [HttpRequest](http_package_classes.md#class-httprequest) - 升级时发送的请求。

返回值：

- ([HttpResponse](http_package_classes.md#class-httpresponse),?StreamingSocket) - 返回一个元组，[HttpResponse](http_package_classes.md#class-httpresponse) 实例表示服务器返回的响应，?StreamingSocket 实例表示获取的底层连接，升级失败时为 None。

异常：

- [HttpException](http_package_exceptions.md#class-httpexception) -
    - 请求报文或响应报文不符合协议；
    - 请求报文不含 Upgrade 头；
    - 发送 CONNECT 请求；
    - 发送带 body 的 TRACE 请求；
- SocketException，[ConnectionException](http_package_exceptions.md#class-connectionexception) - Socket 连接出现异常或被关闭；
- SocketTimeoutException - Socket 连接超时；
- [TlsException](../../tls/tls_package_api/tls_package_exceptions.md#class-tlsexception) - Tls 连接建立失败或通信异常。