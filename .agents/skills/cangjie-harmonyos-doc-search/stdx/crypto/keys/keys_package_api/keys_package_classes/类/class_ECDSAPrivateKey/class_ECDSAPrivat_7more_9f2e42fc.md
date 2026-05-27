## class ECDSAPrivateKey

```cangjie
public class ECDSAPrivateKey <: PrivateKey {
    public init(curve: Curve)
}
```

功能：ECDSA 私钥类，提供生成 ECDSA 私钥能力，ECDSA 的私钥支持签名操作，同时支持 PEM 和 DER 格式的编码解码。使用示例见 [ECDSA 密钥示例](../keys_samples/sample_keys.md#ecdsa-密钥示例)。

父类型：

- [PrivateKey](../../x509/x509_package_api/x509_package_interfaces.md#interface-privatekey)

### init(Curve)

```cangjie
public init(curve: Curve)
```

功能：init 初始化生成私钥。

参数：

- curve: [Curve](keys_package_enums.md#enum-curve) - 椭圆曲线类型。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 初始化失败，抛出异常。

### static func decodeDer(DerBlob)

```cangjie
public static func decodeDer(blob: DerBlob): ECDSAPrivateKey
```

功能：将私钥从 DER 格式解码。

参数：

- blob: [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 二进制格式的私钥对象。

返回值：

- [ECDSAPrivateKey](keys_package_classes.md#class-ecdsaprivatekey) - 解码出的 ECDSA 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败，抛出异常。

### static func decodeDer(DerBlob, ?String)

```cangjie
public static func decodeDer(blob: DerBlob, password!: ?String): ECDSAPrivateKey
```

功能：将加密的私钥从 DER 格式解码。

参数：

- blob: [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 二进制格式的私钥对象。
- password!: ?String - 解密私钥需要提供的密码，密码为 None 时则不解密。

返回值：

- [ECDSAPrivateKey](keys_package_classes.md#class-ecdsaprivatekey) - 解码出的 ECDSA 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败、解密失败或者参数密码为空字符串，抛出异常。

### static func decodeFromPem(String)

```cangjie
public static func decodeFromPem(text: String): ECDSAPrivateKey
```

功能：将私钥从 PEM 格式解码。

参数：

- text: String - PEM 格式的私钥字符流。

返回值：

- [ECDSAPrivateKey](keys_package_classes.md#class-ecdsaprivatekey) - 解码出的 ECDSA 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败、字符流不符合 PEM 格式或文件头不符合私钥头标准时，抛出异常。

### static func decodeFromPem(String, ?String)

```cangjie
public static func decodeFromPem(text: String, password!: ?String): ECDSAPrivateKey
```

功能：将私钥从 PEM 格式解码。

参数：

- text: String - PEM 格式的私钥字符流。
- password!: ?String - 解密私钥需要提供的密码，密码为 None 时则不解密。

返回值：

- [ECDSAPrivateKey](keys_package_classes.md#class-ecdsaprivatekey) - 解码出的 ECDSA 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败、解密失败、参数密码为空字符串、字符流不符合 PEM 格式或文件头不符合私钥头标准时，抛出异常。

### func encodeToDer()

```cangjie
public override func encodeToDer(): DerBlob
```

功能：将私钥编码为 DER 格式。

返回值：

- [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 编码后的 Der 格式私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 编码失败，抛出异常。