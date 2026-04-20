### func beginConfig()

```cangjie
func beginConfig(): Unit
```

**功能：** 开始配置会话。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400105 | Session config locked. |
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
    let session = cameraManager.createSession(SceneMode.NormalPhoto)
    session.beginConfig()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func canAddInput(CameraInput)

```cangjie
func canAddInput(cameraInput: CameraInput): Bool
```

**功能：** 判断当前cameraInput是否可以添加到session中。当前函数需要在[beginConfig](#func-beginconfig)和[commitConfig](#func-commitconfig)之间生效。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cameraInput|[CameraInput](#class-camerainput)|是|-|需要添加的CameraInput实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回true表示支持添加当前cameraInput，返回false表示不支持添加。|

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
    let session = cameraManager.createSession(SceneMode.NormalPhoto)
    let cameraDevice = cameraManager.getSupportedCameras()[0]
    let cameraInput = cameraManager.createCameraInput(cameraDevice)
    Hilog.info(0, "AppLogCj", session.canAddInput(cameraInput).toString())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func canAddOutput(CameraOutput)

```cangjie
func canAddOutput(cameraOutput: CameraOutput): Bool
```

**功能：** 判断当前cameraOutput是否可以添加到session中。当前函数需要在[addInput](#func-addinputcamerainput)和[commitConfig](#func-commitconfig)之间生效。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cameraOutput|[CameraOutput](#interface-cameraoutput)|是|-|需要添加的CameraOutput实例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否可以添加当前cameraOutput到session中。|

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
    let session = cameraManager.createSession(SceneMode.NormalPhoto)
    let cameraDevice = cameraManager.getSupportedCameras()[0]
    let mode = cameraManager.getSupportedSceneModes(cameraDevice)[0]
    let ability = cameraManager.getSupportedOutputCapability(cameraDevice, mode)
    let cameraOutput = cameraManager.createPhotoOutput(profile:ability.photoProfiles[0])
    Hilog.info(0, "AppLogCj", session.canAddOutput(cameraOutput).toString())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```