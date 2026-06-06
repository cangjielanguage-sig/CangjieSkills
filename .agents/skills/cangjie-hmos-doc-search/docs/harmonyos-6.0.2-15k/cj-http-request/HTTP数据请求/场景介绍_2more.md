## 场景介绍

应用通过HTTP发起一个数据请求，支持常见的GET、POST、OPTIONS、HEAD、PUT、DELETE、TRACE、CONNECT方法。

## 接口说明

HTTP数据请求功能主要由http模块提供。

使用该功能需要申请ohos.permission.INTERNET权限。

权限申请请参见[声明权限](../security/AccessToken/cj-declare-permissions.md)。

涉及的接口如下表，具体的接口说明请参见[API文档](../../API_Reference/source_zh_cn/apis/NetworkKit/cj-apis-net-http.md)。

| 接口名                   | 描述                                            |
| ------------------------ | ----------------------------------------------- |
| createHttp()             | 创建一个 HTTP 请求。                              |
| request()                | 根据URL地址，发起HTTP网络请求。                 |
| requestInStream()        | 根据URL地址，发起HTTP网络请求并返回流式响应。   |
| destroy()                | 中断请求任务。                                  |
| onHeadersReceive()       | 订阅HTTP Response Header 事件。                 |
| offHeadersReceive()      | 取消订阅HTTP Response Header 事件。             |
| onceHeadersReceive()     | 订阅HTTP Response Header 事件，但是只触发一次。 |
| onDataReceive()          | 订阅HTTP流式响应数据接收事件。                  |
| offDataReceive()         | 取消订阅HTTP流式响应数据接收事件。              |
| onDataEnd()              | 订阅HTTP流式响应数据接收完毕事件。              |
| offDataEnd()             | 取消订阅HTTP流式响应数据接收完毕事件。          |
| onDataReceiveProgress()  | 订阅HTTP流式响应数据接收进度事件。              |
| offDataReceiveProgress() | 取消订阅HTTP流式响应数据接收进度事件。          |
| onDataSendProgress()     | 订阅HTTP网络请求数据发送进度事件。              |
| offDataSendProgress()    | 取消订阅HTTP网络请求数据发送进度事件。          |