## struct DerBlob

```cangjie
public struct DerBlob <: Equatable<DerBlob> & Hashable {
    public init(content: Array<Byte>)
}
```

功能：Crypto 支持配置二进制证书流，用户读取二进制证书数据并创建 [DerBlob](x509_package_structs.md#struct-derblob) 对象后可将其解析成 [X509Certificate](x509_package_classes.md#class-x509certificate) / [X509CertificateRequest](x509_package_classes.md#class-x509certificaterequest) / [PublicKey](x509_package_interfaces.md#interface-publickey) / [PrivateKey](x509_package_interfaces.md#interface-privatekey) 对象。

父类型：

- Equatable\<[DerBlob](#struct-derblob)>
- Hashable

### prop body

```cangjie
public prop body: Array<Byte>
```

功能：[DerBlob](x509_package_structs.md#struct-derblob) 对象中的字符序列。

类型：Array\<Byte>

### prop size

```cangjie
public prop size: Int64
```

功能：[DerBlob](x509_package_structs.md#struct-derblob) 对象中字符序列的大小。

类型：Int64

### init(Array\<Byte>)

```cangjie
public init(content: Array<Byte>)
```

功能：构造 [DerBlob](x509_package_structs.md#struct-derblob) 对象。

参数：

- content: Array\<Byte> - 二进制字符序列。

### func hashCode()

```cangjie
public override func hashCode(): Int64
```

功能：返回 [DerBlob](x509_package_structs.md#struct-derblob) 对象哈希值。

返回值：

- Int64 - 对 [DerBlob](x509_package_structs.md#struct-derblob) 对象进行哈希计算后得到的结果。

### operator func !=(DerBlob)

```cangjie
public override operator func !=(other: DerBlob): Bool
```

功能：判不等。

参数：

- other: [DerBlob](x509_package_structs.md#struct-derblob) - 被比较的 [DerBlob](x509_package_structs.md#struct-derblob) 对象。

返回值：

- Bool - 若对象不同，返回 true；否则，返回 false。

### operator func ==(DerBlob)

```cangjie
public override operator func ==(other: DerBlob): Bool
```

功能：判等。

参数：

- other: [DerBlob](x509_package_structs.md#struct-derblob) - 被比较的 [DerBlob](x509_package_structs.md#struct-derblob) 对象。

返回值：

- Bool - 若对象相同，返回 true；否则，返回 false。