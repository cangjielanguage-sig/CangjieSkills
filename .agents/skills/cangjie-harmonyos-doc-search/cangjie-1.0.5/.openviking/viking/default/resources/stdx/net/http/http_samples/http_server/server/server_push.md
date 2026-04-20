## server push

仅用于 HTTP/2

client:

示例：

<!-- compile -->
```cangjie
import std.io.*
import std.fs.*
import std.collection.ArrayList
import stdx.net.tls.*
import stdx.crypto.x509.X509Certificate
import stdx.net.http.*

main() {
    // 1. TLS 配置，其中 TLS 证书文件用户需自行提供
    var tlsConfig = TlsClientConfig()
    let pem = String.fromUtf8(readToEnd(File("/rootCerPath", Read)))
    tlsConfig.verifyMode = CustomCA(X509Certificate.decodeFromPem(pem))
    tlsConfig.alpnProtocolsList = ["h2"]
    // 2. 构建 Client 实例
    let client = ClientBuilder().tlsConfig(tlsConfig).build()
    // 3. 发送请求，接收响应
    let response = client.get("https://127.0.0.1.8080/index.html")
    // 4. 接收服务端推送的响应，此例中相当于请求 client.get("http://127.0.0.1.8080/picture.png") 的响应
    let pushResponses: Option<ArrayList<HttpResponse>> = response.getPush()
    client.close()
}
```

server:

示例：

<!-- compile -->
```cangjie
import std.io.*
import std.fs.*
import stdx.net.tls.*
import stdx.crypto.x509.{X509Certificate, PrivateKey}
import stdx.net.http.*

main() {
    // 1. TLS 配置，其中 TLS 证书文件用户需自行提供
    let pem0 = String.fromUtf8(readToEnd(File("/certPath", Read)))
    let pem02 = String.fromUtf8(readToEnd(File("/keyPath", Read)))
    var tlsConfig = TlsServerConfig(X509Certificate.decodeFromPem(pem0), PrivateKey.decodeFromPem(pem02))
    tlsConfig.supportedAlpnProtocols = ["h2"]
    // 2. 构建 Server 实例
    let server = ServerBuilder().addr("127.0.0.1").port(8080).tlsConfig(tlsConfig).build()
    // 3. 注册原 request 的 handler
    server
        .distributor
        .register(
            "/index.html",
            {
                httpContext =>
                let pusher = HttpResponsePusher.getPusher(httpContext)
                match (pusher) {
                    case Some(pusher) => pusher.push("/picture.png", "GET", httpContext.request.headers)
                    case None => ()
                }
            }
        )
    // 4. 注册服务端推送请求对应的 handler
    server.distributor.register("/picture.png", {
        httpContext => httpContext.responseBuilder.body("picture.png")
    })
    // 4. 启动服务
    server.serve()
}
```