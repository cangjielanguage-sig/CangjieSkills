### static func prefetchResource(RequestInfo, Array\<WebHeader>, String, Int32)

```cangjie
public static func prefetchResource(
    request: RequestInfo,
    additionalHeaders!: Array<WebHeader> = Array<WebHeader>(),
    cacheKey!: String = "", cacheValidTime!: Int32 = 0): Unit
```

**功能：** 根据指定的请求信息和附加的http请求头去预获取资源请求，存入内存缓存，并指定其缓存key和有效期，以加快加载速度。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|request|[RequestInfo](#class-requestinfo)|是|-|预获取请求的信息。|
|additionalHeaders|Array\<[WebHeader](#class-webheader)>|否|Array\<WebHeader>()| **命名参数。** 预获取请求的附加HTTP请求头。|
|cacheKey|String|否|""| **命名参数。** 用于后续查询预获取资源缓存的key。仅支持字母和数字，未传入或传入空则取默认值url作为key。|
|cacheValidTime|Int32|否|0| **命名参数。** 预获取资源缓存的有效期。单位：秒。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Invalid input parameter.Possible causes: 1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed.|
  |17100002|Invalid url.|

### static func prepareForPageLoad(String, Bool, Int32)

```cangjie
public static func prepareForPageLoad(url: String, preconnectable: Bool, numSockets: Int32): Unit
```

**功能：** 预连接url，在加载url之前调用此API，对url只进行dns解析，socket建链操作，并不获取主资源子资源。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|预连接的url。|
|preconnectable|Bool|是|-|是否进行预连接。如果preconnectable为true，则对url进行dns解析，socket建链预连接；如果preconnectable为false，则不做任何预连接操作。|
|numSockets|Int32|是|-|要预连接的socket数。socket数目连接需要大于0，最多允许6个连接。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100002|Invalid url.|
  |171000013|The number of preconnect sockets is invalid.|

**示例：**

<!-- compile -->

```cangjie
// main_ability.cj

import kit.AbilityKit.*
import ohos.base.AppLog
import kit.ArkWeb.*

class MainAbility <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        AppLog.info("MainAbility OnCreated.${want.abilityName}")
        match (launchParam.launchReason) {
            case LaunchReason.START_ABILITY => AppLog.info("START_ABILITY")
            case _ => ()
        }
        WebviewController.initializeWebEngine()
        WebviewController.prepareForPageLoad("https://www.example.com", true, 2)
        AppLog.info("prepareForPageLoad success")
        AppLog.info("MainAbility onCreate done")
    }
}
```