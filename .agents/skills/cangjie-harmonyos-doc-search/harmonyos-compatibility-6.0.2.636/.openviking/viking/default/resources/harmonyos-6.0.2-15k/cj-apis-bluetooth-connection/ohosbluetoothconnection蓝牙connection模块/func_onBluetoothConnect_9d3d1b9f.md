## func on(BluetoothConnectionCallbackType, Callback1Argument\<BondStateParam>)

```cangjie
public func on(`type`: BluetoothConnectionCallbackType, callback: Callback1Argument<BondStateParam>): Unit
```

**功能：** 订阅蓝牙配对状态改变事件。使用Callback异步回调。

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[BluetoothConnectionCallbackType](#enum-bluetoothconnectioncallbacktype)|是|填写`BOND_STATE_CHANGE`，表示蓝牙配对状态改变事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BondStateParam](#class-bondstateparam)>|是|表示回调函数的入参，配对的状态。回调函数由用户创建通过该接口注册。|

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
class BondStateChangeCallback <: Callback1Argument<BondStateParam> {
    public func invoke(state: BondStateParam): Unit {
        Hilog.info(0, "Bluetooth", "bond state has change")
    }
}

let onStateChange = BondStateChangeCallback()
try {
    on(BOND_STATE_CHANGE, onStateChange)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```