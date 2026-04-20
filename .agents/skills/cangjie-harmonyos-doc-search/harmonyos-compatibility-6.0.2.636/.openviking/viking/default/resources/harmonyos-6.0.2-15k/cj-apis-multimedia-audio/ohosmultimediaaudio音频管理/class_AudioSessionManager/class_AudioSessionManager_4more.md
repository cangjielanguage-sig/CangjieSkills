## class AudioSessionManager

```cangjie
public class AudioSessionManager {}
```

**功能：** 音频会话管理。在使用[AudioSessionManager](#class-audiosessionmanager)的API前，需要使用[getSessionManager](#func-getsessionmanager)获取[AudioSessionManager](#class-audiosessionmanager)实例。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

### func activateAudioSession(AudioSessionStrategy)

```cangjie
public func activateAudioSession(strategy: AudioSessionStrategy): Unit
```

**功能：** 激活音频会话。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|strategy|[AudioSessionStrategy](#class-audiosessionstrategy)|是|-|音频会话策略。|

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
    let smgr = instance.getSessionManager()
    let strategy = AudioSessionStrategy(AudioConcurrencyMode.CONCURRENCY_DEFAULT)
    smgr.activateAudioSession(strategy)
} catch (e: BusinessException) {
    Hilog.error(0, "activateAudioSession", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func deactivateAudioSession()

```cangjie
public func deactivateAudioSession(): Unit
```

**功能：** 停用音频会话。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

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
    let smgr = instance.getSessionManager()
    let strategy = AudioSessionStrategy(AudioConcurrencyMode.CONCURRENCY_DEFAULT)
    smgr.avtivateAudioSession(strategy)
    smgr.deactivateAudioSession()
} catch (e: BusinessException) {
    Hilog.error(0, "deavtivateAudioSession", "errCode: ${e.code}, errMessage: ${e.message}")
}
```

### func isAudioSessionActivated(): Bool

```cangjie
public func isAudioSessionActivated(): Bool
```

**功能：** 检查音频会话是否已激活，返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|Bool|返回当前pid应用程序的音频会话是否已激活，true表示已激活，false表示已停用。|

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
    let ret = smgr.isAudioSessionActivated()
} catch (e: BusinessException) {
    Hilog.error(0, "isAudioSessionActivated", "errCode: ${e.code}, errMessage: ${e.message}")
}
```