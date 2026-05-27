# 查询用户注册凭据的状态

调用者需感知用户注册凭据（人脸、指纹、口令）的变化，可以通过该接口查询当前用户注册凭据的状态。

## 接口说明

具体参数、返回值、错误码等描述，请参见对应的[API文档](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#func-getenrolledstateuserauthtype)。

| 接口名称 | 功能描述 |
| -------- | -------- |
| getEnrolledState(authType: UserAuthType): EnrolledState | 根据指定的认证类型，查询用户注册凭据的状态，用于感知注册凭据变化。 |

## 开发步骤

1. [申请权限](./cj-prerequisites.md#申请权限)：ohos.permission.ACCESS_BIOMETRIC。
2. 指定认证类型（[UserAuthType](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#enum-userauthtype)），调用[getEnrolledState](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#func-getenrolledstateuserauthtype)接口查询用户注册凭据的状态。

以查询用户人脸注册凭据的状态为例：

```cangjie
import ohos.base.*
import kit.BasicServicesKit.*
import kit.UserAuthenticationKit.*

try {
  let enrolledState = getEnrolledState(UserAuthType.FACE)
  AppLog.info('get current enrolled state success, enrolledState: ${enrolledState.credentialCount} ${enrolledState.credentialDigest}')
} catch (error: BusinessException) {
  AppLog.error('get current enrolled state failed, Code is ${error.code}, message is ${error.message}')
}
```
