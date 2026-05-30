## interface Stabilization

```cangjie
sealed interface Stabilization <: StabilizationQuery {
    func getActiveVideoStabilizationMode(): VideoStabilizationMode
    func setVideoStabilizationMode(mode: VideoStabilizationMode): Unit
}
```

**功能：** 提供设备在录像模式下视频防抖的相关操作。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- [StabilizationQuery](#interface-stabilizationquery)

### func getActiveVideoStabilizationMode()

```cangjie
func getActiveVideoStabilizationMode(): VideoStabilizationMode
```

**功能：** 查询当前正在使用的视频防抖模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[VideoStabilizationMode](#enum-videostabilizationmode)|视频防抖是否正在使用。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID|错误信息|
  |:----|:----|
  |7400103|Session not config.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let session = cameraManager.createSession(SceneMode.NORMAL_VIDEO)
var videoSessionOption = session as VideoSession
let videoSession = videoSessionOption.getOrThrow()
AppLog.info(videoSession.getActiveVideoStabilizationMode())
```

### func setVideoStabilizationMode(VideoStabilizationMode)

```cangjie
func setVideoStabilizationMode(mode: VideoStabilizationMode): Unit
```

**功能：** 设置视频防抖模式。需要先检查设备是否支持对应的防抖模式，可以通过[isVideoStabilizationModeSupported](#func-isvideostabilizationmodesupportedvideostabilizationmode)方法判断所设置的模式是否支持。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[VideoStabilizationMode](#enum-videostabilizationmode)|是|-|需要设置的视频防抖模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID|错误信息|
  |:----|:----|
  |7400103|Session not config.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let session = cameraManager.createSession(SceneMode.NORMAL_VIDEO)
var videoSessionOption = session as VideoSession
let videoSession = videoSessionOption.getOrThrow()
let vsMode = VideoStabilizationMode.OFF
videoSession.setVideoStabilizationMode(vsMode)
```