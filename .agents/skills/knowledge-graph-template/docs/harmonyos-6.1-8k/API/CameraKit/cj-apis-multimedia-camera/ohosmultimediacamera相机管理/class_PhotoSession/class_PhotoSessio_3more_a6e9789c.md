## class PhotoSession

```cangjie
public class PhotoSession <: Session & Flash & AutoExposure & Focus & Zoom & ColorManagement {}
```

**功能：** 普通拍照模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦、色彩空间及微距的操作。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- [Session](#interface-session)
- [Flash](#interface-flash)
- [AutoExposure](#interface-autoexposure)
- [Focus](#interface-focus)
- [Zoom](#interface-zoom)
- [ColorManagement](#interface-colormanagement)

### func canPreconfig(PreconfigType, PreconfigRatio)

```cangjie
public func canPreconfig(preconfigType: PreconfigType, preconfigRatio!: PreconfigRatio = PreconfigRatio_4_3): Bool
```

**功能：** 查询当前Session是否支持指定的预配置类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|preconfigType|[PreconfigType](#enum-preconfigtype)|是|-|指定配置预期分辨率。|
|preconfigRatio|[PreconfigRatio](#enum-preconfigratio)|否|PreconfigRatio_4_3|**命名参数。** 可选画幅比例，默认为4:3。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true: 支持指定预配值类型。false: 不支持指定预配值类型。|

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
    let photoSession = cameraManager.createSession(SceneMode.NormalPhoto) as PhotoSession
    let session = photoSession.getOrThrow()
    Hilog.info(0, "AppLogCj", session.canPreconfig(Preconfig1080p, preconfigRatio: PreconfigRatio_16_9).toString())
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```

### func off(CameraEvents, Callback0Argument)

```cangjie
public func off(eventType: CameraEvents, callback: Callback0Argument): Unit
```

**功能：** 注销监听普通拍照会话的错误事件，通过注册回调函数获取结果。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[CameraEvents](#enum-cameraevents)|是|-|监听事件，必须为CameraError，session创建成功之后可监听该接口。|
|callback|[Callback0Argument](../arkinterop/cj-api-callback_invoke.md#class-callback0argument)|是|-|回调函数，用于处理[BusinessException](../arkinterop/cj-api-business_exception.md#class-businessexception)。|

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
    let photoSession = cameraManager.createSession(SceneMode.NormalPhoto) as PhotoSession
    let session = photoSession.getOrThrow()
    session.off(CameraEvents.FocusStateChange)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```