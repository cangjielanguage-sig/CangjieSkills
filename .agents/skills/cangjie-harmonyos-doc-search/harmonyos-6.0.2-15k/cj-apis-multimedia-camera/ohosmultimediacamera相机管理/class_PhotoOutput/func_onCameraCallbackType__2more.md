### func on(CameraCallbackType, Callback1Argument\<Int32>)

```cangjie
public func on(`type`: CameraCallbackType, callback: Callback1Argument<Int32>): Unit
```

**功能：** 监听预估的拍照时间。

> **说明：**
>
> 不支持在on监听的回调方法里调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为estimatedCaptureDuration，photoOutput创建成功后可监听。拍照完全结束可触发该事件发生并返回相应信息。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Int32>|是|-|回调函数，用于获取预估的单次拍照底层出sensor采集帧时间，如果上报-1，代表没有预估时间。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.hilog.Hilog
import ohos.base.*

// 此处代码可添加在依赖项定义中
class TestCallbackEstimatedCaptureDuration <: Callback1Argument<Int32> {
    public init() {}
    public open func invoke(res: Int32): Unit {
        Hilog.info(0, "Camera", "Call invoke EstimatedCaptureDuration. time: ${res}")
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let device = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(device)[0]
let ability = cameraManager.getSupportedOutputCapability(device, mode)
let output = cameraManager.createPhotoOutput(ability.photoProfiles[0])
let testCallbackEstimatedCaptureDuration = TestCallbackEstimatedCaptureDuration()
output.on(CameraCallbackType.EstimatedCaptureDuration, testCallbackEstimatedCaptureDuration)
```

### func on(CameraCallbackType, Callback1Argument\<BusinessException>)

```cangjie
public func on(`type`: CameraCallbackType, callback: Callback1Argument<BusinessException>): Unit
```

**功能：** 监听拍照输出发生错误，通过注册回调函数获取结果。

> **说明：**
>
> 不支持在on监听的回调方法里调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为error，photoOutput创建成功后可监听。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)>|是|-|回调函数，用于获取错误信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.hilog.Hilog
import ohos.base.*

// 此处代码可添加在依赖项定义中
class TestCallbackError <: Callback1Argument<BusinessException> {
    public init() {}
    public open func invoke(res: BusinessException): Unit {
        Hilog.info(0, "Camera", "Call invoke error. code: ${res.code}, msg: ${res.message}")
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let device = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(device)[0]
let ability = cameraManager.getSupportedOutputCapability(device, mode)
let output = cameraManager.createPhotoOutput(ability.photoProfiles[0])
let testCallbackError = TestCallbackError()
output.on(CameraCallbackType.CameraError, testCallbackError)
```