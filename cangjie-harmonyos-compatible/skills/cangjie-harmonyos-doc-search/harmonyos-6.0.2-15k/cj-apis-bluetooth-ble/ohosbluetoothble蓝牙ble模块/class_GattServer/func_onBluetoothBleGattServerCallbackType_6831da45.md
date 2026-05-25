### func on(BluetoothBleGattServerCallbackType, Callback1Argument\<DescriptorWriteRequest>)

```cangjie
public func on(`type`: BluetoothBleGattServerCallbackType, callback: Callback1Argument<DescriptorWriteRequest>): Unit
```

**功能：** server端订阅MTU状态变化事件。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[BluetoothBleGattServerCallbackType](#enum-bluetoothblegattservercallbacktype)|是|填写DESCRIPTOR_WRITE，表示描述符写请求事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[DescriptorWriteRequest](#class-descriptorwriterequest)>|是|返回MTU字节数的值，通过注册回调函数获取。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

// 此处代码可添加在依赖项定义中
let gattServer = createGattServer()

class DescriptorWriteCallback <: Callback1Argument<DescriptorWriteRequest> {
    public func invoke(desReq: DescriptorWriteRequest): Unit {
        let deviceId: String = desReq.deviceId
        let transId: Int32 = desReq.transId
        let offset: Int32 = desReq.offset
        Hilog.info(0, "Bluetooth", "receive descriptorWrite")
        Hilog.info(0, "Bluetooth", "receive descriptorWrite: needRsp=" + desReq.needRsp.toString())
        if (!desReq.needRsp) {
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
            gattServer.sendResponse(serverResponse)
        } catch (e: BusinessException) {
            AppLog.error("gattServer send response fail because ${e}")
        }
    }
}

let descriptorWriteCallback = DescriptorWriteCallback()
try {
    gattServer.on(DESCRIPTOR_WRITE, descriptorWriteCallback)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```