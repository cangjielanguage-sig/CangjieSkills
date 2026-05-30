## class WebDataBase

```cangjie
public class WebDataBase {}
```

**功能：** Web组件数据库管理对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### static func deleteHttpAuthCredentials()

```cangjie
public static func deleteHttpAuthCredentials(): Unit
```

**功能：** 清除所有已保存的HTTP身份验证凭据，该方法为同步方法。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

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
                Button("deleteHttpAuthCredentials").onClick {
                    WebDataBase.deleteHttpAuthCredentials()
                }
            }.width(100.percent)
            Web(src: "www.huawei.com", controller: controller)
        }.height(100.percent)
    }
}
```

### static func existHttpAuthCredentials()

```cangjie
public static func existHttpAuthCredentials(): Bool
```

**功能：** 判断是否存在任何已保存的HTTP身份验证凭据，该方法为同步方法。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否存在任何已保存的HTTP身份验证凭据。存在返回true，不存在返回false。|

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
    let host: String = "www.example.com"
    let realm: String = "protected example"
    let controller = WebviewController()
    func build() {
        Row {
            Column {
                Button("existHttpAuthCredentials").onClick {
                    let isExist = WebDataBase.existHttpAuthCredentials()
                    AppLog.info("${isExist}")
                }
            }.width(100.percent)
            Web(src: "www.huawei.com", controller: controller)
        }.height(100.percent)
    }
}
```

### static func getHttpAuthCredentials(String, String)

```cangjie
public static func getHttpAuthCredentials(host: String, realm: String): Array<String>
```

**功能：** 检索给定主机和域的HTTP身份验证凭据，该方法为同步方法。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|host|String|是|-|HTTP身份验证凭据应用的主机。|
|realm|String|是|-|HTTP身份验证凭据应用的域。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|包含用户名和密码的组数，检索失败返回空数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed.|

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
                Button("getHttpAuthCredentials").onClick {
                    try {
                        let username_password = WebDataBase.getHttpAuthCredentials("www.example.com",
                            "protected example")
                        AppLog.info("username_password: ${username_password}")
                    } catch (error: Exception) {
                        AppLog.info(error.toString())
                    }
                }
            }.width(100.percent)
            Web(src: "www.huawei.com", controller: controller)
        }.height(100.percent)
    }
}
```