### func isCommunicationDeviceActive(CommunicationDeviceType)

```cangjie
public func isCommunicationDeviceActive(deviceType: CommunicationDeviceType): Bool
```

**功能：** 获取指定通信设备的激活状态，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceType|[CommunicationDeviceType](#enum-communicationdevicetype)|是|-|活跃音频设备类型。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回设备的激活状态，true激活，false未激活。|

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
    let ret = routingmgr.isCommunicationDeviceActive(CommunicationDeviceType.SPEAKER)
} catch (e: BusinessException) {
    Hilog.error(0, "getPreferredInputDeviceForCapturerInfo", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func off(AudioRoutingManagerCallbackType, ?CallbackObject)

```cangjie
public func off(`type`: AudioRoutingManagerCallbackType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消监听事件。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AudioRoutingManagerCallbackType](#enum-audioroutingmanagercallbacktype)|是|-|监听事件类型。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 回调函数。|

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

// 此处代码可添加在依赖项定义中
class InputDeviceChangeCallback <: Callback1Argument<AudioDeviceDescriptors> {
    public func invoke(arg: AudioDeviceDescriptors) {
        AppLog.info("callback: ${arg[0].displayName}")
    }
}

try {
    let instance = getAudioManager()
    let routingmgr = instance.getRoutingManager()
    var cb2 = InputDeviceChangeCallback()
    let capturerInfo = AudioCapturerInfo(SourceType.SOURCE_TYPE_VOICE_COMMUNICATION, 0)
    routingmgr.on(AudioRoutingManagerCallbackType.PREFERRED_INPUT_DEVICE_CHANGE_FOR_CAPTURER_INFO, capturerInfo, cb2)
    routingmgr.off(AudioRoutingManagerCallbackType.DEVICE_CHANGE)
} catch (e: BusinessException) {
    Hilog.error(0, "RoutingManager:on/off", "errCode: ${e.code}, errMessage: ${e.message}")
}
```