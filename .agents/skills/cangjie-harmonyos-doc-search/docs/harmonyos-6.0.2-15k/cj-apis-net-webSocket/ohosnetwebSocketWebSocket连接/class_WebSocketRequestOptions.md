## class WebSocketRequestOptions

```cangjie
public class WebSocketRequestOptions {
    public WebSocketRequestOptions(
        public var header !: ?HashMap<String, String> = None,
        public var caPath !: String = "/etc/ssl/certs/cacert.pem",
        public var clientCert !: ?WebSocketClientCert = None,
        public var proxy !: ProxyConfiguration = SYSTEM,
        public var protocol !: String = ""
    )
}
```

**功能：** 建立WebSocket连接时，可选参数的类型和说明。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

### var caPath

```cangjie
public var caPath: String = "/etc/ssl/certs/cacert.pem"
```

**功能：** 如果设置了此参数，系统将使用用户指定路径的CA证书，(开发者需保证该路径下CA证书的可访问性)，否则将使用系统预设CA证书，系统预设CA证书位置：/etc/ssl/certs/cacert.pem。证书路径为沙箱映射路径（开发者可通过Global.getContext().filesDir获取应用沙箱路径）。目前仅支持格式为pem的文本证书。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var clientCert

```cangjie
public var clientCert: ?WebSocketClientCert = None
```

**功能：** 支持传输客户端证书。

**类型：** ?[WebSocketClientCert](#class-websocketclientcert)

**读写能力：** 可读写

**起始版本：** 19

### var header

```cangjie
public var header: ?HashMap<String, String> = None
```

**功能：** 建立WebSocket连接可选参数，代表建立连接时携带的HTTP头信息。参数内容自定义，也可以不指定。

**类型：** ?HashMap\<String,String>

**读写能力：** 可读写

**起始版本：** 19

### var protocol

```cangjie
public var protocol: String = ""
```

**功能：** 自定义Sec-WebSocket-Protocol字段，默认为""。

**类型：** String

**读写能力：** 可读写

**起始版本：** 19

### var proxy

```cangjie
public var proxy: ProxyConfiguration = SYSTEM
```

**功能：** 通信过程中的代理信息，默认使用系统网络代理。

**类型：** [ProxyConfiguration](#enum-proxyconfiguration)

**读写能力：** 可读写

**起始版本：** 19

### WebSocketRequestOptions(?HashMap\<String,String>, String, ?WebSocketClientCert, ProxyConfiguration, String)

```cangjie
public WebSocketRequestOptions(
    public var header !: ?HashMap<String, String> = None,
    public var caPath !: String = "/etc/ssl/certs/cacert.pem",
    public var clientCert !: ?WebSocketClientCert = None,
    public var proxy !: ProxyConfiguration = SYSTEM,
    public var protocol !: String = ""
)
```

**功能：** WebSocketRequestOptions构造函数。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|header|?HashMap\<String,String>|否|None| **命名参数。** 建立WebSocket连接可选参数，代表建立连接时携带的HTTP头信息。参数内容自定义，也可以不指定。|
|caPath|String|否|"/etc/ssl/certs/cacert.pem"| **命名参数。** 如果设置了此参数，系统将使用用户指定路径的CA证书，(开发者需保证该路径下CA证书的可访问性)，否则将使用系统预设CA证书，系统预设CA证书位置：/etc/ssl/certs/cacert.pem。证书路径为沙箱映射路径（开发者可通过Global.getContext().filesDir获取应用沙箱路径）。目前仅支持格式为pem的文本证书。|
|clientCert|?[WebSocketClientCert](#class-websocketclientcert)|否|None| **命名参数。** 支持传输客户端证书。|
|proxy|[ProxyConfiguration](#enum-proxyconfiguration)|否|SYSTEM| **命名参数。** 通信过程中的代理信息，默认使用系统网络代理。|
|protocol|String|否|""| **命名参数。** 自定义Sec-WebSocket-Protocol字段，默认为""。|