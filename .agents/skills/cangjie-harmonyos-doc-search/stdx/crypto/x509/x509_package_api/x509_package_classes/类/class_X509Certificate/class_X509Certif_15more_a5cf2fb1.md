## class X509Certificate

```cangjie
public class X509Certificate <: Equatable<X509Certificate> & Hashable & ToString {
    public init(
        certificateInfo: X509CertificateInfo,
        parent!: X509Certificate,
        publicKey!: PublicKey,
        privateKey!: PrivateKey,
        signatureAlgorithm!: ?SignatureAlgorithm = None
    )
}
```

功能：X509 数字证书是一种用于加密通信的数字证书，它是公钥基础设施（PKI）的核心组件之一。X509 数字证书包含了一个实体的公钥和身份信息，用于验证该实体的身份和确保通信的安全性。

父类型：

- Equatable\<[X509Certificate](#class-x509certificate)>
- Hashable
- ToString

### prop dnsNames

```cangjie
public prop dnsNames: Array<String>
```

功能：解析数字证书备选名称中的域名。

类型：Array\<String>

### prop emailAddresses

```cangjie
public prop emailAddresses: Array<String>
```

功能：解析数字证书备选名称中的 email 地址。

类型：Array\<String>

### prop extKeyUsage

```cangjie
public prop extKeyUsage: ExtKeyUsage
```

功能：解析数字证书中的扩展密钥用法。

类型：[ExtKeyUsage](x509_package_structs.md#struct-extkeyusage)

### prop issuer

```cangjie
public prop issuer: X509Name
```

功能：解析数字证书的颁发者信息。

类型：[X509Name](x509_package_classes.md#class-x509name)

### prop IPAddresses

```cangjie
public prop IPAddresses: Array<IP>
```

功能：解析数字证书备选名称中的 [IP](x509_package_type.md#type-ip) 地址。

类型：Array\<[IP](x509_package_type.md#type-ip)>

### prop keyUsage

```cangjie
public prop keyUsage: KeyUsage
```

功能：解析数字证书中的密钥用法。

类型：[KeyUsage](x509_package_structs.md#struct-keyusage)

### prop notAfter

```cangjie
public prop notAfter: DateTime
```

功能：解析数字证书的有效期截止时间。

类型：DateTime

### prop notBefore

```cangjie
public prop notBefore: DateTime
```

功能：解析数字证书的有效期开始时间。

类型：DateTime

### prop publicKey

```cangjie
public prop publicKey: PublicKey
```

功能：解析数字证书的公钥。

类型：[PublicKey](x509_package_interfaces.md#interface-publickey)

### prop publicKeyAlgorithm

```cangjie
public prop publicKeyAlgorithm: PublicKeyAlgorithm
```

功能：解析数字证书的公钥算法。

类型：[PublicKeyAlgorithm](x509_package_enums.md#enum-publickeyalgorithm)

### prop serialNumber

```cangjie
public prop serialNumber: SerialNumber
```

功能：解析数字证书的序列号。

类型：[SerialNumber](x509_package_structs.md#struct-serialnumber)

### prop signature

```cangjie
public prop signature: Signature
```

功能：解析数字证书的签名。

类型：[Signature](x509_package_structs.md#struct-signature)

### prop signatureAlgorithm

```cangjie
public prop signatureAlgorithm: SignatureAlgorithm
```

功能：解析数字证书的签名算法。

类型：[SignatureAlgorithm](./x509_package_enums.md#enum-signaturealgorithm)

### prop subject

```cangjie
public prop subject: X509Name
```

功能：解析数字证书的使用者信息。

类型：[X509Name](x509_package_classes.md#class-x509name)