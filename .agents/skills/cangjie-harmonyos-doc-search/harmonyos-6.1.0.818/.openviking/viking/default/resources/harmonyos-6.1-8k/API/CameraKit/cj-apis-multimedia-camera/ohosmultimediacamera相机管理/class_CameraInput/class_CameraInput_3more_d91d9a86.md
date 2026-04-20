## class CameraInput

```cangjie
public class CameraInput {}
```

**功能：** 相机设备输入对象。

会话中[Session](#interface-session)使用的相机信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

### func close()

```cangjie
public func close(): Unit
```

**功能：** 关闭相机。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
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
    let cameraDevice = cameraManager.getSupportedCameras()[0]
    let cameraInput = cameraManager.createCameraInput(cameraDevice)
    cameraInput.close()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func off(CameraEvents, CameraDevice, Callback0Argument)

```cangjie
public func off(eventType: CameraEvents, camera: CameraDevice, callback: Callback0Argument): Unit
```

**功能：** 注销监听CameraInput的错误事件。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[CameraEvents](#enum-cameraevents)|是|-|监听事件，固定为CameraError，CameraInput对象创建成功可监听。相机设备出错情况下可触发该事件并返回结果，比如设备不可用或者冲突等返回对应错误信息。|
|camera|[CameraDevice](#class-cameradevice)|是|-|CameraDevice对象。|
|callback|[Callback0Argument](../arkinterop/cj-api-callback_invoke.md#class-callback0argument)|是|-|回调函数。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
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
    let cameraDevice = cameraManager.getSupportedCameras()[0]
    let cameraInput = cameraManager.createCameraInput(cameraDevice)
    cameraInput.off(CameraEvents.CameraError, cameraDevice)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```