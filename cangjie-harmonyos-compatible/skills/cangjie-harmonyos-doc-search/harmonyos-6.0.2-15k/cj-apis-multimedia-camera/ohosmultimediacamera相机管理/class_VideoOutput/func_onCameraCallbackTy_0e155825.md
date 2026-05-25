### func on(CameraCallbackType, Callback0Argument)

```cangjie
public func on(`type`: CameraCallbackType, callback: Callback0Argument): Unit
```

**功能：** 监听录像开始或监听录像结束。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为frameStart或frameEnd，videoOutput创建成功后可监听。底层第一次曝光时触发该事件并返回。|
|callback|[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)|是|-|回调函数，用于获取结果。|

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
class TestCallbackFrameStart <: Callback0Argument {
    public init() {}
    public open func invoke(): Unit {
        Hilog.info(0, "Camera", "Call invoke FrameStart.")
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
let testCallbackFrameStart = TestCallbackFrameStart()
output.on(CameraCallbackType.FrameStart, testCallbackFrameStart)
```