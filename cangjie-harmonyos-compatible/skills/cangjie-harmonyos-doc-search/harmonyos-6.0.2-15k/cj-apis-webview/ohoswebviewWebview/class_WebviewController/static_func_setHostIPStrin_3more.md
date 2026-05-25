### static func setHostIP(String, String, Int32)

```cangjie
public static func setHostIP(hostName : String, address: String, aliveTime: Int32): Unit
```

**功能：** 为主机名称设置IP地址。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|hostName|String|是|-|需要设置IP地址的主机名称。|
|address|String|是|-|被设置的IP地址。|
|aliveTime|Int32|是|-|设置IP地址的高速缓冲存储器的有效时间。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*

let webviewcontroller = WebviewController()

@Entry
@Component
class EntryView {
    func build() {
        Column() {
            Button("clearHostIP").onClick {
                event: ClickEvent => WebviewController.setHostIP("www.example.com", "127.0.0.1", 30)
            }
            Web(src: 'www.example.com', controller: webviewcontroller)
        }
    }
}
```

### static func setHttpDns(SecureDnsMode, String)

```cangjie
public static func setHttpDns(secureDnsMode: SecureDnsMode, secureDnsConfig: String): Unit
```

**功能：** 设置Web组件是否使用HTTPDNS解析dns。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|secureDnsMode|[SecureDnsMode](#enum-securednsmode)|是|-|使用HTTPDNS的模式。|
|secureDnsConfig|String|是|-|HTTPDNS server的配置，必须是https协议并且只允许配置一个server。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import ohos.base.*
import kit.ArkWeb.*

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
        WebviewController.setHttpDns(SecureDnsMode.AUTO, "https://example1.test")
        AppLog.info("MainAbility onCreate done")
    }
}
```

### static func setRenderProcessMode(RenderProcessMode)

```cangjie
public static func setRenderProcessMode(mode: RenderProcessMode): Unit
```

**功能：** 设置ArkWeb渲染子进程模式。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[RenderProcessMode](#enum-renderprocessmode)|是|-|渲染子进程模式|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ArkWeb.*
import kit.UIKit.Web

let webviewcontroller = WebviewController()

@Entry
@Component
class EntryView {
    @State
    var message: String = "Hello World"
    func build() {
        Row {
            Column {
                Text(this.message).fontSize(50).fontWeight(FontWeight.Bold).onClick {
                    evt => try {
                        WebviewController.setRenderProcessMode(RenderProcessMode.MULTIPLE)
                    } catch (e: BusinessException) {
                        AppLog.error("ErrorCode: ${e.code},  Message: ${e.message}")
                    }
                }
                Web(src: 'www.example.com', controller: webviewcontroller)
            }.width(100.percent)
        }.height(100.percent)
    }
}
```