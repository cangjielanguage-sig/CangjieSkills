### func open()

```cangjie
public func open(): Unit
```

**功能：** 打开相机。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400107 | Can not use camera cause of conflict. |
  | 7400108 | Camera disabled cause of security reason. |
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
    cameraInput.open()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func open(Bool)

```cangjie
public func open(isSecureEnabled: Bool): UInt64
```

**功能：** 打开相机。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|isSecureEnabled|Bool|是|-|设置true为使能以安全的方式打开相机，设置false则反之。|

**返回值：**

|类型|说明|
|:----|:----|
|UInt64|打开相机的句柄。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400107 | Can not use camera cause of conflict. |
  | 7400108 | Camera disabled cause of security reason. |
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
    let isSecureEnabled = false
    let handle = cameraInput.open(isSecureEnabled)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```