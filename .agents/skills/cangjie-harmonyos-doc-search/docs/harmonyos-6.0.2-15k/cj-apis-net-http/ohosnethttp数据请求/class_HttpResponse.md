## class HttpResponse

```cangjie
public class HttpResponse <: ToString {}
```

**功能：** request方法回调函数的返回值类型。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**父类型：**

- ToString

### let cookies

```cangjie
public let cookies: String
```

**功能：** 服务器返回的cookies。

**类型：** String

**读写能力：** 只读

**起始版本：** 12

### let header

```cangjie
public let header: HashMap<String, String>
```

**功能：** 发起HTTP请求返回来的响应头。

**类型：** HashMap\<String,String>

**读写能力：** 只读

**起始版本：** 12

### let performanceTiming

```cangjie
public let performanceTiming: PerformanceTiming
```

**功能：** HTTP请求的各个阶段的耗时。

**类型：** [PerformanceTiming](#class-performancetiming)

**读写能力：** 只读

**起始版本：** 12

### let responseCode

```cangjie
public let responseCode: ResponseCode
```

**功能：** 响应的状态码。

**类型：** [ResponseCode](#enum-responsecode)

**读写能力：** 只读

**起始版本：** 12

### let result

```cangjie
public let result: HttpData
```

**功能：** HTTP请求根据响应头中content-type类型返回对应的响应格式内容。

**类型：** [HttpData](#enum-httpdata)

**读写能力：** 只读

**起始版本：** 12

### let resultType

```cangjie
public let resultType: HttpDataType
```

**功能：** 返回值类型。

**类型：** [HttpDataType](#enum-httpdatatype)

**读写能力：** 只读

**起始版本：** 12

### func toString()

```cangjie
public func toString(): String
```

**功能：** 返回字符串形式的[HttpResponse](#class-httpresponse)。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|返回字符串形式的[HttpResponse](#class-httpresponse)。|

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
        Hilog.info(0, "test", "resp: ${r.toString()}")
    } else {
        Hilog.error(0, "test", "response is none")
    }
})
```