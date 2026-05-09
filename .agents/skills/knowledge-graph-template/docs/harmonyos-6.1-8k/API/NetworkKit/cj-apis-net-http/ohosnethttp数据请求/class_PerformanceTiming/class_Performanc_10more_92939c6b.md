## class PerformanceTiming

```cangjie
public class PerformanceTiming {
    public var dnsTiming: Float64
    public var tcpTiming: Float64
    public var tlsTiming: Float64
    public var firstSendTiming: Float64
    public var firstReceiveTiming: Float64
    public var totalFinishTiming: Float64
    public var redirectTiming: Float64
    public var responseHeaderTiming: Float64
    public var responseBodyTiming: Float64
    public var totalTiming: Float64
}
```

**功能：** 性能打点(单位：毫秒)。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var dnsTiming

```cangjie
public var dnsTiming: Float64
```

**功能：** 从[request](#func-requeststring-httprequestoptions-asynccallbackhttpresponse)请求到DNS解析完成耗时。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var firstReceiveTiming

```cangjie
public var firstReceiveTiming: Float64
```

**功能：** 从[request](#func-requeststring-httprequestoptions-asynccallbackhttpresponse)请求到接收第一个字节的耗时。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var firstSendTiming

```cangjie
public var firstSendTiming: Float64
```

**功能：** 从[request](#func-requeststring-httprequestoptions-asynccallbackhttpresponse)请求到开始发送第一个字节的耗时。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var redirectTiming

```cangjie
public var redirectTiming: Float64
```

**功能：** 从[request](#func-requeststring-httprequestoptions-asynccallbackhttpresponse)请求到完成所有重定向步骤的耗时。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var responseBodyTiming

```cangjie
public var responseBodyTiming: Float64
```

**功能：** 从[request](#func-requeststring-httprequestoptions-asynccallbackhttpresponse)请求到body解析完成的耗时。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var responseHeaderTiming

```cangjie
public var responseHeaderTiming: Float64
```

**功能：** 从[request](#func-requeststring-httprequestoptions-asynccallbackhttpresponse)请求到header解析完成的耗时。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var tcpTiming

```cangjie
public var tcpTiming: Float64
```

**功能：** 从[request](#func-requeststring-httprequestoptions-asynccallbackhttpresponse)请求到TCP连接完成耗时。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var tlsTiming

```cangjie
public var tlsTiming: Float64
```

**功能：** 从[request](#func-requeststring-httprequestoptions-asynccallbackhttpresponse)请求到TLS连接完成耗时。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var totalFinishTiming

```cangjie
public var totalFinishTiming: Float64
```

**功能：** 从[request](#func-requeststring-httprequestoptions-asynccallbackhttpresponse)请求到完成请求的耗时。

**类型：** Float64

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22