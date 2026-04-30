## class AudioRoutingManager

```cangjie
public class AudioRoutingManager {}
```

**功能：** 音频路由管理。在使用AudioRoutingManager的接口前，需要使用[getRoutingManager](#func-getroutingmanager)获取[AudioRoutingManager](#class-audioroutingmanager)实例。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

### func getAvailableDevices(DeviceUsage)

```cangjie
public func getAvailableDevices(deviceUsage: DeviceUsage): AudioDeviceDescriptors
```

**功能：** 获取音频可选设备列表，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceUsage|[DeviceUsage](#enum-deviceusage)|是|-|设备的usage。|

**返回值：**

|类型|说明|
|:----|:----|
|[AudioDeviceDescriptors](#type-audiodevicedescriptors)|返回设备列表。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800102|Memory allocation failure.|
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
    let instance = getAudioManager()
    let routingmgr = instance.getRoutingManager()
    let devices = routingmgr.getAvailableDevices(DeviceFlag.OUTPUT_DEVICES_FLAG)
} catch (e: BusinessException) {
    Hilog.error(0, "getAvailableDevices", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getDevices(DeviceFlag)

```cangjie
public func getDevices(deviceFlag: DeviceFlag): AudioDeviceDescriptors
```

**功能：** 获取音频设备列表，同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Device

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|deviceFlag|[DeviceFlag](#enum-deviceflag)|是|-|设备类型的flag。|

**返回值：**

|类型|说明|
|:----|:----|
|[AudioDeviceDescriptors](#type-audiodevicedescriptors)|返回设备列表。|

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
    let devices = routingmgr.getDevices(DeviceFlag.OUTPUT_DEVICES_FLAG)
} catch (e: BusinessException) {
    Hilog.error(0, "getDevices", "errCode: ${e.code}, errMessage: ${e.message}")
}
```