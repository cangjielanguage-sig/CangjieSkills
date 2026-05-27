## class MetadataOutput

```cangjie
public class MetadataOutput <: CameraOutput {}
```

**功能：** metadata流。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- [CameraOutput](#interface-cameraoutput)

### func off(CameraCallbackType, Callback1Argument\<Array\<MetadataObject>>)

```cangjie
public func off(`type`: CameraCallbackType, callback: Callback1Argument<Array<MetadataObject>>): Unit
```

**功能：** 注销监听检测到的metadata对象。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为metadataObjectsAvailable，metadataOutput创建成功后可监听。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<[MetadataObject](#class-metadataobject)>>|是|-|回调函数，取消对应callback。|

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
metadataOutput.off(CameraCallbackType.MetadataObjectsAvailable, testCallback)
```

### func off(CameraCallbackType, Callback1Argument\<BusinessException>)

```cangjie
public func off(`type`: CameraCallbackType, callback: Callback1Argument<BusinessException>): Unit
```

**功能：** 注销监听metadata流的错误。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为error，metadataOutput创建成功后可监听。|
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
let device = cameraManager.getSupportedCameras()[0]
let mode = cameraManager.getSupportedSceneModes(device)[0]
let ability = cameraManager.getSupportedOutputCapability(device, mode)
let metadataOutput = cameraManager.createMetadataOutput(ability.supportedMetadataObjectTypes[0])
let testCallbackError = TestCallbackError()
metadataOutput.off(CameraCallbackType.CameraError, testCallbackError)
```