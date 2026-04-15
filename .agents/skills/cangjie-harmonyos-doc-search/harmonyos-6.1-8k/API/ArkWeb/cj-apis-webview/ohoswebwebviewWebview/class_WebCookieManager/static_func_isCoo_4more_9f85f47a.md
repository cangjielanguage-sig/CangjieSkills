### static func isCookieAllowed()

```cangjie
public static func isCookieAllowed(): Bool
```

**功能：** 获取WebCookieManager实例是否拥有发送和接收cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否拥有发送和接收cookie的权限。<br>true表示拥有发送和接收cookie的权限，false表示无发送和接收cookie的权限。<br>默认值：true。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*
import kit.PerformanceAnalysisKit.Hilog

let result = WebCookieManager.isCookieAllowed()
Hilog.info(0, "AppLogCj",  "WebCookieManager, result: ${result}")
```

### static func isThirdPartyCookieAllowed()

```cangjie
public static func isThirdPartyCookieAllowed(): Bool
```

**功能：** 获取WebCookieManager实例是否拥有发送和接收第三方cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否拥有发送和接收第三方cookie的权限。<br>true表示拥有发送和接收第三方cookie的权限，false表示无发送和接收第三方cookie的权限。<br>默认值：false。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*
import kit.PerformanceAnalysisKit.Hilog

let result = WebCookieManager.isThirdPartyCookieAllowed()
Hilog.info(0, "AppLogCj",  "WebCookieManager, result: ${result}")
```

### static func setAcceptCookiesEnabled(Bool)

```cangjie
public static func setAcceptCookiesEnabled(accept: Bool): Unit
```

**功能：** 设置WebCookieManager实例是否拥有发送和接收cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|accept|Bool|是|-|设置是否拥有发送和接收cookie的权限，true表示拥有发送和接收cookie的权限。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*
import kit.PerformanceAnalysisKit.Hilog

WebCookieManager.setAcceptCookiesEnabled(false)
```

### static func setAcceptThirdPartyCookieEnabled(Bool)

```cangjie
public static func setAcceptThirdPartyCookieEnabled(accept: Bool): Unit
```

**功能：** 设置WebCookieManager实例是否拥有发送和接收第三方cookie的权限。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|accept|Bool|是|-|是否允许设置、获取第三方cookie。<br>true表示允许设置、获取第三方cookie，false表示不允许设置、获取第三方cookie。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ArkWeb.*
import kit.PerformanceAnalysisKit.Hilog

WebCookieManager.setAcceptThirdPartyCookieEnabled(true)
```