### func getStreamManager()

```cangjie
public func getStreamManager(): AudioStreamManager
```

**功能：** 获取音频流管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioStreamManager](#class-audiostreammanager)|[AudioStreamManager](#class-audiostreammanager)实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800301|Create AudioStreamManager failed.|

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
    let smgr = instance.getStreamManager()
} catch (e: BusinessException) {
    Hilog.error(0, "getStreamManager", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getVolumeManager()

```cangjie
public func getVolumeManager(): AudioVolumeManager
```

**功能：** 获取音频音量管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioVolumeManager](#class-audiovolumemanager)|[AudioVolumeManager](#class-audiovolumemanager)实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800301|Create AudioVolumeManager failed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*
import kit.BasicServicesKit.*
import ohos.hilog.*

try {
    let audioMgr: AudioManager = getAudioManager()
    let audioVolMgr: AudioVolumeManager = audioMgr.getVolumeManager()
} catch (e: BusinessException) {
    Hilog.error(0, "AudioVolumeManager", "errCode: ${e.code}, errMessage: ${e.message}")
}
```