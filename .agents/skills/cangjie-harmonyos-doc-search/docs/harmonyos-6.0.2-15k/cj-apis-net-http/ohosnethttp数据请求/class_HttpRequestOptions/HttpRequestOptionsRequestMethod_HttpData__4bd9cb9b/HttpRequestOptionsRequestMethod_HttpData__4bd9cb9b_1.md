### HttpRequestOptions(RequestMethod, ?HttpData, ?HttpDataType, Bool, UInt32, ?HashMap\<String,String>, UInt32, UInt32, ?HttpProtocol, UsingProxy, ?String, ?Int64, ?Int64, ?ClientCert, ?String, ?Array\<String>, UInt32, ?Array\<MultiFormData>)

```cangjie
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
)
```

**功能：** 构造HttpRequestOptions实例。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**