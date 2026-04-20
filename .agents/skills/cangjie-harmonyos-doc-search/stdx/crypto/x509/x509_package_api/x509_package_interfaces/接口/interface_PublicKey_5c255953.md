## interface PublicKey

```cangjie
public interface PublicKey <: Key {
    override func encodeToPem(): PemEntry
    static func decodeDer(blob: DerBlob): PublicKey
    static func decodeFromPem(text: String): PublicKey
}
```

功能：公钥接口。

父类型：

- [Key](#interface-key)

### static func decodeDer(DerBlob)

```cangjie
static func decodeDer(blob: DerBlob): PublicKey
```

功能：将公钥从 DER 格式解码。

参数：

- blob: [DerBlob](x509_package_structs.md#struct-derblob) - DER 格式的公钥对象。

返回值：

- [PublicKey](x509_package_interfaces.md#interface-publickey) - 由 DER 格式解码出的公钥。

异常：

- [X509Exception](x509_package_exceptions.md#class-x509exception) - 当 DER 格式的公钥内容不正确，无法解析时抛出异常。

### static func decodeFromPem(String)

```cangjie
static func decodeFromPem(text: String): PublicKey
```

功能：将公钥从 PEM 格式解码。

参数：

- text: String - PEM 格式的公钥字符流。

返回值：

- [PublicKey](x509_package_interfaces.md#interface-publickey) - 由 PEM 格式解码出的公钥。

异常：

- [X509Exception](x509_package_exceptions.md#class-x509exception) - 字符流不符合 PEM 格式，或文件头不符合公钥头标准时抛出异常。

### func encodeToPem()

```cangjie
override func encodeToPem(): PemEntry
```

功能：将公钥编码为 PEM 格式。

返回值：

- [PemEntry](x509_package_structs.md#struct-pementry) - 公钥数据 PEM 格式编码生成的对象。