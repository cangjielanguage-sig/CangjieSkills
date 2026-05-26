## func startAbility(Want)

```cangjie
public func startAbility(want: Want): Unit
```

**功能：** 拉起目标应用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|want|[Want](../AbilityKit/cj-apis-ability.md#class-want)|是|-|当前Extension相关的Want类型信息，包括ability名称、bundle名称等。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[输入法框架错误码](../../errorcodes/cj-errorcode-inputmethod.md)，[元能力错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |16000001|The specified ability does not exist.|
  |16000002|Incorrect ability type.|
  |16000004|Cannot start an invisible component.|
  |16000005|The specified process does not have the permission.|
  |16000006|Cross-user operations are not allowed.|
  |16000008|The crowdtesting application expires.|
  |16000009|An ability cannot be started or stopped in Wukong mode.|
  |16000010|The call with the continuation and prepare continuation flag is forbidden.|
  |16000011|The context does not exist.|
  |16000012|The application is controlled.|
  |16000013|The application is controlled by EDM.|
  |16000019|No matching ability is found.|
  |16000050|Internal error.|
  |16000053|The ability is not on the top of the UI.|
  |16000055|Installation-free timed out.|
  |16000061|Operation not supported.|
  |16200001|The caller has been released.|
  |16000069|The extension cannot start the third party application.|
  |16000070|The extension cannot start the service.|

**示例：**

<!-- compile -->

```cangjie
import kit.IMEKit.{InputMethodExtensionAbility, InputMethodExtensionContext}
import kit.AbilityKit.Want
import ohos.base.BusinessException

let InputMethod_ABILITY_REGISTER_RESULT = InputMethodExtensionAbility.registerCreator("ExampleAbility") {
    ExampleAbility()
}

class ExampleAbility <: InputMethodExtensionAbility {
    public func onCreate(want: Want): Unit {
        AppLog.info("ExampleAbility oncreate success")
    }

    public func onDestroy(): Unit {
        let want = Want(bundleName: "com.example.myapplication", moduleName: "entry", abilityName: "EntryAbility")
        try {
            this.context.startAbility(want)
        } catch (e: BusinessException) {
            AppLog.error("e.code = ${e.code}")
            AppLog.error("e.message = ${e.message}")
        }
    }
}
```