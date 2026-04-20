## struct TlsServerConfig

```cangjie
public struct TlsServerConfig {
    public var clientIdentityRequired: TlsClientIdentificationMode = Disabled
    public var keylogCallback: ?(TlsSocket, String) -> Unit = None
    public var verifyMode: CertificateVerifyMode = CertificateVerifyMode.Default
    public init(certChain: Array<X509Certificate>, certKey: PrivateKey)
}
```

功能：服务端配置。

### var clientIdentityRequired

```cangjie
public var clientIdentityRequired: TlsClientIdentificationMode = Disabled
```

功能：设置或获取服务端要求客户端的认证模式，默认值为不要求客户端认证服务端证书，也不要求客户端发送本端证书。

类型：[TlsClientIdentificationMode](tls_package_enums.md#enum-tlsclientidentificationmode)

### var keylogCallback

```cangjie
public var keylogCallback: ?(TlsSocket, String) -> Unit = None
```

功能：握手过程的回调函数，提供 TLS 初始秘钥数据，用于调试和解密记录使用。

类型：?([TlsSocket](tls_package_classes.md#class-tlssocket), String) -> Unit

### var verifyMode

```cangjie
public var verifyMode: CertificateVerifyMode = CertificateVerifyMode.Default
```

功能：设置或获取证书的认证模式，默认认证系统证书

类型：[CertificateVerifyMode](tls_package_enums.md#enum-certificateverifymode)

### prop cipherSuitesV1_2

```cangjie
public mut prop cipherSuitesV1_2: Array<String>
```

功能：基于 TLS 1.2 协议下的加密套。

类型：Array\<String>

异常：

- IllegalArgumentException - 列表元素有 '\0' 字符时，抛出异常。

### prop cipherSuitesV1_3

```cangjie
public mut prop cipherSuitesV1_3: Array<String>
```

功能：基于 TLS 1.3 协议下的加密套。

类型：Array\<String>

异常：

- IllegalArgumentException - 列表元素有 '\0' 字符时，抛出异常。

### prop dhParameters

```cangjie
public mut prop dhParameters: ?DHParameters
```

功能：指定服务端的 DH 密钥参数，默认为 `None`， 默认情况下使用 openssl 自动生成的参数值。

类型：?[DHParameters](../../../crypto/x509/x509_package_api/x509_package_interfaces.md#interface-dhparameters)

### prop maxVersion

```cangjie
public mut prop maxVersion: TlsVersion
```

功能：支持的 TLS 最大版本。

> **注意**
>
> 当仅设置`maxVersion`，而未设置`minVersion`，或设置的`maxVersion`低于`minVersion`，将会在握手阶段抛出 [TlsException](tls_package_exceptions.md#class-tlsexception)。

类型：[TlsVersion](tls_package_enums.md#enum-tlsversion)

### prop minVersion

```cangjie
public mut prop minVersion: TlsVersion
```

功能：支持的 TLS 最小版本。

> **注意**
> 当仅设置`minVersion`，而未设置`maxVersion`，或设置的`minVersion`高于`maxVersion`，将会在握手阶段抛出 [TlsException](tls_package_exceptions.md#class-tlsexception)。

类型：[TlsVersion](tls_package_enums.md#enum-tlsversion)

### prop securityLevel

```cangjie
public mut prop securityLevel: Int32
```

功能：指定服务端的安全级别，默认值为 2，可选参数值在 [0,5] 内，参数值含义参见 [openssl-SSL_CTX_set_security_level](https://www.openssl.org/docs/man1.1.1/man3/SSL_CTX_set_security_level.html) 说明。
功能：指定服务端的安全级别，默认值为 2，可选参数值在 0-5 内，参数值含义参见 openssl-SSL_CTX_set_security_level 说明。

类型：Int32

异常：

- IllegalArgumentException - 当配置值不在 0-5 范围内时，抛出异常。

### prop serverCertificate(Array\<X509Certificate>, PrivateKey)

```cangjie
public mut prop serverCertificate(Array<X509Certificate>, PrivateKey)
```

功能：服务端证书和对应的私钥文件。

类型：(Array\<[X509Certificate](../../../crypto/x509/x509_package_api/x509_package_classes.md#class-x509certificate)>, PrivateKey)。