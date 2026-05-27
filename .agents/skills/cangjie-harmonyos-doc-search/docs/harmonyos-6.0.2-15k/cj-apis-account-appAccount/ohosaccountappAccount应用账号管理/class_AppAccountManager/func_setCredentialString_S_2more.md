### func setCredential(String, String, String)

```cangjie
public func setCredential(name: String, credentialType: String, credential: String): Unit
```

**功能：** 设置指定应用账号的凭据。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|credentialType|String|是|-|凭据类型。|
|credential|String|是|-|凭据取值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name, credentialType or credential. |
  | 12300003 | Account not found. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("setCredential_name_first")
    appAccountManager.setCredential("setCredential_name_first", "credentialType1", "credential1")
    appAccountManager.removeAccount("setCredential_name_first")
    AppLog.error("test_setCredential case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_setCredential case1 : ${e.message.toString()}")
}
```

### func setCustomData(String, String, String)

```cangjie
public func setCustomData(name: String, key: String, value: String): Unit
```

**功能：** 设置指定应用账号的自定义数据。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|key|String|是|-|自定义数据的键名。|
|value|String|是|-|自定义数据的取值。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name, key or value. |
  | 12300003 | Account not found. |
  | 12400003 | The number of custom data reaches the upper limit. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*

let appAccountManager = createAppAccountManager()
try {
    appAccountManager.createAccount("setCustomData_name_first")
    appAccountManager.setCustomData("setCustomData_name_first", "key1", "value1")
    appAccountManager.removeAccount("setCustomData_name_first")
    AppLog.error("test_setCustomData case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_setCustomData case1 : ${e.message.toString()}")
}
```