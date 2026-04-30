## class SecureSession

```cangjie
public class SecureSession <: Session & Flash & AutoExposure & Focus & Zoom {}
```

**功能：** 安全模式会话类，提供了对闪光灯、曝光、对焦、变焦的操作。

**系统能力：** SystemCapability.Multimedia.Camera.Core

> **说明：**
>
> - 通过[createSession](#func-createsessionscenemode)接口传入[SceneMode](#enum-scenemode)为SECURE_PHOTO模式创建一个安全模式的会话。该模式开放给人脸识别、银行等有安全诉求的应用，需要结合安全TA使用，支持同时出普通预览流和安全流的业务场景。
>
> - 安全TA可用于图片处理，它具备验证服务器下发数据的验签能力、图片签名、解析及组装tlv逻辑的能力，还具备密钥读取、创建及操作能力。

**系统能力：**  SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- [Session](#interface-session)
- [Flash](#interface-flash)
- [AutoExposure](#interface-autoexposure)
- [Focus](#interface-focus)
- [Zoom](#interface-zoom)

### func addSecureOutput(PreviewOutput)

```cangjie
public func addSecureOutput(previewOutput: PreviewOutput): Unit
```

**功能：** 将其中一条[PreviewOutput](#class-previewoutput)标记成安全输出。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|previewOutput|[PreviewOutput](#class-previewoutput)|是|-|需要标记成安全输出的预览流。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID|错误信息|
  |:----|:----|
  |7400101|Parameter missing or parameter type incorrect.|
  |7400102|Operation not allowed.|
  |7400103|Session not config.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.image.createImageReceiver
import ohos.image.ImageFormat

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let secureSession = cameraManager.createSession(SceneMode.SECURE_PHOTO) as SecureSession
let session = secureSession.getOrThrow()
let device = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(device)[0]
let ability = cameraManager.getSupportedOutputCapability(device, mode)
let receiver = createImageReceiver(8192, 8, ImageFormat.JPEG, 8)
let surfaceId: String = receiver.getReceivingSurfaceId()
let previewOutput = cameraManager.createPreviewOutput(ability.previewProfiles[0], surfaceId)
session.addSecureOutput(previewOutput)
```