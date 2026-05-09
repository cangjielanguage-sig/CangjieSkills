### prop readTimeout

```cangjie
public override mut prop readTimeout: ?Duration
```

功能：读写 [TlsSocket](tls_package_classes.md#class-tlssocket) 的读超时时间。

类型：?Duration

异常：

- SocketException - 本端建连的底层 TCP 套接字关闭，抛出异常。
- [TlsException](tls_package_exceptions.md#class-tlsexception) - 本端配置为 TLS 的套接字已关闭时，抛出异常。
- IllegalArgumentException - 设定的读超时时间为负值时，抛出异常。

### prop remoteAddress

```cangjie
public override prop remoteAddress: SocketAddress
```

功能：读取 [TlsSocket](tls_package_classes.md#class-tlssocket) 的远端地址。

类型：SocketAddress

异常：

- SocketException - 本端建连的底层 TCP 套接字关闭，抛出异常。
- [TlsException](tls_package_exceptions.md#class-tlsexception) - 本端配置为 TLS 的套接字已关闭时，抛出异常。

### prop serverCertificate

```cangjie
public prop serverCertificate: Array<X509Certificate>
```

功能：服务器证书链由服务器提供或在服务器配置中预先配置。在服务端获取时为本端证书，在客户端获取时为对端证书。

>**注意：**
>
> 获取对端证书时，如果对端没有发送证书，该接口可能获取失败，返回 None，详见 [peerCertificate](./tls_package_classes.md#prop-peercertificate)。

类型：Array<[X509Certificate](../../../crypto/x509/x509_package_api/x509_package_classes.md#class-x509certificate)>

异常：

- [TlsException](tls_package_exceptions.md#class-tlsexception) - 当套接字未完成 TLS 握手或本端 TLS 套接字已关闭时，抛出异常。

### prop session

```cangjie
public prop session: ?TlsSession
```

功能：读取 TLS 会话 id ，客户端会在握手成功后捕获当前会话的 id ，可使用该 id 重用该会话，省去 TLS 建立连接的时间。连接建立未成功时，返回 None。

>**说明：**
>
> 服务端不做捕获因此始终为 None。

类型：?[TlsSession](tls_package_structs.md#struct-tlssession)

异常：

- [TlsException](tls_package_exceptions.md#class-tlsexception) - 当套接字未完成 TLS 握手，抛出异常。

### prop socket

```cangjie
public prop socket: StreamingSocket
```

功能：[TlsSocket](tls_package_classes.md#class-tlssocket) 创建所使用的 StreamingSocket。

类型：StreamingSocket

异常：

- [TlsException](tls_package_exceptions.md#class-tlsexception) - 本端配置为 TLS 套接字已关闭时，抛出异常。

### prop tlsVersion

```cangjie
public prop tlsVersion: TlsVersion
```

功能：读取协商到的 TLS 版本。

类型：[TlsVersion](tls_package_enums.md#enum-tlsversion)

异常：

- [TlsException](tls_package_exceptions.md#class-tlsexception) - 当套接字未完成 TLS 握手或本端 TLS 套接字已关闭时，抛出异常。

### prop writeTimeout

```cangjie
public override mut prop writeTimeout: ?Duration
```

功能：读写 [TlsSocket](tls_package_classes.md#class-tlssocket) 的写超时时间。

类型：?Duration

异常：

- SocketException - 本端建连的底层 TCP 套接字关闭，抛出异常。
- [TlsException](tls_package_exceptions.md#class-tlsexception) - 本端配置为 TLS 的套接字已关闭时，抛出异常。
- IllegalArgumentException - 设定的写超时时间为负值时，抛出异常。