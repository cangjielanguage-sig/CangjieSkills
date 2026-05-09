### static func configCookie(String, String, Bool)

```cangjie
public static func configCookie(url: String, value: String, incognito!: Bool = false): Unit
```

**功能：** 为指定URL设置cookie的值。

> **说明：**
>
> - configCookie中的url，可以指定域名的方式来使得页面内请求也附带上cookie。
>
> - 同步cookie的时机建议在Web组件加载之前完成。
>
> - 若通过configCookie进行两次或多次设置cookie，则每次设置的cookie之间会通过"; "进行分隔。
>
> - cookie每30s周期性保存到磁盘中。
>
> - 若存在相同host、path和名称的cookie，将被新cookie替换。若设置的cookie已过期，则不会存储该cookie。如需设置多个cookie，应多次调用此方法。
>
> - value参数必须遵循Set-Cookie HTTP响应头的格式。形式为"key=value"的键值对，后面可跟随以分号分隔的cookie属性列表（例如"key=value;Max-Age=100"）。
>
> - 如果指定的值包含"Secure"属性，则url必须使用"https://"协议。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|要设置的cookie所属的url，建议使用完整的url。|
|value|String|是|-|要设置的cookie的值。|
|incognito|Bool|否|false|**命名参数。** true表示设置隐私模式下对应url的cookies，false表示设置正常非隐私模式下对应url的cookies。<br>默认值：false。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](./cj-errorcode-webview.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17100002 | URL error. No valid cookie found for the specified URL. |
  | 17100005 | The provided cookie value is invalid. It must follow the format specified. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    // cookie从web session中获取，如从http请求的request中获取。此示例中假设获取到的cookie为"ZFY=4Mvfh8V4iYFnDc8CGowMa3KE4m0dV"
    // 设置的cookie
    let cookie = "ZFY=4Mvfh8V4iYFnDc8CGowMa3KE4m0dV"
    // 设置指定url的cookie
    WebCookieManager.configCookie("https://www.example.com", cookie, incognito: false)
    // ... 
    // 此处执行业务逻辑，如加载带有cookie的网页。
    // 执行完后清除cookie
    WebCookieManager.clearSessionCookie()
} catch (e: BusinessException) {
    Hilog.error(0, "AppLogCj", "ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
}
```