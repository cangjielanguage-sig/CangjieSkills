### func on(OnOffType, Array\<String>, Callback1Argument\<Array\<AppAccountInfo>>)

```cangjie
public func on(`type`: OnOffType, owners: Array<String>, callback: Callback1Argument<Array<AppAccountInfo>>): Unit
```

**功能：** 订阅指定应用的账号信息变更事件。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[OnOffType](#enum-onofftype)|是|-|事件回调类型，支持的事件为'accountChange'，当目标应用更新账号信息时，触发该事件。|
|owners|Array\<String>|是|-|事件回调类型，支持的事件为'accountChange'，当目标应用更新账号信息时，触发该事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<[AppAccountInfo](#class-appaccountinfo)>>|是|-|需要注册的回调函数，返回信息为发生变更的应用账号列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid type or owners. |
  | 12400001 | Application not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class MyCallback <: Callback1Argument<Array<AppAccountInfo>> {
    public MyCallback() {}
    public open func invoke(arg: Array<AppAccountInfo>): Unit {
        AppLog.error("callback")
    }
}

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("on_name_first")
    let changeOnCallback = MyCallback()
    // com.example.myapplication当前包名
    appAccountManager.on(OnOffType.ACCOUNTCHANGE, ["com.example.myapplication"],
        changeOnCallback)
    appAccountManager.removeAccount("on_name_first")
    AppLog.error("test_on case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_on case1 : ${e.message.toString()}")
}
```