## struct KeyUsage

```cangjie
public struct KeyUsage <: ToString {
    public static let DigitalSignature: UInt16 = 0x0080
    public static let NonRepudiation: UInt16 = 0x0040
    public static let KeyEncipherment: UInt16 = 0x0020
    public static let DataEncipherment: UInt16 = 0x0010
    public static let KeyAgreement: UInt16 = 0x0008
    public static let CertSign: UInt16 = 0x0004
    public static let CRLSign: UInt16 = 0x0002
    public static let EncipherOnly: UInt16 = 0x0001
    public static let DecipherOnly: UInt16 = 0x0100
    public init(keys: UInt16)
}
```

功能：数字证书扩展字段中通常会包含携带公钥的用法说明，目前支持的用途有：DigitalSignature、NonRepudiation、KeyEncipherment、DataEncipherment、KeyAgreement、CertSign、CRLSign、EncipherOnly、DecipherOnly。

父类型：

- ToString

### static let CRLSign

```cangjie
public static let CRLSign: UInt16 = 0x0002
```

功能：表示私钥可用于对 CRL 签名，而公钥可用于验证 CRL 签名。

类型：UInt16

### static let CertSign

```cangjie
public static let CertSign: UInt16 = 0x0004
```

功能：表示私钥用于证书签名，而公钥用于验证证书签名，专用于 CA 证书。

类型：UInt16

### static let DataEncipherment

```cangjie
public static let DataEncipherment: UInt16 = 0x0010
```

功能：表示公钥用于直接加密数据。

类型：UInt16

### static let DecipherOnly

```cangjie
public static let DecipherOnly: UInt16 = 0x0100
```

功能：表示证书中的公钥在密钥协商过程中，仅仅用于解密计算，配合 key Agreement 使用才有意义。

类型：UInt16

### static let DigitalSignature

```cangjie
public static let DigitalSignature: UInt16 = 0x0080
```

功能：表示私钥可以用于除了签发证书、签发 CRL 和非否认性服务的各种数字签名操作，而公钥用来验证这些签名。

类型：UInt16

### static let EncipherOnly

```cangjie
public static let EncipherOnly: UInt16 = 0x0001
```

功能：表示证书中的公钥在密钥协商过程中，仅仅用于加密计算，配合 key Agreement 使用才有意义。

类型：UInt16

### static let KeyAgreement

```cangjie
public static let KeyAgreement: UInt16 = 0x0008
```

功能：表示密钥用于密钥协商。

类型：UInt16

### static let KeyEncipherment

```cangjie
public static let KeyEncipherment: UInt16 = 0x0020
```

功能：表示密钥用来加密传输其他的密钥。

类型：UInt16

### static let NonRepudiation

```cangjie
public static let NonRepudiation: UInt16 = 0x0040
```

功能：表示私钥可以用于进行非否认性服务中的签名，而公钥用来验证签名。

类型：UInt16

### init(UInt16)

```cangjie
public init(keys: UInt16)
```

功能：构造指定用途的扩展密钥用法，需要注意同一个密钥可以有多种用途。

参数：

- keys: UInt16 - 密钥的用法，建议使用本结构中所提供的密钥用法变量通过按位或的方式传入参数。

### func toString()

```cangjie
public override func toString(): String
```

功能：生成密钥用途字符串。

返回值：

- String - 证书密钥用途字符串。