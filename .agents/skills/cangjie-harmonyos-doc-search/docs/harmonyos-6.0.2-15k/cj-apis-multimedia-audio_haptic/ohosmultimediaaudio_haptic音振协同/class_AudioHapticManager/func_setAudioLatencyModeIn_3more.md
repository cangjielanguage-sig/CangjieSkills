### func setAudioLatencyMode(Int32, AudioLatencyMode)

```cangjie
public func setAudioLatencyMode(id: Int32, latencyMode: AudioLatencyMode): Unit
```

**功能：** 设置音频时延模式。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int32|是|-|已注册资源的source id。|
|latencyMode|[AudioLatencyMode](#enum-audiolatencymode)|是|-|音频时延模式。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types.|
  |5400102|Operation not allowed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*

let audiohapticmanager = getAudioHapticManager()
let id = audiohapticmanager.registerSource("/data/11.wav", "/data/11.json")
audiohapticmanager.setAudioLatencyMode(id, AudioLatencyMode.AUDIO_LATENCY_MODE_FAST)
```

### func setStreamUsage(Int32, StreamUsage)

```cangjie
public func setStreamUsage(id: Int32, usage: StreamUsage): Unit
```

**功能：** 设置音频流使用类型。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int32|是|-|已注册资源的source id。|
|usage|[StreamUsage](cj-apis-multimedia-audio.md#enum-streamusage)|是|-|音频流使用类型。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed.|
  |5400102|Operation not allowed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AudioKit.*

let audiohapticmanager = getAudioHapticManager()
let id = audiohapticmanager.registerSource("/data/11.wav", "/data/11.json")
audiohapticmanager.setStreamUsage(id, StreamUsage.STREAM_USAGE_ALARM)
```

### func unregisterSource(Int32)

```cangjie
public func unregisterSource(id: Int32): Unit
```

**功能：** 取消注册音频和振动资源。

**系统能力：** SystemCapability.Multimedia.AudioHaptic.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|id|Int32|是|-|已注册资源的source id。|

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
audiohapticmanager.unregisterSource(id)
```