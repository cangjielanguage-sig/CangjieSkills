# ohos.bluetooth.ble（蓝牙ble模块）

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

本模块提供了基于低功耗蓝牙（Bluetooth Low Energy，BLE）技术的蓝牙能力，支持发起BLE扫描、发送BLE广播报文、以及基于通用属性协议（Generic Attribute Profile，GATT）的连接和传输数据。

## 导入模块

```cangjie
import kit.ConnectivityKit.*
```

## 权限列表

ohos.permission.ACCESS_BLUETOOTH

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](./../AbilityKit/cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。
- 请将示例代码中的XX:XX:XX:XX:XX:XX或其他地址替换为您的真实地址

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func createGattClientDevice(String)

```cangjie
public func createGattClientDevice(deviceId: String): GattClientDevice
```

**功能：** 创建[GattClientDevice](#class-gattclientdevice)实例，表示GATT连接中的client端。

- 通过该实例可以操作client端行为，如调用[connect](#func-connect)向对端设备发起连接，调用[getServices](#func-getrssivalueasynccallbackint32)获取对端设备支持的所有服务能力。
- 创建该实例所需要的设备地址表示server端设备。可以通过[startBleScanning](#func-startblescanningarrayscanfilter-scanoptions)接口获取server端设备地址，且需保证server端设备的BLE广播是可连接的。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceId|String|是|-|对端设备地址，&nbsp;例如："XX:XX:XX:XX:XX:XX"。|

**返回值：**

|类型|说明|
|:----|:----|
|[GattClientDevice](#class-gattclientdevice)|client端类，使用client端方法之前需要创建该类的实例进行操作。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 801 | Capability not supported. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.business_exception.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog

try {
    let device: GattClientDevice = createGattClientDevice("XX:XX:XX:XX:XX:XX")  // 请替换为您的设备地址
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```

## func createGattServer()

```cangjie
public func createGattServer(): GattServer
```

**功能：** 创建[GattServer](#class-gattserver)实例，表示GATT连接中的server端。

- 通过该实例可以操作server端的行为，如添加服务[addService](#func-addservicegattservice)、通知特征值变化[notifyCharacteristicChanged](#func-notifycharacteristicchangedstring-notifycharacteristic)等。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[GattServer](#class-gattserver)|返回一个Gatt服务的实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog
import ohos.business_exception.BusinessException

try {
    let gattServer: GattServer = createGattServer()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```