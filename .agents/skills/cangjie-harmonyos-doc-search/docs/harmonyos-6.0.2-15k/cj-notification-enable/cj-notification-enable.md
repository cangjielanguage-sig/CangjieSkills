# 请求通知授权

应用需要获取用户授权才能发送通知。在通知发布前调用[requestEnableNotification()](../../API_Reference/source_zh_cn/apis/NotificationKit/cj-apis-notification_manager.md#func-requestenablenotificationabilitycontext)方法，弹窗让用户选择是否允许发送通知，后续再次调用[requestEnableNotification()](../../API_Reference/source_zh_cn/apis/NotificationKit/cj-apis-notification_manager.md#func-requestenablenotificationabilitycontext)方法时，则不再弹窗。

## 接口说明

接口详情参见[API参考](../../API_Reference/source_zh_cn/apis/NotificationKit/cj-apis-notification_manager.md#func-requestenablenotificationabilitycontext)。

**表1** 通知授权接口功能介绍

| **接口名**  | **描述** |
| -------- | -------- |
| isNotificationEnabled():Bool       | 查询通知是否授权。  |
| requestEnableNotification(context: UIAbilityContext): Unit | 请求发送通知的许可，第一次调用会弹窗让用户选择。     |

## 开发步骤

1. 导入NotificationManager模块。

    ```cangjie
    import kit.NotificationKit.*
    import kit.BasicServicesKit.*
    import kit.PerformanceAnalysisKit.*
    import kit.AbilityKit.*

    let TAG: String = '[PublishOperation]'
    let DOMAIN_NUMBER: UInt32 = 0xFF00
    // globalcontext需要在main_ability.cj中的func onCreate中赋值：globalcontext = this.context
    var globalAbilityContext: Option<UIAbilityContext> = Option<UIAbilityContext>.None
    ```

2. 请求通知授权。

    可通过requestEnableNotification的错误码判断用户是否授权。若返回的错误码为1600004，即为拒绝授权。

    ```cangjie
    if (!isNotificationEnabled()) {
        try {
            requestEnableNotification(globalAbilityContext.getOrThrow())
        } catch (e: BusinessException) {
            if (e.code == 1600004) {
                AppLog.error('requestEnableNotification refused, code is ${e.code}, message is ${e.message}')
            } else {
                AppLog.error('requestEnableNotification failed, code is ${e.code}, message is ${e.message}')
            }
        }
    }
    ```
