## class WifiEapConfig

```cangjie
public class WifiEapConfig <: ToString {
    public WifiEapConfig(
        public let eapMethod: EapMethod,
        public let phase2Method: Phase2Method,
        public let identity: String,
        public let anonymousIdentity: String,
        public let password: String,
        public let caCertAlias: String,
        public let caPath: String,
        public let clientCertAlias: String,
        public let certEntry: Array<UInt8>,
        public let certPassword: String,
        public let altSubjectMatch: String,
        public let domainSuffixMatch: String,
        public let realm: String,
        public let plmn: String,
        public let eapSubId: Int32
    )
}
```

**功能：** 可扩展身份验证协议配置信息。

**系统能力：** SystemCapability.Communication.WiFi.STA

**起始版本：** 19

**父类型：**

- ToString

### let altSubjectMatch

```cangjie
public let altSubjectMatch: String
```

**功能：** 替代主题匹配。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let anonymousIdentity

```cangjie
public let anonymousIdentity: String
```

**功能：** 匿名身份。暂未使用。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let caCertAlias

```cangjie
public let caCertAlias: String
```

**功能：** CA 证书别名。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let caPath

```cangjie
public let caPath: String
```

**功能：** CA 证书路径。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let certEntry

```cangjie
public let certEntry: Array<UInt8>
```

**功能：** CA证书内容。当eapMethod为EAP_TLS时，如果该字段为空，则clientCertAlias不能为空。

**类型：** Array\<UInt8>

**读写能力：** 只读

**起始版本：** 19

### let certPassword

```cangjie
public let certPassword: String
```

**功能：** CA证书密码。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let clientCertAlias

```cangjie
public let clientCertAlias: String
```

**功能：** 客户端证书别名。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let domainSuffixMatch

```cangjie
public let domainSuffixMatch: String
```

**功能：** 域后缀匹配。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let eapMethod

```cangjie
public let eapMethod: EapMethod
```

**功能：** EAP认证方式。

**类型：** [EapMethod](#enum-eapmethod)

**读写能力：** 只读

**起始版本：** 19

### let eapSubId

```cangjie
public let eapSubId: Int32
```

**功能：** SIM卡的子ID。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let identity

```cangjie
public let identity: String
```

**功能：** 身份信息。当eapMethod为EAP_PEAP、EAP_TLS或EAP_PWD时，该字段不能为空串。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let password

```cangjie
public let password: String
```

**功能：** 密码。当eapMethod为EAP_PEAP或EAP_PWD时，该字段不能为空串。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let phase2Method

```cangjie
public let phase2Method: Phase2Method
```

**功能：** 第二阶段认证方式。只有eapMethod为EAP_PEAP或EAP_TTLS时需要填写。

**类型：** [Phase2Method](#enum-phase2method)

**读写能力：** 只读

**起始版本：** 19

### let plmn

```cangjie
public let plmn: String
```

**功能：** 公共陆地移动网的直通凭证提供商。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let realm

```cangjie
public let realm: String
```

**功能：** 通行证凭证的领域。

**类型：** String

**读写能力：** 只读

**起始版本：** 19