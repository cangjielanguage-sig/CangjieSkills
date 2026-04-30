### func off(DeviceStatusType, CallbackObject)

```cangjie
public func off(`type`: DeviceStatusType, callback: CallbackObject): Unit
```

**功能：** 解注册回调函数。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[DeviceStatusType](#enum-devicestatustype)|是|-|解注册回调函数类型。|
|callback|[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|是|-|callback的类型需要和type保持一致，并且是已经注册的回调函数。type和对应的callback类型详见[on](#func-ondevicestatustype-callbackobject)函数参数说明。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied. The application does not have the permission required to call the API.|
  |401|Parameter error. Possible causes: 1. Incorrect parameter type; 2. Parameter verification failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.DistributedServiceKit.*

// 所需要的依赖项
class Callback1ArgumentImpl<A> <: Callback1Argument<A> {
    Callback1ArgumentImpl(let callback: (A) -> Unit) {}

    public func invoke(arg: A): Unit {
        callback(arg)
    }
}

let deviceNameChangeCallback = Callback1ArgumentImpl<String> {
    deviceName: String =>
        AppLog.info("in callback, current thread id: ${Thread.currentThread.id}")
        AppLog.info("remote device name changed, the cur name is ${deviceName}")
}

try {
    let dm = createDeviceManager("com.example.myapplication")
    dm.on(DEVICE_NAME_CHANGE, deviceNameChangeCallback)
    sleep(Duration.second * 10)         // 等待触发回调
    dm.off(DEVICE_NAME_CHANGE, deviceNameChangeCallback)
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```