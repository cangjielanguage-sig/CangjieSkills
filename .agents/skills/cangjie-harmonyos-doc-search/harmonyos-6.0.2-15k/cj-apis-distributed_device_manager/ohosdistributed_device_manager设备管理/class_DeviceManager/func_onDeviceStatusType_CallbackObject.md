### func on(DeviceStatusType, CallbackObject)

```cangjie
public func on(`type`: DeviceStatusType, callback: CallbackObject): Unit
```

**功能：** 注册回调函数。

**需要权限：** ohos.permission.DISTRIBUTED_DATASYNC

**系统能力：** SystemCapability.DistributedHardware.DeviceManager

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[DeviceStatusType](#enum-devicestatustype)|是|-|待注册的回调函数类型。|
|callback|[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|是|-|callback是需要注册的回调函数，需要和type的值匹配。具体如下：<br>DEVICE_STATE_CHANGE：Callback2Argument\<[DeviceStateChange](#enum-devicestatechange), [DeviceBasicInfo](#class-devicebasicinfo)>。当发生状态发生变化时回调。<br>DEVICE_NAME_CHANGE： Callback1Argument\<String>。当设备名称改变时通知应用程序。<br>DISCOVER_SUCCESS：Callback1Argument\<[DeviceBasicInfo](#class-devicebasicinfo)>。发现设备成功的回调监听。<br>DISCOVER_FAILURE：Callback1Argument\<Int32>。注册设备发现失败回调监听。|

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
} catch (e: BusinessException) {
    AppLog.error(e.toString())
}
```