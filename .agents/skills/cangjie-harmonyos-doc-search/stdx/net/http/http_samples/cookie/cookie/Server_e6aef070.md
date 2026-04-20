## Server

示例：

<!-- run -->
```cangjie
import stdx.net.http.*
import std.net.*
import std.sync.*

main(): Unit {
    let serverOn = SyncCounter(1)
    spawn {
        serverSetCookie(serverOn)
    }
    serverOn.waitUntilZero()
    clientPacketCapture()
}

func serverSetCookie(serverOn: SyncCounter): Unit {
    // 服务器设置 cookie 时将 cookie 放在 Set-Cookie header 中发给客户端
    // 1. 构建 Server 实例
    let server = ServerBuilder().addr("127.0.0.1").port(8080).build()
    server.afterBind({=> serverOn.dec()})
    // 2. 注册 HttpRequestHandler
    server
        .distributor
        .register(
            "/index",
            {
                httpContext =>
                let cookie = Cookie("name", "value")
                httpContext.responseBuilder.header("Set-Cookie", cookie.toSetCookieString()).body("Hello 仓颉!")
            }
        )
    // 3. 启动服务
    server.serve()
}

func clientPacketCapture(): Unit {
    // 创建客户端 socket，并连接到服务端
    let client = TcpSocket("127.0.0.1", 8080)
    client.connect()
    // 发送请求
    let request = "GET /index HTTP/1.1\r\nHost: 127.0.0.1:8080\r\n\r\n".toArray()
    client.write(request)
    // 读取响应，响应中预期包含 “set-cookie: name=value”
    let buf = Array<UInt8>(500, repeat: 0)
    var len = client.read(buf)
    println(String.fromUtf8(buf[..len]))
}
```

运行结果：

> **注意：**
>
> 响应中 date 字段表示当前日期，每次运行会打印不同的结果。

```text
HTTP/1.1 200 OK
set-cookie: name=value
connection: keep-alive
date: xxxx
content-length: 13

Hello 仓颉!
```