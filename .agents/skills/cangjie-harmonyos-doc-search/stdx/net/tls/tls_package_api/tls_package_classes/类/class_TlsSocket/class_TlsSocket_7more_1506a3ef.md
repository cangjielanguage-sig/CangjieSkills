## class TlsSocket

```cangjie
public class TlsSocket <: StreamingSocket & ToString &Equatable<TlsSocket> & Hashable
```

功能：[TlsSocket](tls_package_classes.md#class-tlssocket) 用于在客户端及服务端间创建加密传输通道。

父类型：

- StreamingSocket
- Equatable\<[TlsSocket](#class-tlssocket)>
- Hashable
- ToString

### prop alpnProtocolName

```cangjie
public prop alpnProtocolName: ?String
```

功能：读取协商到的应用层协议名称。

类型：?String

异常：

- [TlsException](tls_package_exceptions.md#class-tlsexception) - 当套接字未完成 TLS 握手或本端 TLS 套接字已关闭时，抛出异常。
- IllegalMemoryException - 当内存申请失败时，抛出异常。

### prop cipherSuite

```cangjie
public prop cipherSuite: CipherSuite
```

功能：握手后协商到的加密套。

> **说明：**
>
> 密码套件包含加密算法，用于消息认证的散列函数，密钥交换算法。

类型：[CipherSuite](tls_package_structs.md#struct-ciphersuite)

异常：

- [TlsException](tls_package_exceptions.md#class-tlsexception) - 当套接字未完成 TLS 握手或本端 TLS 套接字已关闭时，抛出异常。

### prop clientCertificate

```cangjie
public prop clientCertificate: ?Array<X509Certificate>
```

功能：客户端提供的客户端证书。在客户端获取时为本端证书，在服务端获取时为对端证书。

> **注意：**
>
> 获取对端证书时，如果对端没有发送证书，该接口可能获取失败，返回 None，详见 [peerCertificate](./tls_package_classes.md#prop-peercertificate)。

类型：?Array<[X509Certificate](../../../crypto/x509/x509_package_api/x509_package_classes.md#class-x509certificate)>

异常：

- [TlsException](tls_package_exceptions.md#class-tlsexception) - 当套接字未完成 TLS 握手或本端 TLS 套接字已关闭时，抛出异常。

### prop domain

```cangjie
public prop domain: ?String
```

功能：读取协商到的服务端主机名称。

异常：

- [TlsException](tls_package_exceptions.md#class-tlsexception) - 当套接字未完成 TLS 握手或本端 TLS 套接字已关闭时，抛出异常。

类型：?String

### prop localAddress

```cangjie
public override prop localAddress: SocketAddress
```

功能：读取 [TlsSocket](tls_package_classes.md#class-tlssocket) 的本地地址。

类型：SocketAddress

异常：

- SocketException - 本端建连的底层 TCP 套接字关闭，抛出异常。
- [TlsException](tls_package_exceptions.md#class-tlsexception) - 本端配置为 TLS 的套接字已关闭时，抛出异常。

### prop peerCertificate

```cangjie
public prop peerCertificate: ?Array<X509Certificate>
```

功能：获取对端证书。在客户端获取时同 [serverCertificate](./tls_package_classes.md#prop-servercertificate)，在服务端获取时同 [clientCertificate](./tls_package_classes.md#prop-clientcertificate)。

> **注意：**
>
> - 如果握手时没有要求对端发送证书，此处将无法获取对端证书，返回 None。
>
> - 通过 session 机制恢复连接时，双方都不发送证书，该接口行为如下：
>
>     - 在服务端，如果被恢复的原始连接建立时获取了对端证书，服务端将缓存对端证书，并在此处获取到缓存的证书；
>     - 在客户端，不缓存原始连接的对端证书，此处将无法获取对端证书，返回 None。

类型：?Array<[X509Certificate](../../../crypto/x509/x509_package_api/x509_package_classes.md#class-x509certificate)>

异常：

- [TlsException](tls_package_exceptions.md#class-tlsexception) - 当套接字未完成 TLS 握手或本端 TLS 套接字已关闭时，抛出异常。