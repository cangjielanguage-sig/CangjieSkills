## interface Zoom

```cangjie
public interface Zoom <: ZoomQuery {
    func setZoomRatio(zoomRatio: Float64): Unit
    func getZoomRatio(): Float64
    func setSmoothZoom(targetRatio: Float64, mode: SmoothZoomMode): Unit
    func setSmoothZoom(targetRatio: Float64): Unit
}
```

**功能：** 变焦类，对设备变焦操作。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- [ZoomQuery](#interface-zoomquery)

### func getZoomRatio()

```cangjie
func getZoomRatio(): Float64
```

**功能：** 获取当前的变焦比。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Float64|获取当前的变焦比结果。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400103 | Session not config. |
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
    var photoSessionOption = session as PhotoSession
    let photoSession = photoSessionOption.getOrThrow()
    Hilog.info(0, "AppLogCj", photoSession.getZoomRatio().toString())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func setSmoothZoom(Float64, SmoothZoomMode)

```cangjie
func setSmoothZoom(targetRatio: Float64, mode: SmoothZoomMode): Unit
```

**功能：** 触发平滑变焦。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|targetRatio|Float64|是|-|目标值。通过[getZoomRatioRange](#func-getzoomratiorange)获取支持的变焦范围，如果设置超过支持范围的值，则只保留精度范围内数值。|
|mode|[SmoothZoomMode](#enum-smoothzoommode)|是|-|平滑变焦模式。|

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
    var photoSessionOption = session as PhotoSession
    let photoSession = photoSessionOption.getOrThrow()
    let targetRatio: Float64 = 0.3
    photoSession.setSmoothZoom(targetRatio, SmoothZoomMode.Normal)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```