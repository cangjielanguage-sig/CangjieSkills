# 发起认证

应用发起身份认证请求，获取身份认证结果，从而访问受保护的系统/服务/应用的功能和数据（包括用户个人数据）。

## 接口说明

具体参数、返回值、错误码等描述，请参见对应的[API文档](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#func-getuserauthinstanceauthparam-widgetparam)。

| 接口名称 | 功能描述 |
| -------- | -------- |
| getUserAuthInstance(authParam: AuthParam, widgetParam: WidgetParam): UserAuthInstance | 获取UserAuthInstance对象，用于执行用户身份认证，并支持使用统一[用户身份认证控件](#用户身份认证控件介绍)。|
| on(type: String, callback: (UserAuthResult) -> Unit): Unit | 订阅用户身份认证结果。|
| off(\`type\`: String): Unit | 取消订阅用户身份认证结果。|
| start(): Unit | 执行用户认证。|

## 用户身份认证控件介绍

系统提供了统一的用户认证控件供应用调用，使用用户认证控件的优势：

- 统一用户认证服务将通过该控件完成信息的识别和认证，再将认证结果返回给应用，整体过程安全可控，可以更好地保护用户的生物特征信息。

- 统一固定的UI组件样式，便于用户识别。

    认证控件的样式如图所示，通过[WidgetParam](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#class-widgetparam)配置对应参数。

    ![zh-cn_image_0000001789150921](./figures/zh-cn_image_0000001789150921.png)

- 标注1：用户认证界面的标题（WidgetParam.title），最大长度为500字符。应用可在此配置符合场景的字符串。

- 标注2：导航按键上显示的文本（WidgetParam.navigationButtonText），最大长度为60字符。仅在单指纹、单人脸场景下支持配置。

  当生物认证失败后，将出现该按钮，点击后从生物认证切换到应用自定义认证。

当前支持使用认证控件的认证类型包括：

- 锁屏密码认证
- 人脸认证
- 指纹认证
- 人脸+锁屏密码认证
- 指纹+锁屏密码认证
- 人脸+指纹+锁屏密码认证

> **说明：**
>
> 当前仅在单指纹、单人脸场景下支持配置导航按键上显示的文本（WidgetParam.navigationButtonText）。

## 开发步骤

1. [申请权限](./cj-prerequisites.md#申请权限)：ohos.permission.ACCESS_BIOMETRIC。
2. 指定用户认证相关参数[AuthParam](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#class-authparam)（包括挑战值、认证类型[UserAuthType](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#enum-userauthtype)列表和认证等级[AuthTrustLevel](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#enum-authtrustlevel)）、配置认证控件界面[WidgetParam](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#class-widgetparam)，调用[getUserAuthInstance](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#func-getuserauthinstanceauthparam-widgetparam)获取认证对象。
3. 调用[UserAuthInstance.on](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#func-onstring-userauthresult---unit)接口订阅认证结果。
4. 调用[UserAuthInstance.start](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#func-start)接口发起认证，通过[UserAuthInstance.on](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#func-onstring-userauthresult---unit)的回调返回认证结果[UserAuthResult](../../../API_Reference/source_zh_cn/apis/UserAuthenticationKit/cj-apis-user_auth.md#class-userauthresult)。