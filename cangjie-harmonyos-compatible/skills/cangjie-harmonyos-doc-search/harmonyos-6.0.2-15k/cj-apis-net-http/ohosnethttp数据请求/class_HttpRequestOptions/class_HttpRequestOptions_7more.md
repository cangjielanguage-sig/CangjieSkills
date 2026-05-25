## class HttpRequestOptions

```cangjie
public class HttpRequestOptions {
    public HttpRequestOptions(
        public let method!: RequestMethod = RequestMethod.GET,
        public let extraData!: ?HttpData = None,
        public let expectDataType!: ?HttpDataType = None,
        public let usingCache!: Bool = true,
        public let priority!: UInt32 = 1,
        public let header!: ?HashMap<String, String> = None,
        public let readTimeout!: UInt32 = 60000,
        public let connectTimeout!: UInt32 = 60000,
        public let usingProtocol!: ?HttpProtocol = None,
        public let usingProxy!: UsingProxy = USE_DEFAULT,
        public let caPath!: ?String = None,
        public let resumeFrom!: ?Int64 = None,
        public let resumeTo!: ?Int64 = None,
        public let clientCert!: ?ClientCert = None,
        public let dnsOverHttps!: ?String = None,
        public let dnsServers!: ?Array<String> = None,
        public let maxLimit!: UInt32 = 5 * 1024 * 1024,
        public let multiFormDataList!: ?Array<MultiFormData> = None
    ) {}
}
```

**功能：** 发起请求可选参数的类型和取值范围。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### let caPath

```cangjie
public let caPath: ?String = None
```

**功能：** 如果设置了此参数，系统将使用用户指定路径的CA证书，(开发者需保证该路径下CA证书的可访问性)，否则将使用系统预设CA证书，系统预设CA证书位置：/etc/ssl/certs/cacert.pem。证书路径为沙箱映射路径（开发者可通过Global.getContext().filesDir获取应用沙箱路径）。目前仅支持后缀名为.pem的文本格式证书。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### let clientCert

```cangjie
public let clientCert: ?ClientCert = None
```

**功能：** 支持传输客户端证书。

**类型：** ?[ClientCert](#class-clientcert)

**读写能力：** 只读

**起始版本：** 12

### let connectTimeout

```cangjie
public let connectTimeout: UInt32 = 60000
```

**功能：** 连接超时时间。单位为毫秒（ms），默认为60000ms。

**类型：** UInt32

**读写能力：** 只读

**起始版本：** 12

### let dnsOverHttps

```cangjie
public let dnsOverHttps: ?String = None
```

**功能：** 设置使用HTTPS协议的服务器进行DNS解析。<br />参数必须以以下格式进行URL编码："https:// host:port/path"。

**类型：** ?String

**读写能力：** 只读

**起始版本：** 12

### let dnsServers

```cangjie
public let dnsServers: ?Array<String> = None
```

**功能：** 设置指定的DNS服务器进行DNS解析。<br />可以设置多个DNS解析服务器，最多3个服务器。如果有3个以上，只取前3个。<br />服务器必须是IPv4或者IPv6地址。

**类型：** ?Array\<String>

**读写能力：** 只读

**起始版本：** 12

### let expectDataType

```cangjie
public let expectDataType: ?HttpDataType = None
```

**功能：** 指定返回数据的类型，默认无此字段。如果设置了此参数，系统将优先返回指定的类型。

**类型：** ?[HttpDataType](#enum-httpdatatype)

**读写能力：** 只读

**起始版本：** 12