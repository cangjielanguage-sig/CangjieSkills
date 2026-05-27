## class RSAPrivateKey

```cangjie
public class RSAPrivateKey <: PrivateKey{
    public init(bits: Int32)
    public init(bits: Int32, e: BigInt)
}
```

功能：RSA 私钥类，提供生成 RSA 私钥能力，RSA 私钥支持签名和解密操作，支持 PEM 和 DER 格式的编码解码，符合 PKCS1 标准。使用示例见 [RSA 密钥示例](../keys_samples/sample_keys.md#rsa-密钥示例)。

父类型：

- [PrivateKey](../../x509/x509_package_api/x509_package_interfaces.md#interface-privatekey)

### init(Int32)

```cangjie
public init(bits: Int32)
```

功能：init 初始化生成私钥，公钥指数默认值为 65537，业界推荐。公钥指数 e 的大小直接影响了 RSA 算法的安全性和加密效率。通常情况下，e 的值越小，加密速度越快，但安全性越低。

参数：

- bits: Int32 - 密钥长度，需要大于等于 512 位，并且小于等于 16384 位。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 密钥长度不符合要求或初始化失败，抛出异常。

### init(Int32, BigInt)

```cangjie
public init(bits: Int32, e: BigInt)
```

功能：init 初始化生成私钥，允许用户指定公共指数。

参数：

- bits: Int32 - 密钥长度，需要大于等于 512 位，并且小于等于 16384 位，推荐使用的密钥长度不小于 3072 位。
- e: BigInt - 公钥公共指数，范围是 [3, 2^256-1] 的奇数。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 密钥长度不符合要求、公钥公共指数值不符合要求或初始化失败，抛出异常。

### static func decodeDer(DerBlob)

```cangjie
public static func decodeDer(blob: DerBlob): RSAPrivateKey
```

功能：将私钥从 DER 格式解码。

参数：

- blob: [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 二进制格式的私钥对象。

返回值：

- [RSAPrivateKey](keys_package_classes.md#class-rsaprivatekey) - 解码出的 RSA 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败，抛出异常。

### static func decodeDer(DerBlob, ?String)

```cangjie
public static func decodeDer(blob: DerBlob, password!: ?String): RSAPrivateKey
```

功能：将加密的私钥从 DER 格式解码。

参数：

- blob: [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 二进制格式的私钥对象。
- password!: ?String - 解密私钥需要提供的密码，密码为 None 时则不解密。

返回值：

- [RSAPrivateKey](keys_package_classes.md#class-rsaprivatekey) - 解码出的 RSA 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败、解密失败或者参数密码为空字符串，抛出异常。

### static func decodeFromPem(String)

```cangjie
public static func decodeFromPem(text: String): RSAPrivateKey
```

功能：将私钥从 PEM 格式解码。

参数：

- text: String - PEM 格式的私钥字符流。

返回值：

- [RSAPrivateKey](keys_package_classes.md#class-rsaprivatekey) - 解码出的 RSA 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败、解密失败、字符流不符合 PEM 格式或文件头不符合私钥头标准时，抛出异常。