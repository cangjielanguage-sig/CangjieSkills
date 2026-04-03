## API 列表

### 类

| 类名                                                                                | 功能                                                                                                                                                       |
| ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [TlsSessionContext](./tls_package_api/tls_package_classes.md#class-tlssessioncontext) | 服务端启用 session 特性恢复会话，存储 session 用于对客户端进行验证类型。                                  |
| [TlsSocket](./tls_package_api/tls_package_classes.md#class-tlssocket)               | 用于在客户端及服务端间创建加密传输通道。                                                                                                                   |

### 枚举

| 枚举名                                                                                                 | 功能                                                               |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------ |
| [CertificateVerifyMode](./tls_package_api/tls_package_enums.md#enum-certificateverifymode)                   | 证书认证模式。 |
| [SignatureAlgorithm](./tls_package_api/tls_package_enums.md#enum-signaturealgorithm)                   | 签名算法类型，签名算法用于确保传输数据的身份验证、完整性和真实性。 |
| [SignatureSchemeType](./tls_package_api/tls_package_enums.md#enum-signatureschemetype)                 | 加密算法类型，用于保护网络通信的安全性和隐私性。                   |
| [SignatureType](./tls_package_api/tls_package_enums.md#enum-signaturetype)                             | 签名算法类型，用于认证真实性。                                     |
| [TlsClientIdentificationMode](./tls_package_api/tls_package_enums.md#enum-tlsclientidentificationmode) | 服务端对客户端证书的认证模式。                                     |
| [TlsVersion](./tls_package_api/tls_package_enums.md#enum-tlsversion) | TLS 协议版本。                                     |

### 结构体

| 结构体名                                                                           | 功能               |
| ---------------------------------------------------------------------------------- | ------------------ |
| [CipherSuite](./tls_package_api/tls_package_structs.md#struct-ciphersuite)         | TLS 中的密码套件。 |
| [TlsClientConfig](./tls_package_api/tls_package_structs.md#struct-tlsclientconfig) | 客户端配置。       |
| [TlsServerConfig](./tls_package_api/tls_package_structs.md#struct-tlsserverconfig) | 服务端配置。       |
| [TlsSession](./tls_package_api/tls_package_structs.md#struct-tlssession) | 当客户端 TLS 握手成功后，将会生成一个会话，当连接因一些原因丢失后，客户端可以通过这个会话 id 复用此次会话，省略握手流程。       |

### 异常类

| 类名                                                                           | 功能               |
| ---------------------------------------------------------------------------------- | ------------------ |
| [TlsException](./tls_package_api/tls_package_exceptions.md#class-tlsexception)         | TLS 处理出现错误时抛出的异常类型。 |