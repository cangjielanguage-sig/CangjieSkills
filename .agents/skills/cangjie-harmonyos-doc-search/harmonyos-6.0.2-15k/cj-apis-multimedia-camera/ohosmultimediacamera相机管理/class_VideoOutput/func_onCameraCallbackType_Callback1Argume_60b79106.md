### func on(CameraCallbackType, Callback1Argument\<BusinessException>)

```cangjie
public func on(`type`: CameraCallbackType, callback: Callback1Argument<BusinessException>): Unit
```

**功能：** 监听录像输出发生错误，通过注册回调函数获取结果。

> **说明：**
>
> 不支持在on监听的回调方法里调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为error，videoOutput创建成功后可监听。录像接口调用出现错误时触发该事件并返回对应错误码，比如调用start，CameraOutput.release接口时出现错误返回对应错误信息。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)>|是|-|回调函数，用于获取错误信息。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.image.createImageReceiver
import ohos.image.ImageFormat
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
let mode = cameraManager.getSupportedSceneModes(device)[1]
let ability = cameraManager.getSupportedOutputCapability(device, mode)
let receiver = createImageReceiver(8192, 8, ImageFormat.JPEG, 8)
let surfaceId: String = receiver.getReceivingSurfaceId()
let output = cameraManager.createVideoOutput(ability.videoProfiles[0], surfaceId)
let testCallbackError = TestCallbackError()
output.on(CameraCallbackType.CameraError, testCallbackError)
```