## class PhotoSession

```cangjie
public class PhotoSession <: Session & Flash & AutoExposure & Focus & Zoom & ColorManagement {}
```

**功能：** 普通拍照模式会话类，提供了对闪光灯、曝光、对焦、变焦、色彩空间的操作。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**父类型：**

- [Session](#interface-session)
- [Flash](#interface-flash)
- [AutoExposure](#interface-autoexposure)
- [Focus](#interface-focus)
- [Zoom](#interface-zoom)
- [ColorManagement](#interface-colormanagement)

### func canPreconfig(PreconfigType, PreconfigRatio)

```cangjie
public func canPreconfig(preconfigType: PreconfigType, preconfigRatio!: PreconfigRatio = PRECONFIG_RATIO_4_3): Bool
```

**功能：** 查询当前Session是否支持指定的与配置类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|preconfigType|[PreconfigType](#enum-preconfigtype)|是|-|指定配置预期分辨率。|
|preconfigRatio|[PreconfigRatio](#enum-preconfigratio)|否|PRECONFIG_RATIO_4_3| **命名参数。** 可选画幅比例。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true: 支持指定预配值类型。false: 不支持指定预配值类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID|错误信息|
  |:----|:----|
  |7400201|Camera service fatal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*
import ohos.base.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let photoSession = cameraManager.createSession(SceneMode.NORMAL_PHOTO) as PhotoSession
let session = photoSession.getOrThrow()
AppLog.info(session.canPreconfig(PRECONFIG_1080P, preconfigRatio: PRECONFIG_RATIO_16_9))
```

### func off(CameraCallbackType, Callback1Argument\<BusinessException>)

```cangjie
public func off(`type`: CameraCallbackType, callback: Callback1Argument<BusinessException>): Unit
```

**功能：** 注销监听普通拍照会话的错误事件，通过注册回调函数获取结果。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[CameraCallbackType](#enum-cameracallbacktype)|是|-|监听事件，必须为CameraCallbackType.error，session创建成功之后可监听该接口。|
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
let photoSession = cameraManager.createSession(SceneMode.NORMAL_PHOTO) as PhotoSession
let session = photoSession.getOrThrow()
let callback = TestCallbackError()
session.off(CameraCallbackType.CameraError, callback)
```