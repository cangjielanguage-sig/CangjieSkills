# ohos.user_auth（用户认证）

提供用户认证能力，可应用于设备解锁、支付、应用登录等身份认证场景。

## 导入模块

```cangjie
import kit.UserAuthenticationKit.*
```

## 权限列表

ohos.permission.ACCESS_BIOMETRIC

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func getAvailableStatus(UserAuthType, AuthTrustLevel)

```cangjie
public func getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): Unit
```

**功能：** 查询指定类型和等级的认证能力是否支持。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|authType|[UserAuthType](#enum-userauthtype)|是|-|认证类型。|
|authTrustLevel|[AuthTrustLevel](#enum-authtrustlevel)|是|-|认证信任等级。|

> **错误码返回顺序说明：**
>
> - 无对应执行器注册时，判断系统不支持该认证能力，需返回12500005。
> - 有对应执行器注册时，功能未禁用，但认证安全等级低于业务指定时，需返回12500006。
> - 有对应执行器注册时，功能未禁用，但用户没有注册凭据时，需返回12500010。
> - 有对应执行器注册时，功能未禁用，但密码过期时，需返回12500013。

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户认证错误码](../../errorcodes/cj-errorcode-user-auth.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission verification failed.|
  |401|Incorrect parameters. Possible causes: 1.Mandatory parameters are left unspecified.|
  |12500002|General operation error.|
  |12500005|The authentication type is not supported.|
  |12500006|The authentication trust level is not supported.|
  |12500010|The type of credential has not been enrolled.|
  |12500013|Operation failed because of PIN expired.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.UserAuthenticationKit.*

getAvailableStatus(UserAuthType.FACE, AuthTrustLevel.ATL1)
```

## func getEnrolledState(UserAuthType)

```cangjie
public func getEnrolledState(authType: UserAuthType): EnrolledState
```

**功能：** 查询凭据注册的状态，用于感知用户注册凭据变化。

**需要权限：** ohos.permission.ACCESS_BIOMETRIC

**系统能力：** SystemCapability.UserIAM.UserAuth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|authType|[UserAuthType](#enum-userauthtype)|是|-|认证类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[EnrolledState](#class-enrolledstate)|当查询成功时，返回用户注册凭据的状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[用户认证错误码](../../errorcodes/cj-errorcode-user-auth.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission verification failed.|
  |401|Incorrect parameters. Possible causes: 1.Mandatory parameters are left unspecified.|
  |12500002|General operation error.|
  |12500005|The authentication type is not supported.|
  |12500010|The type of credential has not been enrolled.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.UserAuthenticationKit.*

let res = getEnrolledState(UserAuthType.FACE)
```