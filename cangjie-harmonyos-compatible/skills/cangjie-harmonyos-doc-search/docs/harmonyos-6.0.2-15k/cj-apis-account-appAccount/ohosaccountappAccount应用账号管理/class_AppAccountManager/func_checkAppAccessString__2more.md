### func checkAppAccess(String, String)

```cangjie
public func checkAppAccess(name: String, bundleName: String): Bool
```

**功能：** 检查指定应用是否可访问特定账号的数据。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|bundleName|String|是|-|第三方应用的包名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示指定应用可访问特定账号的数据；返回false表示不可访问。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name or bundleName. |
  | 12300003 | Account not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("checkAppAccess_name_first")
    // com.example.test_app第三方包名
    let data = appAccountManager.checkAppAccess("checkAppAccess_name_first",
        "com.example.test_app")
    // data：true表示指定应用可访问特定账号的数据；返回false表示不可访问。
    appAccountManager.removeAccount("checkAppAccess_name_first")
    AppLog.error("test_checkAppAccess case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_checkAppAccess case1 : ${e.message.toString()}")
    appAccountManager.removeAccount("checkAppAccess_name_first")
}
```

### func checkAuthTokenVisibility(String, String, String)

```cangjie
public func checkAuthTokenVisibility(name: String, authType: String, bundleName: String): Bool
```

**功能：** 检查指定应用账号的特定鉴权类型的授权令牌对指定应用的可见性。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|authType|String|是|-|鉴权类型。|
|bundleName|String|是|-|检查可见性的应用包名。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示可见；返回false表示不可见。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name, authType or bundleName. |
  | 12300003 | Account not found. |
  | 12300107 | AuthType not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("checkAuthTokenVisibility_name_first")
    // com.example.test_app第三方包名
    let data = appAccountManager.checkAuthTokenVisibility("checkAuthTokenVisibility_name_first", "authType", "com.example.test_app")
    // data为true表示可见，data为false表示不可见
    appAccountManager.removeAccount("checkAuthTokenVisibility_name_first")
    AppLog.error("test_checkAuthTokenVisibility case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_checkAuthTokenVisibility case1 : ${e.message.toString()}")
}
```