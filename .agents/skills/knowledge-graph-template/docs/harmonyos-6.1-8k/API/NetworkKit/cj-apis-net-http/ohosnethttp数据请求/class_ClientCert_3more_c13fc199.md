## class ClientCert

```cangjie
public class ClientCert {
    public var certPath: String
    public var keyPath: String
    public var certType: CertType
    public var keyPassword: String
    public init(certPath: String, keyPath: String, certType!: CertType = CertType.Pem, keyPassword!: String = "")
}
```

**功能：** 客户端证书类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var certPath

```cangjie
public var certPath: String
```

**功能：** 证书路径。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var certType

```cangjie
public var certType: CertType
```

**功能：** 证书类型。

**类型：** [CertType](#enum-certtype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var keyPassword

```cangjie
public var keyPassword: String
```

**功能：** 证书密钥的密码。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var keyPath

```cangjie
public var keyPath: String
```

**功能：** 证书密钥的路径。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### init(String, String, CertType, String)

```cangjie
public init(certPath: String, keyPath: String, certType!: CertType = CertType.Pem, keyPassword!: String = "")
```

**功能：** 构造ClientCert实例。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|certPath|String|是|-|证书路径。|
|keyPath|String|是|-|证书密钥的路径。|
|certType|[CertType](#enum-certtype)|否|CertType.Pem|**命名参数。** 证书类型，默认是CertType.Pem。|
|keyPassword|String|否|""|**命名参数。** 证书密钥的密码。默认值为空字符串。|

## class DataReceiveProgressInfo

```cangjie
public class DataReceiveProgressInfo {
    public var receiveSize: Int64
    public var totalSize: Int64
}
```

**功能：** 数据接收信息。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var receiveSize

```cangjie
public var receiveSize: Int64
```

**功能：** 已接收的数据量（单位：字节）。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var totalSize

```cangjie
public var totalSize: Int64
```

**功能：** 总共要接收的数据量（单位：字节）。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

## class DataSendProgressInfo

```cangjie
public class DataSendProgressInfo {
    public var sendSize: Int64
    public var totalSize: Int64
}
```

**功能：** 数据发送信息。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var sendSize

```cangjie
public var sendSize: Int64
```

**功能：** 每次发送的数据量(单位：字节)。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var totalSize

```cangjie
public var totalSize: Int64
```

**功能：** 总共要发送的数据量(单位：字节)。

**类型：** Int64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22