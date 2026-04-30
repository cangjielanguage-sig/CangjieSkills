## class ClientCert

```cangjie
public class ClientCert {
    public ClientCert(
        public let certPath: String,
        public let keyPath: String,
        public let certType!: CertType = CertType.PEM,
        public let keyPassword!: ?String = None
    )
}
```

**功能：** 客户端证书类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### let certPath

```cangjie
public let certPath: String
```

**功能：** 证书路径。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let certType

```cangjie
public let certType: CertType = CertType.PEM
```

**功能：** 证书类型，默认是PEM。

**类型：** [CertType](#enum-certtype)

**读写能力：** 只读

**起始版本：** 12

### let keyPassword

```cangjie
public let keyPassword: ?String = None
```

**功能：** 证书秘钥的密码。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### let keyPath

```cangjie
public let keyPath: String
```

**功能：** 证书秘钥的路径。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### ClientCert(String, String, CertType, ?String)

```cangjie
public ClientCert(
    public let certPath: String,
    public let keyPath: String,
    public let certType!: CertType = CertType.PEM,
    public let keyPassword!: ?String = None
)
```

**功能：** 构建ClientCert实例。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|certPath|String|是|-|证书路径。|
|keyPath|String|是|-|证书秘钥的路径。|
|certType|[CertType](#enum-certtype)|否|CertType.PEM| **命名参数。** 证书类型，默认是PEM。|
|keyPassword|?String|否|None| **命名参数。** 证书秘钥的密码。|

## class DataReceiveProgressInfo

```cangjie
public class DataReceiveProgressInfo {}
```

**功能：** 数据接收信息。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### let receiveSize

```cangjie
public let receiveSize: UInt32
```

**功能：** 已接收的数据量单位为字节。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let totalSize

```cangjie
public let totalSize: UInt32
```

**功能：** 总共要接收的数据量单位为字节。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

## class DataSendProgressInfo

```cangjie
public class DataSendProgressInfo {}
```

**功能：** 数据发送信息。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### let sendSize

```cangjie
public let sendSize: UInt32
```

**功能：** 每次发送的数据量单位为字节。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let totalSize

```cangjie
public let totalSize: UInt32
```

**功能：** 总共要发送的数据量单位为字节。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12