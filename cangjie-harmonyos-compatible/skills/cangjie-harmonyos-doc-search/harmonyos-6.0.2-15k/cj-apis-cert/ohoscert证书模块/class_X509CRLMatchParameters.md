## class X509CRLMatchParameters

```cangjie
public class X509CRLMatchParameters {
    public var issuer: ?Array<Array<UInt8>> = Option.None
    public var x509Cert: ?X509Cert = Option.None
    public var updateDateTime: ?String = Option.None
    public var maxCRL: ?BigInt = Option.None
    public var minCRL: ?BigInt = Option.None
}
```

**功能：** 用于匹配证书吊销列表的过滤参数。如果参数中任一项都未指定，则匹配所有证书吊销列表。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### var issuer

```cangjie
public var issuer: ?Array<Array<UInt8>> = Option.None
```

**功能：** 指定颁发者作为过滤条件，至少要匹配到其中一个issuer。

**类型：** ?Array\<Array\<UInt8>>

**读写能力：** 可读写

**起始版本：** 19

### var maxCRL

```cangjie
public var maxCRL: ?BigInt = Option.None
```

**功能：** 指定CRL个数最大值。

**类型：** ?BigInt

**读写能力：** 可读写

**起始版本：** 19

### var minCRL

```cangjie
public var minCRL: ?BigInt = Option.None
```

**功能：** 指定CRL个数最小值。

**类型：** ?BigInt

**读写能力：** 可读写

**起始版本：** 19

### var updateDateTime

```cangjie
public var updateDateTime: ?String = Option.None
```

**功能：** 指定证书更新时间。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var x509Cert

```cangjie
public var x509Cert: ?X509Cert = Option.None
```

**功能：** 指定具体的证书对象作为过滤条件，判断该证书是否在CRL列表中。

**类型：** ?[X509Cert](#class-x509cert)

**读写能力：** 可读写

**起始版本：** 19