### func on(String, (UserAuthResult) -> Unit)

```cangjie
public func on(`type`: String, callback: (UserAuthResult) -> Unit): Unit
```

**功能：** 订阅用户身份认证结果。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|String|是|-|订阅事件类型，表明该事件用来返回认证结果。|
|callback|([UserAuthResult](#class-userauthresult)) -> Unit|是|-|认证接口的回调函数，用于返回认证结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户认证错误码](../../errorcodes/cj-errorcode-user-auth.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Incorrect parameters. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.|
  |12500002|General operation error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.UserAuthenticationKit.*

let userAuthInstance = getUserAuthInstance(
    AuthParam([], [UserAuthType.FINGERPRINT], AuthTrustLevel.ATL3),
    WidgetParam("TEST FINGERPRINT_ATL3", "")
)
userAuthInstance.on("result", {u => userAuthInstance.off("result")})
```

### func start()

```cangjie
public func start(): Unit
```

**功能：** 开始认证。

> **说明：**
>
> 每个UserAuthInstance只能进行一次认证，若需要再次进行认证则需重新获取UserAuthInstance。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户认证错误码](../../errorcodes/cj-errorcode-user-auth.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission verification failed.|
  |401|Incorrect parameters. Possible causes: 1.Incorrect parameter types.|
  |12500001|Authentication failed.|
  |12500002|General operation error.|
  |12500003|Authentication canceled.|
  |12500004|Authentication timeout.|
  |12500005|The authentication type is not supported.|
  |12500006|The authentication trust level is not supported.|
  |12500007|Authentication service is busy.|
  |12500009|Authentication is locked out.|
  |12500010|The type of credential has not been enrolled.|
  |12500011|Switched to the custom authentication process.|
  |12500013|Operation failed because of PIN expired.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.UserAuthenticationKit.*

let userAuthInstance = getUserAuthInstance(
    AuthParam([], [UserAuthType.FINGERPRINT], AuthTrustLevel.ATL3),
    WidgetParam("TEST FINGERPRINT_ATL3", "")
)
userAuthInstance.on("result", {u => userAuthInstance.off("result")})
userAuthInstance.start()
```