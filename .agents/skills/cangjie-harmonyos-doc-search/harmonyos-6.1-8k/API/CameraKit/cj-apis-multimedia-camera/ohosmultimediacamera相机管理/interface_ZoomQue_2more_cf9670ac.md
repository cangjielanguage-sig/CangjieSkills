## interface ZoomQuery

```cangjie
public interface ZoomQuery {
    func getZoomRatioRange(): Array<Float64>
}
```

**功能：** 提供了与设备的缩放相关的查询功能，包括获取支持的缩放比例范围。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func getZoomRatioRange()

```cangjie
func getZoomRatioRange(): Array<Float64>
```

**功能：** 获取支持的变焦范围。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<Float64>|用于获取可变焦距比范围，返回的数组包括其最小值和最大值。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400103 | Session not config, only throw in session usage. |

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
    let zoomRatio: Float64 = 0.5
    Hilog.info(0, "AppLogCj", photoSession.getZoomRatioRange().toString())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

## class CameraDevice

```cangjie
public class CameraDevice {
    public let cameraId: String
    public let cameraPosition: CameraPosition
    public let cameraType: CameraType
    public let connectionType: ConnectionType
    public let cameraOrientation: UInt32
}
```

**功能：** 相机设备信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let cameraId

```cangjie
public let cameraId: String
```

**功能：** 相机ID。

**类型：** String

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let cameraOrientation

```cangjie
public let cameraOrientation: UInt32
```

**功能：** 相机安装角度，不会随着屏幕旋转而改变，取值范围为0°-360°，单位：度。

**类型：** UInt32

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let cameraPosition

```cangjie
public let cameraPosition: CameraPosition
```

**功能：** 相机位置。

**类型：** [CameraPosition](#enum-cameraposition)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let cameraType

```cangjie
public let cameraType: CameraType
```

**功能：** 相机类型。

**类型：** [CameraType](#enum-cameratype)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### let connectionType

```cangjie
public let connectionType: ConnectionType
```

**功能：** 相机连接类型。

**类型：** [ConnectionType](#enum-connectiontype)

**读写能力：** 只读

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22