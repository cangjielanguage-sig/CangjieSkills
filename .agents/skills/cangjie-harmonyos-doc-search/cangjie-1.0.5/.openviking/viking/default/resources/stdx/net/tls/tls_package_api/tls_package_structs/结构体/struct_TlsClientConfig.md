## struct TlsClientConfig

```cangjie
public struct TlsClientConfig {
    public var keylogCallback: ?(TlsSocket, String) -> Unit = None
    public var verifyMode: CertificateVerifyMode = CertificateVerifyMode.Default
    public init()
}
```

功能：客户端配置。

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

功能：设置或获取证书的认证模式，默认为 `Default`。

类型：[CertificateVerifyMode](tls_package_enums.md#enum-certificateverifymode)

### prop alpnProtocolsList

```cangjie
public mut prop alpnProtocolsList: Array<String>
```

功能：要求的应用层协议名称。若列表为空，则客户端将不协商应用层协议。

类型：Array\<String>

异常：

- IllegalArgumentException - 列表元素有 '\0' 字符时，抛出异常。

### prop cipherSuitesV1_2

```cangjie
public mut prop cipherSuitesV1_2: ?Array<String>
```

功能：基于 TLS 1.2 协议下的加密套。

类型：?Array\<String>

异常：

- IllegalArgumentException - 列表元素有 '\0' 字符时，抛出异常。

### prop cipherSuitesV1_3

```cangjie
public mut prop cipherSuitesV1_3: ?Array<String>
```

功能：基于 TLS 1.3 协议下的加密套。

类型：?Array\<String>

异常：

- IllegalArgumentException - 列表元素有 '\0' 字符时，抛出异常。

### prop clientCertificate

```cangjie
public mut prop clientCertificate: ?(Array<X509Certificate>, PrivateKey)
```

功能：客户端证书和私钥。

类型：?(Array\<[X509Certificate](../../../crypto/x509/x509_package_api/x509_package_classes.md#class-x509certificate)>, PrivateKey)

### prop domain

```cangjie
public mut prop domain: ?String
```

功能：读写要求的服务端主机地址（SNI），`None` 表示不要求。

类型：?String

异常：

- IllegalArgumentException - 参数有 '\0' 字符时，抛出异常。

### prop maxVersion

```cangjie
public mut prop maxVersion: TlsVersion
```

功能：支持的 TLS 最大的版本。

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

功能：指定客户端的安全级别，默认值为 2，可选参数值在 0-5 内，参数值含义参见 openssl-SSL_CTX_set_security_level 说明。

类型：Int32

### prop signatureAlgorithms

```cangjie
public mut prop signatureAlgorithms: ?Array<SignatureAlgorithm>
```

功能：指定保序的签名和哈希算法。在值为 `None` 或者列表为空时，客户端会使用默认的列表。指定列表后，客户端可能不会发送不合适的签名算法。
参见 [RFC5246 7.4.1.4.1 (TLS 1.2)](https://www.rfc-editor.org/rfc/rfc5246.html#section-7.4.1.4.1) 章节， [RFC8446 4.2.3. (TLS 1.3)](https://www.rfc-editor.org/rfc/rfc8446.html#section-4.2.3) 章节。

类型：?Array\<[SignatureAlgorithm](tls_package_enums.md#enum-signaturealgorithm)>

### init()

```cangjie
public init()
```

功能：构造 [TlsClientConfig](tls_package_structs.md#struct-tlsclientconfig)。