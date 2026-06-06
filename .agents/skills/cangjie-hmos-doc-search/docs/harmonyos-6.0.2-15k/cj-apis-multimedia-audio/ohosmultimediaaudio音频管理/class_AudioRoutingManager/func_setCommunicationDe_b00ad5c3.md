### func setCommunicationDevice(CommunicationDeviceType, Bool)

```cangjie
public func setCommunicationDevice(deviceType: CommunicationDeviceType, active: Bool): Unit
```

**功能：** 设置通信设备激活状态。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceType|[CommunicationDeviceType](#enum-communicationdevicetype)|是|-|音频设备类型。|
|active|Bool|是|-|设备激活状态，true激活，false未激活。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |6800101|Invalid parameter.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

try {
    let instance = getAudioManager()
    let routingmgr = instance.getRoutingManager()
    routingmgr.setCommunicationDevice(CommunicationDeviceType.SPEAKER, true)
} catch (e: BusinessException) {
    Hilog.error(0, "setCommunicationDevice", "errCode: ${e.code}, errMessage: ${e.message}")
}
```