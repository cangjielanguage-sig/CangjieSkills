## func off(BluetoothConnectionCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: BluetoothConnectionCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅蓝牙设备发现上报事件。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[BluetoothConnectionCallbackType](#enum-bluetoothconnectioncallbacktype)|是|-|填写`BATTERY_CHANGE`，表示蓝牙远端设备的电池信息变更事件。填写`BLUETOOTH_DEVICE_FIND`，表示蓝牙设备发现事件。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 表示取消订阅蓝牙设备发现事件上报。不填该参数则取消订阅该type对应的所有回调。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |801|Capability not supported.|
  |2900099|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.*

// 此处代码可添加在依赖项定义中
class FindDevicesCallback <: Callback1Argument<Array<String>> {
    public func invoke(devices: Array<String>): Unit {
        for (device in devices) {
            Hilog.info(0, "Bluetooth", "find device ${device}")
        }
    }
}

let onReceiveEvent = FindDevicesCallback()
try {
    on(BLUETOOTH_DEVICE_FIND, onReceiveEvent)
    off(BLUETOOTH_DEVICE_FIND, callback: onReceiveEvent)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

## func on(BluetoothConnectionCallbackType, Callback1Argument\<BatteryInfo>)

```cangjie
public func on(`type`: BluetoothConnectionCallbackType, callback: Callback1Argument<BatteryInfo>): Unit
```

**功能：** 订阅蓝牙远程设备的电量信息变更事件。使用Callback异步回调。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[BluetoothConnectionCallbackType](#enum-bluetoothconnectioncallbacktype)|是|填写`BATTERY_CHANGE`，表示蓝牙远端设备的电池信息变更事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BatteryInfo](#class-batteryinfo)>|是|表示回调函数的入参，返回电量信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :------------|
  |201|Permission denied.|
  |2900099|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.*

// 此处代码可添加在依赖项定义中
class BatteryCallback <: Callback1Argument<BatteryInfo> {
    public func invoke(data: BatteryInfo): Unit {
        Hilog.info(0, "Bluetooth", "remote device battery has change")
    }
}

let onPairStatusChanged = BatteryCallback()
try {
    on(BATTERY_CHANGE, onPairStatusChanged)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```