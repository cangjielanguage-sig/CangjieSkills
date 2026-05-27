## 场景介绍

使用WebSocket建立服务器与客户端的双向连接，需要先通过createWebSocket()方法创建WebSocket对象，然后通过connect()方法连接到服务器。当连接成功后，客户端会收到open事件的回调，之后客户端就可以通过send()方法与服务器进行通信。当服务器发信息给客户端时，客户端会收到message事件的回调。当客户端不要此连接时，可以通过调用close()方法主动断开连接，之后客户端会收到close事件的回调。

若在上述任一过程中发生错误，客户端会收到error事件的回调。

WebSocket支持心跳检测机制，在客户端和服务端建立WebSocket连接之后，每间隔一段时间会客户端会发送Ping帧给服务器，服务器收到后应立即回复Pong帧。

## 接口说明

WebSocket连接功能主要由[webSocket模块](../../API_Reference/source_zh_cn/apis/NetworkKit/cj-apis-net-webSocket.md)提供。使用该功能需要申请ohos.permission.INTERNET权限。具体接口说明如下表。

| 接口名            | 描述                                      |
| ----------------- | ----------------------------------------- |
| createWebSocket() | 创建一个WebSocket连接。                   |
| connect()         | 根据URL地址，建立一个WebSocket连接。      |
| send()            | 通过WebSocket连接发送数据。               |
| close()           | 关闭WebSocket连接。                       |
| on()              | 订阅WebSocket的打开事件。                 |
| off()             | 取消订阅WebSocket的打开事件。             |
| on()              | 订阅WebSocket的接收到服务器消息事件。     |
| off()             | 取消订阅WebSocket的接收到服务器消息事件。 |
| on()              | 订阅WebSocket的关闭事件。                 |
| off()             | 取消订阅WebSocket的关闭事件。             |
| on()              | 订阅WebSocket的Error事件。                |
| off()             | 取消订阅WebSocket的Error事件。            |