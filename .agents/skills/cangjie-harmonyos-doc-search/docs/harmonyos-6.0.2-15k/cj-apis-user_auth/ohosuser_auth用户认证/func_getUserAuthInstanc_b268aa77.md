## func getUserAuthInstance(AuthParam, WidgetParam)

```cangjie
public func getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance
```

**功能：** 获取[UserAuthInstance](#class-userauthinstance)对象，用于执行用户身份认证，并支持使用统一用户身份认证控件。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|authParam|[AuthParam](#class-authparam)|是|-|用户认证相关参数。|
|widgetParam|[WidgetParam](#class-widgetparam)|是|-|用户认证界面配置相关参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[UserAuthInstance](#class-userauthinstance)|支持用户界面的认证器对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户认证错误码](../../errorcodes/cj-errorcode-user-auth.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Incorrect parameters. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed.|
  |12500002|General operation error.|
  |12500005|The authentication type is not supported.|
  |12500006|The authentication trust level is not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.UserAuthenticationKit.*

let userAuthInstance = getUserAuthInstance(
    AuthParam([], [UserAuthType.FACE], AuthTrustLevel.ATL1),
    WidgetParam("TEST FACE_ATL1", "")
)
```