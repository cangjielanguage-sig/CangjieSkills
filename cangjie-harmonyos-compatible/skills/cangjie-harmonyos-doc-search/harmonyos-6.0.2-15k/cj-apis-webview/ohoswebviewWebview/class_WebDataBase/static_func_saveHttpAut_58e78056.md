### static func saveHttpAuthCredentials(String, String, String, String)

```cangjie
public static func saveHttpAuthCredentials(host: String, realm: String, username: String, password: String): Unit
```

**功能：** 保存给定主机和域的HTTP身份验证凭据，该方法为同步方法。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|host|String|是|-|HTTP身份验证凭据应用的主机。|
|realm|String|是|-|HTTP身份验证凭据应用的域。|
|username|String|是|-|用户名。|
|password|String|是|-|密码。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.Web

@Entry
@Component
class EntryView {
    let controller = WebviewController()
    func build() {
        Row {
            Column {
                Button("saveHttpAuthCredentials").onClick {
                    WebDataBase.saveHttpAuthCredentials("www.example.com", "protected example", "Stromgol", "Laroche")
                }
            }.width(100.percent)
            Web(src: "www.huawei.com", controller: controller)
        }.height(100.percent)
    }
}
```