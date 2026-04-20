### func request(String, AsyncCallback\<HttpResponse>)

```cangjie
public func request(url: String, callback: AsyncCallback<HttpResponse>): Unit
```

**功能：** 根据URL地址，发起HTTP网络请求，

> **说明：**
>
>(1) 此接口仅支持接收5MB以内的数据，如果需要接收超过5MB的数据。
>
>(2) 如需传入cookies，请开发者自行在参数options中添加。
>
>(3) 若URL包含中文或其他语言，需先调用encodeURL(URL)编码，再发起请求。

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|发起网络请求的URL地址。|
|callback|[AsyncCallback](../arkinterop/cj-api-business_exception.md#type-asynccallbackt)\<[HttpResponse](#class-httpresponse)>|是|-|回调函数。|

**异常：**

- BusinessException：对应错误码如下表，[HTTP错误码](./cj-errorcode-net-http.md)和[通用错误码](../cj-errorcode-universal.md)。
- HTTP接口返回错误码映射关系：2300000 + curl错误码。更多常用错误码，可参考：[curl错误码](https://curl.se/libcurl/c/libcurl-errors.html)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 2300001 | Unsupported protocol. |
  | 2300003 | URL using bad/illegal format or missing URL. |
  | 2300005 | Couldn't resolve proxy name. |
  | 2300006 | Couldn't resolve host name. |
  | 2300007 | Couldn't connect to server. |
  | 2300008 | Weird server reply. |
  | 2300009 | Access denied to remote resource. |
  | 2300016 | Error in the HTTP2 framing layer. |
  | 2300018 | Transferred a partial file. |
  | 2300023 | Failed writing received data to disk/application. |
  | 2300025 | Upload failed. |
  | 2300026 | Failed to open/read local data from file/application. |
  | 2300027 | Out of memory. |
  | 2300028 | Timeout was reached. |
  | 2300047 | Number of redirects hit maximum amount. |
  | 2300052 | Server returned nothing (no headers, no data). |
  | 2300055 | Failed sending data to the peer. |
  | 2300056 | Failure when receiving data from the peer. |
  | 2300058 | Problem with the local SSL certificate. |
  | 2300059 | Couldn't use specified SSL cipher. |
  | 2300060 | SSL peer certificate or SSH remote key was not OK. |
  | 2300061 | Unrecognized or bad HTTP Content or Transfer-Encoding. |
  | 2300063 | Maximum file size exceeded. |
  | 2300070 | Disk full or allocation exceeded. |
  | 2300073 | Remote file already exists. |
  | 2300077 | Problem with the SSL CA cert (path? access rights?). |
  | 2300078 | Remote file not found. |
  | 2300094 | An authentication function returned an error. |
  | 2300997 | Cleartext traffic not permitted. |
  | 2300998 | It is not allowed to access this domain. |
  | 2300999 | Unknown Other Error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.NetworkKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let httpRequest = createHttp()
    httpRequest.request("http://www.example.com", {err, resp =>
        if (let Some(e) <- err) {
            Hilog.error(0, "AppLogCj","exception: ${e.message}")
        }
        if (let Some(r) <- resp) {
            Hilog.info(0, "http_test", "resp: ${r.responseCode}")
        } else {
            Hilog.error(0, "AppLogCj", "response is none")
        }
    })
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```