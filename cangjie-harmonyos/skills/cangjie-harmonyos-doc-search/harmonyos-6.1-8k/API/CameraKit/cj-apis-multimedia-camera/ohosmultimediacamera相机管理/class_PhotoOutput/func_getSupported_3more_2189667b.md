### func getSupportedMovingPhotoVideoCodecTypes()

```cangjie
public func getSupportedMovingPhotoVideoCodecTypes(): Array<VideoCodecType>
```

**功能：** 查询支持的动态照片短视频编码类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[VideoCodecType](#enum-videocodectype)>|支持的动态照片短视频编码类型列表。|

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
    let device = cameraManager.getSupportedCameras()[0]
    let mode = cameraManager.getSupportedSceneModes(device)[0]
    let ability = cameraManager.getSupportedOutputCapability(device, mode)
    let output = cameraManager.createPhotoOutput(profile:ability.photoProfiles[0])
    let videoCodecTypes = output.getSupportedMovingPhotoVideoCodecTypes()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isMirrorSupported()

```cangjie
public func isMirrorSupported(): Bool
```

**功能：** 查询是否支持镜像拍照。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回是否支持镜像拍照，true表示支持，false表示不支持。|

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
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let device = cameraManager.getSupportedCameras()[0]
    let mode = cameraManager.getSupportedSceneModes(device)[0]
    let ability = cameraManager.getSupportedOutputCapability(device, mode)
    let output = cameraManager.createPhotoOutput(profile:ability.photoProfiles[0])
    Hilog.info(0, "AppLogCj", output.isMirrorSupported().toString())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func isMovingPhotoSupported()

```cangjie
public func isMovingPhotoSupported(): Bool
```

**功能：** 查询是否支持动态照片拍摄。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回是否支持动态照片拍照。true表示支持，false表示不支持。|

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
import ohos.business_exception.BusinessException
import kit.PerformanceAnalysisKit.Hilog

try {
    let ctx = Global.abilityContext // 此处需手动配置模板，获取Context上下文。上下文获取方式请参见使用说明。
    let cameraManager = getCameraManager(ctx)
    let device = cameraManager.getSupportedCameras()[0]
    let mode = cameraManager.getSupportedSceneModes(device)[0]
    let ability = cameraManager.getSupportedOutputCapability(device, mode)
    let output = cameraManager.createPhotoOutput(profile:ability.photoProfiles[0])
    Hilog.info(0, "AppLogCj", output.isMovingPhotoSupported().toString())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```