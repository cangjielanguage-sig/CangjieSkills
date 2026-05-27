# ohos.bluetooth.socket（蓝牙socket模块）

socket模块提供了操作和管理蓝牙socket的方法。

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

## func getDeviceId(Int32)

```cangjie
public func getDeviceId(clientSocket: Int32): String
```

**功能：** 通过clientSocket获取对端设备地址。服务端、客户端均可调用，传入非法clientSocket无法获取。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|clientSocket|Int32|是|-|客户端Socket的id。|

**返回值：**

|类型|说明|
|:----|:----|
|String|返回对端设备地址，例如："XX:XX:XX:XX:XX:XX"。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

try {
    let devices = getPairedDevices()
    let deviceId = devices[0]
    let sppOption: SppOptions = SppOptions('00001101-0000-1000-8000-00805f9b34fb', true, SPPRFCOMM)
    sppConnect(deviceId, sppOption){
        error, fd =>
            if (let Some(e) <- error) {
                throw e
            }
            if (let Some(clintSocket) <- fd) {
                let device = getDeviceId(clintSocket)
            }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

## func off(BluetoothSocketCallbackType, Int32, ?CallbackObject)

```cangjie
public func off(`type`: BluetoothSocketCallbackType, clientSocket: Int32, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅spp读请求事件，入参clientSocket由sppAccept或sppConnect接口获取。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[BluetoothSocketCallbackType](#enum-bluetoothsocketcallbacktype)|是|-|回调事件类型。|
|clientSocket|Int32|是|-|客户端Socket的id。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None|表示取消订阅回调事件。不填该参数则取消订阅该\`type`对应的所有回调。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

class Cb <: Callback1Argument<Array<UInt8>> {
    public func invoke(data: Array<UInt8>): Unit {
        AppLog.info("spp data ${String.fromUtf8(data)}")
    }
}

try {
    let devices = getPairedDevices()
    let deviceId = devices[0]
    let sppOption: SppOptions = SppOptions('00001101-0000-1000-8000-00805f9b34fb', true, SPPRFCOMM)
    sppConnect(deviceId, sppOption){
        error, fd =>
            if (let Some(e) <- error) {
                throw e
            }
            if (let Some(clintSocket) <- fd) {
                let callback = Cb()
                on(SppRead, clintSocket, callback)
                off(SppRead, clintSocket, callback)
            }
    }
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```