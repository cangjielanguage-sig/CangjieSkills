### func createPreviewOutput(Profile, String)

```cangjie
public func createPreviewOutput(profile: Profile, surfaceId: String): PreviewOutput
```

**功能：** 创建预览输出对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|profile|[Profile](#class-profile)|是|-|支持的预览配置信息，通过[getSupportedOutputCapability](#func-getsupportedoutputcapabilitycameradevice-scenemode)接口获取。|
|surfaceId|String|是|-|从[ImageReceiver](../ImageKit/cj-apis-image.md#class-imagereceiver)组件获取的surfaceId。|

**返回值：**

|类型|说明|
|:----|:----|
|[PreviewOutput](#class-previewoutput)|PreviewOutput实例。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400101 | Parameter missing or parameter type incorrect. |
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
    let cameraDevices = cameraManager.getSupportedCameras()
    let camera = cameraDevices[0]
    let mode = cameraManager.getSupportedSceneModes(camera)[0]
    let cameraOutputCapability = cameraManager.getSupportedOutputCapability(camera, mode)
    let profile = cameraOutputCapability.previewProfiles[0]
    let size = ImageSize(8, 8192)
    let receiver = createImageReceiver(size, ImageFormat.Jpeg, 8)
    let surfaceId: String = receiver.getReceivingSurfaceId()
    let previewOutput = cameraManager.createPreviewOutput(profile, surfaceId)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```