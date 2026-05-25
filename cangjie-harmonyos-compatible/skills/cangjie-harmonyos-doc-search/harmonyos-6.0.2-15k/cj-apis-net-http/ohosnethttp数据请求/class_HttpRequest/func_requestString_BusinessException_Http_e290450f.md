### func request(String, (?BusinessException, ?HttpResponse) -> Unit, ?HttpRequestOptions)

```cangjie
public func request(url: String, callback: (?BusinessException, ?HttpResponse) -> Unit,
    options!: ?HttpRequestOptions = None): Unit
```

**功能：** 根据URL地址，发起HTTP网络请求，在callback回调函数中返回响应。

> **说明：**
>
> 此接口仅支持数据大小为5MB以内的数据接收。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|发起网络请求的URL地址。|
|callback|(?[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception), ?[HttpResponse](#class-httpresponse)) -> Unit|是|-|回调函数。|
|options|?[HttpRequestOptions](#class-httprequestoptions)|否|None| **命名参数。** 参考[HttpRequestOptions](#class-httprequestoptions)。|

**异常：**

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |201|Permission denied.|
  |2300001|Unsupported protocol.|
  |2300003|URL using bad/illegal format or missing URL.|
  |2300005|Couldn't resolve proxy name.|
  |2300006|Couldn't resolve host name.|
  |2300007|Couldn't connect to server.|
  |2300008|Weird server reply.|
  |2300009|Access denied to remote resource.|
  |2300016|Error in the HTTP2 framing layer.|
  |2300018|Transferred a partial file.|
  |2300023|Failed writing received data to disk/application.|
  |2300025|Upload failed.|
  |2300026|Failed to open/read local data from file/application.|
  |2300027|Out of memory.|
  |2300028|Timeout was reached.|
  |2300047|Number of redirects hit maximum amount.|
  |2300052|Server returned nothing (no headers, no data).|
  |2300055|Failed sending data to the peer.|
  |2300056|Failure when receiving data from the peer.|
  |2300058|Problem with the local SSL certificate.|
  |2300059|Couldn't use specified SSL cipher.|
  |2300060|SSL peer certificate or SSH remote key was not OK.|
  |2300061|Unrecognized or bad HTTP Content or Transfer-Encoding.|
  |2300063|Maximum file size exceeded.|
  |2300070|Disk full or allocation exceeded.|
  |2300073|Remote file already exists.|
  |2300077|Problem with the SSL CA cert (path? access rights?).|
  |2300078|Remote file not found.|
  |2300094|An authentication function returned an error.|
  |2300999|Unknown Other Error.|

> **错误码说明：**
>
> 以上错误码的详细介绍参见[HTTP错误码](../../errorcodes/cj-errorcode-net-http.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。
> HTTP接口返回错误码映射关系：2300000 + curl错误码。更多常用错误码，可参考：[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)。

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
        Hilog.info(0, "test", "resp: ${r}")
    } else {
        Hilog.error(0, "test", "response is none")
    }
})
```