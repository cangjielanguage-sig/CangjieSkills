### func handleReadyStateChanged(ReadyState)

```cangjie
public func handleReadyStateChanged(state: ReadyState): Unit
```

**功能：** 当播放器的缓存状态发生变化时，调用该方法将播放器的缓存状态通知给ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|state|[ReadyState](#enum-readystate)|是|-|播放器的缓存状态。|

### func handleSeekFinished()

```cangjie
public func handleSeekFinished(): Unit
```

**功能：** 当播放器seek完成后，调用该方法通知ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func handleSeeking()

```cangjie
public func handleSeeking(): Unit
```

**功能：** 当播放器进入seek状态时，调用该方法通知ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func handleStatusChanged(PlaybackStatus)

```cangjie
public func handleStatusChanged(status: PlaybackStatus): Unit
```

**功能：** 当播放器的播放状态发生变化时，调用该方法将播放状态通知给ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|status|[PlaybackStatus](#enum-playbackstatus)|是|-|播放器的播放状态。|

### func handleTimeUpdate(Float64)

```cangjie
public func handleTimeUpdate(currentPlayTime: Float64) : Unit
```

**功能：** 当媒体的播放进度发生变化时，调用该方法将媒体的播放进度通知给ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|currentPlayTime|Float64|是|-|当前播放时间。单位：秒。|

### func handleVideoSizeChanged(Float64, Float64)

```cangjie
public func handleVideoSizeChanged(width: Float64, height: Float64): Unit
```

**功能：** 当播放器解析出视频的尺寸时，调用该方法通知ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|width|Float64|是|-|视频的宽。|
|height|Float64|是|-|视频的高。|

### func handleVolumeChanged(Float64)

```cangjie
public func handleVolumeChanged(volume: Float64) : Unit
```

**功能：** 当播放器的音量发生变化时，调用该方法将音量通知给ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|volume|Float64|是|-|播放器的音量。|