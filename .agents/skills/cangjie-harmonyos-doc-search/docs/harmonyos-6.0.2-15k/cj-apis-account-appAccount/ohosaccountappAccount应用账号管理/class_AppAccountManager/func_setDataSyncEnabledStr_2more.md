### func setDataSyncEnabled(String, Bool)

```cangjie
public func setDataSyncEnabled(name: String, isEnabled: Bool): Unit
```

**功能：** 开启或禁止指定应用账号的数据同步功能。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|isEnabled|Bool|是|-|是否开启数据同步。|

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
    appAccountManager.createAccount("setDataSyncEnabled_name_first")
    appAccountManager.setDataSyncEnabled("setDataSyncEnabled_name_first", true)
    appAccountManager.removeAccount("setDataSyncEnabled_name_first")
    AppLog.error("test_setDataSyncEnabled case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_setDataSyncEnabled case1 : ${e.message.toString()}")
}
```

### func verifyCredential(String, String, AuthCallback, ?VerifyCredentialOptions)

```cangjie
public func verifyCredential(name: String, owner: String, callback: AuthCallback, options: ?VerifyCredentialOptions = None): Unit
```

**功能：** 验证用户凭据。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|owner|String|是|-|应用账号所有者的包名。|
|callback|[AuthCallback](#class-authcallback)|是|-|回调函数，返回验证结果。|
|options|?[VerifyCredentialOptions](#class-verifycredentialoptions)|否|None|验证凭据的选项。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name, owner or options. |
  | 12300003 | Account not found. |
  | 12300010 | Account service busy. |
  | 12300113 | Authenticator service not found. |
  | 12300114 | Authenticator service exception. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    var options = VerifyCredentialOptions(credentialType: "verifyCredential_name_first",
        credential: "credential")
    appAccountManager.createAccount("verifyCredential_name_first")
    // com.example.myapplication当前包名
    appAccountManager.verifyCredential(
        "verifyCredential_name_first",
        "com.example.myapplication",
        AuthCallback(
            {
                code, result =>
                AppLog.error("===>verifyCredential_resultCode : ${code}")
                appAccountManager.removeAccount("verifyCredential_name_first")
            },
            {Want =>},
            onRequestContinued: {=>}
        ),
        options: options
    )
    AppLog.error("test_verifyCredential case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_verifyCredential case1 : ${e.message.toString()}")
}
```