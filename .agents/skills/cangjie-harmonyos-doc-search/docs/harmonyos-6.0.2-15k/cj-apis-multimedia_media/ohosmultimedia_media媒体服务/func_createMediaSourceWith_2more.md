## func createMediaSourceWithUrl(String, HashMap\<String, String>)

```cangjie
public func createMediaSourceWithUrl(url: String, headers!: HashMap<String, String> = HashMap<String, String>()): MediaSource
```

**功能：** 创建流媒体预下载媒体来源实例方法。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|- 流媒体预下载媒体来源url，支持的流媒体格式：HLS、HTTP-FLV、Dash、Https。<br> - 本地m3u8的fd路径。|
|headers|HashMap\<String, String>|否|HashMap\<String, String>()| **命名参数。** 支持流媒体预下载HttpHeader自定义。|

**返回值：**

|类型|说明|
|:----|:----|
|[MediaSource](#class-mediasource)|媒体数据信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed.|
  |5400101|No memory.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import std.collection.HashMap

let headers = HashMap<String, String>()
headers.add("User-Agent", "User-Agent-Value")
let mediaSource: MediaSource = createMediaSourceWithUrl("http://xxx", headers: headers)
```

## func createSoundPool(Int32, AudioRendererInfo)

```cangjie
public func createSoundPool(maxStreams: Int32, audioRenderInfo: AudioRendererInfo): ?SoundPool
```

**功能：** 创建音频池实例。

**系统能力：** SystemCapability.Multimedia.Media.SoundPool

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|maxStreams|Int32|是|-|soundPool实例的最大播放的流数。|
|audioRenderInfo|[AudioRendererInfo](../AudioKit/cj-apis-multimedia-audio.md#class-audiorendererinfo)|是|-|音频播放参数信息。其中audioRenderInfo中的参数usage取值为STREAM_USAGE_UNKNOWN，STREAM_USAGE_MUSIC，STREAM_USAGE_MOVIE，STREAM_USAGE_AUDIOBOOK时，SoundPool播放短音时为混音模式，不会打断其他音频播放。|

**返回值：**

|类型|说明|
|:----|:----|
|?[SoundPool](#class-soundpool)|返回SoundPool实例，失败时返回None。用于音频池实例的加载播放功能。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400101|No memory.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import kit.AudioKit.*

let audioRendererInfo: AudioRendererInfo = AudioRendererInfo(STREAM_USAGE_MUSIC, 0)
let soundpool = createSoundPool(5, audioRendererInfo)
```