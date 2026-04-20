# ohos.bluetooth.ble（蓝牙ble模块）

ble模块提供了对蓝牙操作和管理的方法。

## 导入模块

```cangjie
import kit.ConnectivityKit.*
```

## 权限列表

ohos.permission.ACCESS_BLUETOOTH

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](../AbilityKit/cj-apis-ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../../cj-development-intro.md#仓颉示例代码说明)。

## func createGattClientDevice(String)

```cangjie
public func createGattClientDevice(deviceId: String): GattClientDevice
```

**功能：** 创建一个可使用的GattClientDevice实例。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|deviceId|String|是|对端设备地址，例如："XX:XX:XX:XX:XX:XX"。|

**返回值：**

|类型|说明|
|:----|:----|
|[GattClientDevice](#class-gattclientdevice)|client端类，使用client端方法之前需要创建该类的实例进行操作。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

try {
    let device: GattClientDevice  = createGattClientDevice("XX:XX:XX:XX:XX:XX")
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

## func createGattServer()

```cangjie
public func createGattServer(): GattServer
```

**功能：** 创建一个可使用的GattServer实例。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[GattServer](#class-gattserver)|返回一个Gatt服务的实例。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

let gattServer: GattServer = createGattServer()
```