## interface Stabilization

```cangjie
public interface Stabilization <: StabilizationQuery {
    func getActiveVideoStabilizationMode(): VideoStabilizationMode
    func setVideoStabilizationMode(mode: VideoStabilizationMode): Unit
}
```

**功能：** 提供设备在录像模式下设置视频防抖的操作。

> **说明：**
>
> - 对视频进行防抖设置的前提是会话中有录像流（[VideoOutput](#class-videooutput)）。
>
> - 设置防抖操作时，[VideoStabilizationMode.HIGH](#high)需要在[Profile](#class-profile)的分辨率为1920*1080的场景下生效。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- [StabilizationQuery](#interface-stabilizationquery)

### func getActiveVideoStabilizationMode()

```cangjie
func getActiveVideoStabilizationMode(): VideoStabilizationMode
```

**功能：** 查询当前正在使用的视频防抖模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[VideoStabilizationMode](#enum-videostabilizationmode)|视频防抖是否正在使用。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400103 | Session not config. |

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
    let session = cameraManager.createSession(SceneMode.NormalVideo)
    var videoSessionOption = session as VideoSession
    let videoSession = videoSessionOption.getOrThrow()
    Hilog.info(0, "AppLogCj", videoSession.getActiveVideoStabilizationMode().toString())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func setVideoStabilizationMode(VideoStabilizationMode)

```cangjie
func setVideoStabilizationMode(mode: VideoStabilizationMode): Unit
```

**功能：** 设置视频防抖模式。需要先检查设备是否支持对应的防抖模式，可以通过[isVideoStabilizationModeSupported](#func-isvideostabilizationmodesupportedvideostabilizationmode)方法判断所设置的模式是否支持。建议在[commitConfig](#func-commitconfig)与[start](#func-start)之间设置视频防抖。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[VideoStabilizationMode](#enum-videostabilizationmode)|是|-|需要设置的视频防抖模式。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400103 | Session not config. |

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
    let session = cameraManager.createSession(SceneMode.NormalVideo)
    var videoSessionOption = session as VideoSession
    let videoSession = videoSessionOption.getOrThrow()
    let vsMode = VideoStabilizationMode.Off
    videoSession.setVideoStabilizationMode(vsMode)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```