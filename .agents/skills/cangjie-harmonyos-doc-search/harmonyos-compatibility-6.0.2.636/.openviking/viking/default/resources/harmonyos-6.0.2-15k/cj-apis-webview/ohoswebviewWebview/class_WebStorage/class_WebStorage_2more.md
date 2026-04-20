## class WebStorage

```cangjie
public class WebStorage {}
```

**功能：** 通过WebStorage可管理Web SQL数据库接口和HTML5 Web存储接口，每个应用中的所有Web组件共享一个WebStorage。

> **说明：**
>
> 调用WebStorage下的方法，都需要先加载Web组件。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### static func deleteAllData(Bool)

```cangjie
public static func deleteAllData(incognito!: Bool = false): Unit
```

**功能：** 清除Web SQL数据库当前使用的所有存储。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|incognito|Bool|否|false| **命名参数。** true表示删除隐私模式下内存中的所有web数据，false表示删除正常非隐私模式下Web的SQL数据库当前使用的所有存储。|

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
    let webController = WebviewController()
    func build() {
        Column(10) {
            Button("deleteAllData").onClick {
                evt =>
                AppLog.info("deleteAllData")
                WebStorage.deleteAllData()
            }.width(400.px).height(150.px)
            Web(src: ("storage.html"), controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd({
                evt => AppLog.info("page end url: ${evt.url}")
            })
        }
    }
}
```

加载的html文件，请参考[deleteOrigin](#static-func-deleteoriginstring)接口下的html文件。