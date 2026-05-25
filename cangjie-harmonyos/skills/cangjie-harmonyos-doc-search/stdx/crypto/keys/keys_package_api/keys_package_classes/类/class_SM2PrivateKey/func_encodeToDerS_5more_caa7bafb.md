### func encodeToDer(?String)

```cangjie
public func encodeToDer(password!: ?String): DerBlob
```

功能：使用 AES-256-CBC 加密私钥，将私钥编码为 DER 格式。

参数：

- password!: ?String - 加密私钥需要提供的密码，密码为 None 时则不加密。

返回值：

- [DerBlob](../../x509/x509_package_api/x509_package_structs.md#struct-derblob) - 编码后的 DER 格式公钥。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 编码失败、加密失败或者参数密码为空字符串，抛出异常。

### func encodeToPem(?String)

```cangjie
public func encodeToPem(password!: ?String): PemEntry
```

功能：将加密的私钥编码为 PEM 格式。

参数：

- password!: ?String - 加密私钥需要提供的密码，密码为 None 时则不加密。

返回值：

- [PemEntry](../../x509/x509_package_api/x509_package_structs.md#struct-pementry) - 私钥 PEM 格式的对象。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 编码失败、加密失败或者参数密码为空字符串，抛出异常。

### func encodeToPem()

```cangjie
public func encodeToPem(): PemEntry
```

功能：将私钥编码为 PEM 格式。

返回值：

- [PemEntry](../../x509/x509_package_api/x509_package_structs.md#struct-pementry) - 私钥 PEM 格式的对象。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 编码失败，抛出异常。

### func sign(Array\<Byte>)

```cangjie
public func sign(data: Array<Byte>): Array<Byte>
```

功能：sign 对数据进行签名，SM2 采用 [SM3](../../digest/digest_package_api/digest_package_classes.md#class-sm3) 数据摘要算法。

参数：

- data: Array\<Byte> - 数据。

返回值：

- Array\<Byte> - 签名后的数据。

异常：

- [CryptoException](../../digest/digest_package_api/digest_package_exceptions.md#class-cryptoexception) - 签名失败，抛出异常。

### func toString()

```cangjie
public override func toString(): String
```

功能：输出私钥种类。

返回值：

- String - 密钥类别描述。