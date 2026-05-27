# 发布文本类型通知

文本类型通知主要应用于发送短信息、提示信息等，支持普通文本类型和多行文本类型。

**表1** 基础类型通知中的内容分类

| 类型                             | 描述          |
| ------------------------------- | ------------- |
| NOTIFICATION_CONTENT_BASIC_TEXT | 普通文本类型。 |
| NOTIFICATION_CONTENT_MULTILINE  | 多行文本类型。 |

## 接口说明

通知发布接口说明详见下表，通知发布的详情可通过入参[NotificationRequest](../../API_Reference/source_zh_cn/apis/NotificationKit/cj-apis-notification_manager.md#class-notificationrequest)来进行指定，可以包括通知内容、通知ID、通知的通道类型和通知发布时间等信息。

| **接口名** | **描述** |
| -------- | -------- |
| publish(request: NotificationRequest): Unit | 发布通知。                 |

## 开发步骤

1. 导入模块。

    ```cangjie
    import kit.NotificationKit.*
    import kit.BasicServicesKit.*
    import kit.PerformanceAnalysisKit.*

    let TAG: String = '[PublishOperation]'
    let DOMAIN_NUMBER: UInt32 = 0xFF00
    ```

2. 构造NotificationRequest对象，并发布通知。
   - 普通文本类型通知由标题、文本内容和附加信息三个字段组成，其中标题和文本内容是必填字段，大小均需要小于200字节，超出部分会被截断。

    ```cangjie
    let notificationRequest = NotificationRequest(
        NotificationContent(
            ContentType.NOTIFICATION_CONTENT_BASIC_TEXT,
            normal: NotificationBasicContent('test_title', 'test_text', additionalText: 'test_additionalText')),
        id: 1)
    publish(notificationRequest)
    ```

   - 多行文本类型通知继承了普通文本类型的字段，同时新增了多行文本内容、内容概要和通知展开时的标题，其字段均小于200字节，超出部分会被截断。通知默认显示与普通文本相同，展开后，标题显示为展开后标题内容，多行文本内容多行显示。

    ```cangjie
    let notificationRequest = NotificationRequest(
        NotificationContent(
            ContentType.NOTIFICATION_CONTENT_MULTILINE,
            multiLine: NotificationMultiLineContent('test_title', 'test_text', None, 'test_briefText', 'test_longTitle',
                ['line_01', 'line_02', 'line_03', 'line_04'])),
        id: 3)
    // 发布通知
    publish(notificationRequest)
    ```
