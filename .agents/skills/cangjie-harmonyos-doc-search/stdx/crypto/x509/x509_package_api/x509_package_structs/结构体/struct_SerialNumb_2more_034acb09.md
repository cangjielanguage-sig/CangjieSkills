## struct SerialNumber

```cangjie
public struct SerialNumber <: Equatable<SerialNumber> & Hashable & ToString {
    public init(length!: UInt8 = 16)
}
```

功能：结构体 [SerialNumber](x509_package_structs.md#struct-serialnumber) 为数字证书的序列号，是数字证书中的一个唯一标识符，用于标识数字证书的唯一性。根据规范，证书序列号的长度不应超过 20 字节。详见 [rfc5280](https://www.rfc-editor.org/rfc/rfc5280)。

父类型：

- Equatable\<[SerialNumber](#struct-serialnumber)>
- Hashable
- ToString

### init(UInt8)

```cangjie
public init(length!: UInt8 = 16)
```

功能：生成指定长度的随机序列号。

参数：

- length!: UInt8 - 序列号长度，单位为字节，类型为 UInt8，默认值为 16。

异常：

- [X509Exception](./x509_package_exceptions.md#class-x509exception) - length 等于 0 或大于 20 时，抛出异常。

### func hashCode()

```cangjie
public override func hashCode(): Int64
```

功能：返回证书序列号哈希值。

返回值：

- Int64 - 对证书序列号对象进行哈希计算后得到的结果。

### func toString()

```cangjie
public override func toString(): String
```

功能：生成证书序列号字符串，格式为 16 进制。

返回值：

- String - 证书序列号字符串。

### operator func !=(SerialNumber)

```cangjie
public override operator func !=(other: SerialNumber): Bool
```

功能：判不等。

参数：

- other: [SerialNumber](x509_package_structs.md#struct-serialnumber) - 被比较的证书序列号对象。

返回值：

- Bool - 若序列号不同，返回 true；否则，返回 false。

### operator func ==(SerialNumber)

```cangjie
public override operator func ==(other: SerialNumber): Bool
```

功能：判等。

参数：

- other: [SerialNumber](x509_package_structs.md#struct-serialnumber) - 被比较的证书序列号对象。

返回值：

- Bool - 若序列号相同，返回 true；否则，返回 false。

## struct Signature

```cangjie
public struct Signature <: Equatable<Signature> & Hashable {
}
```

功能：数字证书的签名，用来验证身份的正确性。

父类型：

- Equatable\<[Signature](#struct-signature)>
- Hashable

### prop signatureValue

```cangjie
public prop signatureValue: DerBlob
```

功能：返回证书签名的二进制。

类型：[DerBlob](x509_package_structs.md#struct-derblob)

### func hashCode()

```cangjie
public override func hashCode(): Int64
```

功能：返回证书签名哈希值。

返回值：

- Int64 - 对证书签名对象进行哈希计算后得到的结果。

### operator func !=(Signature)

```cangjie
public override operator func !=(other: Signature): Bool
```

功能：判不等。

参数：

- other: [Signature](x509_package_structs.md#struct-signature) - 被比较的证书签名。

返回值：

- Bool - 若证书签名不同，返回 true；否则，返回 false。

### operator func ==(Signature)

```cangjie
public override operator func ==(other: Signature): Bool
```

功能：判等。

参数：

- other: [Signature](x509_package_structs.md#struct-signature) - 被比较的证书签名。

返回值：

- Bool - 若证书签名相同，返回 true；否则，返回 false。