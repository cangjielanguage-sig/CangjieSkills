## interface ColorManagement

```cangjie
public interface ColorManagement <: ColorManagementQuery {
    func setColorSpace(colorSpace: ColorSpace): Unit
    func getActiveColorSpace(): ColorSpace
}
```

**功能：** 色彩管理类，用于设置色彩空间参数。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- [ColorManagementQuery](#interface-colormanagementquery)

### func getActiveColorSpace()

```cangjie
func getActiveColorSpace(): ColorSpace
```

**功能：** 获取当前设置的色彩空间。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[ColorSpace](../ArkGraphics2D/cj-apis-color_manager.md#enum-colorspace)|当前设置的色彩空间。|

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
    let colorSpace = photoSession.getActiveColorSpace()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```