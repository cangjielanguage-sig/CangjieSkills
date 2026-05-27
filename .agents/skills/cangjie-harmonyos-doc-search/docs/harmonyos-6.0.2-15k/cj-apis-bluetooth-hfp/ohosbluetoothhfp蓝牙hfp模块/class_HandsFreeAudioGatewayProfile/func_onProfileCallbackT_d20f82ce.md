### func on(ProfileCallbackType, Callback1Argument\<StateChangeParam>)

```cangjie
public func on(`type`: ProfileCallbackType, callback: Callback1Argument<StateChangeParam>): Unit
```

**功能：** 订阅连接状态变化事件。使用Callback异步回调。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[ProfileCallbackType](cj-apis-bluetooth-baseProfile.md#enum-profilecallbacktype)|是|填写CONNECTIONSTATECHANGE，表示连接状态变化事件类型。 |
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[StateChangeParam](cj-apis-bluetooth-baseProfile.md#struct-statechangeparam)>|是|表示回调函数的入参。|

**异常：**

- BusinessException：对应错误码如下表，详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |801|Capability not supported.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.ConnectivityKit.*
import ohos.hilog.Hilog

// 此处定义所需要的依赖项等
class StateChangeCallback <: Callback1Argument<StateChangeParam> {
    public func invoke(arg: StateChangeParam): Unit {
        let connectionState = arg.state.toString()
        Hilog.info(0, "Bluetooth", "profile connection state has change to ${connectionState}")
    }
}

let changeCallBack = StateChangeCallback()
let hdfProfile = createHfpAgProfile()
try {
    hdfProfile.on(ProfileCallbackType.CONNECTION_STATE_CHANGE, changeCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```