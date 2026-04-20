### static func hasCookie(Bool)

```cangjie
public static func hasCookie(incognito!: Bool = false): Bool
```

**功能：** 获取是否存在cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|incognito|Bool|否|false|**命名参数。** true表示隐私模式下查询是否存在cookies，false表示正常非隐私模式下查询是否存在cookies。<br>默认值：false。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true表示存在cookie，false表示不存在cookie。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*
import kit.PerformanceAnalysisKit.Hilog

let result = WebCookieManager.hasCookie()
Hilog.info(0, "AppLogCj", "WebCookiemanager result: ${result}")
```

### static func fetchCookie(String, Bool)

```cangjie
public static func fetchCookie(url: String, incognito!: Bool = false): String
```

**功能：** 获取指定url对应cookie的值。

> **说明：**
>
> - 系统会自动清理过期的cookie，对于同名key的数据，新数据将会覆盖前一个数据。
>
> - 为了获取可正常使用的cookie值，fetchCookie需传入完整链接。
>
> - fetchCookie用于获取所有的cookie值，每条cookie值之间会通过"; "进行分隔，但无法单独获取某一条特定的cookie值。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|要获取的cookie所属的url，建议使用完整的url。|
|incognito|Bool|否|false|**命名参数。** true表示获取隐私模式下webview的内存cookies，false表示正常非隐私模式下的cookies。<br>默认值：false。|

**返回值：**

|类型|说明|
|:----|:----|
|String|指定url对应的cookie的值。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](./cj-errorcode-webview.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 17100002 | URL error. No valid cookie found for the specified URL. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    // 需要设置的cookie，其中cookie的格式为name=value，本例中name为ZFY，value为4Mvfh8V4iYFnDc8CGowMa3KE4m0dV
    let cookie = "ZFY=4Mvfh8V4iYFnDc8CGowMa3KE4m0dV"
    // 设置指定url的cookie
    WebCookieManager.configCookie("https://www.example.com", cookie, incognito: false)
    // 设置完后获取指定url的cookie
    let value = WebCookieManager.fetchCookie("https://www.example.com")
    Hilog.info(0, "AppLogCj",  "WebCookieManager,fetchCookie cookie = ${value}", "")
} catch (e: BusinessException) {
    Hilog.error(0, "AppLogCj", "ErrorCode: ${e.code}, ErrorMessage: ${e.message}", "")
}
```