let option = HttpRequestOptions(
        method: RequestMethod.Post, // 可选，默认为http.RequestMethod.GET
        // 当使用POST请求时此字段用于传递内容
        extraData: HttpData.StringData("data to send"),
        expectDataType: HttpDataType.StringValue, // 可选，指定返回数据的类型
        usingCache: true, // 可选，默认为true
        priority: 1, // 可选，默认为1
        // 开发者根据自身业务需要添加header字段
        header: HashMap<String, String>([("content-type", "application/json")]),
        readTimeout: 60000, // 可选，默认为60000ms
        connectTimeout: 60000, // 可选，默认为60000ms
        usingProtocol: HttpProtocol.Http1_1, // 可选，协议类型默认值由系统自动指定
        usingProxy: UsingProxy.UseDefault, //可选，默认不使用网络代理，自API 10开始支持该属性
        caPath: "/path/to/cacert.pem", // 可选，默认使用系统预设CA证书，自API 10开始支持该属性
        clientCert: ClientCert(
            "/path/to/client.pem", // 默认不使用客户端证书
            "/path/to/client.key", // 若证书包含Key信息，传入空字符串
            certType: CertType.Pem, // 可选，默认使用PEM
            keyPassword: "passwordToKey" // 可选，输入key文件的密码
        ),
        multiFormDataList: [ // 可选，仅当Header中，'content-Type'为'multipart/form-data'时生效
            MultiFormData (
                "Part1", // 数据名
                "text/plain", // 数据类型
                data: StringData("Example data"), // 可选，数据内容
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

    // 填写HTTP请求的URL地址，可以带参数也可以不带参数。URL地址需要开发者自定义。请求的参数可以在extraData中指定

    httpRequest.requestInStream(
        "EXAMPLE_URL",
        option,
        {err, code =>
        if (let Some(e) <- err) {
            loggerError("exception: ${e.message}")
        }
        if (let Some(respCode) <- code) {
            loggerInfo("ResponseCode: ${respCode}")
        } else {
            loggerError("response is none")
        }
    })
}
```