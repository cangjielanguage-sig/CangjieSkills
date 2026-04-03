## class UserAuthInstance

```cangjie
public class UserAuthInstance {}
```

**功能：** 用于执行用户身份认证，并支持使用统一用户身份认证控件。

使用以下接口前，都需要先通过[getUserAuthInstance](#func-getuserauthinstanceauthparam-widgetparam)方法获取[UserAuthInstance](#class-userauthinstance)对象。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

### func cancel()

```cangjie
public func cancel(): Unit
```

**功能：** 取消认证。

> **说明：**
>
>
> 此时UserAuthInstance需要是正在进行认证的对象。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户认证错误码](../../errorcodes/cj-errorcode-user-auth.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission verification failed.|
  |401|Incorrect parameters. Possible causes: 1.Incorrect parameter types.|
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
userAuthInstance.start()
userAuthInstance.cancel()
```

### func off(String)

```cangjie
public func off(`type`: String): Unit
```

**功能：** 取消订阅用户身份认证结果。

> **说明：**
>
> 需要使用已经成功订阅事件的[UserAuthInstance](#class-userauthinstance)对象调用该接口进行取消订阅。

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|String|是|-|订阅事件类型，表明该事件用来返回认证结果。|

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