## class AppAccountManager

```cangjie
public class AppAccountManager {}
```

**功能：** 应用账号管理器类。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

### func checkAccountLabels(String, String, Array\<String>, AsyncCallback\<Bool>)

```cangjie
public func checkAccountLabels(
    name: String,
    owner: String,
    labels: Array<String>,
    callback: AsyncCallback<Bool>
): Unit
```

**功能：** 检查指定应用账号是否满足特定的标签集合。该方法依赖目标应用的认证器提供标签检查的能力。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|应用账号的名称。|
|owner|String|是|-|应用账号所有者的包名。|
|labels|Array\<String>|是|-|标签数组。|
|callback|AsyncCallback\<Bool>|是|-|回调函数。当检查成功时，err为null，data为true表示满足特定的标签集合，data为false表示不满足；否则为错误对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid name, owner or labels. |
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
    var resultCallback = {
        errorCode: Option<AsyncError>, data: Option<Bool> => match (errorCode) {
            case Some(e) => AppLog.error("checkAccountLabels error: errcode is ${e.code}")
            case _ => AppLog.error("checkAccountLabels success: result is ${data}")
        }
    }
    appAccountManager.createAccount("checkAccountLabels_name_first")
    // com.example.test_app第三方包名
    appAccountManager.checkAccountLabels("checkAccountLabels_name_first", "com.example.test_app", ["level4"], resultCallback)
    appAccountManager.removeAccount("checkAccountLabels_name_first")
    AppLog.error("test_checkAccountLabels case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_checkAccountLabels case1 : ${e.message.toString()}")
    appAccountManager.removeAccount("checkAccountLabels_name_first")
}
```