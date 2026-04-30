### func isMovingPhotoSupported()

```cangjie
public func isMovingPhotoSupported(): Bool
```

**功能：** 查询是否支持动态照片拍摄。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回是否支持动态照片拍照，true表示支持，false表示不支持。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID       | 错误信息       |
  | :------------- | :-------------- |
  | 7400201 |  Camera service fatal error. |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let device = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(device)[0]
let ability = cameraManager.getSupportedOutputCapability(device, mode)
let output = cameraManager.createPhotoOutput(ability.photoProfiles[0])
AppLog.info(output.isMovingPhotoSupported())
```

### func off(CameraCallbackType, Callback1Argument\<CaptureStartInfo>)

```cangjie
public func off(`type`: CameraCallbackType, callback: Callback1Argument<CaptureStartInfo>): Unit
```

**功能：** 注销监听拍照。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为captureStartWithInfo，photoOutput创建成功后可监听。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[CaptureStartInfo](#struct-capturestartinfo)>|是|-|回调函数，取消对应callback。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*
import ohos.hilog.Hilog

// 此处代码可添加在依赖项定义中
class TestCallbackCaptureStartWithInfo <: Callback1Argument<CaptureStartInfo> {
    public init() {}
    public open func invoke(res: CaptureStartInfo): Unit {
        Hilog.info(0, "Camera", "Call invoke CaptureStartWithInfo. captureId: ${res.captureId}, time： ${res.time}")
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let device = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(device)[0]
let ability = cameraManager.getSupportedOutputCapability(device, mode)
let output = cameraManager.createPhotoOutput(ability.photoProfiles[0])
let testCallbackCaptureStartWithInfo = TestCallbackCaptureStartWithInfo()
output.off(CameraCallbackType.CaptureStartWithInfo, testCallbackCaptureStartWithInfo)
```