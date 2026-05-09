# 查找设备

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

## 简介

本指南主要提供了BLE扫描和BLE广播相关操作的开发指导。可以实现发现周边BLE设备和其他设备发现本机设备的场景。

## 开发步骤

### 申请蓝牙权限

需要申请权限ohos.permission.ACCESS_BLUETOOTH。如何配置和申请权限，请参考[声明权限](../../security/AccessToken/cj-declare-permissions.md)和[向用户申请授权](../../security/AccessToken/cj-request-user-authorization.md)。

## 场景介绍

主要场景有：

- 开启、关闭广播
- 开启、关闭扫描

## 接口说明

完整的仓颉 API 说明以及实例代码请参见：[BLE 接口](../../reference/ConnectivityKit/cj-apis-bluetooth-ble.md)。

具体接口说明如下表。

| 接口名 | 功能描述 |
| ---------------------------------- | -----------------------------------------------|
| startBleScanning() | 发起BLE扫描流程。 |
| stopBleScanning() | 停止BLE扫描流程。 |
| startAdvertising() | 开始发送BLE广播。 |
| stopAdvertising() | 停止发送BLE广播。 |
| on(eventType: BluetoothBleCallbackType) | 订阅BLE广播状态。 |
| off(eventType: BluetoothBleCallbackType) | 取消订阅BLE广播状态。 |
| on(eventType: BluetoothBleCallbackType) | 订阅BLE设备发现上报事件。 |
| off(eventType: BluetoothBleCallbackType) | 取消订阅BLE设备发现上报事件。  |