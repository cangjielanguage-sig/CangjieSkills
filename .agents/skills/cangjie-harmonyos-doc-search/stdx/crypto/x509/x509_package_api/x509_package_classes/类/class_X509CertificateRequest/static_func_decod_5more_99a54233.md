### static func decodeFromPem(String)

```cangjie
public static func decodeFromPem(pem: String): Array<X509CertificateRequest>
```

功能：将数字证书签名请求从 PEM 格式解码。

参数：

- pem: String - PEM 格式的数字证书签名请求字符流。

返回值：

- Array\<[X509CertificateRequest](x509_package_classes.md#class-x509certificaterequest)> - 由 PEM 格式解码出的数字证书签名请求数组。

异常：

- [X509Exception](./x509_package_exceptions.md#class-x509exception) - 字符流不符合 PEM 格式时，或文件头不符合数字证书签名请求头标准时抛出异常。

### func encodeToDer()

```cangjie
public func encodeToDer(): DerBlob
```

功能：将数字证书签名请求编码成 Der 格式。

返回值：

- [DerBlob](x509_package_structs.md#struct-derblob) - 编码后的 Der 格式的数字证书签名请求。

### func encodeToPem()

```cangjie
public func encodeToPem(): PemEntry
```

功能：将数字证书签名请求编码成 PEM 格式。

返回值：

- [PemEntry](x509_package_structs.md#struct-pementry) - 编码后的 PEM 格式的数字证书签名请求。

### func hashCode()

```cangjie
public override func hashCode(): Int64
```

功能：返回证书签名请求哈希值。

返回值：

- Int64 - 对证书签名请求对象进行哈希计算后得到的结果。

### func toString()

```cangjie
public override func toString(): String
```

功能：生成证书签名请求名称字符串，包含证书签名请求的使用者信息。

返回值：

- String - 证书签名请求名称字符串。