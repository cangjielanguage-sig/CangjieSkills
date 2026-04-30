## class NativeMediaPlayerHandler

```cangjie
public class NativeMediaPlayerHandler  {
    public init()
}
```

**功能：** [CreateNativeMediaPlayerCallback](#type-createnativemediaplayercallback)回调函数的参数。应用通过该对象将播放器的状态报告给ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### init()

```cangjie
public init()
```

**功能：** 构造WebviewController对象。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func handleBufferedEndTimeChanged(Float64)

```cangjie
public func handleBufferedEndTimeChanged(bufferedEndTime: Float64): Unit
```

**功能：** 当媒体的缓冲时长发生变化时，调用该方法将媒体的缓冲时长通知给ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bufferedEndTime|Float64|是|-|媒体的缓冲时长。|

### func handleDurationChanged(Float64)

```cangjie
public func handleDurationChanged(duration: Float64) : Unit
```

**功能：** 当播放器解析出媒体的总时长时，调用该方法将媒体的总时长通知给ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|duration|Float64|是|-|媒体的总时长。单位：秒 。|

### func handleEnded()

```cangjie
public func handleEnded(): Unit
```

**功能：** 当媒体播放结束时，调用该方法通知给ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

### func handleError(MediaError, String)

```cangjie
public func handleError(error: MediaError, errorMessage: String): Unit
```

**功能：** 当播放器发生错误时，调用该方法通知ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|error|[MediaError](#enum-mediaerror)|是|-|错误类型。|
|errorMessage|String|是|-|错误的详细描述。|

### func handleFullscreenChanged(Bool)

```cangjie
public func handleFullscreenChanged(fullscreen: Bool): Unit
```

**功能：** 当播放器的全屏状态发生变化时，调用该方法将播放器的全屏状态通知给ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fullscreen|Bool|是|-|是否全屏。|

### func handleMutedChanged(Bool)

```cangjie
public func handleMutedChanged(muted: Bool) : Unit
```

**功能：** 当播放器的静音状态发生变化时，调用该方法将静音状态通知给ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|muted|Bool|是|-|当前播放器是否静音。|

### func handleNetworkStateChanged(NetworkState)

```cangjie
public func handleNetworkStateChanged(state: NetworkState): Unit
```

**功能：** 当播放器的网络状态发生变化时，调用该方法将播放器的网络状态通知给ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|state|[NetworkState](#enum-networkstate)|是|-|播放器的网络状态。|

### func handlePlaybackRateChanged(Float64)

```cangjie
public func handlePlaybackRateChanged(playbackRate: Float64): Unit
```

**功能：** 当播放器的播放速率发生变化时，调用该方法将播放速度通知给ArkWeb内核。

**系统能力：** SystemCapability.Web.Webview.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|playbackRate|Float64|是|-|播放速率。|