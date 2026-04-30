## interface StabilizationQuery

```cangjie
sealed interface StabilizationQuery {
    func isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): Bool
}
```

**功能：** 提供查询设备在录像模式下是否支持对应的视频防抖模式的能力。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### func isVideoStabilizationModeSupported(VideoStabilizationMode)

```cangjie
func isVideoStabilizationModeSupported(vsMode: VideoStabilizationMode): Bool
```

**功能：** 查询是否支持指定的视频防抖模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|vsMode|[VideoStabilizationMode](#enum-videostabilizationmode)|是|-|视频防抖模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回视频防抖模式是否支持，true表示支持，false表示不支持。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID|错误信息|
  |:----|:----|
  |7400103|Session not config, only throw in session usage.|

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
videoSession.isVideoStabilizationModeSupported(vsMode)
```