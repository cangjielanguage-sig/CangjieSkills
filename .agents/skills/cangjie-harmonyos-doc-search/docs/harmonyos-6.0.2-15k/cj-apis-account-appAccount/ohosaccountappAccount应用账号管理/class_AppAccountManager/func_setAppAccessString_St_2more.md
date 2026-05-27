### func setAppAccess(String, String, Bool)

```cangjie
public func setAppAccess(name: String, bundleName: String, isAccessible: Bool): Unit
```

**功能：** 设置指定应用对特定账号的访问权限。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|bundleName|String|是|-|第三方应用的包名。|
|isAccessible|Bool|是|-|是否可访问。true表示允许访问，false表示禁止访问。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name or bundleName. |
  | 12300003 | Account not found. |
  | 12400001 | Application not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("setAppAccess_name_first")
    // com.example.test_app第三方包名
    appAccountManager.setAppAccess("setAppAccess_name_first", "com.example.test_app", true)
    appAccountManager.removeAccount("setAppAccess_name_first")
    AppLog.error("test_setAppAccess case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_setAppAccess case1 : ${e.message.toString()}")
    appAccountManager.removeAccount("setAppAccess_name_first")
}
```

### func setAuthToken(String, String, String)

```cangjie
public func setAuthToken(name: String, authType: String, token: String): Unit
```

**功能：** 为指定应用账号设置特定鉴权类型的授权令牌。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|authType|String|是|-|鉴权类型。|
|token|String|是|-|授权令牌。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name, authType or token. |
  | 12300003 | Account not found. |
  | 12400004 | The number of tokens reaches the upper limit. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("setAuthToken_name_first")
    appAccountManager.setAuthToken("setAuthToken_name_first", "authType", "test_token")
    appAccountManager.removeAccount("setAuthToken_name_first")
    AppLog.error("test_setAuthToken success")
} catch (e: BusinessException) {
    AppLog.error("test_setAuthToken :${e.message.toString()}")
}
```