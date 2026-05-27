### func off(CameraCallbackType, Callback1Argument\<FoldStatusInfo>)

```cangjie
public func off(`type`: CameraCallbackType, callback: Callback1Argument<FoldStatusInfo>): Unit
```

**功能：** 关闭折叠设备折叠状态变化的监听。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为foldStatusChange。表示折叠设备折叠状态发生变化。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[FoldStatusInfo](#struct-foldstatusinfo)>|是|-|回调函数，取消对应callback。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*
import ohos.hilog.Hilog

// 此处代码可添加在依赖项定义中
class TestCallbackFoldStatusChange <: Callback1Argument<FoldStatusInfo> {
    public init() {}
    public open func invoke(res: FoldStatusInfo): Unit {
        Hilog.info(0, "Camera", "Call invoke FoldStatusChange.")
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let testCallbackFoldStatusChange = TestCallbackFoldStatusChange()
cameraManager.off(CameraCallbackType.FoldStatusChange, testCallbackFoldStatusChange)
```

### func off(CameraCallbackType, Callback1Argument\<TorchStatusInfo>)

```cangjie
public func off(`type`: CameraCallbackType, callback: Callback1Argument<TorchStatusInfo>): Unit
```

**功能：** 手电筒状态变化注销回调，通过注销回调函数以取消获取手电筒状态变化。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为torchStatusChange。cameraManager对象获取成功后可监听。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[TorchStatusInfo](#struct-torchstatusinfo)>|是|-|回调函数，取消对应callback。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.hilog.Hilog
import ohos.base.*

// 此处代码可添加在依赖项定义中
class TestCallbackTorchStatusChange <: Callback1Argument<TorchStatusInfo> {
    public init() {}
    public open func invoke(res: TorchStatusInfo): Unit {
        Hilog.info(0, "Camera", "Call invoke TorchStatusChange. isTorchAvailable: ${res.isTorchAvailable}, isTorchActive: ${res.isTorchActive}, torchLevel:${res.torchLevel}")
    }
}

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let testCallbackTorchStatusChange = TestCallbackTorchStatusChange()
cameraManager.off(CameraCallbackType.TorchStatusChange, testCallbackTorchStatusChange)
```

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
cameraManager.off(CameraCallbackType.TorchStatusChange)
```