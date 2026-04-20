## enum UsingProxy

```cangjie
public enum UsingProxy {
    | NOT_USE
    | USE_DEFAULT
    | USE_SPECIFIED(HttpProxy)
    | ...
}
```

**功能：** 使用代理的类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

### NOT_USE

```cangjie
NOT_USE
```

**功能：** 不使用代理。

**起始版本：** 12

### USE_DEFAULT

```cangjie
USE_DEFAULT
```

**功能：** 使用默认代理。

**起始版本：** 12

### USE_SPECIFIED(HttpProxy)

```cangjie
USE_SPECIFIED(HttpProxy)
```

**功能：** 使用指定类型代理。

**起始版本：** 12

## 完整示例

```cangjie
import kit.NetworkKit.*
import ohos.base.*
import std.collection.*

// 每一个httpRequest对应一个HTTP请求任务，不可复用
let httpRequest = createHttp()
// 用于订阅HTTP响应头，此接口会比request请求先返回。可以根据业务需要订阅此消息
httpRequest.onHeadersReceive({header: HashMap<String, String> =>
    AppLog.info("header: ${header}")
})

let option = HttpRequestOptions(
    method: RequestMethod.POST, // 可选，默认为http.RequestMethod.GET
    // 当使用POST请求时此字段用于传递内容
    extraData: HttpData.STRING_DATA("data to send"),
    expectDataType: HttpDataType.STRING, // 可选，指定返回数据的类型
    usingCache: true, // 可选，默认为true
    priority: 1, // 可选，默认为1
    // 开发者根据自身业务需要添加header字段
    header: HashMap<String, String>([("content-type", "application/json")]),
    readTimeout: 60000, // 可选，默认为60000ms
    connectTimeout: 60000, // 可选，默认为60000ms
    usingProtocol: HttpProtocol.HTTP1_1, // 可选，协议类型默认值由系统自动指定
    usingProxy: UsingProxy.USE_DEFAULT, //可选，默认不使用网络代理，自API 10开始支持该属性
    caPath: "/path/to/cacert.pem", // 可选，默认使用系统预设CA证书，自API 10开始支持该属性
    clientCert: ClientCert(
        "/path/to/client.pem", // 默认不使用客户端证书
        "/path/to/client.key", // 若证书包含Key信息，传入空字符串
        certType: CertType.PEM, // 可选，默认使用PEM
        keyPassword: "passwordToKey" // 可选，输入key文件的密码
    ),
    multiFormDataList: [ // 可选，仅当Header中，'content-Type'为'multipart/form-data'时生效
        MultiFormData (
            "Part1", // 数据名
            "text/plain", // 数据类型
            data: STRING_DATA("Example data"), // 可选，数据内容
            remoteFileName: "example.txt" // 可选
        ),
        MultiFormData (
            "Part2", // 数据名
            "text/plain", // 数据类型
            filePath: "/data/app/el2/100/base/com.example.myapplication/haps/entry/files/fileName.txt", // 可选，传入文件路径
            remoteFileName: "fileName.txt" // 可选
        )
    ]
)

httpRequest.request( // 填写HTTP请求的URL地址，可以带参数也可以不带参数。URL地址需要开发者自定义。请求的参数可以在extraData中指定
    "http://www.example.com", { err, resp =>
        if (let Some(e) <- err) {
            Hilog.error(0, "test","exception: ${e.message}")
            throw e
        }
        if (let Some(r) <- resp) {
            Hilog.error(0, "test", "${r}")
        } else {
            Hilog.error(0, "test", "resp is none")
        }
        httpRequest.destroy()
    }, options: option)
```