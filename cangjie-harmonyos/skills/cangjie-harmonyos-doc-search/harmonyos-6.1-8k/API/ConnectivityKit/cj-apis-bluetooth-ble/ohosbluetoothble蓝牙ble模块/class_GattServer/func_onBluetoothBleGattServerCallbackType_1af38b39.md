### func on(BluetoothBleGattServerCallbackType, Callback1Argument\<CharacteristicWriteRequest>)

```cangjie
public func on(eventType: BluetoothBleGattServerCallbackType, callback: Callback1Argument<CharacteristicWriteRequest>): Unit
```

**功能：** server端订阅client的特征值写请求事件，server端收到该事件后需要根据[CharacteristicWriteRequest](#class-characteristicwriterequest)中的needRsp决定是否调用[sendResponse](#func-sendresponseserverresponse)接口回复client。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[BluetoothBleGattServerCallbackType](#enum-bluetoothblegattservercallbacktype)|是|-|事件回调类型，支持的事件为CharacteristicWrite，表示特征值写请求事件。<br>当收到client端设备的写特征值请求时，触发该事件。|
|callback|[Callback1Argument](../arkinterop/cj-api-callback_invoke.md#class-callback1argumenta)\<[CharacteristicWriteRequest](#class-characteristicwriterequest)>|是|-|指定订阅的回调函数，会携带client端发送的写请求数据。|

**异常：**

- BusinessException：对应错误码如下表，详见[通用错误码](../cj-errorcode-universal.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 201 | Permission denied. |
  | 801 | Capability not supported. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.callback_invoke.*
import ohos.business_exception.*
import kit.ConnectivityKit.*
import kit.PerformanceAnalysisKit.Hilog

// 此处代码可添加在依赖项定义中
class CharacteristicWriteCallback <: Callback1Argument<CharacteristicWriteRequest> {
    let gattWriteServer: GattServer
    init(gattWriteServer: GattServer) {
    	this.gattWriteServer = gattWriteServer
    }
    public func invoke(err: ?BusinessException, charReq: CharacteristicWriteRequest): Unit {
        let deviceId: String = charReq.deviceId
        let transId: Int32 = charReq.transId
        let offset: Int32 = charReq.offset
        Hilog.info(0, "Bluetooth", "receive characteristicWrite")

        Hilog.info(0, "Bluetooth", "receive characteristicWrite: needRsp=" + charReq
            .needRsp
            .toString())
        if (!charReq.needRsp) {
            return
        }
        let rspBuffer = Array<Byte>()
        let serverResponse: ServerResponse = ServerResponse(
            deviceId,
            transId,
            0,
            offset,
            rspBuffer
        )
        try {
            gattWriteServer.sendResponse(serverResponse)
        } catch (e: BusinessException) {
            Hilog.info(0, "Bluetooth", "gattServer send response fail because ${e}")
        }
    }
}

try {
    let gattWriteServer = createGattServer()
    let characteristicWriteCallback = CharacteristicWriteCallback(gattWriteServer)
    gattWriteServer.on(BluetoothBleGattServerCallbackType.CharacteristicWrite, characteristicWriteCallback)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}", "")
}
```