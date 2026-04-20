### func getPreferredInputDeviceForCapturerInfo(AudioCapturerInfo)

```cangjie
public func getPreferredInputDeviceForCapturerInfo(capturerInfo: AudioCapturerInfo): AudioDeviceDescriptors
```

**功能：** 根据音频信息，返回优先级最高的输入设备，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|capturerInfo|[AudioCapturerInfo](#class-audiocapturerinfo)|是|-|表示采集器信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[AudioDeviceDescriptors](#type-audiodevicedescriptors)|返回优先级最高的输入设备信息。|

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
    let capturerInfo = AudioCapturerInfo(SourceType.SOURCE_TYPE_VOICE_COMMUNICATION, 0)
    let arr = routingmgr.getPreferredInputDeviceForCapturerInfo(capturerInfo)
} catch (e: BusinessException) {
     Hilog.error(0, "getPreferredInputDeviceForCapturerInfo", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getPreferredOutputDeviceForRendererInfo(AudioRendererInfo)

```cangjie
public func getPreferredOutputDeviceForRendererInfo(rendererInfo: AudioRendererInfo): AudioDeviceDescriptors
```

**功能：** 根据音频信息，返回优先级最高的输出设备，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|rendererInfo|[AudioRendererInfo](#class-audiorendererinfo)|是|-|表示渲染器信息。|

**返回值：**

|类型|说明|
|:----|:----|
|[AudioDeviceDescriptors](#type-audiodevicedescriptors)|返回优先级最高的输出设备信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800301|System error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

try {
    let rendererInfo: AudioRendererInfo = AudioRendererInfo(StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, 0)
    let routingMgr: AudioRoutingManager = getAudioManager().getRoutingManager()
    let descs: AudioDeviceDescriptors = routingMgr.getPreferredOutputDeviceForRendererInfo(rendererInfo)
    for (desc in descs) {
        let addr = desc.address
        let chCnts = desc.channelCounts
        let chMask = desc.channelMasks
        let devRole = desc.deviceRole
        let devType = desc.deviceType
        let dispName = desc.displayName
        let encType = desc.encodingTypes
        let id = desc.id
        let name = desc.name
        let sampleRate = desc.sampleRates
        Hilog.info(0, "desc.displayName", "desc.displayName: ${dispName}")
    }
} catch (e: BusinessException) {
    Hilog.error(0, "getPreferredOutputDeviceForRendererInfo", "errCode: ${e.code}, errMessage: ${e.message}")
}
```