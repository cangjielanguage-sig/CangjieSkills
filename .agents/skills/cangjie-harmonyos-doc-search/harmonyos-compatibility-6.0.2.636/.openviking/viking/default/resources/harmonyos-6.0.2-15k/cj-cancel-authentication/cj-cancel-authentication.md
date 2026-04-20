# 认证过程中取消认证

统一用户认证框架提供了cancel接口，当应用在认证过程中，需要取消认证时可调用该接口。

## 接口说明

具体参数、返回值、错误码等描述，请参见对应的[API文档](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#func-cancel)。

此处仅展示了取消认证操作的接口，在取消认证前，需要先发起认证，发起认证的接口列表、详细说明请参见[发起认证](./cj-start-authentication.md)章节和API文档。

| 接口名称 | 功能描述 |
| -------- | -------- |
| cancel(): Unit | 取消本次认证操作。 |

## 开发步骤

1. [申请权限](cj-prerequisites.md#申请权限)：ohos.permission.ACCESS_BIOMETRIC。
2. 指定用户认证相关参数[AuthParam](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#class-authparam)（包括挑战值、认证类型[UserAuthType](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#enum-userauthtype)列表和认证等级[AuthTrustLevel](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#enum-authtrustlevel)），获取认证对象[UserAuthInstance](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#class-userauthinstance)，并调用[UserAuthInstance.start](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#func-start)发起认证。此步骤详细说明请参见[发起认证](./cj-start-authentication.md)。
3. 通过使用已经成功发起认证的UserAuthInstance对象调用[UserAuthInstance.cancel](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#func-cancel)接口取消本次认证。

示例代码为发起认证可信等级≥ATL3的人脸+锁屏密码认证后，取消认证请求：

```cangjie
import ohos.base.*
import kit.BasicServicesKit.*
import kit.CryptoArchitectureKit.*
import kit.UserAuthenticationKit.*

try {
  let rand = createRandom()
  let len: Int32 = 16
  let randData = rand.generateRandom(len).data
  // 设置认证参数
  let authParam = AuthParam(randData,[UserAuthType.PIN, UserAuthType.FACE],AuthTrustLevel.ATL3,)
  // 配置认证界面
  let widgetParam = WidgetParam('请进行身份认证', '')
  // 获取认证对象
  let userAuthInstance = getUserAuthInstance(authParam, widgetParam)
  AppLog.info('get userAuth instance success')
  // 开始认证
  userAuthInstance.start()
  AppLog.info('auth start success')
  // 取消认证
  userAuthInstance.cancel()
  AppLog.info('auth cancel success')
} catch (error :BusinessException) {
  AppLog.error('auth catch error. Code is ${error.code}, message is ${error.message}')
}
```
