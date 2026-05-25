## struct PemEntry

```cangjie
public struct PemEntry <: ToString {
    public static let LABEL_CERTIFICATE = "CERTIFICATE"
    public static let LABEL_X509_CRL = "X509 CRL"
    public static let LABEL_CERTIFICATE_REQUEST = "CERTIFICATE REQUEST"
    public static let LABEL_PRIVATE_KEY = "PRIVATE KEY"
    public static let LABEL_EC_PRIVATE_KEY = "EC PRIVATE KEY"
    public static let LABEL_ENCRYPTED_PRIVATE_KEY = "ENCRYPTED PRIVATE KEY"
    public static let LABEL_RSA_PRIVATE_KEY = "RSA PRIVATE KEY"
    public static let LABEL_SM2_PRIVATE_KEY = "SM2 PRIVATE KEY"
    public static let LABEL_PUBLIC_KEY = "PUBLIC KEY"
    public static let LABEL_EC_PARAMETERS = "EC PARAMETERS"
    public static let LABEL_DH_PARAMETERS = "DH PARAMETERS"
    public PemEntry(
        public let label: String,
        public let headers: Array<(String, String)>,
        public let body: ?DerBlob
    )
    public init(label: String, body: DerBlob)
}
```

功能：PEM 文本格式经常用于存储证书和密钥，PEM 编码结构包含以下几个部分：

第一行是 “-----BEGIN”，标签和 “-----” 组成的 utf8 编码的字符串；
中间是正文，是实际二进制内容经过 base64 编码得到的可打印字符串，详细的 PEM 编码规范可参考 [RFC 7468](https://www.rfc-editor.org/rfc/rfc7468.html)；
最后一行是 “-----END”，标签和 “-----” 组成的 utf8 编码的字符串，详见 [RFC 1421](https://www.rfc-editor.org/rfc/rfc1421.html)。
在旧版的 PEM 编码标准中在第一行和正文之间还包含条目头。

为了支持不同的用户场景，我们提供了 [PemEntry](x509_package_structs.md#struct-pementry) 和 [Pem](x509_package_structs.md#struct-pem) 类型，[PemEntry](x509_package_structs.md#struct-pementry) 用于存储单个 PEM 基础结构。

父类型：

- ToString

### static let LABEL_CERTIFICATE

```cangjie
public static let LABEL_CERTIFICATE = "CERTIFICATE"
```

功能：记录条目类型为证书。

类型：String

### static let LABEL_CERTIFICATE_REQUEST

```cangjie
public static let LABEL_CERTIFICATE_REQUEST = "CERTIFICATE REQUEST"
```

功能：记录条目类型为证书签名请求。

类型：String

### static let LABEL_DH_PARAMETERS

```cangjie
public static let LABEL_DH_PARAMETERS = "DH PARAMETERS"
```

功能：记录条目类型为 DH 密钥参数。

类型：String

### static let LABEL_EC_PARAMETERS

```cangjie
public static let LABEL_EC_PARAMETERS = "EC PARAMETERS"
```

功能：记录条目类型为椭圆曲线参数。

类型：String

### static let LABEL_EC_PRIVATE_KEY

```cangjie
public static let LABEL_EC_PRIVATE_KEY = "EC PRIVATE KEY"
```

功能：记录条目类型为椭圆曲线私钥。

类型：String

### static let LABEL_ENCRYPTED_PRIVATE_KEY

```cangjie
public static let LABEL_ENCRYPTED_PRIVATE_KEY = "ENCRYPTED PRIVATE KEY"
```

功能：记录条目类型为 PKCS #8 标准加密的私钥。

类型：String

### static let LABEL_PRIVATE_KEY

```cangjie
public static let LABEL_PRIVATE_KEY = "PRIVATE KEY"
```

功能：记录条目类型为 PKCS #8 标准未加密的私钥。

类型：String

### static let LABEL_PUBLIC_KEY

```cangjie
public static let LABEL_PUBLIC_KEY = "PUBLIC KEY"
```

功能：记录条目类型为公钥。

类型：String

### static let LABEL_RSA_PRIVATE_KEY

```cangjie
public static let LABEL_RSA_PRIVATE_KEY = "RSA PRIVATE KEY"
```

功能：记录条目类型为 RSA 私钥。

类型：String

### static let LABEL_SM2_PRIVATE_KEY

```cangjie
public static let LABEL_SM2_PRIVATE_KEY = "SM2 PRIVATE KEY"
```

功能：记录条目类型为 SM2 私钥。

类型：String

### static let LABEL_X509_CRL

```cangjie
public static let LABEL_X509_CRL = "X509 CRL"
```

功能：记录条目类型为证书吊销列表。

类型：String