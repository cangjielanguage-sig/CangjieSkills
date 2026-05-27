## class X509CertificateRequest

```cangjie
public class X509CertificateRequest <: Hashable & ToString {
    public init(
        privateKey: PrivateKey,
        certificateRequestInfo!: ?X509CertificateRequestInfo = None,
        signatureAlgorithm!: ?SignatureAlgorithm = None
    )
}
```

功能：数字证书签名请求。

父类型：

- Hashable
- ToString

### prop IPAddresses

```cangjie
public prop IPAddresses: Array<IP>
```

功能：解析数字证书签名请求备选名称中的 [IP](x509_package_type.md#type-ip) 地址。

类型：Array\<[IP](x509_package_type.md#type-ip)>

### prop dnsNames

```cangjie
public prop dnsNames: Array<String>
```

功能：解析数字证书签名请求备选名称中的域名。

类型：Array\<String>

### prop emailAddresses

```cangjie
public prop emailAddresses: Array<String>
```

功能：解析数字证书签名请求备选名称中的 email 地址。

类型：Array\<String>

### prop publicKey

```cangjie
public prop publicKey: PublicKey
```

功能：解析数字证书签名请求的公钥。

类型：[PublicKey](x509_package_interfaces.md#interface-publickey)

### prop publicKeyAlgorithm

```cangjie
public prop publicKeyAlgorithm: PublicKeyAlgorithm
```

功能：解析数字证书签名请求的公钥算法。

类型：[PublicKeyAlgorithm](x509_package_enums.md#enum-publickeyalgorithm)

### prop signature

```cangjie
public prop signature: Signature
```

功能：解析数字证书签名请求的签名。

类型：[Signature](x509_package_structs.md#struct-signature)

### prop signatureAlgorithm

```cangjie
public prop signatureAlgorithm: SignatureAlgorithm
```

功能：解析数字证书签名请求的签名算法。

类型：[SignatureAlgorithm](./x509_package_enums.md#enum-signaturealgorithm)

### prop subject

```cangjie
public prop subject: X509Name
```

功能：解析数字证书签名请求的使用者信息。

类型：[X509Name](x509_package_classes.md#class-x509name)

### init(PrivateKey, ?X509CertificateRequestInfo, ?SignatureAlgorithm)

```cangjie
public init(
    privateKey: PrivateKey,
    certificateRequestInfo!: ?X509CertificateRequestInfo = None,
    signatureAlgorithm!: ?SignatureAlgorithm = None
)
```

功能：创建数字证书签名请求对象。

参数：

- privateKey: [PrivateKey](x509_package_interfaces.md#interface-privatekey) - 私钥，仅支持 RSA、ECDSA 和 DSA 私钥。
- certificateRequestInfo!: ?[X509CertificateRequestInfo](x509_package_structs.md#struct-x509certificaterequestinfo) - 数字证书签名信息，默认值为 None。
- signatureAlgorithm!: ?[SignatureAlgorithm](./x509_package_enums.md#enum-signaturealgorithm) - 证书签名算法，默认值为 None，使用默认值时默认的摘要类型是 [SHA256](../../digest/digest_package_api/digest_package_classes.md#class-sha256)。

异常：

- [X509Exception](./x509_package_exceptions.md#class-x509exception) - 私钥类型不支持、私钥类型和证书签名算法中的私钥类型不匹配或数字证书签名信息设置失败时，抛出异常。

### static func decodeFromDer(DerBlob)

```cangjie
public static func decodeFromDer(der: DerBlob): X509CertificateRequest
```

功能：将 DER 格式的数字证书签名请求解码。

参数：

- der: [DerBlob](x509_package_structs.md#struct-derblob) - DER 格式的二进制数据。

返回值：

- [X509CertificateRequest](x509_package_classes.md#class-x509certificaterequest) - 由 DER 格式解码出的数字证书签名请求。

异常：

- [X509Exception](./x509_package_exceptions.md#class-x509exception) - 数据为空时，或数据不是有效的数字证书签名请求 DER 格式时抛出异常。