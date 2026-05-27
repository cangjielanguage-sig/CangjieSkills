## class CameraInput

```cangjie
public class CameraInput
```

**功能：** 相机设备输入对象。会话中Session使用的相机信息。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

### func close()

```cangjie
public func close(): Unit
```

**功能：** 关闭相机。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID         | 错误信息        |
  | :-------------- | :-------------- |
  | 7400201                |  Camera service fatal error.                                  |

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let cameraDevice = cameraManager.getSupportedCameras()[0]
let cameraInput = cameraManager.createCameraInput(cameraDevice)
cameraInput.close()
```

### func off(CameraCallbackType, CameraDevice, Callback1Argument\<BusinessException>)

```cangjie
public func off(`type`: CameraCallbackType, camera: CameraDevice, callback: Callback1Argument<BusinessException>): Unit
```

**功能：** 注销监听CameraInput的错误事件。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为error，CameraInput对象创建成功可监听。相机设备出错情况下可触发该事件并返回结果，比如设备不可用或者冲突等返回对应错误信息。|
|camera|[CameraDevice](#class-cameradevice)|是|-|CameraDevice对象。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)>|是|-|回调函数，取消对应callback。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.hilog.Hilog
import ohos.base.*

// 此处代码可添加在依赖项定义中
class TestCallbackError <: Callback1Argument<BusinessException> {
    public init() {}
    public open func invoke(res: BusinessException): Unit {
        Hilog.info(0, "Camera", "Call invoke error. code: ${res.code}, msg: ${res.message}")
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let cameraDevice = cameraManager.getSupportedCameras()[0]
let cameraInput = cameraManager.createCameraInput(cameraDevice)
let testCallbackError = TestCallbackError()
cameraInput.off(CameraCallbackType.CameraError, cameraDevice, testCallbackError)
```

### func off(CameraCallbackType, CameraDevice)

```cangjie
public func off(`type`: CameraCallbackType, camera: CameraDevice): Unit
```

**功能：** 取消对应监听事件的所有回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件。|
|camera|[CameraDevice](#class-cameradevice)|是|-|CameraDevice对象。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let cameraDevice = cameraManager.getSupportedCameras()[0]
let cameraInput = cameraManager.createCameraInput(cameraDevice)
cameraInput.off(CameraCallbackType.CameraError, cameraDevice)
```