## class PerformanceTiming

```cangjie
public class PerformanceTiming <: ToString {}
```

**功能：** 性能打点数据，单位为毫秒。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**父类型：**

- ToString

### let dnsTiming

```cangjie
public let dnsTiming: Float64
```

**功能：** 从[request](#func-requeststring-businessexception-httpresponse---unit-httprequestoptions)请求到DNS解析完成耗时。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let firstReceiveTiming

```cangjie
public let firstReceiveTiming: Float64
```

**功能：** 从[request](#func-requeststring-businessexception-httpresponse---unit-httprequestoptions))请求到接收第一个字节的耗时。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let firstSendTiming

```cangjie
public let firstSendTiming: Float64
```

**功能：** 从[request](#func-requeststring-businessexception-httpresponse---unit-httprequestoptions))请求到开始发送第一个字节的耗时。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let redirectTiming

```cangjie
public let redirectTiming: Float64
```

**功能：** 从[request](#func-requeststring-businessexception-httpresponse---unit-httprequestoptions))请求到完成所有重定向步骤的耗时。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let responseBodyTiming

```cangjie
public let responseBodyTiming: Float64
```

**功能：** 从[request](#func-requeststring-businessexception-httpresponse---unit-httprequestoptions))请求到body解析完成的耗时。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let responseHeaderTiming

```cangjie
public let responseHeaderTiming: Float64
```

**功能：** 从[request](#func-requeststring-businessexception-httpresponse---unit-httprequestoptions))请求到header解析完成的耗时。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let tcpTiming

```cangjie
public let tcpTiming: Float64
```

**功能：** 从[request](#func-requeststring-businessexception-httpresponse---unit-httprequestoptions))请求到TCP连接完成耗时。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let tlsTiming

```cangjie
public let tlsTiming: Float64
```

**功能：** 从[request](#func-requeststring-businessexception-httpresponse---unit-httprequestoptions))请求到TLS连接完成耗时。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let totalFinishTiming

```cangjie
public let totalFinishTiming: Float64
```

**功能：** 从[request](#func-requeststring-businessexception-httpresponse---unit-httprequestoptions))请求到完成请求的耗时。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### let totalTiming

```cangjie
public let totalTiming: Float64
```

**功能：** 从[request](#func-requeststring-businessexception-httpresponse---unit-httprequestoptions))请求回调到应用程序的耗时。

**类型：** Float64

**读写能力：** 只读

**起始版本：** 12

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回字符串形式的[PerformanceTiming](#class-performancetiming)。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回字符串形式的[PerformanceTiming](#class-performancetiming)。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import ohos.hilog.Hilog

let httpRequest = createHttp()
httpRequest.request("http://www.example.com", {err, resp =>
    if (let Some(e) <- err) {
        Hilog.error(0, "test","exception: ${e.message}")
    }
    if (let Some(r) <- resp) {
        Hilog.info(0, "test", "resp: ${r.performanceTiming.toString()}")
    } else {
        Hilog.error(0, "test", "response is none")
    }
})
```