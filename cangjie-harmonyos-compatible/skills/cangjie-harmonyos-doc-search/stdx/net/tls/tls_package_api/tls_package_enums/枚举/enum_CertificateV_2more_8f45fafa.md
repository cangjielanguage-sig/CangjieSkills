## enum CertificateVerifyMode

```cangjie
public enum CertificateVerifyMode {
    | CustomCA(Array<X509Certificate>)
    | Default
    | TrustAll
}
```

功能：对证书验证的处理模式。

> **说明：**
>
> CustomCA 模式可使用用户配置的证书地址，适用于用户证书无法设置为系统证书的场景。
>
> 证书认证模式，TCP 连接建立成功后，客户端和服务端可交换证书，Default 模式使用系统证书。
>
> 在开发测试阶段，可使用 TrustAll 模式，该模式表示本端不作对对端证书的校验。此模式本端信任任意建立连接对象，一般仅在开发测试阶段使用。

### CustomCA(Array\<X509Certificate>)

```cangjie
CustomCA(Array<X509Certificate>)
```

功能：表示根据提供的 CA 列表与系统 CA 进行验证。

### Default

```cangjie
Default
```

功能：表示默认验证模式，根据系统 CA 验证证书。

### TrustAll

```cangjie
TrustAll
```

功能：表示信任所有证书。

## enum SignatureAlgorithm

```cangjie
public enum SignatureAlgorithm <: ToString & Equatable<SignatureAlgorithm> {
    | SignatureAndHashAlgorithm(SignatureType, HashType)
    | SignatureScheme(SignatureSchemeType)
}
```

功能：签名算法类型，签名算法用于确保传输数据的身份验证、完整性和真实性。

父类型：

- ToString
- Equatable\<[SignatureAlgorithm](../../../crypto/x509/x509_package_api/x509_package_enums.md#enum-signaturealgorithm)>

### SignatureAndHashAlgorithm(SignatureType, HashType)

```cangjie
SignatureAndHashAlgorithm(SignatureType, HashType)
```

功能：表明哪个签名和哈希算法对会被用于数字签名，自 TLS 1.2 及以后版本，包含签名和哈希算法类型。

### SignatureScheme(SignatureSchemeType)

```cangjie
SignatureScheme(SignatureSchemeType)
```

功能：签名方案，自 TLS 1.3 及以后版本，业界更为推荐的指定签名算法的方式。

### func toString()

```cangjie
public func toString():String
```

功能：转换签名算法的字符串表示。

返回值：

- String - 签名算法名称。

### operator func !=(SignatureAlgorithm)

```cangjie
public operator func !=(other: SignatureAlgorithm) : Bool
```

功能：判断签名算法类型是否不同。

参数：

- other: [SignatureAlgorithm](tls_package_enums.md#enum-signaturealgorithm) - 对比的签名算法类型。

返回值：

- Bool - 不相同返回 `true`；否则，返回 `false`。

### operator func ==(SignatureAlgorithm)

```cangjie
public operator func ==(other: SignatureAlgorithm) : Bool
```

功能：判断签名算法类型是否相同。

参数：

- other: [SignatureAlgorithm](tls_package_enums.md#enum-signaturealgorithm) - 对比的签名算法类型。

返回值：

- Bool - 相同返回 `true`；否则，返回 `false`。