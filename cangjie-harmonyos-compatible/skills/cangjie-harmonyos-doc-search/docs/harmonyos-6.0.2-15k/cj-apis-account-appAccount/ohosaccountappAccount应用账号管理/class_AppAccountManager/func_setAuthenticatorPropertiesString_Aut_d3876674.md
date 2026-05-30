### func setAuthenticatorProperties(String, AuthCallback, ?SetPropertiesOptions)

```cangjie
public func setAuthenticatorProperties(owner: String, callback: AuthCallback, options: ?SetPropertiesOptions = None): Unit
```

**功能：** 设置指定应用的认证器属性。

**系统能力：** SystemCapability.Account.AppAccount

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|owner|String|是|-|认证器的所有者的包名。|
|callback|[AuthCallback](#class-authcallback)|是|-|回调函数，返回设置属性的结果。|
|options|?[SetPropertiesOptions](#class-setpropertiesoptions)|否|None|设置属性的选项。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[账号管理错误码](../../errorcodes/cj-errorcode-basic-account.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :-------- |
  | 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
  | 12300001 | System service exception. |
  | 12300002 | Invalid owner or options. |
  | 12300010 | Account service busy. |
  | 12300113 | Authenticator service not found. |
  | 12300114 | Authenticator service exception. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.BasicServicesKit.*
import ohos.base.*
import std.collection.HashMap

let appAccountManager = createAppAccountManager()
try {
    let strV = AppAccountValueType.STRING("credential")
    let data = HashMap<String, AppAccountValueType>()
    data.add("credentialType", strV)
    var options = SetPropertiesOptions(properties: data)
    appAccountManager.createAccount("setAuthenticatorProperties_name_first")
    // com.example.test_app第三方包名
    appAccountManager.setAuthenticatorProperties(
        "com.example.test_app",
        AuthCallback(
            {
                code, result =>
                AppLog.error("===>setAuthenticatorProperties_resultCode : ${code}")
                appAccountManager.removeAccount("setAuthenticatorProperties_name_first")
            },
            {Want =>},
            onRequestContinued: {=>}
        ),
        options: options
    )
    AppLog.error("test_setAuthenticatorProperties case1 success")
} catch (e: BusinessException) {
    AppLog.error("test_setAuthenticatorProperties case1 : ${e.message.toString()}")
}
```