### func setTorchMode(TorchMode)

```cangjie
public func setTorchMode(mode: TorchMode): Unit
```

**功能：** 设置设备手电筒模式。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mode|[TorchMode](#enum-torchmode)|是|-|手电筒模式。|

**异常：**

- BusinessException：对应错误码如下表，详见[Camera错误码](./cj-errorcode-multimedia-camera.md)。

  | 错误码ID | 错误信息 |
  | :---- | :--- |
  | 7400102 | Operation not allowed. |
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
    cameraManager.setTorchMode(TorchMode.On)
    cameraManager.setTorchMode(TorchMode.Off)
} catch (e: BusinessException) {
    Hilog.info(0, "test", "${e.message}")
}
```