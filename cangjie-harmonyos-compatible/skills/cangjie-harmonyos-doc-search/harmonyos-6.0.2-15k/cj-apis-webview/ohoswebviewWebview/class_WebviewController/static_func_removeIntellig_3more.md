### static func removeIntelligentTrackingPreventionBypassingList(Array\<String>)

```cangjie
public static func removeIntelligentTrackingPreventionBypassingList(hostList: Array<String>): Unit
```

**功能：** 删除部分由入参指定的绕过智能防跟踪功能的域名列表。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hostList|Array\<String>|是|-|绕过智能防跟踪功能的域名列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types.|

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
        Column(10) {
            Button('removeIntelligentTrackingPreventionBypassingList').onClick {
                _ => try {
                    let hostList = ["www.example.com"]
                    WebviewController.removeIntelligentTrackingPreventionBypassingList(hostList)
                } catch (e: BusinessException) {
                    AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                }
            }
            Web(src: "www.example.com", controller: controller)
        }
    }
}
```

### static func resumeAllTimers()

```cangjie
public static func resumeAllTimers(): Unit
```

**功能：** 恢复从[pauseAllTimers](#static-func-pausealltimers)接口中被暂停的所有的定时器。

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
    let webController = WebviewController()
    func build() {
        Column(10) {
            Button("resumeAllTimers").onClick {
                evt =>
                AppLog.info("resumeAllTimers")
                WebviewController.resumeAllTimers()
            }.width(400.px).height(150.px)
            Web(src: "www.example.com", controller: webController)
        }
    }
}
```

### static func setConnectionTimeout(Int32)

```cangjie
public static func setConnectionTimeout(timeout: Int32): Unit
```

**功能：** 设置网络连接超时时间，使用者可通过Web组件中的onErrorReceive方法获取超时错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|timeout|Int32|是|-|socket连接超时时间，以秒为单位，socket必须为大于0的整数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|

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
            Button("setConnectionTimeout").onClick {
                evt =>
                AppLog.info("setConnectionTimeout")
                WebviewController.setConnectionTimeout(5)
                AppLog.info("setConnectionTimeout: 5s")
            }.width(400.px).height(150.px)
            Web(src: "www.example.com", controller: webController).onPageBegin(
                {
                evt => AppLog.info("page begin url: ${evt.url}")
            }).onPageEnd({
                evt => AppLog.info("page end url: ${evt.url}")
            })
        }
    }
}
```