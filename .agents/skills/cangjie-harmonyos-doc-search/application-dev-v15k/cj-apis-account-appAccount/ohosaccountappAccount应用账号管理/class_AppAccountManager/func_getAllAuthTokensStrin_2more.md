### func getAllAuthTokens(String, String)

```cangjie
public func getAllAuthTokens(name: String, owner: String): Array<AuthTokenInfo>
```

**功能：** 获取指定账号对调用方可见的所有授权令牌。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|owner|String|是|-|应用账号所有者的包名。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[AuthTokenInfo](#class-authtokeninfo)>|返回授权令牌数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name or owner. |
  | 12300003 | Account not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("getAllAuthTokens_name_first")
    let data = appAccountManager.getAllAuthTokens("getAllAuthTokens_name_first",
        "com.example.myapplication")
    // data.size: 0
    appAccountManager.removeAccount("getAllAuthTokens_name_first")
    AppLog.error("test_getAllAuthTokens case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_getAllAuthTokens case1 : ${e.message.toString()}")
}
```

### func getAuthList(String, String)

```cangjie
public func getAuthList(name: String, authType: String): Array<String>
```

**功能：** 获取指定应用账号的特定鉴权类型的授权列表，即被授权的包名数组（令牌的授权列表通过[setAuthTokenVisibility](#func-setauthtokenvisibilitystring-string-string-bool)来设置）。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|authType|String|是|-|鉴权类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|返回被授权的包名数组。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name or authType. |
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
    appAccountManager.createAccount("getAuthList_name_first")
    let data = appAccountManager.getAuthList("getAuthList_name_first", "authType")
    // data.size: 1
    // data[0]: "com.example.test_app"(通过setAuthTokenVisibility设置)
    appAccountManager.removeAccount("getAuthList_name_first")
    AppLog.error("test_getAuthList case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_getAuthList case1 : ${e.message.toString()}")
}
```