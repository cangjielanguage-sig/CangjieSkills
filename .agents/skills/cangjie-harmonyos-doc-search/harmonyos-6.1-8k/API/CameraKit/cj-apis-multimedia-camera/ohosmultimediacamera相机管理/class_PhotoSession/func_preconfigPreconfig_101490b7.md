### func preconfig(PreconfigType, PreconfigRatio)

```cangjie
public func preconfig(
    preconfigType: PreconfigType,
    preconfigRatio!: PreconfigRatio = PreconfigRatio.PreconfigRatio_4_3
): Unit
```

**功能：** 对当前Session进行预配置。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|preconfigType|[PreconfigType](#enum-preconfigtype)|是|-|指定配置预期分辨率。|
|preconfigRatio|[PreconfigRatio](#enum-preconfigratio)|否|PreconfigRatio.PreconfigRatio_4_3|**命名参数。** 可选画幅比例，默认为4:3。|

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
    session.preconfig(Preconfig1080p, preconfigRatio: PreconfigRatio_16_9)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```