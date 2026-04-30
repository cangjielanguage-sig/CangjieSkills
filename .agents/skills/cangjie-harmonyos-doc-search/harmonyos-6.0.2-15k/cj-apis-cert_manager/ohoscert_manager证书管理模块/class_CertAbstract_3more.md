## class CertAbstract

```cangjie
public class CertAbstract {}
```

**功能：** 表示证书简要信息。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

### let certAlias

```cangjie
public let certAlias: String
```

**功能：** 表示证书的别名。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let state

```cangjie
public let state: Bool
```

**功能：** 表示证书的状态，true为启用状态、false为禁用状态。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let subjectName

```cangjie
public let subjectName: String
```

**功能：** 表示证书的使用者名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let uri

```cangjie
public let uri: String
```

**功能：** 表示证书的唯一标识符。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

## class CertInfo

```cangjie
public class CertInfo {}
```

**功能：** 表示证书详细信息。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

### let cert

```cangjie
public let cert: Array<UInt8>
```

**功能：** 表示证书二进制数据。

**类型：** Array\<UInt8>

**读写能力：** 只读

**起始版本：** 19

### let certAlias

```cangjie
public let certAlias: String
```

**功能：** 表示证书的别名。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let fingerprintSha256

```cangjie
public let fingerprintSha256: String
```

**功能：** 表示证书的指纹值。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let issuerName

```cangjie
public let issuerName: String
```

**功能：** 表示证书的颁发者名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let notAfter

```cangjie
public let notAfter: String
```

**功能：** 表示证书有效期截止日期。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let notBefore

```cangjie
public let notBefore: String
```

**功能：** 表示证书有效期起始日期。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let serial

```cangjie
public let serial: String
```

**功能：** 表示证书的序列号。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let state

```cangjie
public let state: Bool
```

**功能：** 表示证书的状态，true为启用状态、false为禁用状态。

**类型：** Bool

**读写能力：** 只读

**起始版本：** 19

### let subjectName

```cangjie
public let subjectName: String
```

**功能：** 表示证书的使用者名称。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let uri

```cangjie
public let uri: String
```

**功能：** 表示证书的唯一标识符。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

## class Credential

```cangjie
public class Credential {}
```

**功能：** 表示凭据详细信息。

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 19

### let alias

```cangjie
public let alias: String
```

**功能：** 表示凭据的别名。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let certNum

```cangjie
public let certNum: Int32
```

**功能：** 表示凭据中包含的证书个数。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let credentialData

```cangjie
public let credentialData: Array<UInt8>
```

**功能：** 表示凭据二进制数据。

**类型：** Array\<UInt8>

**读写能力：** 只读

**起始版本：** 19

### let credentialType

```cangjie
public let credentialType: String
```

**功能：** 表示凭据的类型。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### let keyNum

```cangjie
public let keyNum: Int32
```

**功能：** 表示凭据中包含的密钥个数。

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### let keyUri

```cangjie
public let keyUri: String
```

**功能：** 表示凭据的唯一标识符。

**类型：** String

**读写能力：** 只读

**起始版本：** 19