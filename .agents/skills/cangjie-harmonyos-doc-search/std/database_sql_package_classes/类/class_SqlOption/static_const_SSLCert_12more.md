### static const SSLCert

```cangjie
public static const SSLCert: String = "ssl.cert"
```

功能：客户端 SSL 公钥证书文件的路径名。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const SSLKey

```cangjie
public static const SSLKey: String = "ssl.key"
```

功能：客户端 SSL 私钥文件的路径名。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const SSLKeyPassword

```cangjie
public static const SSLKeyPassword: String = "ssl.key.password"
```

功能：客户端 SSL 私钥文件的密码。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const SSLMode

```cangjie
public static const SSLMode: String = "ssl.mode"
```

功能：获取 SSLMode 传输层加密模式。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const SSLModeDisabled

```cangjie
public static const SSLModeDisabled: String = "ssl.mode.disabled"
```

功能：建立未加密的连接。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const SSLModePreferred

```cangjie
public static const SSLModePreferred: String = "ssl.mode.preferred"
```

功能：如果服务器支持加密连接，则建立加密连接；如果无法建立加密连接，则回退到未加密连接，这是 SSLMode 的默认值。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const SSLModeRequired

```cangjie
public static const SSLModeRequired: String = "ssl.mode.required"
```

功能：如果服务器支持加密连接，则建立加密连接。如果无法建立加密连接，则连接失败。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const SSLModeVerifyCA

```cangjie
public static const SSLModeVerifyCA: String = "ssl.mode.verify_ca"
```

功能：SSLModeVerifyCA 和 SSLModeRequired 类似，但是增加了校验服务器证书，如果校验失败，则连接失败。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const SSLModeVerifyFull

```cangjie
public static const SSLModeVerifyFull: String = "ssl.mode.verify_full"
```

功能：SSLModeVerifyFull 和 SSLModeVerifyCA 类似，但通过验证服务器证书中的标识与客户端连接的主机名是否匹配，来执行主机名身份验证。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const SSLSni

```cangjie
public static const SSLSni: String = "ssl.sni"
```

功能：客户端通过该标识在握手过程开始时试图连接到哪个主机名。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const Tls12Ciphersuites

```cangjie
public static const Tls12Ciphersuites: String = "tls1.2.ciphersuites"
```

功能：此选项指定客户端允许使用 TLSv1.2 及以下的加密连接使用哪些密码套件。
值为冒号分隔的字符串，比如 `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_[SHA256]():TLS_DHE_RSA_WITH_AES_128_CBC_SHA`。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)

### static const Tls13Ciphersuites

```cangjie
public static const Tls13Ciphersuites: String = "tls1.3.ciphersuites"
```

功能：此选项指定客户端允许使用 TLSv1.3 的加密连接使用哪些密码套件。
值为冒号分隔的字符串，比如 `TLS_AES_256_GCM_[SHA384]():TLS_CHACHA20_POLY1305_[SHA256]()`。

类型：[String](../../core/core_package_api/core_package_structs.md#struct-string)