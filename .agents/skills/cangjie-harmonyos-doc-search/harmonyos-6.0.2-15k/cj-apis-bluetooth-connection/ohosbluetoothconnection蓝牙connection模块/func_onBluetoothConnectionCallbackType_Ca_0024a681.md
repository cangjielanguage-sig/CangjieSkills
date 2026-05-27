## func on(BluetoothConnectionCallbackType, Callback1Argument\<Array\<String>>)

```cangjie
public func on(`type`: BluetoothConnectionCallbackType, callback: Callback1Argument<Array<String>>): Unit
```

**功能：** 订阅蓝牙设备发现上报事件。使用Callback异步回调。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[BluetoothConnectionCallbackType](#enum-bluetoothconnectioncallbacktype)|是|填写 `BLUETOOTH_DEVICE_FIND`，表示蓝牙设备发现事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<String>>|是|表示回调函数的入参，发现的设备集合。回调函数由用户创建通过该接口注册。基于信息安全考虑，此处获取的设备地址为随机MAC地址。配对成功后，该地址不会变更；已配对设备取消配对后重新扫描或蓝牙服务下电时，该随机地址会变更。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  | 错误码ID | 错误信息 |
  | :-------- | :---------------------------- |
  |201 | Permission denied. |
  |401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
  |801 | Capability not supported. |
  |2900099 | Operation failed.|

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
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```