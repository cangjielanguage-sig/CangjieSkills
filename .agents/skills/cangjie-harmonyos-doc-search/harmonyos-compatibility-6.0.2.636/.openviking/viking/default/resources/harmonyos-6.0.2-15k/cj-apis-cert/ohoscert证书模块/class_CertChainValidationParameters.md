## class CertChainValidationParameters

```cangjie
public class CertChainValidationParameters {
    public CertChainValidationParameters(
        public let trustAnchors!: Array<X509TrustAnchor>
    )
    public var date: ?String = Option.None
    public var certCRLs: ?Array<CertCRLCollection> = Option.None
    public var revocationCheckParam: ?RevocationCheckParameter = Option.None
    public var policy: ?ValidationPolicyType = Option.None
    public var sslHostname: ?String = Option.None
    public var keyUsage: ?Array<KeyUsageType> = Option.None
}
```

**功能：** 表示证书链校验的参数。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### var certCRLs

```cangjie
public var certCRLs: ?Array<CertCRLCollection> = Option.None
```

**功能：** 表示需要校验证书是否在证书吊销列表中。

**类型：** ?Array\<[CertCRLCollection](#class-certcrlcollection)>

**读写能力：** 可读写

**起始版本：** 19

### var date

```cangjie
public var date: ?String = Option.None
```

**功能：** 表示需要校验证书的有效期。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### var keyUsage

```cangjie
public var keyUsage: ?Array<KeyUsageType> = Option.None
```

**功能：** 表示需要校验证书中的密钥用途。

**类型：** ?Array\<[KeyUsageType](#enum-keyusagetype)>

**读写能力：** 可读写

**起始版本：** 19

### var policy

```cangjie
public var policy: ?ValidationPolicyType = Option.None
```

**功能：** 表示需要校验证书的策略类型。

**类型：** ?[ValidationPolicyType](#enum-validationpolicytype)

**读写能力：** 可读写

**起始版本：** 19

### var revocationCheckParam

```cangjie
public var revocationCheckParam: ?RevocationCheckParameter = Option.None
```

**功能：** 表示需要在线校验证书吊销状态的参数对象。

**类型：** ?[RevocationCheckParameter](#class-revocationcheckparameter)

**读写能力：** 可读写

**起始版本：** 19

### var sslHostname

```cangjie
public var sslHostname: ?String = Option.None
```

**功能：** 表示需要校验证书中主机名，与policy配合使用。

**类型：** ?String

**读写能力：** 可读写

**起始版本：** 19

### let trustAnchors

```cangjie
public let trustAnchors: Array<X509TrustAnchor>
```

**功能：** 表示信任锚列表。

**类型：** Array\<[X509TrustAnchor](#class-x509trustanchor)>

**读写能力：** 只读

**起始版本：** 19

### CertChainValidationParameters(Array\<X509TrustAnchor>)

```cangjie
public CertChainValidationParameters(
    public let trustAnchors!: Array<X509TrustAnchor>)
```

**功能：** 构造CertChainValidationParameters实例。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|trustAnchors|Array\<[X509TrustAnchor](#class-x509trustanchor)>|是| **命名参数。** 表示信任锚列表。|