## class SM2PrivateKey

```cangjie
public class SM2PrivateKey <: PrivateKey {
    public init()
}
```

功能：SM2 私钥类，提供生成 SM2 私钥能力，SM2 私钥支持签名和解密操作，支持 PEM 和 DER 格式的编码解码，符合 PKCS1 标准。使用示例见 [SM2 密钥示例](../keys_samples/sample_keys.md#sm2-密钥示例)。

父类型：

- [PrivateKey](../../x509/x509_package_api/x509_package_interfaces.md#interface-privatekey)

### init()

```cangjie
public init()
```

功能：init 初始化生成私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 初始化失败，抛出异常。

### static func decodeDer(DerBlob)

```cangjie
public static func decodeDer(blob: DerBlob): SM2PrivateKey
```

功能：将私钥从 DER 格式解码。

参数：

- blob: [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 二进制格式的私钥对象。

返回值：

- [SM2PrivateKey](keys_package_classes.md#class-sm2privatekey) - 解码出的 SM2 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败，抛出异常。

### static func decodeDer(DerBlob, ?String)

```cangjie
public static func decodeDer(blob: DerBlob, password!: ?String): SM2PrivateKey
```

功能：将加密的私钥从 DER 格式解码。

参数：

- blob: [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 二进制格式的私钥对象。
- password!: ?String - 解密私钥需要提供的密码，密码为 None 时则不解密。

返回值：

- [SM2PrivateKey](keys_package_classes.md#class-sm2privatekey) - 解码出的 SM2 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败、解密失败或者参数密码为空字符串，抛出异常。

### static func decodeFromPem(String)

```cangjie
public static func decodeFromPem(text: String): SM2PrivateKey
```

功能：将私钥从 PEM 格式解码。

参数：

- text: String - PEM 格式的私钥字符流。

返回值：

- [SM2PrivateKey](keys_package_classes.md#class-sm2privatekey) - 解码出的 SM2 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败、解密失败、字符流不符合 PEM 格式或文件头不符合私钥头标准时，抛出异常。

### static func decodeFromPem(String, ?String)

```cangjie
public static func decodeFromPem(text: String, password!: ?String): SM2PrivateKey
```

功能：将私钥从 PEM 格式解码。

参数：

- text: String - PEM 格式的私钥字符流。
- password!: ?String - 解密私钥需要提供的密码，密码为 None 时则不解密。

返回值：

- [SM2PrivateKey](keys_package_classes.md#class-sm2privatekey) - 解码出的 SM2 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败、解密失败、参数密码为空字符串、字符流不符合 PEM 格式或文件头不符合私钥头标准时，抛出异常。

### func decrypt(Array\<Byte>)

```cangjie
public func decrypt(input: Array<Byte>): Array<Byte>
```

功能：decrypt 解密出原始数据，待解密密文需要遵循 ASN.1 编码规则。

参数：

- input: Array\<Byte> - 加密的数据。

返回值：

- Array\<Byte> - 解密后的数据。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解密失败，抛出异常。

### func encodeToDer()

```cangjie
public func encodeToDer(): DerBlob
```

功能：将私钥编码为 DER 格式。

返回值：

- [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 编码后的 DER 格式私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 编码失败，抛出异常。