### func startAbilityByType(String, String, AbilityStartCallback)

```cangjie
public func startAbilityByType(abilityType: String, wantParam: String,
    abilityStartCallback: AbilityStartCallback): Unit
```

**功能：** 通过type隐式启动UIExtensionAbility。仅支持在主线程调用，仅支持处于前台的应用调用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|abilityType|String|是|-|显示拉起的UIExtensionAbility类型。|
|wantParam|String|是|-|json风格的字符串，表示扩展参数。|
|abilityStartCallback|[AbilityStartCallback](#class-abilitystartcallback)|是|-|执行结果回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16000050|Internal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*

let uiAbilityContext = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let callBack = AbilityStartCallback(
    {
        code, name, message =>
        AppLog.info("AbilityStartCallback onError code ${code}")
        AppLog.info("AbilityStartCallback onError code ${name}")
        AppLog.info("AbilityStartCallback onError message ${message}")
    },
    onResult: {
        result =>
        AppLog.info("AbilityStartCallback onResult result ${result.resultCode}")
        AppLog.info("AbilityStartCallback onResult result ${result.want.uri}")
        AppLog.info("AbilityStartCallback onResult result ${result.want.parameters}")
        AppLog.info("AbilityStartCallback onResult result ${result.want.bundleName}")
    }
)

let flag = Int64(Flags.FLAG_AUTH_READ_URI_PERMISSION.getValue())
uiAbilityContext.startAbilityByType("photoEditor", ##"{"ability.params.stream",["file://com.example.myapplication"],"ability.want.params.uriPermissionFlag":${flag}}"##, callBack)
AppLog.info("startAbilityByType success")
```