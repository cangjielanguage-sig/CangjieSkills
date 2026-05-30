### func preconfig(PreconfigType, PreconfigRatio)

```cangjie
public func preconfig(preconfigType: PreconfigType, preconfigRatio!: PreconfigRatio = PreconfigRatio.PRECONFIG_RATIO_16_9): Unit
```

**功能：** 对当前Session进行预配置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|preconfigType|[PreconfigType](#enum-preconfigtype)|是|-|指定配置预期分辨率。|
|preconfigRatio|[PreconfigRatio](#enum-preconfigratio)|否|PreconfigRatio.PRECONFIG_RATIO_16_9| **命名参数。** 可选画幅比例。|

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

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let videoSession = cameraManager.createSession(SceneMode.NORMAL_VIDEO) as VideoSession
let session = videoSession.getOrThrow()
session.preconfig(PRECONFIG_1080P, preconfigRatio: PRECONFIG_RATIO_16_9)
```