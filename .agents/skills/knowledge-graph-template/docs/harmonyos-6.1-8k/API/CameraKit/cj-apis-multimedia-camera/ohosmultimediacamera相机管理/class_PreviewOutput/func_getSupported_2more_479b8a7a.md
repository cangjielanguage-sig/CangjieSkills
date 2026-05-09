### func getSupportedFrameRates()

```cangjie
public func getSupportedFrameRates(): Array<FrameRateRange>
```

**功能：** 查询支持的帧率范围。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[FrameRateRange](#class-frameraterange)>|支持的帧率范围列表。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400201 | Camera service fatal error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import kit.ImageKit.createImageReceiver
import kit.ImageKit.Size as ImageSize
import kit.ImageKit.ImageFormat
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let device = cameraManager.getSupportedCameras()[0]
    let mode = cameraManager.getSupportedSceneModes(device)[0]
    let ability = cameraManager.getSupportedOutputCapability(device, mode)
    let size = ImageSize(8, 8192)
    let receiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
    let surfaceId: String = receiver.getReceivingSurfaceId()
    let output = cameraManager.createPreviewOutput(ability.previewProfiles[0], surfaceId)
    let frameRateRanges = output.getSupportedFrameRates()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func off(CameraEvents, Callback0Argument)

```cangjie
public func off(eventType: CameraEvents, callback: Callback0Argument): Unit
```

**功能：** 注销监听特定事件。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[CameraEvents](#enum-cameraevents)|是|-|监听事件，必须为[FrameStart, FrameEnd, CameraError]其中之一。|
|callback|[Callback0Argument](../arkinterop/cj-api-callback_invoke.md#class-callback0argument)|是|-|回调函数。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400201 | Camera service fatal error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import kit.ImageKit.createImageReceiver
import kit.ImageKit.Size as ImageSize
import kit.ImageKit.ImageFormat
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let device = cameraManager.getSupportedCameras()[0]
    let mode = cameraManager.getSupportedSceneModes(device)[0]
    let ability = cameraManager.getSupportedOutputCapability(device, mode)
    let size = ImageSize(8, 8192)
    let receiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
    let surfaceId: String = receiver.getReceivingSurfaceId()
    let output = cameraManager.createPreviewOutput(ability.previewProfiles[0], surfaceId)
    output.off(CameraEvents.CameraError)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```