## interface AutoExposure

```cangjie
sealed interface AutoExposure <: AutoExposureQuery {
    func getExposureMode(): ExposureMode
    func setExposureMode(aeMode: ExposureMode): Unit
    func getMeteringPoint(): Point
    func setMeteringPoint(point: Point): Unit
    func setExposureBias(exposureBias: Float32): Unit
    func getExposureValue(): Float32
}
```

**功能：** 设备自动曝光（AE）操作。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- [AutoExposureQuery](#interface-autoexposurequery)

### func getExposureMode()

```cangjie
func getExposureMode(): ExposureMode
```

**功能：** 获取当前曝光模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[ExposureMode](#enum-exposuremode)|当前曝光模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |7400103|Session not config.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let session = cameraManager.createSession(SceneMode.NORMAL_PHOTO)
let photoSession = session as PhotoSession
AppLog.info(photoSession.getOrThrow().getExposureMode())
```

### func getExposureValue()

```cangjie
func getExposureValue(): Float32
```

**功能：** 查询当前曝光值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Float32|曝光值。曝光补偿存在步长，如步长为0.5。则设置1.2时，获取到实际生效曝光补偿为1.0。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |7400103|Session not config.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let session = cameraManager.createSession(SceneMode.NORMAL_PHOTO)
let photoSession = session as PhotoSession
AppLog.info(photoSession.getOrThrow().getExposureValue())
```

### func getMeteringPoint()

```cangjie
func getMeteringPoint(): Point
```

**功能：** 查询曝光区域中心点。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[Point](#struct-point)|当前曝光点。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |7400103|Session not config.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let session = cameraManager.createSession(SceneMode.NORMAL_PHOTO)
let photoSession = session as PhotoSession
let point = photoSession.getOrThrow().getMeteringPoint()
```