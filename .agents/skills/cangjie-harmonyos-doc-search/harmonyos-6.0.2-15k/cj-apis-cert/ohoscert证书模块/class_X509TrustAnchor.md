## class X509TrustAnchor

```cangjie
public class X509TrustAnchor {
    public var CACert: ?X509Cert = Option.None
    public var CAPubKey: ?Array<UInt8> = Option.None
    public var CASubject: ?Array<UInt8> = Option.None
    public var nameConstraints: ?Array<UInt8> = Option.None
    public init()
}
```

**功能：** 表示X509信任锚，用于校验证书链。使用信任锚中的证书或者公钥作为可信根，对证书链进行校验。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### var CACert

```cangjie
public var CACert: ?X509Cert = Option.None
```

**功能：** 信任的CA证书。

**类型：** ?[X509Cert](#class-x509cert)

**读写能力：** 可读写

**起始版本：** 19

### var CAPubKey

```cangjie
public var CAPubKey: ?Array<UInt8> = Option.None
```

**功能：** 信任的CA证书公钥，DER格式。

**类型：** ?Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### var CASubject

```cangjie
public var CASubject: ?Array<UInt8> = Option.None
```

**功能：** 信任的CA证书主题，DER格式。

**类型：** ?Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### var nameConstraints

```cangjie
public var nameConstraints: ?Array<UInt8> = Option.None
```

**功能：** 名称约束，DER格式。

**类型：** ?Array\<UInt8>

**读写能力：** 可读写

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** 构造X509TrustAnchor实例。

**起始版本：** 19