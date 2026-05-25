# server

> **注意：**
>
> 以下示例仅用于展示服务端写法，可编译并运行（部分用例需用户自行提供有效证书文件），但无法展示处理请求的效果。如需查看运行效果，需用户自行提供客户端对示例服务端发起请求。

## Hello 仓颉

示例：

<!-- compile -->
```cangjie
import stdx.net.http.ServerBuilder

main() {
    // 1. 构建 Server 实例
    let server = ServerBuilder().addr("127.0.0.1").port(8080).build()
    // 2. 注册 HttpRequestHandler
    server.distributor.register("/index", {
        httpContext => httpContext.responseBuilder.body("Hello 仓颉!")
    })
    // 3. 启动服务
    server.serve()
}
```

## 通过 request distributor 注册处理器

示例：

<!-- compile -->
```cangjie
import stdx.net.http.{ServerBuilder, HttpRequestHandler, FuncHandler}

main() {
    // 1. 构建 Server 实例
    let server = ServerBuilder().addr("127.0.0.1").port(8080).build()
    // 注册三个不同的 HttpRequestHandler，该服务端可根据请求路径自动分发、处理请求。
    var a: HttpRequestHandler = FuncHandler({
        httpContext => httpContext.responseBuilder.body("index")
    })
    var b: HttpRequestHandler = FuncHandler({
        httpContext => httpContext.responseBuilder.body("id")
    })
    var c: HttpRequestHandler = FuncHandler({
        httpContext => httpContext.responseBuilder.body("help")
    })
    server.distributor.register("/index", a)
    server.distributor.register("/id", b)
    server.distributor.register("/help", c)
    // 2. 启动服务
    server.serve()
}
```

## 自定义 request distributor 与处理器

示例：

<!-- compile -->
```cangjie
import stdx.net.http.*
import std.collection.HashMap

// 自定义请求分发器
class NaiveDistributor <: HttpRequestDistributor {
    let map = HashMap<String, HttpRequestHandler>()
    public func register(path: String, handler: HttpRequestHandler): Unit {
        map.add(path, handler)
    }

    public func distribute(path: String): HttpRequestHandler {
        if (path == "/index") {
            return PageHandler()
        }
        return NotFoundHandler()
    }
}

// 返回一个简单的 HTML 页面
class PageHandler <: HttpRequestHandler {
    public func handle(httpContext: HttpContext): Unit {
        httpContext.responseBuilder.body("<html></html>")
    }
}

main() {
    // 1. 构建 Server 实例并接入自定义分发器
    let server = ServerBuilder().addr("127.0.0.1").port(8080).distributor(NaiveDistributor()).build()
    // 2. 启动服务
    server.serve()
}
```

## 自定义 server 网络配置

示例：

<!-- compile -->
```cangjie
import std.io.*
import std.fs.*
import stdx.net.tls.*
import stdx.crypto.x509.{X509Certificate, PrivateKey}
import stdx.net.http.*

main() {
    // 1. 自定义配置
    // TCP 配置
    var transportCfg = TransportConfig()
    transportCfg.readBufferSize = 8192
    // TLS 配置，需要传入配套的证书与私钥文件路径，此处证书和私钥文件需要用户自行提供
    let pem0 = String.fromUtf8(readToEnd(File("/certPath", Read)))
    let pem02 = String.fromUtf8(readToEnd(File("/keyPath", Read)))
    var tlsConfig = TlsServerConfig(X509Certificate.decodeFromPem(pem0), PrivateKey.decodeFromPem(pem02))
    tlsConfig.supportedAlpnProtocols = ["h2"]
    // 2. 构建 Server 实例
    let server = ServerBuilder()
        .addr("127.0.0.1")
        .port(8080)
        .transportConfig(transportCfg)
        .tlsConfig(tlsConfig)
        .headerTableSize(10 * 1024)
        .maxRequestHeaderSize(1024 * 1024)
        .build()
    // 3. 注册 HttpRequestHandler
    server.distributor.register("/index", {
        httpContext => httpContext.responseBuilder.body("Hello 仓颉!")
    })
    // 4. 启动服务
    server.serve()
}
```