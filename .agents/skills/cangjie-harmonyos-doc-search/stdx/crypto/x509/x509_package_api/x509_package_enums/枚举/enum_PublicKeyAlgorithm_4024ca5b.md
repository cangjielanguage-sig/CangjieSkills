## enum PublicKeyAlgorithm

```cangjie
public enum PublicKeyAlgorithm <: Equatable<PublicKeyAlgorithm> & ToString {
    RSA | DSA | ECDSA | UnknownPublicKeyAlgorithm
}
```

功能：数字证书中包含的公钥信息，目前支持的种类有：RSA、DSA、ECDSA。

父类型：

- Equatable\<[PublicKeyAlgorithm](#enum-publickeyalgorithm)>
- ToString

### DSA

```cangjie
DSA
```

功能：DSA 公钥算法。

### ECDSA

```cangjie
ECDSA
```

功能：ECDSA 公钥算法。

### RSA

```cangjie
RSA
```

功能：RSA 公钥算法。

### UnknownPublicKeyAlgorithm

```cangjie
UnknownPublicKeyAlgorithm
```

功能：未知公钥算法。

### func toString()

```cangjie
public override func toString(): String
```

功能：生成证书携带的公钥算法名称字符串。

返回值：

- String - 证书携带的公钥算法名称字符串。

### operator func !=(PublicKeyAlgorithm)

```cangjie
public override operator func !=(other: PublicKeyAlgorithm): Bool
```

功能：判不等。

参数：

- other: [PublicKeyAlgorithm](x509_package_enums.md#enum-publickeyalgorithm) - 被比较的公钥算法。

返回值：

- Bool - 若公钥算法不同，返回 true；否则，返回 false。

### operator func ==(PublicKeyAlgorithm)

```cangjie
public override operator func ==(other: PublicKeyAlgorithm): Bool
```

功能：判等。

参数：

- other: [PublicKeyAlgorithm](x509_package_enums.md#enum-publickeyalgorithm) - 被比较的公钥算法。

返回值：

- Bool - 若公钥算法相同，返回 true；否则，返回 false。