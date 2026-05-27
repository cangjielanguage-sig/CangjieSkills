### func off(ProfileCallbackType, CallbackObject)

```cangjie
public func off(`type`: ProfileCallbackType, callback: CallbackObject): Unit
```

**功能：** 取消订阅连接状态变化事件。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|\`type`|[ProfileCallbackType](cj-apis-bluetooth-baseProfile.md#enum-profilecallbacktype)|是|回调事件类型。|
|callback|[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|是|回调事件。|

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
let hidProfile = createHidHostProfile()
try {
    hidProfile.on(ProfileCallbackType.CONNECTION_STATE_CHANGE, changeCallBack)
    hidProfile.off(ProfileCallbackType.CONNECTION_STATE_CHANGE, changeCallBack)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func off(ProfileCallbackType)

```cangjie
public func off(`type`: ProfileCallbackType): Unit
```

**功能：** 取消订阅连接状态变化事件。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[ProfileCallbackType](cj-apis-bluetooth-baseProfile.md#enum-profilecallbacktype)|是|回调事件类型。|

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
let hidProfile = createHidHostProfile()
try {
    hidProfile.on(ProfileCallbackType.CONNECTION_STATE_CHANGE, changeCallBack)
    hidProfile.off(ProfileCallbackType.CONNECTION_STATE_CHANGE)
} catch (e: BusinessException) {
    Hilog.info(0, "Bluetooth", "errCode: ${e.code}, errMessage: ${e.message}")
}
```