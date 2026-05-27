## 简介

P2P模式，主要提供了WLAN设备的一种点对点连接技术，它可以在两台STA之间直接建立TCP/IP链接，并不需要AP的参与。

## 场景介绍

P2P模式的主要场景有：

- 创建/删除P2P群组
- 建立P2P连接

## 接口说明

完整的 Cangjie API 说明以及实例代码请参见：[P2P 接口](../../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-wifi_manager.md#class-wifip2pdevice)。

具体接口说明如下表。

| 接口名 | 功能描述 |
| -------- | -------- |
| createGroup() | 创建群组。 |
| removeGroup() | 删除群组。 |
| startDiscoverDevices()  | 开始发现设备。 |
| getP2pPeerDevices() | 获取P2P对端设备列表信息。 |
| p2pConnect() | 执行P2P连接。 |
| getP2pLinkedInfo() | 获取P2P连接信息。 |
| onP2pPersistentGroupChange() | 注册P2P永久组状态改变事件。 |
| offP2pPersistentGroupChange() | 取消注册P2P永久组状态改变事件。 |
| onP2pPeerDeviceChange() | 注册P2P对端设备状态改变事件。 |
| offP2pPeerDeviceChange() | 取消注册P2P对端设备状态改变事件。 |
| onP2pConnectionChange() | 注册P2P连接状态改变事件。 |
| offP2pConnectionChange() | 取消注册P2P连接状态改变事件。 |