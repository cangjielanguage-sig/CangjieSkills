## enum SignatureType

```cangjie
public enum SignatureType <: ToString & Equatable<SignatureType> {
    | DSA
    | ECDSA
    | RSA
}
```

功能：签名算法类型，用于认证真实性。参见 [RFC5246 7.4.1.4.1](https://www.rfc-editor.org/rfc/rfc5246.html#section-7.4.1.4.1) 章节。

父类型：

- ToString
- Equatable\<[SignatureType](#enum-signaturetype)>

### DSA

```cangjie
DSA
```

功能：创建一个 `DSA` 类型的枚举实例，表示采用数字签名算法。

### ECDSA

```cangjie
ECDSA
```

功能：创建一个 `ECDSA` 类型的枚举实例，表示采用椭圆曲线数字签名算法。

### RSA

```cangjie
RSA
```

功能：创建一个 `RSA` 类型的枚举实例，表示采用 RSA 加密算法。

### func toString()

```cangjie
public func toString(): String
```

功能：转换为签名算法的字符串表示。

返回值：

- String - 签名算法的名称。

### operator func !=(SignatureType)

```cangjie
public operator func !=(other: SignatureType) : Bool
```

功能：判断两者是否为不同的签名算法。

参数：

- other: [SignatureType](tls_package_enums.md#enum-signaturetype) - 对比的签名算法类型。

返回值：

- Bool - 不相同返回 `true`；否则，返回 `false`。

### operator func ==(SignatureType)

```cangjie
public operator func ==(other: SignatureType) : Bool
```

功能：判断两者是否为相同的签名算法。

参数：

- other: [SignatureType](tls_package_enums.md#enum-signaturetype) - 对比的签名算法类型。

返回值：

- Bool - 相同返回 `true`；否则，返回 `false`。

## enum TlsClientIdentificationMode

```cangjie
public enum TlsClientIdentificationMode {
    | Disabled
    | Optional
    | Required
}
```

功能：服务端对客户端证书的认证模式。

### Disabled

```cangjie
Disabled
```

功能：表示服务端不校验客户端证书，客户端可以不发送证书和公钥，即单向认证。

### Optional

```cangjie
Optional
```

功能：表示服务端校验客户端证书，但客户端可以不提供证书及公钥，不提供时则单向认证，提供时则为双向认证。

### Required

```cangjie
Required
```

功能：表示服务端校验客户端证书，并且要求客户端必须提供证书和公钥，即双向认证。

## enum TlsVersion

```cangjie
public enum TlsVersion <: ToString {
    | V1_2
    | V1_3
    | Unknown
}
```

功能：TLS 协议版本。

父类型：

- ToString

### Unknown

```cangjie
Unknown
```

功能：表示未知协议版本。

### V1_2

```cangjie
V1_2
```

功能：表示 TLS 1.2 版本。

### V1_3

```cangjie
V1_3
```

功能：表示 TLS 1.3 版本。

### func toString()

```cangjie
public override func toString(): String
```

功能：返回当前 [TlsVersion](tls_package_enums.md#enum-tlsversion) 的字符串表示。

返回值：

- String - 当前 [TlsVersion](tls_package_enums.md#enum-tlsversion) 的字符串表示。