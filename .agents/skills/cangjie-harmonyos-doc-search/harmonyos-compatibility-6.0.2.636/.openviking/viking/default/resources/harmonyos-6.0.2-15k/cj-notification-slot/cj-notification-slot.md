# 管理通知渠道

系统支持多种通知渠道，不同通知渠道对应的通知提醒方式不同，可以根据应用的实际场景选择适合的通知渠道，并对通知渠道进行管理（支持创建、查询、删除等操作）。

## 通知渠道类型说明

不同类型的通知渠道对应的通知提醒方式不同，详见下表。其中，Y代表支持，N代表不支持。

| SlotType             | 取值   | 分类     | 通知中心 | 横幅 | 锁屏 | 铃声/振动 | 状态栏图标 | 自动亮屏 |
| -------------------- | ------ | --------| ------- |------|------|----------|-----------|---------|
| UNKNOWN_TYPE         | 0      | 未知类型 | Y | N | N | N | N | N |
| SOCIAL_COMMUNICATION | 1      | 社交通信 | Y | Y | Y | Y | Y | Y |
| SERVICE_INFORMATION  | 2      | 服务提醒 | Y | Y | Y | Y | Y | Y |
| CONTENT_INFORMATION  | 3      | 内容资讯 | Y | N | N | N | N | N |
| CUSTOMER_SERVICE     | 5      | 客服消息 | Y | N | N | Y | Y | N |
| OTHER_TYPES          | 0xFFFF | 其他     | Y | N | N | N | N | N |

## 接口说明

通知渠道的主要接口如下。其他接口的详细介绍请参见[API参考](../../API_Reference/source_zh_cn/apis/NotificationKit/cj-apis-notification_manager.md)。

| **接口名** | **描述** |
| ---------- | -------- |
| addSlot(type: SlotType): Unit                 | 创建指定类型的通知渠道。           |
| getSlot(slotType: SlotType): NotificationSlot | 获取一个指定类型的通知渠道。       |
| removeSlot(slotType: SlotType): Unit          | 删除此应用程序指定类型的通知渠道。  |

除了可以使用`addslot()`创建通知渠道外，还可以在发布通知的[NotificationRequest](../../API_Reference/source_zh_cn/apis/NotificationKit/cj-apis-notification_manager.md#class-notificationrequest)中携带notificationSlotType字段，如果对应渠道不存在，会自动创建。

## 开发步骤

1. 导入notificationManager模块。

    ```cangjie
    import kit.NotificationKit.*
    import kit.BasicServicesKit.*
    import kit.PerformanceAnalysisKit.*

    let TAG: String = '[PublishOperation]'
    let DOMAIN_NUMBER: UInt32 = 0xFF00
    ```

2. 创建指定类型的通知渠道。

    ```cangjie
    // addslot回调
    addSlot(SlotType.SOCIAL_COMMUNICATION)
    ```

3. 查询指定类型的通知渠道。

    获取对应渠道是否创建以及该渠道支持的通知提醒方式，比如是否有声音提示，是否有震动，锁屏是否可见等。

    ```cangjie
    // getSlot回调
    let data = getSlot(SlotType.SOCIAL_COMMUNICATION)
    AppLog.info('slot enable status is ${data.enabled}')
    AppLog.info('vibrationEnabled status is ${data.vibrationEnabled}')
    AppLog.info('lightEnabled status is ${data.lightEnabled}')
    let level = match (data.level) {
        case SlotLevel.LEVEL_LOW => 'LEVEL_LOW'
        case SlotLevel.LEVEL_MIN => 'LEVEL_MIN'
        case SlotLevel.LEVEL_HIGH => 'LEVEL_HIGH'
        case SlotLevel.LEVEL_NONE => 'LEVEL_NONE'
        case SlotLevel.LEVEL_DEFAULT => 'LEVEL_DEFAULT'
    }
    AppLog.info('slot level is ${level}')
    ```

4. 删除指定类型的通知渠道。

    ```cangjie
    // removeSlot回调
    removeSlot(SlotType.SOCIAL_COMMUNICATION)
    ```
