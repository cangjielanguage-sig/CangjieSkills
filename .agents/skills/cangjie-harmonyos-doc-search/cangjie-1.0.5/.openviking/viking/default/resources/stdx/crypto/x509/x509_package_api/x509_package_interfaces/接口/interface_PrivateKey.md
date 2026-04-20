## interface PrivateKey

```cangjie
public interface PrivateKey <: Key {
    static func decodeDer(blob: DerBlob): PrivateKey
    static func decodeFromPem(text: String): PrivateKey
    static func decodeDer(blob: DerBlob, password!: ?String): PrivateKey
    static func decodeFromPem(text: String, password!: ?String): PrivateKey
    func encodeToDer(password!: ?String): DerBlob
    override func encodeToPem(): PemEntry
    func encodeToPem(password!: ?String): PemEntry
}
```

功能：提供私钥接口。

父类型：

- [Key](#interface-key)

### static func decodeDer(DerBlob)

```cangjie
static func decodeDer(blob: DerBlob): PrivateKey
```

功能：将私钥从 DER 格式解码。

参数：

- blob: [DerBlob](x509_package_structs.md#struct-derblob) - DER 格式的私钥对象。

返回值：

- [PrivateKey](x509_package_interfaces.md#interface-privatekey) - 由 DER 格式解码出的私钥。

异常：

- [X509Exception](x509_package_exceptions.md#class-x509exception) - 当 DER 格式的私钥内容不正确，无法解析时抛出异常。

### static func decodeDer(DerBlob, ?String)

```cangjie
static func decodeDer(blob: DerBlob, password!: ?String): PrivateKey
```

功能：将 DER 格式的私钥解密解码成 [PrivateKey](x509_package_interfaces.md#interface-privatekey) 对象，密码为 None 时则不解密。

参数：

- blob: [DerBlob](x509_package_structs.md#struct-derblob) - DER 格式的私钥。
- password!: ?String - 解密密码。

返回值：

- [PrivateKey](x509_package_interfaces.md#interface-privatekey) - 解密解码后的私钥对象。

异常：

- [X509Exception](x509_package_exceptions.md#class-x509exception) - 解密解码失败，或者`password`为空字符串。

### static func decodeFromPem(String)

```cangjie
static func decodeFromPem(text: String): PrivateKey
```

功能：将私钥从 PEM 格式解码。

参数：

- text: String - PEM 格式的私钥字符流。

返回值：

- [PrivateKey](x509_package_interfaces.md#interface-privatekey) - 由 PEM 格式解码出的私钥。

异常：

- [X509Exception](x509_package_exceptions.md#class-x509exception) - 字符流不符合 PEM 格式，或文件头不符合公钥头标准时抛出异常。

### static func decodeFromPem(String, ?String)

```cangjie
static func decodeFromPem(text: String, password!: ?String): PrivateKey
```

功能：将 PEM 格式的私钥解密解码成 [PrivateKey](x509_package_interfaces.md#interface-privatekey) 对象，密码为 None 时则不解密。

参数：

- text: String - PEM 格式的私钥。
- password!: ?String - 解密密码。

返回值：

- [PrivateKey](x509_package_interfaces.md#interface-privatekey) - 解密解码后的私钥对象。

异常：

- [X509Exception](x509_package_exceptions.md#class-x509exception) - 解密解码失败，或者`password`为空字符串。

### func encodeToDer(?String)

```cangjie
func encodeToDer(password!: ?String): DerBlob
```

功能：将私钥加密编码成 DER 格式，密码为 None 时则不加密。

参数：

- password!: ?String - 加密密码。

返回值：

- [DerBlob](x509_package_structs.md#struct-derblob) - 加密后的 DER 格式的私钥。

异常：

- [X509Exception](x509_package_exceptions.md#class-x509exception) - 加密失败，或者`password`为空字符串。

### func encodeToPem()

```cangjie
override func encodeToPem(): PemEntry
```

功能：将私钥编码成 PEM 格式。

返回值：

- [PemEntry](x509_package_structs.md#struct-pementry) - 编码后的 PEM 格式的私钥。

异常：

- [X509Exception](x509_package_exceptions.md#class-x509exception) - 编码失败。

### func encodeToPem(?String)

```cangjie
func encodeToPem(password!: ?String): PemEntry
```

功能：将私钥加密编码成 PEM 格式，密码为 None 时则不加密。

参数：

- password!: ?String - 加密密码。

返回值：

- [PemEntry](x509_package_structs.md#struct-pementry) - 加密后的 PEM 格式的私钥。

异常：

- [X509Exception](x509_package_exceptions.md#class-x509exception) - 加密失败，或者`password`为空字符串。