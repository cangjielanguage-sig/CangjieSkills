// server:
func handler1(ctx: HttpContext): Unit {
    // 2 完成 websocket 握手，获取 websocket 实例
    let websocketServer = WebSocket.upgradeFromServer(ctx, subProtocols: ArrayList<String>(["foo", "bar", "foo1"]),
        userFunc: {request: HttpRequest =>
            let value = request.headers.getFirst("test") ?? ""
            let headers = HttpHeaders()
            headers.add("rsp", value)
            headers
        })
    // 3 消息收发
    // 收 hello
    let data = ArrayList<UInt8>()
    var frame = websocketServer.read()
    while(true) {
        match(frame.frameType) {
            case ContinuationWebFrame =>
                data.add(all: frame.payload)
                if (frame.fin) {
                    break
                }
            case TextWebFrame | BinaryWebFrame =>
                if (!data.isEmpty()) {
                    throw Exception("invalid frame")
                }
                data.add(all: frame.payload)
                if (frame.fin) {
                    break
                }
            case CloseWebFrame =>
                websocketServer.write(CloseWebFrame, frame.payload)
                break
            case PingWebFrame =>
                websocketServer.writePongFrame(frame.payload)
            case _ => ()
        }
        frame = websocketServer.read()
    }
    println("data: ${String.fromUtf8(data.toArray())}")    // hello
    // 发 4097 个 a
    websocketServer.write(TextWebFrame, Array<UInt8>(4097, repeat: 97))

    // 4 关闭 websocket，
    // 收发 CloseFrame
    let websocketFrame = websocketServer.read()
    println("close frame type: ${websocketFrame.frameType}")   // CloseWebFrame
    println("close frame payload: ${websocketFrame.payload}")     // 3, 232
    websocketServer.write(CloseWebFrame, websocketFrame.payload)
    // 关闭底层连接
    websocketServer.closeConn()
}
```

该示例运行结果如下：

```text
subProtocol: foo1
echo
data: hello
data size: 4097
last item: a
close frame type: CloseWebFrame
close frame payload: [3, 232]
close frame type: CloseWebFrame
close frame payload: [3, 232]
```