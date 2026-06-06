## class CertChainBuildParameters

```cangjie
public class CertChainBuildParameters {
    public CertChainBuildParameters(
        public var certMatchParameters: X509CertMatchParameters,
        public var validationParameters: CertChainValidationParameters,
        public var maxLength!: ?Int32 = Option.None
    )
}
```

**功能：** 用于指定证书链创建参数。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

### var certMatchParameters

```cangjie
public var certMatchParameters: X509CertMatchParameters
```

**功能：** 指定过滤条件。

**类型：** [X509CertMatchParameters](#class-x509certmatchparameters)

**读写能力：** 可读写

**起始版本：** 19

### var maxLength

```cangjie
public var maxLength: ?Int32 = Option.None
```

**功能：** 指定验证条件。

**类型：** ?Int32

**读写能力：** 可读写

**起始版本：** 19

### var validationParameters

```cangjie
public var validationParameters: CertChainValidationParameters
```

**功能：** 指定最终证书链中CA证书的最大长度。

**类型：** [CertChainValidationParameters](#class-certchainvalidationparameters)

**读写能力：** 可读写

**起始版本：** 19

### CertChainBuildParameters(X509CertMatchParameters, CertChainValidationParameters, ?Int32)

```cangjie
public CertChainBuildParameters(
    public var certMatchParameters: X509CertMatchParameters,
    public var validationParameters: CertChainValidationParameters,
    public var maxLength!: ?Int32 = Option.None
)
```

**功能：** 构造CertChainBuildParameters实例。

**系统能力：** SystemCapability.Security.Cert

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|certMatchParameters|[X509CertMatchParameters](#class-x509certmatchparameters)|是|-|指定过滤条件。|
|validationParameters|[CertChainValidationParameters](#class-certchainvalidationparameters)|是|-|指定验证条件。|
|maxLength|?Int32|否|Option.None| **命名参数。** 指定最终证书链中CA证书的最大长度。|