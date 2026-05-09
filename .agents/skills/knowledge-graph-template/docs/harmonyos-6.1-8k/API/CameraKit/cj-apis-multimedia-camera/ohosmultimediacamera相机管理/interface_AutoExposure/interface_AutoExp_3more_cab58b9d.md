## interface AutoExposure

```cangjie
public interface AutoExposure <: AutoExposureQuery {
    func getExposureMode(): ExposureMode
    func setExposureMode(aeMode: ExposureMode): Unit
    func getMeteringPoint(): Point
    func setMeteringPoint(point: Point): Unit
    func setExposureBias(exposureBias: Float64): Unit
    func getExposureValue(): Float64
}
```

**功能：** 自动曝光类，对设备自动曝光（AE）操作。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- [AutoExposureQuery](#interface-autoexposurequery)

### func getExposureMode()

```cangjie
func getExposureMode(): ExposureMode
```

**功能：** 获取当前曝光模式。

> **说明：**
>
> 若未通过[setExposureMode](#func-setexposuremodeexposuremode)接口进行设置，直接调用该接口查询当前曝光模式，会返回无效值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[ExposureMode](#enum-exposuremode)|获取当前曝光模式。接口调用失败会抛出相应错误码。|

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
    let session = cameraManager.createSession(SceneMode.NormalPhoto)
    let photoSession = session as PhotoSession
    Hilog.info(0, "AppLogCj", photoSession.getOrThrow().getExposureMode().toString())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getExposureValue()

```cangjie
func getExposureValue(): Float64
```

**功能：** 查询当前曝光值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Float64|获取曝光值。曝光补偿存在步长，如步长为0.5。则设置1.2时，获取到实际生效曝光补偿为1.0。|

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
    let session = cameraManager.createSession(SceneMode.NormalPhoto)
    let photoSession = session as PhotoSession
    Hilog.info(0, "AppLogCj", photoSession.getOrThrow().getExposureValue().toString())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```