## interface ZoomQuery

```cangjie
sealed interface ZoomQuery {
    func getZoomRatioRange(): Array<Float32>
}
```

**功能：** 提供了与设备缩放能力相关的查询功能，包括获取支持的缩放比例范围。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### func getZoomRatioRange()

```cangjie
func getZoomRatioRange(): Array<Float32>
```

**功能：** 获取支持的变焦范围。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float32>|用于获取可变焦距比范围，返回的数组包括其最小值和最大值。|

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
let session = cameraManager.createSession(SceneMode.NORMAL_PHOTO)
var photoSessionOption = session as PhotoSession
let photoSession = photoSessionOption.getOrThrow()
let zoomRatio: Float32 = 0.5
AppLog.info(photoSession.getZoomRatioRange())
```