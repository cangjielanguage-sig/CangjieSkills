### func deleteAuthToken(String, String, String, String)

```cangjie
public func deleteAuthToken(name: String, owner: String, authType: String, token: String): Unit
```

**功能：** 删除指定应用账号的特定鉴权类型的授权令牌。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|owner|String|是|-|应用账号所有者的包名。|
|authType|String|是|-|鉴权类型。|
|token|String|是|-|授权令牌。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name, owner, authType or token. |
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
    appAccountManager.createAccount("deleteAuthToken_name_first")
    // com.example.myapplication为当前包名
    appAccountManager.deleteAuthToken("deleteAuthToken_name_first", "com.example.myapplication", "authType", "test_token")
    appAccountManager.removeAccount("deleteAuthToken_name_first")
    AppLog.error("test_deleteAuthToken success")
} catch (e: BusinessException) {
    AppLog.error("test_deleteAuthToken :${e.message.toString()}")
}
```

### func deleteCredential(String, String)

```cangjie
public func deleteCredential(name: String, credentialType: String): Unit
```

**功能：** 删除指定应用账号的特定类型的凭据信息。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|credentialType|String|是|-|凭据类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name or credentialType. |
  | 12300003 | Account not found. |
  | 12300102 | Invalid name or credentialType. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("getCredential_name_first")
    appAccountManager.deleteCredential("getCredential_name_first", "credentialType1")
    appAccountManager.removeAccount("getCredential_name_first")
    AppLog.error("test_deleteCredential case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_deleteCredential case1 : ${e.message.toString()}")
}
```