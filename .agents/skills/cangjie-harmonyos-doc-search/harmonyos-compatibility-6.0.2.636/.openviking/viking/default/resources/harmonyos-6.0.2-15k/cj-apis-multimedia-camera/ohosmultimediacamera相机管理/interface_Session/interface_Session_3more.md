## interface Session

```cangjie
sealed interface Session {
    func beginConfig(): Unit
    func commitConfig(): Unit
    func canAddInput(cameraInput: CameraInput): Bool
    func addInput(cameraInput: CameraInput): Unit
    func removeInput(cameraInput: CameraInput): Unit
    func canAddOutput(cameraOutput: CameraOutput): Bool
    func addOutput(cameraOutput: CameraOutput): Unit
    func removeOutput(cameraOutput: CameraOutput): Unit
    func start(): Unit
    func stop(): Unit
    func release(): Unit
}
```

**功能：** 会话类型，保存一次相机运行所需要的所有资源[CameraInput](#class-camerainput)、[CameraOutput](#interface-cameraoutput)，并向相机设备申请完成相机功能（录像，拍照）。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### func addInput(CameraInput)

```cangjie
func addInput(cameraInput: CameraInput): Unit
```

**功能：** 把[CameraInput](#class-camerainput)加入到会话。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cameraInput|[CameraInput](#class-camerainput)|是|-|需要添加的CameraInput实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID         | 错误信息        |
  | :-------------- | :-------------- |
  | 7400101                |  Parameter missing or parameter type incorrect.        |
  | 7400102                |  Operation not allowed.                                  |
  | 7400103                |  Session not config.                                   |
  | 7400201                |  Camera service fatal error.                                   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let session = cameraManager.createSession(SceneMode.NORMAL_PHOTO)
let cameraDevice = cameraManager.getSupportedCameras()[0]
let cameraInput = cameraManager.createCameraInput(cameraDevice)
session.addInput(cameraInput)
```

### func addOutput(CameraOutput)

```cangjie
func addOutput(cameraOutput: CameraOutput): Unit
```

**功能：** 把[CameraOutput](#interface-cameraoutput)加入到会话。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|cameraOutput|[CameraOutput](#interface-cameraoutput)|是|-|需要添加的CameraOutput实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID         | 错误信息        |
  | :-------------- | :-------------- |
  | 7400101                |  Parameter missing or parameter type incorrect.        |
  | 7400102                |  Operation not allowed.                                  |
  | 7400103                |  Session not config.                                   |
  | 7400201                |  Camera service fatal error.                                   |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let session = cameraManager.createSession(SceneMode.NORMAL_PHOTO)
let cameraDevice = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(cameraDevice)[0]
let ability = cameraManager.getSupportedOutputCapability(cameraDevice, mode)
let cameraOutput = cameraManager.createPhotoOutput(ability.photoProfiles[0])
session.addOutput(cameraOutput)
```