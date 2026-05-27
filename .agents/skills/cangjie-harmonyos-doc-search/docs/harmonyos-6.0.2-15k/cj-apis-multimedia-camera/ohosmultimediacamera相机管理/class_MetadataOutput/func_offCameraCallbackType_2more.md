### func off(CameraCallbackType)

```cangjie
public func off(`type`: CameraCallbackType): Unit
```

**功能：** 取消对应监听事件的所有回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let device = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(device)[0]
let ability = cameraManager.getSupportedOutputCapability(device, mode)
let metadataOutput = cameraManager.createMetadataOutput(ability.supportedMetadataObjectTypes[0])
metadataOutput.off(CameraCallbackType.CameraError)
```

### func on(CameraCallbackType, Callback1Argument\<Array\<MetadataObject>>)

```cangjie
public func on(`type`: CameraCallbackType, callback: Callback1Argument<Array<MetadataObject>>): Unit
```

**功能：** 监听检测到的metadata对象，通过注册回调函数获取结果。

> **说明：**
>
> 不支持在on监听的回调方法里调用off注销回调。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为metadataObjectsAvailable，metadataOutput创建成功后可监听。检测到有效的metadata数据时触发该事件发生并返回相应的metadata数据。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<[MetadataObject](#class-metadataobject)>>|是|-|回调函数，用于获取metadata数据。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.hilog.Hilog
import ohos.base.*

// 此处代码可添加在依赖项定义中
class TestCallback <: Callback1Argument<Array<MetadataObject>> {
    public init() {}
    public open func invoke(res: Array<MetadataObject>): Unit {
        Hilog.info(0, "Camera", "Call invoke error.")
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let device = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(device)[0]
let ability = cameraManager.getSupportedOutputCapability(device, mode)
let metadataOutput = cameraManager.createMetadataOutput(ability.supportedMetadataObjectTypes[0])
let testCallback = TestCallback()
metadataOutput.on(CameraCallbackType.MetadataObjectsAvailable, testCallback)
```