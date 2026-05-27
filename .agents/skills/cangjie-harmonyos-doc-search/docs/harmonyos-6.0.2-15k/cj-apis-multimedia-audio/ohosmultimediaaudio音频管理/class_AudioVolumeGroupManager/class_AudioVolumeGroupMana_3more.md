## class AudioVolumeGroupManager

```cangjie
public class AudioVolumeGroupManager {}
```

**功能：** 获取指定流的音量，使用callback方式异步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

### func getMaxAmplitudeForInputDevice(AudioDeviceDescriptor)

```cangjie
public func getMaxAmplitudeForInputDevice(device: AudioDeviceDescriptor): Float32
```

**功能：** 获取指定流的最大音量，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|device|[AudioDeviceDescriptor](#class-audiodevicedescriptor)|是|-|描述音频设备。|

**返回值：**

|类型|说明|
|:----|:----|
|Float32|输入设备音频流的最大电平值，大小取值在0-1之间。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800101|Invalid parameter.|
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
    let LOCAL_VOLUME_GROUP_ID: Int32 = 1
    let rendererInfo: AudioRendererInfo = AudioRendererInfo(StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, 0)
    let routingMgr: AudioRoutingManager = getAudioManager().getRoutingManager()
    let descs: AudioDeviceDescriptors = routingMgr.getPreferredOutputDeviceForRendererInfo(rendererInfo)
    let audioVolGrpMgr: AudioVolumeGroupManager = getAudioManager().getVolumeManager().getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
    let maxAmp: Float32 = audioVolGrpMgr.getMaxAmplitudeForInputDevice(descs[0])
} catch (e: BusinessException) {
    Hilog.error(0, "getMaxAmplitudeForInputDevice", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getMaxAmplitudeForOutputDevice(AudioDeviceDescriptor)

```cangjie
public func getMaxAmplitudeForOutputDevice(device: AudioDeviceDescriptor): Float32
```

**功能：** 获取指定流的最大音量，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|device|[AudioDeviceDescriptor](#class-audiodevicedescriptor)|是|-|描述音频设备。|

**返回值：**

|类型|说明|
|:----|:----|
|Float32|输入设备音频流的最大电平值，大小取值在0-1之间。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800101|Invalid parameter.|
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
    let LOCAL_VOLUME_GROUP_ID: Int32 = 1
    let rendererInfo: AudioRendererInfo = AudioRendererInfo(StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, 0)
    let routingMgr: AudioRoutingManager = getAudioManager().getRoutingManager()
    let descs: AudioDeviceDescriptors = routingMgr.getPreferredOutputDeviceForRendererInfo(rendererInfo)
    let audioVolGrpMgr: AudioVolumeGroupManager = getAudioManager().getVolumeManager().getVolumeGroupManager(LOCAL_VOLUME_GROUP_ID)
    let maxAmp: Float32 = audioVolGrpMgr.getMaxAmplitudeForOutputDevice(descs[0])
} catch (e: BusinessException) {
    Hilog.error(0, "getMaxAmplitudeForInputDevice", "errCode: ${e.code}, errMessage: ${e.message}")
}
```