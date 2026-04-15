### func createCameraInput(CameraPosition, CameraType)

```cangjie
public func createCameraInput(position: CameraPosition, cameraType: CameraType): CameraInput
```

**功能：** 根据相机位置和类型创建CameraInput实例。

该接口使用前需要开发者根据应用具体使用场景自行指定相机位置和类型，例如打开前置相机进入自拍功能。

**需要权限：** ohos.permission.CAMERA

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|position|[CameraPosition](#enum-cameraposition)|是|-|相机位置，通过[getSupportedCameras](#func-getsupportedcameras)接口获取设备，然后获取设备位置信息。|
|cameraType|[CameraType](#enum-cameratype)|是|-|相机类型，通过[getSupportedCameras](#func-getsupportedcameras)接口获取设备，然后获取设备类型信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[CameraInput](#class-camerainput)|CameraInput实例。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400101 | Parameter missing or parameter type incorrect. |
  | 7400102 | Operation not allowed. |
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
    let cameraDevice0 = cameraDevices[0]
    let position = cameraDevice0.cameraPosition
    let cameraType = cameraDevice0.cameraType
    let cameraInput = cameraManager.createCameraInput(position , cameraType)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```