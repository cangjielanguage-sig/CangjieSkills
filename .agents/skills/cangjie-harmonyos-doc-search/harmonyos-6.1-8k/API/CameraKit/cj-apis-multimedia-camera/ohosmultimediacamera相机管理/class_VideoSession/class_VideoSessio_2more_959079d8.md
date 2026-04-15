## class VideoSession

```cangjie
public class VideoSession <: Session & Flash & AutoExposure & Focus & Zoom & Stabilization & ColorManagement {}
```

**功能：** 普通录像模式会话类，提供了对闪光灯、曝光、白平衡、对焦、变焦、视频防抖、色彩空间、微距及控制器的操作。

> **说明：**
>
> 默认的视频录制模式，适用于一般场景。支持720P、1080p等多种分辨率的录制，可选择不同帧率（如30fps、60fps）。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**父类型：**

- [Session](#interface-session)
- [Flash](#interface-flash)
- [AutoExposure](#interface-autoexposure)
- [Focus](#interface-focus)
- [Zoom](#interface-zoom)
- [Stabilization](#interface-stabilization)
- [ColorManagement](#interface-colormanagement)

### func canPreconfig(PreconfigType, PreconfigRatio)

```cangjie
public func canPreconfig(preconfigType: PreconfigType, preconfigRatio!: PreconfigRatio = PreconfigRatio_16_9): Bool
```

**功能：** 查询当前Session是否支持指定的预配置类型。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|preconfigType|[PreconfigType](#enum-preconfigtype)|是|-|指定配置预期分辨率。|
|preconfigRatio|[PreconfigRatio](#enum-preconfigratio)|否|PreconfigRatio_16_9|**命名参数。** 可选画幅比例，默认为16:9。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true: 支持指定预配置类型。<br/>false: 不支持指定预配置类型。|

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
    let videoSession = cameraManager.createSession(SceneMode.NormalVideo) as VideoSession
    let session = videoSession.getOrThrow()
    let result = session.canPreconfig(Preconfig1080p, preconfigRatio: PreconfigRatio_16_9)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```