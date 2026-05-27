### func isTorchModeSupported(TorchMode)

```cangjie
public func isTorchModeSupported(torchMode: TorchMode): Bool
```

**功能：** 检测是否支持设置的手电筒模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|torchMode|[TorchMode](#enum-torchmode)|是|-|手电筒模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示设备支持设置的手电筒模式。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let torchMode = cameraManager.getTorchMode()
AppLog.info(cameraManager.isTorchModeSupported(torchMode))
```

### func isTorchSupported()

```cangjie
public func isTorchSupported(): Bool
```

**功能：** 检测设备是否支持手电筒。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示设备支持手电筒。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
AppLog.info(cameraManager.isTorchSupported())
```

### func off(CameraCallbackType, Callback1Argument\<CameraStatusInfo>)

```cangjie
public func off(`type`: CameraCallbackType, callback: Callback1Argument<CameraStatusInfo>): Unit
```

**功能：** 相机设备状态注销回调，通过注销回调函数以取消获取相机的状态变化。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为cameraStatus。cameraManager对象获取成功后可监听。目前只支持对设备打开或者关闭会触发该事件并返回对应信息。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[CameraStatusInfo](#struct-camerastatusinfo)>|是|-|回调函数，取消对应callback。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*
import ohos.hilog.Hilog

// 此处代码可添加在依赖项定义中
class TestCallbackCameraStatus <: Callback1Argument<CameraStatusInfo> {
    public init() {}
    public open func invoke(res: CameraStatusInfo): Unit {
        Hilog.info(0, "Camera", "Call invoke CameraStatus. CameraDevice: ${res.camera.cameraId}, CameraStatus: ${res.status}")
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let testCallbackCameraStatus = TestCallbackCameraStatus()
cameraManager.off(CameraCallbackType.CameraStatus, testCallbackCameraStatus)
```