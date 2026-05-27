## interface Zoom

```cangjie
sealed interface Zoom <: ZoomQuery {
    func setZoomRatio(zoomRatio: Float32): Unit
    func getZoomRatio(): Float32
    func setSmoothZoom(targetRatio: Float32, mode: SmoothZoomMode): Unit
    func setSmoothZoom(targetRatio: Float32): Unit
}
```

**功能：** 设备变焦（缩放）操作。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- [ZoomQuery](#interface-zoomquery)

### func getZoomRatio()

```cangjie
func getZoomRatio(): Float32
```

**功能：** 获取当前的变焦比。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float32|当前的变焦比结果。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID|错误信息|
  |:----|:----|
  |7400103|Session not config.|
  |7400201|Camera service fatal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let session = cameraManager.createSession(SceneMode.NORMAL_PHOTO)
var photoSessionOption = session as PhotoSession
let photoSession = photoSessionOption.getOrThrow()
AppLog.info(photoSession.getZoomRatio())
```

### func setSmoothZoom(Float32, SmoothZoomMode)

```cangjie
func setSmoothZoom(targetRatio: Float32, mode: SmoothZoomMode): Unit
```

**功能：** 触发平滑变焦。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|targetRatio|Float32|是|-|目标值。|
|mode|[SmoothZoomMode](#enum-smoothzoommode)|是|-|模式。|

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
let session = cameraManager.createSession(SceneMode.NORMAL_PHOTO)
var photoSessionOption = session as PhotoSession
let photoSession = photoSessionOption.getOrThrow()
let targetRatio: Float32 = 0.3
photoSession.setSmoothZoom(targetRatio, SmoothZoomMode.NORMAL)
```

### func setSmoothZoom(Float32)

```cangjie
func setSmoothZoom(targetRatio: Float32): Unit
```

**功能：** 触发平滑变焦。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|targetRatio|Float32|是|-|目标值。|

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
let session = cameraManager.createSession(SceneMode.NORMAL_PHOTO)
var photoSessionOption = session as PhotoSession
let photoSession = photoSessionOption.getOrThrow()
let targetRatio: Float32 = 0.3
photoSession.setSmoothZoom(targetRatio)
```