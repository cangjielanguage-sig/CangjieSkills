### prop videoScaleType

```cangjie
public mut prop videoScaleType: VideoScaleType
```

**功能：** 视频缩放模式，默认VIDEO_SCALE_TYPE_FIT，动态属性。<br/>只允许在**prepared**/**playing**/**paused**/**completed**状态下设置。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** [VideoScaleType](#enum-videoscaletype)

**读写能力：** 可读写

**起始版本：** 19

### prop width

```cangjie
public prop width: Int32
```

**功能：** 视频宽，单位为像素（px），可查询参数。<br/>返回为(0)表示无效值，**prepared**/**playing**/**paused**/**completed**状态下有效。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**类型：** Int32

**读写能力：** 只读

**起始版本：** 19

### func addSubtitleFromFd(Int32, Int64, Int64)

```cangjie
public func addSubtitleFromFd(fd: Int32, offset!: Int64 = 0, length!: Int64 = 0): Unit
```

**功能：** 依据fd为视频添加外挂字幕，当前仅支持与视频资源同时设置（在avplayer设置fdSrc视频资源后设置外挂字幕）。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|fd|Int32|是|-|资源句柄，通过[resourceManager.getRawFd](../LocalizationKit/cj-apis-resource_manager.md#func-getrawfdstring)获取。|
|offset|Int64|否|0| **命名参数。** 资源偏移量，需要基于预置资源的信息输入，非法值会造成字幕频资源解析错误。|
|length|Int64|否|0| **命名参数。** 资源长度，默认值为文件中从偏移量开始的剩余字节，需要基于预置资源的信息输入，非法值会造成字幕频资源解析错误。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|The parameter check failed.|
  |5400102|Operation not allowed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.*

let abilityContext = Global.abilityContext // 需获取Context应用上下文，详见本文使用说明
let resMgr = abilityContext.resourceManager
let fileDescriptor = resMgr.getRawFd('xxx.srt')
let player = createAVPlayer()
player.addSubtitleFromFd(fileDescriptor.fd, offset: fileDescriptor.offset,
    length: fileDescriptor.length)
```

### func addSubtitleFromUrl(String)

```cangjie
public func addSubtitleFromUrl(url: String): Unit
```

**功能：** 依据url为视频添加外挂字幕，当前仅支持与视频资源同时设置（在avplayer设置fdSrc视频资源后设置外挂字幕）。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|url|String|是|-|外挂字幕文件地址。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|The parameter check failed.|
  |5400102|Operation not allowed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*

let fdUrl = "http://xxx.xxx.xxx/xx/index.srt"
let player = createAVPlayer()
player.addSubtitleFromUrl(fdUrl)
```