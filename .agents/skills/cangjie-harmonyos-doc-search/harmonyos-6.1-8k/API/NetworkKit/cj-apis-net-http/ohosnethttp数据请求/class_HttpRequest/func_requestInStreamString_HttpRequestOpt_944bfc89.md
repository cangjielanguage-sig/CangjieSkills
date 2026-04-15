### func requestInStream(String, HttpRequestOptions, AsyncCallback\<UInt32>)

```cangjie
public func requestInStream(url: String, options: HttpRequestOptions, callback: AsyncCallback<UInt32>): Unit
```

**功能：** 根据URL地址和相关配置项，发起HTTP网络请求并返回流式响应，

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|发起网络请求的URL地址。|
|options|[HttpRequestOptions](#class-httprequestoptions)|是|-|参考[HttpRequestOptions](#class-httprequestoptions)。|
|callback|[AsyncCallback](../arkinterop/cj-api-business_exception.md#type-asynccallbackt)\<UInt32>|是|-|回调函数。|

**异常：**

- BusinessException：对应错误码如下表，详见[HTTP错误码](./cj-errorcode-net-http.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 2300001 | Unsupported protocol. |
  | 2300003 | Invalid URL format or missing URL. |
  | 2300005 | Failed to resolve the proxy name. |
  | 2300006 | Failed to resolve the host name. |
  | 2300007 | Failed to connect to the server. |
  | 2300008 | Invalid server response. |
  | 2300009 | Access to the remote resource denied. |
  | 2300016 | Error in the HTTP2 framing layer. |
  | 2300018 | Transferred a partial file. |
  | 2300023 | Failed to write the received data to the disk or application. |
  | 2300025 | Upload failed. |
  | 2300026 | Failed to open or read local data from the file or application. |
  | 2300027 | Out of memory. |
  | 2300028 | Operation timeout. |
  | 2300047 | The number of redirections reaches the maximum allowed. |
  | 2300052 | The server returned nothing (no header or data). |
  | 2300055 | Failed to send data to the peer. |
  | 2300056 | Failed to receive data from the peer. |
  | 2300058 | Local SSL certificate error. |
  | 2300059 | The specified SSL cipher cannot be used. |
  | 2300060 | Invalid SSL peer certificate or SSH remote key. |
  | 2300061 | Invalid HTTP encoding format. |
  | 2300063 | Maximum file size exceeded. |
  | 2300070 | Remote disk full. |
  | 2300073 | Remote file already exists. |
  | 2300077 | The SSL CA certificate does not exist or is inaccessible. |
  | 2300078 | Remote file not found. |
  | 2300094 | Authentication error. |
  | 2300997 | Cleartext traffic not permitted. |
  | 2300998 | It is not allowed to access this domain. |
  | 2300999 | Internal error. |

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
    httpRequest.requestInStream("http://www.example.com", {err, code =>
        if (let Some(e) <- err) {
            Hilog.error(0, "AppLogCj","exception: ${e.message}")
        }
        if (let Some(respCode) <- code) {
            Hilog.info(0, "AppLogCj", "resp: ${respCode}")
        } else {
            Hilog.error(0, "AppLogCj", "response is none")
        }
    })
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```