### func stop()

```cangjie
public func stop(): Unit
```

**功能：** 停止播放。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operate not permit.|
  |5400105|Service died.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*

let audiohapticmanager = getAudioHapticManager()
let id = audiohapticmanager.registerSource("/data/11.wav", "/data/11.json")
let player = audiohapticmanager.createPlayer(id)
player.isMuted(AudioHapticType.AUDIO_HAPTIC_TYPE_HAPTIC)
```