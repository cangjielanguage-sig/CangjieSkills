## class WebviewController

```cangjie
public class WebviewController  {
    public init()
    public init(webTag: String)
}
```

**功能：** 清除主名称所拥有的的IP地址。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

### init()

```cangjie
public init()
```

**功能：** 创建WebviewController对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

### init(String)

```cangjie
public init(webTag: String)
```

**功能：** 创建WebviewController对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|webTag|String|是|-|指定Web组件的名称。|

### static func addIntelligentTrackingPreventionBypassingList(Array\<String>)

```cangjie
public static func addIntelligentTrackingPreventionBypassingList(hostList: Array<String>): Unit
```

**功能：** 添加绕过智能防跟踪功能的域名列表。

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
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.|

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
            Button('addIntelligentTrackingPreventionBypassingList').onClick {
                _ =>
                let hostList = ["www.example.com"]
                WebviewController.addIntelligentTrackingPreventionBypassingList(hostList)
            }
            Web(src: "www.example.com", controller: controller)
        }
    }
}
```

### static func clearHostIP(String)

```cangjie
public static func clearHostIP(hostName: String): Unit
```

**功能：** 清除指定主机的IP地址。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hostName|String|是|-|需要清除IP地址的主机域名。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed.|

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
        Column() {
            Button("clearHostIP").onClick {
                WebviewController.clearHostIP("www.example.com")
            }
            Web(src: 'www.example.com', controller: this.controller)
        }
    }
}
```

### static func clearIntelligentTrackingPreventionBypassingList()

```cangjie
public static func clearIntelligentTrackingPreventionBypassingList(): Unit
```

**功能：** 删除通过[addIntelligentTrackingPreventionBypassingList](#static-func-addintelligenttrackingpreventionbypassinglistarraystring)接口添加的所有域名。

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
        Column(10) {
            Button('clearIntelligentTrackingPreventionBypassingList').onClick {
                _ => WebviewController.clearIntelligentTrackingPreventionBypassingList()
            }
            Web(src: "www.example.com", controller: controller)
        }
    }
}
```