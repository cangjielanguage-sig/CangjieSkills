## func on(BluetoothBleCallbackType, Callback1Argument\<AdvertisingStateChangeInfo>)

```cangjie
public func on(`type`: BluetoothBleCallbackType, callback: Callback1Argument<AdvertisingStateChangeInfo>): Unit
```

**功能：** 订阅BLE广播状态。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[BluetoothBleCallbackType](#enum-bluetoothblecallbacktype)|是|填写 ADVERTISING_STATE_CHANGE，表示广播状态事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AdvertisingStateChangeInfo](#class-advertisingstatechangeinfo)>|是|表示回调函数的入参，广播状态。回调函数由用户创建通过该接口注册。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[蓝牙服务子系统错误码](../../errorcodes/cj-errorcode-bluetooth_manager.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.|
  |801|Capability not supported.|
  |2900099|Operation failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

// 此处代码可添加在依赖项定义中
class AdvertisingStateChange <: Callback1Argument<AdvertisingStateChangeInfo> {
    public func invoke(info: AdvertisingStateChangeInfo): Unit {
        Hilog.info(0, "Bluetooth", "the advertising state is ${info.state}")
    }
}

let advertisingStateChange = AdvertisingStateChange()
try {
    on(ADVERTISING_STATE_CHANGE, advertisingStateChange)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```