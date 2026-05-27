## 简介

广播与扫描，主要提供了蓝牙设备的开启广播、关闭广播、开启扫描、关闭扫描方法，通过广播和扫描发现对端蓝牙设备，实现低功耗的通信。

## 场景介绍

主要场景有：

- 开启、关闭广播
- 开启、关闭扫描

## 接口说明

完整的仓颉 API 说明以及实例代码请参见：[BLE 接口](../../../API_Reference/source_zh_cn/apis/ConnectivityKit/cj-apis-bluetooth-ble.md)。

具体接口说明如下表。

| 接口名 | 功能描述 |
| ---------------------------------- | -----------------------------------------------|
| startBLEScan() | 发起BLE扫描流程。 |
| stopBLEScan() | 停止BLE扫描流程。 |
| startAdvertising() | 开始发送BLE广播。 |
| disableAdvertising() | 临时停止BLE广播。 |
| enableAdvertising() | 临时启动BLE广播。 |
| stopAdvertising() | 停止发送BLE广播。 |
| on(`type`: BluetoothBleCallbackType) | 订阅BLE广播状态。 |
| off(`type`: BluetoothBleCallbackType) | 取消订阅BLE广播状态。 |
| on(`type`: BluetoothBleCallbackType) | 订阅BLE设备发现上报事件。 |
| off(`type`: BluetoothBleCallbackType) | 取消订阅BLE设备发现上报事件。  |