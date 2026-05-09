## class RSAPublicKey

```cangjie
public class RSAPublicKey <: PublicKey {
    public init(pri: RSAPrivateKey)
}
```

功能：RSA 公钥类，提供生成 RSA 公钥能力，RSA 公钥支持验证签名和加密操作，支持 PEM 和 DER 格式的编码解码。使用示例见 [RSA 密钥示例](../keys_samples/sample_keys.md#rsa-密钥示例)。

父类型：

- [PublicKey](../../x509/x509_package_api/x509_package_interfaces.md#interface-publickey)

### init(RSAPrivateKey)

```cangjie
public init(pri: RSAPrivateKey)
```

功能：init 初始化公钥，从私钥中获取对应的公钥。

参数：

- pri: [RSAPrivateKey](keys_package_classes.md#class-rsaprivatekey) - RSA 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 初始化失败，抛出异常。

### static func decodeDer(DerBlob)

```cangjie
public static func decodeDer(blob: DerBlob): RSAPublicKey
```

功能：将公钥从 DER 格式解码。

参数：

- blob: [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 二进制格式的公钥对象。

返回值：

- [RSAPublicKey](keys_package_classes.md#class-rsapublickey) - 解码出的 RSA 公钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败，抛出异常。

### static func decodeFromPem(String)

```cangjie
public static func decodeFromPem(text: String): RSAPublicKey
```

功能：将公钥从 PEM 格式解码。

参数：

- text: String - PEM 格式的公钥字符流。

返回值：

- [RSAPublicKey](keys_package_classes.md#class-rsapublickey) - 解码出的 RSA 公钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败、字符流不符合 PEM 格式或文件头不符合公钥头标准时，抛出异常。

### func encodeToDer()

```cangjie
public override func encodeToDer(): DerBlob
```

功能：将公钥编码为 DER 格式。

返回值：

- [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 编码后的 Der 格式公钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 编码失败，抛出异常。

### func encodeToPem()

```cangjie
public override func encodeToPem(): PemEntry
```

功能：将公钥编码为 PEM 格式。

返回值：

- [PemEntry](../../x509/x509_package_api/x509_package_structs.md#struct-pementry) 对象。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 编码失败，抛出异常。

### func encrypt(InputStream, OutputStream, PadOption)

```cangjie
public func encrypt(input: InputStream, output: OutputStream, padType!: PadOption): Unit
```

功能：encrypt 给一段数据进行加密。

参数：

- input: InputStream - 需要加密的数据。
- output: OutputStream - 加密后的数据。
- padType!: [PadOption](keys_package_enums.md#enum-padoption) - 填充模式，可以选择 PKCS1 或 OAEP 模式，不支持 PSS 模式，在对安全场景要求较高的情况下，推荐使用 OAEP 填充模式。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 设置填充模式失败或加密失败，抛出异常。

### func toString()

```cangjie
public override func toString(): String
```

功能：输出公钥种类。

返回值：

- String - 密钥类别描述。