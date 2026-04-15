### init(RequestMethod, HttpData, ?HttpDataType, Bool, UInt32, HashMap\<String,String>, UInt32, UInt32, ?HttpProtocol, UsingProxy, String, Int64, Int64, ClientCert, String, Array\<String>, UInt32, Array\<MultiFormData>)

```cangjie
public init(method!: RequestMethod = RequestMethod.Get, extraData!: HttpData = HttpData.StringData(""),
    expectDataType!: ?HttpDataType = None, usingCache!: Bool = true, priority!: UInt32 = 1,
    header!: HashMap<String, String> = HashMap<String, String>(), readTimeout!: UInt32 = 60000,
    connectTimeout!: UInt32 = 60000, usingProtocol!: ?HttpProtocol = None,
    usingProxy!: UsingProxy = UsingProxy.UseDefault, caPath!: String = "", resumeFrom!: Int64 = 0,
    resumeTo!: Int64 = 0, clientCert!: ClientCert = ClientCert("", ""), dnsOverHttps!: String = "",
    dnsServers!: Array<String> = Array<String>(), maxLimit!: UInt32 = 5 * 1024 * 1024,
    multiFormDataList!: Array<MultiFormData> = Array<MultiFormData>())
```

**功能：** 构造HttpRequestOptions实例。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**