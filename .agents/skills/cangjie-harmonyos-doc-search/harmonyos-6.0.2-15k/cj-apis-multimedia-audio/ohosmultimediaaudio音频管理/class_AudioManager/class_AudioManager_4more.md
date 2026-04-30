## class AudioManager

```cangjie
public class AudioManager {}
```

**功能：** 管理音频音量和音频设备。在调用[AudioManager](#class-audiomanager)的接口前，需要先通过[getAudioManager](#func-getaudiomanager)创建实例。

**需要权限：** ohos.permission.MODIFY_AUDIO_SETTINGS

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

### func getAudioScene()

```cangjie
public func getAudioScene(): AudioScene
```

**功能：** 获取音频场景模式。

**系统能力：** SystemCapability.Multimedia.Audio.Communication

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioScene](#enum-audioscene)|返回音频场景模式。|

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
    let instance = getAudioManager()
    let sen = instance.getAudioScene()
} catch (e: BusinessException) {
    Hilog.error(0, "getAudioScene", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getRoutingManager()

```cangjie
public func getRoutingManager(): AudioRoutingManager
```

**功能：** 获取音频会话管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AudioRoutingManager](#class-audioroutingmanager)|[AudioRoutingManager](#class-audioroutingmanager)实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Audio错误码](../../errorcodes/cj-errorcode-multimedia-audio.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6800301|Create AudioRoutingManager failed.|

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
} catch (e: BusinessException) {
    Hilog.error(0, "getRoutingManager", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func getSessionManager()

```cangjie
public func getSessionManager(): AudioSessionManager
```

**功能：** 获取音频会话管理器。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[AudioSessionManager](#class-audiosessionmanager)|[AudioSessionManager](#class-audiosessionmanager)实例。|

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
    let smgr = instance.getSessionManager()
} catch (e: BusinessException) {
    Hilog.error(0, "getSessionManager()", "errCode: ${e.code}, errMessage: ${e.message}")
}
```