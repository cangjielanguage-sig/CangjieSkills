## class NativeMediaPlayerBridge

```cangjie
public abstract class NativeMediaPlayerBridge {
    public init()
}
```

**功能：** [CreateNativeMediaPlayerCallback](#type-createnativemediaplayercallback)回调函数的返回值类型。接管网页媒体的播放器和ArkWeb内核之间的一个接口类。ArkWeb内核通过该接口类的实例对象来控制应用创建的用来接管网页媒体的播放器。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** 构造一个NativeMediaPlayerBridge对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func enterFullscreen()

```cangjie
public open func enterFullscreen(): Unit
```

**功能：** 播放器进入全屏。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func exitFullscreen()

```cangjie
public open func exitFullscreen(): Unit
```

**功能：** 播放器退出全屏。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func pause()

```cangjie
public open func pause(): Unit
```

**功能：** 暂停播放。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Webview错误码](../../errorcodes/cj-errorcode-webview.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |17100019|The download task is not started yet.|

### func play()

```cangjie
public open func play(): Unit
```

**功能：** 播放视频。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func release()

```cangjie
public open func release(): Unit
```

**功能：** 释放播放器。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func resumePlayer()

```cangjie
public open func resumePlayer(): Unit
```

**功能：** 通知应用重建应用内播放器，并恢复应用内播放器的状态信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func seek(Float64)

```cangjie
public open func seek(targetTime: Float64): Unit
```

**功能：** 播放器跳转到某个时间点。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|targetTime|Float64|是|-|单位：秒。|

### func setMuted(Bool)

```cangjie
public open func setMuted(muted: Bool): Unit
```

**功能：** 设置静音状态。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|muted|Bool|是|-|是否静音。|

### func setPlaybackRate(Float64)

```cangjie
public open func setPlaybackRate(playbackRate: Float64): Unit
```

**功能：** 设置播放速率。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|playbackRate|Float64|是|-|播放速率。取值范围是\[0.0, 10.0]。其中 1.0 表示原速播放。|

### func setVolume(Float64)

```cangjie
public open func setVolume(volume: Float64): Unit
```

**功能：** 设置播放器音量。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|volume|Float64|是|-|播放器的音量。取值范围是\[0.0, 1.0]。其中 0.0 表示静音， 1.0 表示最大音量。|

### func suspendPlayer(SuspendType)

```cangjie
public open func suspendPlayer(`type`: SuspendType): Unit
```

**功能：** 通知应用挂起应用内播放器，并保存应用内播放器的状态信息。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type`|[SuspendType](#enum-suspendtype)|是|-|播放器挂起类型。|