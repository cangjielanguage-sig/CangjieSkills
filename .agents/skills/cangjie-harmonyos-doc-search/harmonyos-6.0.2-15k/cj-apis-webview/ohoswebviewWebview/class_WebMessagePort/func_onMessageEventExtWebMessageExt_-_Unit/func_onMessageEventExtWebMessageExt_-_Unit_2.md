let webController = WebviewController()
var ports = Array<WebMessagePort>()
var nativePort: ?WebMessagePort = None
var message = WebMessageExt()
// 应用与网页互发消息的示例：使用"init_web_messageport"的通道，通过端口0在应用侧接受网页发送的消息，通过端口1在网页侧接受应用发送的消息。
@Entry
@Component
class EntryView {
    @State
    var msg1 = ""
    @State
    var msg2 = ""
    func build() {
        Column(10) {
            Text(this.msg1).fontSize(16)
            Text(this.msg2).fontSize(16)
            Button("SendToH5 setString").onClick {
                evt =>
                AppLog.info("In Cangjie side send start")
                if (let Some(p) <- nativePort) {
                    message.setType(WebMessageType.STRING)
                    message.setString("helloFromCangjie")
                    p.postMessageEventExt(message)
                }
            }.width(600.px).height(150.px)
            Button("SendToH5 setNumber").onClick {
                evt =>
                AppLog.info("In Cangjie side send start")
                if (let Some(p) <- nativePort) {
                    message.setType(WebMessageType.NUMBER)
                    message.setNumber(123.3)
                    p.postMessageEventExt(message)
                }
            }.width(600.px).height(150.px)
            Button("SendToH5 setBoolean").onClick {
                evt =>
                AppLog.info("In Cangjie side send start")
                if (let Some(p) <- nativePort) {
                    message.setType(WebMessageType.BOOLEAN)
                    message.setBoolean(true)
                    p.postMessageEventExt(message)
                }
            }.width(600.px).height(150.px)
            Button("SendToH5 setArrayBuffer").onClick {
                evt =>
                AppLog.info("In Cangjie side send start")
                if (let Some(p) <- nativePort) {
                    message.setType(WebMessageType.ARRAY_BUFFER)
                    message.setArrayBuffer("helloFromCangjie".toArray())
                    p.postMessageEventExt(message)
                }
            }.width(600.px).height(150.px)
            Button("SendToH5 setArray").onClick {
                evt =>
                AppLog.info("In Cangjie side send start")
                if (let Some(p) <- nativePort) {
                    message.setType(WebMessageType.ARRAY)
                    message.setArray([1, 2])
                    p.postMessageEventExt(message)
                }
            }.width(600.px).height(150.px)
            Button("SendToH5 setError").onClick {
                evt =>
                AppLog.info("In Cangjie side send start")
                if (let Some(p) <- nativePort) {
                    message.setType(WebMessageType.ERROR)
                    message.setError(webError("RangeError", "error message"))
                    p.postMessageEventExt(message)
                }
            }.width(600.px).height(150.px)
            Web(src: ("index.html"), controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd(
                {
                    evt =>
                    AppLog.info("page end url: ${evt.url}")
                    // 1. 创建消息端口
                    ports = webController.createWebMessagePorts(isExtentionType: true)
                    // 2. 发送端口1到HTML5
                    webController.postMessage("init_web_messageport", [ports[1]], "*")
                    // 3. 保存端口0到本地
                    nativePort = ports[0]
                    // 4. 设置回调函数
                    nativePort?.onMessageEventExt(
                        {
                            msgExt: WebMessageExt =>
                            let msgType = msgExt.getType()
                            match (msgType) {
                                case WebMessageType.STRING =>
                                    this.msg1 = "result type:" + "STRING"
                                    this.msg2 = "result getString:" + ((msgExt.getString()))
                                case WebMessageType.NUMBER =>
                                    this.msg1 = "result type:" + "NUMBER"
                                    this.msg2 = "result getNumber: ${msgExt.getNumber()}"
                                case WebMessageType.BOOLEAN =>
                                    this.msg1 = "result type:" + "BOOLEAN"
                                    this.msg2 = "result getBoolean: ${msgExt.getBoolean()}"
                                case WebMessageType.ARRAY_BUFFER =>
                                    this.msg1 = "result type:" + "ARRAY_BUFFER"
                                    this.msg2 = "result getArrayBuffer: ${msgExt.getArrayBuffer()}"
                                case WebMessageType.ARRAY =>
                                    this.msg1 = "result type:" + "ARRAY"
                                    let array = msgExt.getArray()
                                    this.msg2 = "result getArray:" + match (array) {
                                        case ARRAYSTRING(s) => "${s}"
                                        case ARRAYI64(i) => "${i}"
                                        case ARRAYF64(f) => "${f}"
                                        case ARRAYBOOL(b) => "${b}"
                                        case _ => throw IllegalArgumentException("The type is not supported.")
                                    }
                                case WebMessageType.ERROR =>
                                    this.msg1 = "result type:" + "ERROR"
                                    let err = msgExt.getError()
                                    this.msg2 = "result getError: ${err.errorName}, ${err.errorMsg}"
                                case _ =>
                                    this.msg1 = "result type:" + "NOT_SUPPORT"
                                    this.msg2 = "result NOT_SUPPORT"
                            }
                        }
                    )
                }
            )
        }.width(100.percent)
    }
}
```