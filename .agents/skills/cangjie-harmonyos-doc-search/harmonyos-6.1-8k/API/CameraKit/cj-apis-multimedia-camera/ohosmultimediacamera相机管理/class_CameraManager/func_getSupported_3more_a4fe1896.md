### func getSupportedCameras()

```cangjie
public func getSupportedCameras(): Array<CameraDevice>
```

**功能：** 获取支持指定的相机设备对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[CameraDevice](#class-cameradevice)>|相机设备列表。|

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
    let cameraDevices = cameraManager.getSupportedCameras()
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getSupportedOutputCapability(CameraDevice, SceneMode)

```cangjie
public func getSupportedOutputCapability(camera: CameraDevice, mode: SceneMode): CameraOutputCapability
```

**功能：** 查询相机设备在模式下支持的输出能力。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|camera|[CameraDevice](#class-cameradevice)|是|-|相机设备，通过[getSupportedCameras](#func-getsupportedcameras)接口获取。|
|mode|[SceneMode](#enum-scenemode)|是|-|相机模式，通过[getSupportedSceneModes](#func-getsupportedscenemodescameradevice)接口获取。|

**返回值：**

|类型|说明|
|:----|:----|
|[CameraOutputCapability](#class-cameraoutputcapability)|相机输出能力。|

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
    let cameraDevices = cameraManager.getSupportedCameras()
    let camera = cameraDevices[0]
    let mode = cameraManager.getSupportedSceneModes(camera)[0]
    let cameraOutputCapability = cameraManager.getSupportedOutputCapability(camera, mode)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func getSupportedSceneModes(CameraDevice)

```cangjie
public func getSupportedSceneModes(camera: CameraDevice): Array<SceneMode>
```

**功能：** 获取指定的相机设备对象支持的模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|camera|[CameraDevice](#class-cameradevice)|是|-|相机设备，通过[getSupportedCameras](#func-getsupportedcameras)接口获取。|

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[SceneMode](#enum-scenemode)>|相机支持的模式列表。|

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
    let cameraDevices = cameraManager.getSupportedCameras()
    let camera = cameraDevices[0]
    let mode = cameraManager.getSupportedSceneModes(camera)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```