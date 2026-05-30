## func off(BluetoothAccessCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: BluetoothAccessCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅蓝牙设备开关状态事件。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[BluetoothAccessCallbackType](#enum-bluetoothaccesscallbacktype)|是|-|表示蓝牙状态改变事件。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 表示取消订阅蓝牙状态改变事件上报。缺省该参数则取消订阅该type对应的所有回调。|

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

// 此处定义所需要的依赖项等
class StateChangeback <: Callback1Argument<BluetoothState> {
    public func invoke(arg: BluetoothState): Unit {
        Hilog.info(0, "Bluetooth", "BluetoothState has change")
    }
}

let changeCallBack = StateChangeback()
try {
    on(STATE_CHANGE, changeCallBack)
    off(STATE_CHANGE, callback: changeCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

## func on(BluetoothAccessCallbackType, Callback1Argument\<BluetoothState>)

```cangjie
public func on(`type`: BluetoothAccessCallbackType, callback: Callback1Argument<BluetoothState>): Unit
```

**功能：** 订阅蓝牙设备开关状态事件。使用Callback异步回调。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[BluetoothAccessCallbackType](#enum-bluetoothaccesscallbacktype)|是|表示蓝牙状态改变事件。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BluetoothState](#enum-bluetoothstate)>|是|表示回调函数的入参，蓝牙状态。回调函数由用户创建通过该接口注册。|

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

// 此处定义所需要的依赖项等
class StateChangeback <: Callback1Argument<BluetoothState> {
    public func invoke(arg: BluetoothState): Unit {
        Hilog.info(0, "Bluetooth", "BluetoothState has change")
        AppLog.info("BluetoothState has change")
    }
}

let changeCallBack = StateChangeback()
try {
    on(STATE_CHANGE, changeCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```