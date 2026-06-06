### func checkDataSyncEnabled(String)

```cangjie
public func checkDataSyncEnabled(name: String): Bool
```

**功能：** 检查指定应用账号是否开启数据同步功能。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示指定应用账号已开启数据同步功能；返回false表示未开启。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 201 | Permission verification failed. The application does not have the permission required to call the API. |
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
    appAccountManager.createAccount("checkDataSyncEnabled_name_first")
    let data = appAccountManager.checkDataSyncEnabled("checkDataSyncEnabled_name_first")
    // data：返回true表示指定应用账号已开启数据同步功能；返回false表示未开启；通过setDataSyncEnabled设置
    appAccountManager.removeAccount("checkDataSyncEnabled_name_first")
    AppLog.error("test_checkDataSyncEnabled case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_checkDataSyncEnabled case1 : ${e.message.toString()}")
    appAccountManager.removeAccount("checkDataSyncEnabled_name_first")
}
```

### func createAccount(String, ?CreateAccountOptions)

```cangjie
public func createAccount(name: String, options!: ?CreateAccountOptions = None): Unit
```

**功能：** 根据账号名和可选项创建应用账号。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|options|?[CreateAccountOptions](#class-createaccountoptions)|否|None| **命名参数。** 创建应用账号的选项，可提供自定义数据，但不建议包含敏感数据（如密码、Token等）。不填无影响，默认为空，表示创建的该账号无额外信息需要添加。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name or options. |
  | 12300004 | Account already exists. |
  | 12300007 | The number of accounts reaches the upper limit. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("createAccount_name_first")
    AppLog.error("test_createAccount case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_createAccount case1 : ${e.message.toString()}")
}
```