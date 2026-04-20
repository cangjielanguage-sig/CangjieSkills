## class WebCookieManager

```cangjie
public class WebCookieManager {}
```

**功能：** 通过WebCookie可以控制Web组件中的cookie的各种行为，其中每个应用中的所有web组件共享一个WebCookieManager实例。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

### static func clearAllCookies(Bool)

```cangjie
public static func clearAllCookies(incognito!: Bool = false): Unit
```

**功能：** 清除所有cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|incognito|Bool|否|false|**命名参数。** true表示清除隐私模式下Webview的所有内存cookies，false表示清除正常非隐私模式下的持久化cookies。<br>默认值：false。|

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
    WebCookieManager.clearAllCookies()
} catch (e: BusinessException) {
    Hilog.error(0, "AppLogCj", "ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
}
```

### static func clearSessionCookie()

```cangjie
public static func clearSessionCookie(): Unit
```

**功能：** 清除所有会话cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

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