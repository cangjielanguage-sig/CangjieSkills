# 管理通知角标

针对未读的通知，系统提供了角标设置接口，将未读通知个数显示在桌面图标的右上角角标上。

通知增加时，角标上显示的未读通知个数需要增加。

通知被查看后，角标上显示的未读通知个数需要减少，没有未读通知时，不显示角标。

## 接口说明

当角标设定个数取值0时，表示清除角标。取值大于99时，通知角标将显示99+。

- 增加角标数，支持如下两种方法：

    - 发布通知时，在[NotificationRequest](../../API_Reference/source_zh_cn/apis/NotificationKit/cj-apis-notification_manager.md#class-notificationrequest)的badgeNumber字段里携带，桌面收到通知后，在原角标数上累加、呈现。

    - 调用接口[setBadgeNumber()](../../API_Reference/source_zh_cn/apis/NotificationKit/cj-apis-notification_manager.md#func-setbadgenumberint32)设置，桌面按设置的角标数呈现。

- 减少角标数，目前仅支持通过[setBadgeNumber()](../../API_Reference/source_zh_cn/apis/NotificationKit/cj-apis-notification_manager.md#func-setbadgenumberint32)设置。

  | **接口名** | **描述** |
  | -------- | -------- |
  | setBadgeNumber(badgeNumber: Int32): Unit | 设置角标个数。 |

## 开发步骤

1. 导入NotificationManager模块。

    ```cangjie
    import kit.NotificationKit.*
    import kit.BasicServicesKit.*
    import kit.PerformanceAnalysisKit.*

    let TAG: String = '[PublishOperation]'
    let DOMAIN_NUMBER: UInt32 = 0xFF00
    ```

2. 增加角标个数。

    发布通知在[NotificationRequest](../../API_Reference/source_zh_cn/apis/NotificationKit/cj-apis-notification_manager.md#class-notificationrequest)的badgeNumber字段里携带，可参考[通知发布](./cj-text-notification.md)章节。

    示例为调用setBadgeNumber接口增加角标，在发布完新的通知后，调用该接口。

    ```cangjie
    let badgeNumber: Int32 = 9
    setBadgeNumber(badgeNumber)
    ```

3. 减少角标个数。

    一条通知被查看后，应用需要调用接口设置剩余未读通知个数，桌面刷新角标。

    ```cangjie
    let badgeNumber: Int32 = 8
    setBadgeNumber(badgeNumber)
    ```
