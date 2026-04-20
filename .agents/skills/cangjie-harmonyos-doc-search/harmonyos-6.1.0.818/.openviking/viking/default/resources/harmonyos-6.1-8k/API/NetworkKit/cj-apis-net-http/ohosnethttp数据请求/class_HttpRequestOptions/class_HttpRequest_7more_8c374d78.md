## class HttpRequestOptions

```cangjie
public class HttpRequestOptions {
    public var method: RequestMethod
    public var extraData: HttpData
    public var expectDataType: ?HttpDataType
    public var usingCache: Bool
    public var priority: UInt32
    public var header: HashMap<String, String>
    public var readTimeout: UInt32
    public var connectTimeout: UInt32
    public var usingProtocol: ?HttpProtocol
    public var usingProxy: UsingProxy
    public var caPath: String
    public var resumeFrom: Int64
    public var resumeTo: Int64
    public var clientCert: ClientCert
    public var dnsOverHttps: String
    public var dnsServers: Array<String>
    public var maxLimit: UInt32
    public var multiFormDataList: Array<MultiFormData>
    public init(method!: RequestMethod = RequestMethod.Get, extraData!: HttpData = HttpData.StringData(""),
        expectDataType!: ?HttpDataType = None, usingCache!: Bool = true, priority!: UInt32 = 1,
        header!: HashMap<String, String> = HashMap<String, String>(), readTimeout!: UInt32 = 60000,
        connectTimeout!: UInt32 = 60000, usingProtocol!: ?HttpProtocol = None,
        usingProxy!: UsingProxy = UsingProxy.UseDefault, caPath!: String = "", resumeFrom!: Int64 = 0,
        resumeTo!: Int64 = 0, clientCert!: ClientCert = ClientCert("", ""), dnsOverHttps!: String = "",
        dnsServers!: Array<String> = Array<String>(), maxLimit!: UInt32 = 5 * 1024 * 1024,
        multiFormDataList!: Array<MultiFormData> = Array<MultiFormData>())
}
```

**功能：** 发起HTTP请求时，可选配置信息。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var caPath

```cangjie
public var caPath: String
```

**功能：** 如果设置了此参数，系统将使用用户指定路径的CA证书（开发者需保证该路径下CA证书的可访问性），否则将使用系统预设CA证书。<br />系统预设CA证书位置：/etc/ssl/certs/cacert.pem。证书路径为沙箱映射路径（开发者可通过UIAbilityContext提供的能力获取应用沙箱路径）。目前仅支持后缀名为.pem的文本格式证书。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var clientCert

```cangjie
public var clientCert: ClientCert
```

**功能：** 支持传输客户端证书。

**类型：** [ClientCert](#class-clientcert)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var connectTimeout

```cangjie
public var connectTimeout: UInt32
```

**功能：** 连接超时时间。单位为毫秒（ms）。传入值需为UInt32范围内的整数。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var dnsOverHttps

```cangjie
public var dnsOverHttps: String
```

**功能：** 设置使用HTTPS协议的服务器进行DNS解析。<br />- 参数必须根据以下格式进行URL编码："https:// host:port/path"。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var dnsServers

```cangjie
public var dnsServers: Array<String>
```

**功能：** 设置指定的DNS服务器进行DNS解析。<br />- 最多可以设置3个DNS解析服务器。如果有3个以上，只取前3个。<br />- 服务器必须是IPV4或者IPV6地址。

**类型：** Array\<String>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var expectDataType

```cangjie
public var expectDataType:?HttpDataType
```

**功能：** 指定返回数据的类型。如果设置了此参数，系统将优先返回指定的类型。

**类型：** ?[HttpDataType](#enum-httpdatatype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22