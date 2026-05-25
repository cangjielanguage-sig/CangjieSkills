## enum SignatureSchemeType

```cangjie
public enum SignatureSchemeType <: ToString & Equatable<SignatureSchemeType> {
    | RSA_PKCS1_SHA256
    | RSA_PKCS1_SHA384
    | RSA_PKCS1_SHA512
    | ECDSA_SECP256R1_SHA256
    | ECDSA_SECP384R1_SHA384
    | ECDSA_SECP521R1_SHA512
    | RSA_PSS_RSAE_SHA256
    | RSA_PSS_RSAE_SHA384
    | RSA_PSS_RSAE_SHA512
    | ED25519
    | ED448
    | RSA_PSS_PSS_SHA256
    | RSA_PSS_PSS_SHA384
    | RSA_PSS_PSS_SHA512
}
```

功能：加密算法类型，用于保护网络通信的安全性和隐私性。

父类型：

- ToString
- Equatable\<[SignatureSchemeType](#enum-signatureschemetype)>

### ECDSA_SECP256R1_SHA256

```cangjie
ECDSA_SECP256R1_SHA256
```

功能：创建一个 `ECDSA_SECP256R1_SHA256` 类型的枚举实例，表示加密算法类型使用 `ECDSA_SECP256R1_SHA256`。

### ECDSA_SECP384R1_SHA384

```cangjie
ECDSA_SECP384R1_SHA384
```

功能：创建一个 `ECDSA_SECP384R1_SHA384` 类型的枚举实例，表示加密算法类型使用 `ECDSA_SECP384R1_SHA384`。

### ECDSA_SECP521R1_SHA512

```cangjie
ECDSA_SECP521R1_SHA512
```

功能：创建一个 `ECDSA_SECP521R1_SHA512` 类型的枚举实例，表示加密算法类型使用 `ECDSA_SECP521R1_SHA512`。

### ED25519

```cangjie
ED25519
```

功能：创建一个 `ED25519` 类型的枚举实例，表示加密算法类型使用 ED25519。

### ED448

```cangjie
ED448
```

功能：创建一个 `ED448` 类型的枚举实例，表示加密算法类型使用 ED448。

### RSA_PKCS1_SHA256

```cangjie
RSA_PKCS1_SHA256
```

功能：创建一个 `RSA_PKCS1_SHA256` 类型的枚举实例，表示加密算法类型使用 `RSA_PKCS1_SHA256`。

### RSA_PKCS1_SHA384

```cangjie
RSA_PKCS1_SHA384
```

功能：创建一个 `RSA_PKCS1_SHA384` 类型的枚举实例，表示加密算法类型使用 `RSA_PKCS1_SHA384`。

### RSA_PKCS1_SHA512

```cangjie
RSA_PKCS1_SHA512
```

功能：创建一个 `RSA_PKCS1_SHA512` 类型的枚举实例，表示加密算法类型使用 `RSA_PKCS1_SHA512`。

### RSA_PSS_PSS_SHA256

```cangjie
RSA_PSS_PSS_SHA256
```

功能：创建一个 `RSA_PSS_PSS_SHA256` 类型的枚举实例，表示加密算法类型使用 `RSA_PSS_PSS_SHA256`。

### RSA_PSS_PSS_SHA384

```cangjie
RSA_PSS_PSS_SHA384
```

功能：创建一个 `RSA_PSS_PSS_SHA384` 类型的枚举实例，表示加密算法类型使用 `RSA_PSS_PSS_SHA384`。

### RSA_PSS_PSS_SHA512

```cangjie
RSA_PSS_PSS_SHA512
```

功能：创建一个 `RSA_PSS_PSS_SHA512` 类型的枚举实例，表示加密算法类型使用 `RSA_PSS_PSS_SHA512`。

### RSA_PSS_RSAE_SHA256

```cangjie
RSA_PSS_RSAE_SHA256
```

功能：创建一个 `RSA_PSS_RSAE_SHA256` 类型的枚举实例，表示加密算法类型使用 `RSA_PSS_RSAE_SHA256`。

### RSA_PSS_RSAE_SHA384

```cangjie
RSA_PSS_RSAE_SHA384
```

功能：创建一个 `RSA_PSS_RSAE_SHA384` 类型的枚举实例，表示加密算法类型使用 `RSA_PSS_RSAE_SHA384`。

### RSA_PSS_RSAE_SHA512

```cangjie
RSA_PSS_RSAE_SHA512
```

功能：创建一个 `RSA_PSS_RSAE_SHA512` 类型的枚举实例，表示加密算法类型使用 `RSA_PSS_RSAE_SHA384`。

### func toString()

```cangjie
public func toString(): String
```

功能：加密算法类型的字符串表示。

如 `RSA_PKCS1_SHA256` 的字符串表示为 "rsa_pkcs1_sha256"。

返回值：

- String - 加密算法类型的字符串表示。

### operator func !=(SignatureSchemeType)

```cangjie
public operator func !=(other: SignatureSchemeType): Bool
```

功能：判断两者是否为不同加密算法类型。

参数：

- other: [SignatureSchemeType](tls_package_enums.md#enum-signatureschemetype) - 对比的加密算法类型。

返回值：

- Bool - 不相同返回 true；否则，返回 false。

### operator func ==(SignatureSchemeType)

```cangjie
public operator func ==(other: SignatureSchemeType): Bool
```

功能：判断两者是否为同一加密算法类型。

参数：

- other: [SignatureSchemeType](tls_package_enums.md#enum-signatureschemetype) - 对比的加密算法类型。

返回值：

- Bool - 相同返回 true；否则，返回 false。