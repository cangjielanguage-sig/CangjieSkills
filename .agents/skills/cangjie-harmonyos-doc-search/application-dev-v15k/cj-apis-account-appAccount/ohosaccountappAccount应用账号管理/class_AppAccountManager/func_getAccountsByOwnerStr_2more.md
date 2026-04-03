### func getAccountsByOwner(String)

```cangjie
public func getAccountsByOwner(owner: String): Array<AppAccountInfo>
```

**功能：** 获取调用方可访问的指定所有者的应用账号列表。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|owner|String|是|-|应用账号所有者的包名。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[AppAccountInfo](#class-appaccountinfo)>|获取到的应用账号列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid owner. |
  | 12400001 | Application not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("getAccountsByOwner_name_first")
    // com.example.myapplication当前包名
    let data = appAccountManager.getAccountsByOwner("com.example.myapplication")
    // data长度为1
    // data[0].name: "getAccountsByOwner_name_first"
    // data[0].owner: "com.example.myapplication"
    appAccountManager.removeAccount("getAccountsByOwner_name_first")
    AppLog.error("test_getAccountsByOwner case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_getAccountsByOwner case1 : ${e.message.toString()}")
}
```

### func getAllAccounts()

```cangjie
public func getAllAccounts(): Array<AppAccountInfo>
```

**功能：** 获取所有可访问的应用账号信息。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[AppAccountInfo](#class-appaccountinfo)>|返回全部应用已授权账号信息对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 12300001 | System service exception. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("getAllAccounts_name_first")
    let data = appAccountManager.getAllAccounts()
    // data.size: 1
    // data[0].name: "getAllAccounts_name_first"
    // data[0].owner: "com.example.myapplication"
    appAccountManager.removeAccount("getAllAccounts_name_first")
    AppLog.error("test_getAllAccounts success")
} catch (e: BusinessException) {
    AppLog.error("test_getAllAccounts :${e.message.toString()}")
    appAccountManager.removeAccount("getAllAccounts_name_first")
}
```