## func on(BluetoothSocketCallbackType, Int32, Callback1Argument\<Array\<Byte>>)

```cangjie
public func on(`type`: BluetoothSocketCallbackType, clientSocket: Int32, callback: Callback1Argument<Array<Byte>>): Unit
```

**功能：** 订阅spp读请求事件，入参clientSocket由sppAccept或sppConnect接口获取。使用Callback异步回调。

**系统能力：** SystemCapability.Communication.Bluetooth.Core。

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|`type`|[BluetoothSocketCallbackType](#enum-bluetoothsocketcallbacktype)|是|-|回调事件类型。|
|clientSocket|Int32|是|-|客户端socket的id。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<[Byte]>>|是|-|表示回调函数的入参，读取到的数据。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |801|Capability not supported.|
  |2901054|IO error.|
  |2900099|Operation failed.|

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