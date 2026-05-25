### init(X509CertificateInfo, X509Certificate, PublicKey, PrivateKey, ?SignatureAlgorithm)

```cangjie
public init(
    certificateInfo: X509CertificateInfo,
    parent!: X509Certificate,
    publicKey!: PublicKey,
    privateKey!: PrivateKey,
    signatureAlgorithm!: ?SignatureAlgorithm = None
)
```

功能：创建数字证书对象。

参数：

- certificateInfo: [X509CertificateInfo](x509_package_structs.md#struct-x509certificateinfo) - 数字证书配置信息。
- parent!: [X509Certificate](x509_package_classes.md#class-x509certificate) - 颁发者证书。
- publicKey!: [PublicKey](x509_package_interfaces.md#interface-publickey) - 申请人公钥，仅支持 RSA、ECDSA 和 DSA 公钥。
- privateKey!: [PrivateKey](x509_package_interfaces.md#interface-privatekey) - 颁发者私钥，仅支持 RSA、ECDSA 和 DSA 私钥。
- signatureAlgorithm!: ?[SignatureAlgorithm](./x509_package_enums.md#enum-signaturealgorithm) - 证书签名算法，默认值为 None，使用默认值时默认的摘要类型是 [SHA256](../../digest/digest_package_api/digest_package_classes.md#class-sha256)。

异常：

- [X509Exception](./x509_package_exceptions.md#class-x509exception) - 公钥或私钥类型不支持、私钥类型和证书签名算法中的私钥类型不匹配或数字证书信息设置失败时，抛出异常。

### static func decodeFromDer(DerBlob)

```cangjie
public static func decodeFromDer(der: DerBlob): X509Certificate
```

功能：将 DER 格式的数字证书解码。

参数：

- der: [DerBlob](x509_package_structs.md#struct-derblob) - DER 格式的二进制数据。

返回值：

- [X509Certificate](x509_package_classes.md#class-x509certificate) - 由 DER 格式解码出的数字证书。

异常：

- [X509Exception](./x509_package_exceptions.md#class-x509exception) - 数据为空时，或数据不是有效的数字证书 DER 格式时抛出异常。

### static func decodeFromPem(String)

```cangjie
public static func decodeFromPem(pem: String): Array<X509Certificate>
```

功能：将数字证书从 PEM 格式解码。

参数：

- pem: String - PEM 格式的数字证书字符流。

返回值：

- Array\<[X509Certificate](x509_package_classes.md#class-x509certificate)> - 由 PEM 格式解码出的数字证书数组。

异常：

- [X509Exception](./x509_package_exceptions.md#class-x509exception) - 字符流不符合 PEM 格式时，或文件头不符合数字证书头标准时抛出异常。

### func encodeToDer()

```cangjie
public func encodeToDer(): DerBlob
```

功能：将数字证书编码成 Der 格式。

返回值：

- [DerBlob](x509_package_structs.md#struct-derblob) - 编码后的 Der 格式的数字证书。

### func encodeToPem()

```cangjie
public func encodeToPem(): PemEntry
```

功能：将数字证书编码成 PEM 格式。

返回值：

- [PemEntry](x509_package_structs.md#struct-pementry) - 编码后的 PEM 格式的数字证书。

### func hashCode()

```cangjie
public override func hashCode(): Int64
```

功能：返回证书哈希值。

返回值：

- Int64 - 对证书对象进行哈希计算后得到的结果。

### static func systemRootCerts()

```cangjie
public static func systemRootCerts(): Array<X509Certificate>
```

功能：返回操作系统的根证书，支持 Linux，MacOS 和 Windows 平台。

返回值：

- Array\<[X509Certificate](x509_package_classes.md#class-x509certificate)> - 操作系统的根证书链。

### func toString()

```cangjie
public override func toString(): String
```

功能：生成证书名称字符串，包含证书的使用者信息、有效期以及颁发者信息。

返回值：

- String - 证书名称字符串。