## class HttpResponse

```cangjie
public class HttpResponse {
    public var result: HttpData
    public var resultType: HttpDataType
    public var responseCode: UInt32
    public var header: HashMap<String, String>
    public var cookies: String
    public var performanceTiming: PerformanceTiming
}
```

**功能：** request方法回调函数的返回值类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var cookies

```cangjie
public var cookies: String
```

**功能：** 服务器返回的原始cookies。开发者可自行处理。

**类型：** String

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var header

```cangjie
public var header: HashMap<String, String>
```

**功能：** 发起HTTP请求返回来的响应头。当前返回的是JSON格式字符串，如需具体字段内容，需开发者自行解析。常见字段及解析方式如下：

- content-type：header['content-type']。

- status-line：header['status-line']。

- date：header.date/header['date']。

- server：header.server/header['server']。

**类型：** HashMap\<String,String>

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var performanceTiming

```cangjie
public var performanceTiming: PerformanceTiming
```

**功能：** HTTP请求的各个阶段的耗时。

**类型：** [PerformanceTiming](#class-performancetiming)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var responseCode

```cangjie
public var responseCode: UInt32
```

**功能：** 回调函数执行成功时，此字段为[ResponseCode](#var-responsecode)。

**类型：** UInt32

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var result

```cangjie
public var result: HttpData
```

**功能：** HTTP请求根据响应头中content-type类型返回对应的响应格式内容，若HttpRequestOptions无expectDataType字段，按如下规则返回：<br />- application/json：返回JSON格式的字符串。<br />- application/octet-stream：ArrayBuffer。<br />- image：ArrayBuffer。<br />- 其他：string。<br /> 若HttpRequestOption有expectDataType字段，开发者需传入与服务器返回类型相同的数据类型。

**类型：** [HttpData](#enum-httpdata)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

### var resultType

```cangjie
public var resultType: HttpDataType
```

**功能：** 返回值类型。

**类型：** [HttpDataType](#enum-httpdatatype)

**读写能力：** 可读写

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22