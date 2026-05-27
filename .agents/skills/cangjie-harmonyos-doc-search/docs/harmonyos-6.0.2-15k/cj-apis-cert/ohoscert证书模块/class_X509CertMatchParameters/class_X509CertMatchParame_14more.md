## class X509CertMatchParameters

```cangjie
public class X509CertMatchParameters {
    public var subjectAlternativeNames: ?Array<GeneralName> = Option.None
    public var matchAllSubjectAltNames: ?Bool = Option.None
    public var authorityKeyIdentifier: ?Array<UInt8> = Option.None
    public var minPathLenConstraint: ?Int32 = Option.None
    public var x509Cert: ?X509Cert = Option.None
    public var validDate: ?String = Option.None
    public var issuer: ?Array<UInt8> = Option.None
    public var extendedKeyUsage: ?Array<String> = Option.None
    public var nameConstraints: ?Array<UInt8> = Option.None
    public var certPolicy: ?Array<String> = Option.None
    public var privateKeyValid: ?String = Option.None
    public var keyUsage: ?Array<Bool> = Option.None
    public var serialNumber: ?BigInt = Option.None
    public var subject: ?Array<UInt8> = Option.None
    public var subjectKeyIdentifier: ?Array<UInt8> = Option.None
    public var publicKey: ?DataBlob = Option.None
    public var publicKeyAlgID: ?String = Option.None
}
```

**功能：** 用于匹配证书的过滤参数。如果参数中任一项都未指定，则匹配所有证书。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### var authorityKeyIdentifier

```cangjie
public var authorityKeyIdentifier: ?Array<UInt8> = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### var certPolicy

```cangjie
public var certPolicy: ?Array<String> = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### var extendedKeyUsage

```cangjie
public var extendedKeyUsage: ?Array<String> = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?Array\<String>

**读写能力：** 可读写

**起始版本：** 19

### var issuer

```cangjie
public var issuer: ?Array<UInt8> = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### var keyUsage

```cangjie
public var keyUsage: ?Array<Bool> = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?Array\<Bool>

**读写能力：** 可读写

**起始版本：** 19

### var matchAllSubjectAltNames

```cangjie
public var matchAllSubjectAltNames: ?Bool = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?Bool

**读写能力：** 可读写

**起始版本：** 19

### var minPathLenConstraint

```cangjie
public var minPathLenConstraint: ?Int32 = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var nameConstraints

```cangjie
public var nameConstraints: ?Array<UInt8> = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### var privateKeyValid

```cangjie
public var privateKeyValid: ?String = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var publicKey

```cangjie
public var publicKey: ?DataBlob = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?[DataBlob](#class-datablob)

**读写能力：** 可读写

**起始版本：** 19

### var publicKeyAlgID

```cangjie
public var publicKeyAlgID: ?String = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var serialNumber

```cangjie
public var serialNumber: ?BigInt = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?BigInt

**读写能力：** 可读写

**起始版本：** 19

### var subject

```cangjie
public var subject: ?Array<UInt8> = Option.None
```

**功能：** 表示指定具体的证书对象。

**类型：** ?Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19