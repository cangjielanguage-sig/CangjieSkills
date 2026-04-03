## response 中的 chunked 与 trailer

示例：

<!-- compile -->
```cangjie
import stdx.net.http.*
import std.io.*
import std.collection.HashMap

func checksum(chunk: Array<UInt8>): Int64 {
    var sum = 0
    for (i in chunk) {
        if (i == UInt8(UInt32(r'\n'))) {
            sum += 1
        }
    }
    return sum / 2
}

main() {
    // 1. 构建 Server 实例
    let server = ServerBuilder().addr("127.0.0.1").port(8080).build()
    // 2. 注册 HttpRequestHandler
    server
        .distributor
        .register(
            "/index",
            {
                httpContext =>
                let responseBuilder = httpContext.responseBuilder
                // 设置响应头 transfer-encoding 和 trailer
                responseBuilder.header("transfer-encoding", "chunked")
                responseBuilder.header("trailer", "checkSum")
                // 用 HttpResponseWriter 分段发送响应体
                let writer = HttpResponseWriter(httpContext)
                var sum = 0
                for (_ in 0..10) {
                    let chunk = Array<UInt8>(10, repeat: 0)
                    sum += checksum(chunk)
                    writer.write(chunk)
                }
                // 发送响应 trailer，trailer 部分在响应体之后发送
                responseBuilder.trailer("checkSum", "${sum}")
            }
        )
    // 3. 启动服务
    server.serve()
}
```

## 处理重定向 request

示例：

<!-- compile -->
```cangjie
import stdx.net.http.*

main() {
    // 1. 构建 Server 实例
    let server = ServerBuilder().addr("127.0.0.1").port(8080).build()
    // 2. 注册用于重定向的 HttpRequestHandler
    server.distributor.register("/redirecta", RedirectHandler("/movedsource", 308))
    server.distributor.register("/redirectb", RedirectHandler("http://www.example.com", 308))
    // 3. 启动服务
    server.serve()
}
```

## tls 证书热加载

示例：

<!-- compile -->
```cangjie
import std.io.*
import std.fs.*
import stdx.net.tls.*
import stdx.crypto.x509.{X509Certificate, PrivateKey}
import stdx.net.http.*

//该程序需要用户配置存在且合法的文件路径才能执行
main() {
    // 1. TLS 配置，其中 TLS 证书和私钥文件用户需自行提供
    let pem0 = String.fromUtf8(readToEnd(File("/certPath", Read)))
    let pem02 = String.fromUtf8(readToEnd(File("/keyPath", Read)))
    var tlsConfig = TlsServerConfig(X509Certificate.decodeFromPem(pem0), PrivateKey.decodeFromPem(pem02))
    tlsConfig.supportedAlpnProtocols = ["http/1.1"]
    let pem = String.fromUtf8(readToEnd(File("/rootCerPath", Read)))
    tlsConfig.verifyMode = CustomCA(X509Certificate.decodeFromPem(pem))
    // 2. 构建 Server 实例，并启动服务
    let server = ServerBuilder().addr("127.0.0.1").port(8080).tlsConfig(tlsConfig).build()
    spawn {
        server.serve()
    }
    // 3. 更新 TLS 证书和私钥，之后建立的连接将使用新的证书和私钥进行认证和加密
    server.updateCert("/newCerPath", "/newKeyPath")
    // 4. 更新 CA，双向认证时使用，之后建立的连接将使用新的 CA 进行认证
    server.updateCA("/newRootCerPath")
}
```