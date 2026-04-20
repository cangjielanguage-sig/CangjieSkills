### func setAuthTokenVisibility(String, String, String, Bool)

```cangjie
public func setAuthTokenVisibility(name: String, authType: String, bundleName: String, isVisible: Bool): Unit
```

**功能：** 设置指定账号的特定鉴权类型的授权令牌对指定应用的可见性。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|authType|String|是|-|鉴权类型。|
|bundleName|String|是|-|被设置可见性的应用包名。|
|isVisible|Bool|是|-|是否可见。true表示可见，false表示不可见。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name, authType or bundleName. |
  | 12300003 | Account not found. |
  | 12300107 | AuthType not found. |
  | 12400001 | Application not found. |
  | 12400005 | The size of authorization list reaches the upper limit. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("setAuthTokenVisibility_name_first")
    // com.example.test_app第三方包名
    appAccountManager.setAuthTokenVisibility("setAuthTokenVisibility_name_first", "authType",
        "com.example.test_app", true)
    appAccountManager.removeAccount("setAuthTokenVisibility_name_first")
    AppLog.error("test_setAuthTokenVisibility case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_setAuthTokenVisibility case1 : ${e.message.toString()}")
}
```