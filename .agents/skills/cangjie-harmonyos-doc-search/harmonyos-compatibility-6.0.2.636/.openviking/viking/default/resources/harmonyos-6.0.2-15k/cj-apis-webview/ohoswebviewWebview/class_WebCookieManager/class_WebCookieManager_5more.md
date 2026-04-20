## class WebCookieManager

```cangjie
public class WebCookieManager {}
```

**功能：** 通过WebCookie可以控制Web组件中的cookie的各种行为，其中每个应用中的所有web组件共享一个WebCookieManager实例。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

### static func clearAllCookies(Bool)

```cangjie
public static func clearAllCookies(incognito!: Bool = false): Unit
```

**功能：** 清除所有cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|incognito|Bool|否|false| **命名参数。** true表示清除隐私模式下webview的所有内存cookies，false表示清除正常非隐私模式下的所有cookies。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*
import kit.UIKit.Web

WebCookieManager.clearAllCookies()
```

### static func clearSessionCookie()

```cangjie
public static func clearSessionCookie(): Unit
```

**功能：** 清除所有会话cookie。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*

WebCookieManager.clearSessionCookie()
```

### static func configCookie(String, String, Bool)

```cangjie
public static func configCookie(url: String, value: String, incognito!: Bool = false): Unit
```

**功能：** 为指定url设置cookie的值。

> **说明：**
>
> - 通过url指定域名，来使得页面内请求也附带上cookie。
> - 同步cookie的时机，建议在webview组件加载之前。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|要设置的cookie所属的URL，建议使用完整的URL。|
|value|String|是|-|要设置的cookie的值。|
|incognito|Bool|否|false| **命名参数。** true表示设置隐私模式下对应url的cookies，false表示设置正常非隐私模式下对应URL的cookies。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100002|Invalid url.|
  |17100005|Invalid cookie value.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*

WebCookieManager.configCookie("https://www.example.com", "a=b,c=d,e=f")
```

### static func configCookie(String, String, Bool, Bool)

```cangjie
public static func configCookie(url: String, value: String, incognito!: Bool, includeHttpOnly!: Bool): Unit
```

**功能：** 为指定URL设置cookie的值。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|要设置的cookie所属的URL，建议使用完整的URL。|
|value|String|是|-|要设置的cookie的值。|
|incognito|Bool|是|-|true表示设置隐私模式下对应URL的cookies，false表示设置正常非隐私模式下对应URL的cookies。|
|includeHttpOnly|Bool|是|-|true表示允许覆盖含有http-only的cookies，false表示不允许覆盖含有http-only的cookies。|

**异常：**

- BusinessException：对应错误码如下表，详见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Invalid input parameter.|
  |17100002|Invalid url.|
  |17100005|Invalid cookie value.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*

try {
    WebCookieManager.configCookie("https://www.example.com", "a=b", incognito: false, includeHttpOnly: false)
} catch (e: BusinessException) {
    AppLog.error("ErrorCode: ${e.code}, ErrorMessage: ${e.message}")
}
```