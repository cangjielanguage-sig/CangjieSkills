## request接口开发步骤

1. 从kit.NetworkKit中导入http。
2. 调用createHttp()方法，创建一个HttpRequest对象。
3. 调用该对象的on()方法，订阅http响应头事件，此接口会比request请求先返回。可以根据业务需要订阅此消息。
4. 调用该对象的request()方法，传入http请求的url地址和可选参数，发起网络请求。
5. 按照实际业务需要，解析返回结果。
6. 调用该对象的off()方法，取消订阅http响应头事件。
7. 当该请求使用完毕时，调用destroy()方法主动销毁。

```cangjie
// 引入包名
import kit.NetworkKit.*
import kit.BasicServicesKit.*
import ohos.base.*
import std.collection.*

// 每一个httpRequest对应一个HTTP请求任务，不可复用
let httpRequest = createHttp()

// 请求的配置
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

httpRequest.request(
    // 填写HTTP请求的URL地址，可以带参数也可以不带参数。URL地址需要开发者自定义。请求的参数可以在extraData中指定
    "EXAMPLE_URL",
    {
        err, resp =>
        if (let Some(v) <- err) {
            AppLog.error("v")
        }
        if (let Some(v) <- resp) {
            // data.result为HTTP响应内容，可根据业务需要进行解析
            AppLog.info("Result: ${v.result}")
            AppLog.info("code: ${v.responseCode.getValue()}")
            // data.header为HTTP响应头，可根据业务需要进行解析
            AppLog.info("header: ${v.header}")
            AppLog.info("cookies: ${v.cookies}")
            // 当该请求使用完毕时，调用destroy方法主动销毁
            httpRequest.destroy()
        }
    },
    options: option)
```