## class AudioHapticManager

```cangjie
public class AudioHapticManager {}
```

**功能：** 管理音振协同功能。在调用[AudioHapticManager](#class-audiohapticmanager)的接口前，需要先通过[getAudioHapticManager](#func-getaudiohapticmanager)创建实例。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

### func createPlayer(Int32, AudioHapticPlayerOptions)

```cangjie
public func createPlayer(
    id: Int32,
    options!: AudioHapticPlayerOptions = AudioHapticPlayerOptions()
): AudioHapticPlayer
```

**功能：** 创建音振播放器。

如果应用创建的AudioHapticPlayer需要触发振动，则需要校验应用是否拥有该权限。

**需要权限：** ohos.permission.VIBRATE

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int32|是|-|已注册资源的source id。|
|options|[AudioHapticPlayerOptions](#class-audiohapticplayeroptions)|否|AudioHapticPlayerOptions()| **命名参数。** 音振播放器选项。不传时options中选项都为false。|

**返回值：**

|类型|说明|
|:----|:----|
|[AudioHapticPlayer](#class-audiohapticplayer)|创建的音振播放器。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |201|Permission denied.|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|
  |5400102|Operation not allowed.|
  |5400103|I/O error.|
  |5400106|Unsupport format.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*

let audiohapticmanager = getAudioHapticManager()
let id = audiohapticmanager.registerSource("/data/11.wav", "/data/11.json")
let player = audiohapticmanager.createPlayer(id)
```

### func registerSource(String, String)

```cangjie
public func registerSource(audioUri: String, hapticUri: String): Int32
```

**功能：** 注册音频和振动资源的Uri。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|audioUri|String|是|-|音频资源的Uri。对普通时延模式，音频资源格式和路径格式的支持可参考[media.AVPlayer](../MediaKit/cj-apis-multimedia_media.md#class-avplayer)；对低时延模式，音频资源格式支持可参考[SoundPool](../MediaKit/cj-apis-multimedia_media.md#class-soundpool)，路径格式需满足[文件管理模块open函数](../CoreFileKit/cj-apis-file_fs.md#static-func-openstring-int64)的要求。对两种时延模式，均建议传入文件的绝对路径。|
|hapticUri|String|是|-|振动资源的Uri。振动资源格式支持可参考[vibrator](../SensorServiceKit/cj-apis-vibrator.md)，路径格式需满足[文件管理模块open函数](../CoreFileKit/cj-apis-file_fs.md#static-func-openstring-int64)的要求。建议传入文件的绝对路径。|

**返回值：**

|类型|说明|
|:----|:----|
|Int32|注册资源的source id。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*

let audiohapticmanager = getAudioHapticManager()
let id = audiohapticmanager.registerSource("/data/11.wav", "/data/11.json")
```