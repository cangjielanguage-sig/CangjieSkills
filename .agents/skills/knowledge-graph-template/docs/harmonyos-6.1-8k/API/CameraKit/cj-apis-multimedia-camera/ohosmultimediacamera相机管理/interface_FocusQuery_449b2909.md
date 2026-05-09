## interface FocusQuery

```cangjie
public interface FocusQuery {
    func isFocusModeSupported(afMode: FocusMode): Bool
}
```

**功能：** 提供了查询是否支持当前对焦模式的方法。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func isFocusModeSupported(FocusMode)

```cangjie
func isFocusModeSupported(afMode: FocusMode): Bool
```

**功能：** 检测对焦模式是否支持。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|afMode|[FocusMode](#enum-focusmode)|是|-|指定的焦距模式。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|检测对焦模式是否支持。true表示支持，false表示不支持。|

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
    var photoSessionOption = session as PhotoSession
    let photoSession = photoSessionOption.getOrThrow()
    let afMode = FocusMode.FocusModeManual
    Hilog.info(0, "AppLogCj", photoSession.isFocusModeSupported(afMode).toString())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```