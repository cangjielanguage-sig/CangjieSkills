# 查询支持的认证能力

不同的设备对于认证能力（人脸、指纹、口令）的支持性各有差异，开发者在发起认证前应当先查询当前设备支持的用户认证能力。

## 接口说明

具体参数、返回值、错误码等描述，请参见对应的[API文档](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#func-getavailablestatususerauthtype-authtrustlevel)。

| 接口名称 | 功能描述 |
| -------- | -------- |
| getAvailableStatus(authType: UserAuthType, authTrustLevel: AuthTrustLevel): Unit | 根据指定的认证类型、认证等级，检测当前设备是否支持相应的认证能力。 |

## 开发步骤

1. [申请权限](./cj-prerequisites.md#申请权限)：ohos.permission.ACCESS_BIOMETRIC。
2. 指定认证类型（[UserAuthType](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#enum-userauthtype)）和认证等级（[AuthTrustLevel](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#enum-authtrustlevel)），调用[getAvailableStatus](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#func-getavailablestatususerauthtype-authtrustlevel)接口查询当前的设备是否支持相应的认证能力。

认证可信等级的详细介绍请参见[认证可信等级划分原则](../../security/UserAuthenticationKit/cj-user-authentication-overview.md)。

以查询设备是否支持认证可信等级≥ATL1的人脸认证功能为例：

```cangjie
import ohos.base.*
import kit.BasicServicesKit.*
import kit.UserAuthenticationKit.*

// 查询认证能力是否支持
try {
    getAvailableStatus(UserAuthType.FACE, AuthTrustLevel.ATL1)
    AppLog.info('current auth trust level is supported')
} catch (err:BusinessException) {
    AppLog.error('current auth trust level is not supported. Code is ${err.code}, message is ${err.message}')
}
```
