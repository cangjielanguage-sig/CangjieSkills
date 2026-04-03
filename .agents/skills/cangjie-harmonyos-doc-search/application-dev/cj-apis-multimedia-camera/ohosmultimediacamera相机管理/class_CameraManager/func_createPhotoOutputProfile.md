### func createPhotoOutput(?Profile)

```cangjie
public func createPhotoOutput(profile!: ?Profile = None): PhotoOutput
```

**功能：** 创建拍照输出对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|profile|?[Profile](#class-profile)|否|None|支持的拍照配置信息，通过[getSupportedOutputCapability](#func-getsupportedcameras)接口获取。如果使用[preconfig](#func-preconfigpreconfigtype-preconfigratio)进行预配置，传入profile参数会覆盖preconfig的预配置参数。|

**返回值：**

|类型|说明|
|:----|:----|
|[PhotoOutput](#class-photooutput)|PhotoOutput实例。|

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
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let cameraDevices = cameraManager.getSupportedCameras()
    let camera = cameraDevices[0]
    let mode = cameraManager.getSupportedSceneModes(camera)[0]
    let cameraOutputCapability = cameraManager.getSupportedOutputCapability(camera, mode)
    let profile = cameraOutputCapability.photoProfiles[0]
    let photoOutput  = cameraManager.createPhotoOutput(profile:profile)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```