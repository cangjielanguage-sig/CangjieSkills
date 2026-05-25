### func setMediaMuted(MediaType, Bool)

```cangjie
public func setMediaMuted(mediaType: MediaType, muted: Bool): Unit
```

**功能：** 设置音频静音/取消音频静音。只能在prepared/playing/paused/completed状态下调用。仅支持设置mediaType为音频格式。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|mediaType|[MediaType](#enum-mediatype)|是|-|播放策略。|
|muted|Bool|是|-|是否静音播放。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |5400102|Operation not allowed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

let player = createAVPlayer()
try {
    player.prepare()
    player.setMediaMuted(MediaType.MEDIA_TYPE_AUD, true)
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

### func setMediaSource(MediaSource, ?PlaybackStrategy)

```cangjie
public func setMediaSource(src: MediaSource, strategy!: ?PlaybackStrategy = None): Unit
```

**功能：** 流媒体预下载资源设置，下载url对应的流媒体数据，并暂存在内存中。注意：此接口的异常并不直接抛出，而是在[监听AVPlayer的错误事件](#func-onavplayercallbacktype-callback1argumentbusinessexception)中给出。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|src|[MediaSource](#class-mediasource)|是|-|流媒体预下载媒体来源。|
|strategy|?[PlaybackStrategy](#class-playbackstrategy)|否|None| **命名参数。** 流媒体预下载播放策略。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |5400102|Operation not allowed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import std.collection.HashMap

let player = createAVPlayer()
let headers = HashMap<String, String>()
headers.add("User-Agent", "User-Agent-Value")
let mediaSource = createMediaSourceWithUrl("http://xxx", headers: headers)
let playbackStrategy = PlaybackStrategy(preferredWidth: 1, preferredHeight: 2,
    preferredBufferDuration: 3, preferredHdr: false)
player.setMediaSource(mediaSource, strategy: playbackStrategy)
```