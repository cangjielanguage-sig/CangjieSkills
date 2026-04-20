# 网络连接管理

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

## 简介

网络连接管理提供管理网络一些基础能力，包括 WiFi、蜂窝、以太网等多网络连接优先级管理、网络质量评估、订阅默认或指定网络连接状态变化、查询网络连接信息、DNS解析等功能。

## 基本概念

- 网络生产者：数据网络的提供方。比如WiFi、蜂窝、Ethernet等。
- 网络消费者：数据网络的使用方。比如应用或系统服务。
- 网络探测：检测网络有效性，避免将网络从可用网络切换到不可用网络。内容包括绑定网络探测、DNS探测、HTTP探测及HTTPS探测。
- 网络优选：处理多网络共存时选择最优网络。在网络状态、网络信息及评分发生变化时被触发。

## 约束

开发语言：Cangjie

## 场景介绍

网络连接管理的典型场景如下所示。

- 接收指定网络的状态变化通知。
- 获取所有注册的网络。
- 根据数据网络查询网络的连接信息。
- 使用对应网络解析域名，获取所有IP。

具体开发方式介绍如下。

## 接口说明

完整的Cangjie API说明以及实例代码请参见[网络连接管理](../reference/NetworkKit/cj-apis-net-connection.md)。

| 接口名 | 描述 |
| ------------------------- | --------------------------- |
| getDefaultNet(): NetHandle | 获取一个含有默认网络的netId的NetHandle对象。 |
| getAppNet(): NetHandle  | 获取一个App绑定的包含了网络netId的NetHandle对象。 |
| setAppNet(netHandle: NetHandle): Unit | 绑定App到指定网络，绑定后的App只能通过指定网络访问外网。 |
| getDefaultNet(): NetHandle | 使用同步方法获取默认激活的数据网络。可以使用getNetCapabilities去获取网络的类型、拥有的能力等信息 |
| hasDefaultNet(): Bool | 检查默认数据网络是否被激活。  |
| getAllNets(): Array\<NetHandle> | 获取所处于连接状态的网络的NetHandle对象列表。 |
| getConnectionProperties(netHandle: NetHandle): ConnectionProperties  | 查询netHandle对应的网络的连接信息。  |
| getNetCapabilities(netHandle: NetHandle): NetCapabilities | 获取netHandle对应的网络的能力信息。 |
| isDefaultNetMetered(): Bool | 检查默认数据网络是否被激活。 |
| reportNetConnected(netHandle: NetHandle): Unit | 向网络管理报告网络处于可用状态，调用此接口说明应用程序认为网络的可用性(ohos.net.connection.NetCap.NET_CAPABILITY_VAILDATED)与网络管理不一致。 |
| reportNetDisconnected(netHandle: NetHandle): Unit | 向网络管理报告网络处于不可用状态，调用此接口说明应用程序认为网络的可用性(ohos.net.connection.NetCap.NET_CAPABILITY_VAILDATED)与网络管理不一致。 |
| getAddressesByName(host: String): Array\<NetAddress> | 使用对应网络解析域名，获取所有IP。 |
| createNetConnection(netSpecifier!: ?NetSpecifier = None, timeout!: UInt32 = 0): NetConnection | 返回一个NetConnection对象，netSpecifier指定关注的网络的各项特征。timeout是超时时间(单位：毫秒)，netSpecifier是timeout的必要条件，两者都没有则表示关注默认网络。 |
| getAddressByName(host: String): NetAddress  | 使用对应网络解析域名，获取一个IP，调用callback。 |
| on(event: NetConnectionEvent, callback: Callback1Argument\<NetHandle>): Unit | 订阅网络可用事件或网络丢失事件。 |
| on(event: NetConnectionEvent, callback: Callback1Argument\<NetCapabilityInfo>): Unit | 订阅网络能力变化事件。 |
| on(event: NetConnectionEvent, callback: Callback1Argument\<NetConnectionPropertyInfo>): Unit  | 订阅网络连接信息变化事件。 |
| on(event: NetConnectionEvent, callback: Callback1Argument\<NetBlockStatusInfo>): Unit         | 订阅网络阻塞状态事件，使用callback方式作为异步方法。 |
| on(event: NetConnectionEvent, callback: Callback0Argument): Unit  | 订阅网络不可用事件。 |
| register(): Unit | 订阅指定网络状态变化的通知。 |
| unregister(): Unit | 取消订阅默认网络状态变化的通知。 |