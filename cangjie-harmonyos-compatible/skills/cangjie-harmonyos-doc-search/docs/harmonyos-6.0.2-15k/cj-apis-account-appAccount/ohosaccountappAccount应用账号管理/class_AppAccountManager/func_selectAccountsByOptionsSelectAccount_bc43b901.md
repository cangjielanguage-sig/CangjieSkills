### func selectAccountsByOptions(SelectAccountsOptions, AsyncCallback\<Array\<AppAccountInfo>>)

```cangjie
public func selectAccountsByOptions(
    options: SelectAccountsOptions,
    callback: AsyncCallback<Array<AppAccountInfo>>
): Unit
```

**功能：** 根据选项选择调用方可访问的账号列表。使用callback异步回调。如果选项中包含标签约束，则该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|options|[SelectAccountsOptions](#class-selectaccountsoptions)|是|-|选择账号的选项。|
|callback|AsyncCallback\<Array\<[AppAccountInfo](#class-appaccountinfo)>>|是|-|回调函数。当根据选项选择请求方可访问的账号列表时，err为null，data为可访问的账号信息对象；否则为错误对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300010 | Account service busy. |
  | 12300114 | Authenticator service exception. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    var resultCallback = {
        errorCode: Option<AsyncError>, data: Option<Array<AppAccountInfo>> => match (errorCode) {
            case Some(e) => AppLog.error("selectAccountsByOptions error: errcode is ${e.code}")
            case _ => match (data) {
                case Some(value) => for (i in (0..value.size)) {
                    AppLog.error("selectAccountsByOptions success: ")
                    AppLog.error("result is ${value[i].name} - ${value[i].owner}")
                }
                case _ => AppLog.error("selectAccountsByOptions error: result is null")
            }
        }
    }
    // com.example.test_app第三方包名
    let info = AppAccountInfo("selectAccountsByOptions_name_first", "com.example.test_app")
    let data: Array<AppAccountInfo> = [info]
    var select_options = SelectAccountsOptions(allowedAccounts: data)
    appAccountManager.createAccount("selectAccountsByOptions_name_first")
    appAccountManager.selectAccountsByOptions(select_options, resultCallback)
    appAccountManager.removeAccount("selectAccountsByOptions_name_first")
    AppLog.error("test_selectAccountsByOptions success")
} catch (e: BusinessException) {
    AppLog.error("test_selectAccountsByOptions :${e.message.toString()}")
    appAccountManager.removeAccount("selectAccountsByOptions_name_first")
}
```