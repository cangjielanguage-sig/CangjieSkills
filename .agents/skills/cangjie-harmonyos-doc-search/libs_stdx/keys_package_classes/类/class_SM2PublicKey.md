## class SM2PublicKey

```cangjie
public class SM2PublicKey <: PublicKey {
    public init(pri: SM2PrivateKey)
}
```

功能：SM2 公钥类，提供生成 SM2 公钥能力，SM2 公钥支持验证签名和加密操作，支持 PEM 和 DER 格式的编码解码。使用示例见 [SM2 密钥示例](../keys_samples/sample_keys.md#sm2-密钥示例)。

父类型：

- [PublicKey](../../x509/x509_package_api/x509_package_interfaces.md#interface-publickey)

### init(SM2PrivateKey)

```cangjie
public init(pri: SM2PrivateKey)
```

功能：init 初始化公钥，从私钥中获取对应的公钥。

参数：

- pri: [SM2PrivateKey](keys_package_classes.md#class-sm2privatekey) - SM2 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 初始化失败，抛出异常。

### static func decodeDer(DerBlob)

```cangjie
public static func decodeDer(blob: DerBlob): SM2PublicKey
```

功能：将公钥从 DER 格式解码。

参数：

- blob: [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 二进制格式的公钥对象。

返回值：

- [SM2PublicKey](keys_package_classes.md#class-sm2publickey) - 解码出的 SM2 公钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败，抛出异常。

### static func decodeFromPem(String)

```cangjie
public static func decodeFromPem(text: String): SM2PublicKey
```

功能：将公钥从 PEM 格式解码。

参数：

- text: String - PEM 格式的公钥字符流。

返回值：

- [SM2PublicKey](keys_package_classes.md#class-sm2publickey) - 解码出的 SM2 公钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败、字符流不符合 PEM 格式或文件头不符合公钥头标准时，抛出异常。

### func encodeToDer()

```cangjie
public func encodeToDer(): DerBlob
```

功能：将公钥编码为 DER 格式。

返回值：

- [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 编码后的 Der 格式公钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 编码失败，抛出异常。

### func encodeToPem()

```cangjie
public func encodeToPem(): PemEntry
```

功能：将公钥编码为 PEM 格式。

返回值：

- [PemEntry](../../x509/x509_package_api/x509_package_structs.md#struct-pementry) 对象。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 编码失败，抛出异常。

### func encrypt(Array\<Byte>)

```cangjie
public func encrypt(input: Array<Byte>): Array<Byte>
```

功能：encrypt 给一段数据进行加密，输出密文遵循 ASN.1 编码规则。

参数：

- input: Array\<Byte> - 需要加密的数据。

返回值：

- Array\<Byte> - 加密后的数据。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 加密失败，抛出异常。

### func toString()

```cangjie
public override func toString(): String
```

功能：输出公钥种类。

返回值：

- String - 密钥类别描述。

### func verify(Array\<Byte>, Array\<Byte>)

```cangjie
public func verify(data: Array<Byte>, sig: Array<Byte>): Bool
```

功能：verify 验证签名结果。

参数：

- data: Array\<Byte> - 数据。
- sig: Array\<Byte> - 数据的签名结果。

返回值：

- Bool - 返回 true 表示验证成功，false 失败。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 设置填充模式失败或验证失败，抛出异常。