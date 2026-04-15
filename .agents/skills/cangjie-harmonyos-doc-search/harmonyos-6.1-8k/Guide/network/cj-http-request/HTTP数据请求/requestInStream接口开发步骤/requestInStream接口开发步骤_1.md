## requestInStream接口开发步骤

1. 从kit.NetworkKit中导入http。
2. 调用createHttp()方法，创建一个HttpRequest对象。
3. 调用该对象的on()方法，可以根据业务需要订阅HTTP响应头事件、HTTP流式响应数据接收事件、HTTP流式响应数据接收进度事件和HTTP流式响应数据接收完毕事件。
4. 调用该对象的requestInStream()方法，传入http请求的url地址和可选参数，发起网络请求。
5. 按照实际业务需要，可以解析返回的响应码。
6. 调用该对象的off()方法，取消订阅响应事件。
7. 当该请求使用完毕时，调用destroy()方法主动销毁。

<!-- compile -->

```cangjie
// 引入包名
import kit.PerformanceAnalysisKit.Hilog
import kit.NetworkKit.*
import std.collection.*
import ohos.callback_invoke.*
import ohos.business_exception.*

func loggerInfo(str: String) {
    Hilog.info(0, "CangjieTest", str)
}

func loggerError(str: String) {
    Hilog.error(0, "CangjieTest", str)
}

class HeadersReceiveCb <: Callback1Argument<HashMap<String, String>> {
    let callback_: (HashMap<String, String>)->Unit
    public init(callback: (HashMap<String, String>)->Unit) {callback_ = callback}
    public open func invoke(err: ?BusinessException, val: HashMap<String, String>): Unit {
        callback_(val)
    }
}

class DataReceiveCb <: Callback1Argument<Array<Byte>> {
    let callback_: (Array<Byte>)->Unit
    public init(callback: (Array<Byte>)->Unit) {callback_ = callback}
    public open func invoke(err: ?BusinessException, val: Array<Byte>): Unit {
        callback_(val)
    }
}

class DataEndCb <: Callback0Argument {
    let callback_: ()->Unit
    public init(callback: ()->Unit) {callback_ = callback}
    public open func invoke(err: ?BusinessException): Unit {
        callback_()
    }
}

class DataReceiveProgressCb <: Callback1Argument<DataReceiveProgressInfo> {
    let callback_: (DataReceiveProgressInfo)->Unit
    public init(callback: (DataReceiveProgressInfo)->Unit) {callback_ = callback}
    public open func invoke(err: ?BusinessException, val: DataReceiveProgressInfo): Unit {
        callback_(val)
    }
}

func test() {
    // 每一个httpRequest对应一个HTTP请求任务，不可复用
    let httpRequest = createHttp()
    // 用于订阅HTTP响应头事件
    let headersReceiveCallBack = HeadersReceiveCb({ header => loggerInfo("header: ${header}") })
    httpRequest.on(HttpRequestEvent.HeadersReceive, headersReceiveCallBack)
    // 用于订阅HTTP流式响应数据接收事件
    let res = ArrayList<Byte>()
    let dataReceiveCallBack = DataReceiveCb({ bytes =>
        res.add(all: bytes)
        loggerInfo("receive length: ${bytes.size}")
    })
    httpRequest.on(HttpRequestEvent.DataReceive, dataReceiveCallBack)

    // 用于订阅HTTP流式响应数据接收完毕事件
    let dataEndCallBack = DataEndCb({ =>
        loggerInfo("No more data in response, data receive end")
        // 取消订阅HTTP响应头事件
        httpRequest.off(HttpRequestEvent.HeadersReceive)
        // 取消订阅HTTP流式响应数据接收事件
        httpRequest.off(HttpRequestEvent.DataReceive)
        // 取消订阅HTTP流式响应数据接收进度事件
        httpRequest.off(HttpRequestEvent.DataReceiveProgress)
        // 取消订阅HTTP流式响应数据接收完毕事件
        httpRequest.off(HttpRequestEvent.DataEnd)
        // 当该请求使用完毕时，调用destroy方法主动销毁
        httpRequest.destroy()
    })
    httpRequest.on(HttpRequestEvent.DataEnd,dataEndCallBack)
    // 用于订阅HTTP流式响应数据接收进度事件
    let dataReceiveProgressCallBack = DataReceiveProgressCb({ progress =>
        loggerInfo("dataReceiveProgress receiveSize: ${progress.receiveSize} totalSize: ${progress.totalSize}")
    })
    httpRequest.on(HttpRequestEvent.DataReceiveProgress, dataReceiveProgressCallBack)