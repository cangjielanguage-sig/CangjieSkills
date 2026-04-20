### func setZoomRatio(Float32)

```cangjie
func setZoomRatio(zoomRatio: Float32): Unit
```

**功能：** 设置变焦比，变焦精度最高为小数点后两位，如果设置超过支持的精度范围，则只保留精度范围内数值。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|zoomRatio|Float32|是|-|可变焦距比，通过[getZoomRatioRange](#func-getzoomratiorange)获取支持的变焦范围，如果设置超过支持范围的值，则只保留精度范围内数值。设置可变焦距比到底层生效需要一定时间，获取正确设置的可变焦距比需要等待1~2帧的时间。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Camera错误码](../../errorcodes/cj-errorcode-multimedia-camera.md)。

  | 错误码ID|错误信息|
  |:----|:----|
  |7400103|Session not config.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.CameraKit.*

let ctx = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let cameraManager = getCameraManager(ctx)
let session = cameraManager.createSession(SceneMode.NORMAL_PHOTO)
var photoSessionOption = session as PhotoSession
let photoSession = photoSessionOption.getOrThrow()
let zoomRatio: Float32 = 0.5
photoSession.setZoomRatio(zoomRatio)
```