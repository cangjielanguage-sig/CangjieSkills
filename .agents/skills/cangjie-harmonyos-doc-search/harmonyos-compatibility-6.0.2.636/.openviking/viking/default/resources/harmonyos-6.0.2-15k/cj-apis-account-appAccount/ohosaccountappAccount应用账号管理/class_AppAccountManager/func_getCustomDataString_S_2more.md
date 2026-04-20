### func getCustomData(String, String)

```cangjie
public func getCustomData(name: String, key: String): String
```

**功能：** 根据指定键名获取特定应用账号的自定义数据。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|key|String|是|-|自定义数据的键名。|

**返回值：**

|类型|说明|
|:----|:----|
|String|自定义数据的取值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name or key. |
  | 12300003 | Account not found. |
  | 12400002 | Custom data not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("getCustomData_name_first")
    let data = appAccountManager.getCustomData("getCustomData_name_first", "key1")
    // data: "value1"(由setCustomData设置)
    appAccountManager.removeAccount("getCustomData_name_first")
    AppLog.error("test_getCustomData case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_getCustomData case1 : ${e.message.toString()}")
}
```

### func off(OnOffType, ?Callback1Argument\<Array\<AppAccountInfo>>)

```cangjie
public func off(`type`: OnOffType, callback: ?Callback1Argument<Array<AppAccountInfo>> = None): Unit
```

**功能：** 取消订阅账号信息变更事件。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[OnOffType](#enum-onofftype)|是|-|事件回调类型，支持的事件为'accountChange'，当账号所有者更新账号信息时，触发该事件。|
|callback|?[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<[AppAccountInfo](#class-appaccountinfo)>>|否|None|需要注销的回调函数，默认为空，表示取消该类型事件所有的回调。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid type. |

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
    appAccountManager.createAccount("off_name_first")
    let changeOnCallback = MyCallback()
    // com.example.myapplication当前包名
    appAccountManager.on(OnOffType.ACCOUNTCHANGE, ["com.example.myapplication"],
        changeOnCallback)
    appAccountManager.off(OnOffType.ACCOUNTCHANGE, callback: changeOnCallback)
    appAccountManager.removeAccount("off_name_first")
    AppLog.error("test_off case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_off case1 : ${e.message.toString()}")
}
```