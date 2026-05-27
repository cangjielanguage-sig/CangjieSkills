### static func decodeFromPem(String, ?String)

```cangjie
public static func decodeFromPem(text: String, password!: ?String): RSAPrivateKey
```

功能：将私钥从 PEM 格式解码。

参数：

- text: String - PEM 格式的私钥字符流。
- password!: ?String - 解密私钥需要提供的密码，密码为 None 时则不解密。

返回值：

- [RSAPrivateKey](keys_package_classes.md#class-rsaprivatekey) - 解码出的 RSA 私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 解码失败、解密失败、参数密码为空字符串、字符流不符合 PEM 格式或文件头不符合私钥头标准时，抛出异常。

### func decrypt(InputStream, OutputStream, PadOption)

```cangjie
public func decrypt(input: InputStream, output: OutputStream, padType!: PadOption): Unit
```

功能：decrypt 解密出原始数据。

参数：

- input: InputStream - 加密的数据。
- output: OutputStream - 解密后的数据。
- padType!: [PadOption](keys_package_enums.md#enum-padoption) - 填充模式，可以选择 PKCS1 或 OAEP 模式，不支持 PSS 模式，在对安全场景要求较高的情况下，推荐使用 OAEP 填充模式。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 设置填充模式失败或解密失败，抛出异常。

### func encodeToDer()

```cangjie
public override func encodeToDer(): DerBlob
```

功能：将私钥编码为 DER 格式。

返回值：

- [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 编码后的 DER 格式私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 编码失败，抛出异常。

### func encodeToDer(?String)

```cangjie
public func encodeToDer(password!: ?String): DerBlob
```

功能：使用 AES-256-CBC 加密私钥，将私钥编码为 DER 格式。

参数：

- password!: ?String - 加密私钥需要提供的密码，密码为 None 时则不加密。

返回值：

- [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 编码后的 DER 格式私钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 编码失败、加密失败或者参数密码为空字符串，抛出异常。

### func encodeToPem()

```cangjie
public override func encodeToPem(): PemEntry
```

功能：将私钥编码为 PEM 格式。

返回值：

- [PemEntry](../../x509/x509_package_api/x509_package_structs.md#struct-pementry) - 私钥 PEM 格式的对象。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 编码失败，抛出异常。

### func sign(Digest, Array\<Byte>, PadOption)

```cangjie
public func sign(hash: Digest, digest: Array<Byte>, padType!: PadOption): Array<Byte>
```

功能：对数据的摘要结果进行签名。

参数：

- hash: Digest - 摘要方法，获取 digest 结果使用的摘要方法。
- digest: Array\<Byte> - 数据的摘要结果。
- padType!: [PadOption](keys_package_enums.md#enum-padoption) - 填充模式，可以选择 PKCS1 或 PSS 模式，不支持 OAEP 模式，在对安全场景要求较高的情况下，推荐使用 PSS 填充模式。

返回值：

- Array\<Byte> - 签名后的数据。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 设置摘要方法失败、设置填充模式失败或签名失败，抛出异常。

### func toString()

```cangjie
public override func toString(): String
```

功能：输出私钥种类。

返回值：

- String - 密钥类别描述。