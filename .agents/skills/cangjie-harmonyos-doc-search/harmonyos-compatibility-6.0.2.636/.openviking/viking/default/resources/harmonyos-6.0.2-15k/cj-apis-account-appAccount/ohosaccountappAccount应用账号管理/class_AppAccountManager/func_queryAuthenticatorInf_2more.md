### func queryAuthenticatorInfo(String)

```cangjie
public func queryAuthenticatorInfo(owner: String): AuthenticatorInfo
```

**功能：** 获取指定应用的认证器信息。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|owner|String|是|-|应用账号所有者的包名。|

**返回值：**

|类型|说明|
|:----|:----|
|[AuthenticatorInfo](#class-authenticatorinfo)|返回认证器信息对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid owner. |
  | 12300113 | Authenticator service not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    // com.example.myapplication当前包名
    let data = appAccountManager.queryAuthenticatorInfo("com.example.myapplication")
    AppLog.error("test_getAuthList data_iconId : ${data.iconId}")
    AppLog.error("test_getAuthList data_iconId : ${data.labelId}")
    AppLog.error("test_getAuthList success")
} catch (e: BusinessException) {
    AppLog.error("test_getAuthList : ${e.message.toString()}")
}
```

### func removeAccount(String)

```cangjie
public func removeAccount(name: String): Unit
```

**功能：** 删除应用账号。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name. |
  | 12300003 | Account not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("removeAccount_name_first")
    appAccountManager.removeAccount("removeAccount_name_first")
    AppLog.error("test_removeAccount case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_removeAccount case1 : ${e.message.toString()}")
}
```