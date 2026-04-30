### func on(AVPlayerCallbackType, Callback1Argument\<Array\<Float32>>)

```cangjie
public func on(`type`: AVPlayerCallbackType, callback: Callback1Argument<Array<Float32>>): Unit
```

**功能：** 订阅音频最大电平值，音频资源播放时定时上报。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVPlayerCallbackType](#enum-avplayercallbacktype)|是|-|事件回调类型，支持的事件为：[AmplitudeUpdate](#amplitudeupdate)。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<Float32>>|是|-|音频最大电平值更新事件回调方法。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.MediaKit.*
import ohos.base.*

// 此处代码可添加在依赖项定义中
class AmplitudeUpdateCallback <: Callback1Argument<Array<Float32>> {
    public init() {}
    public open func invoke(value: Array<Float32>): Unit {
        AppLog.info("amplitudeUpdate = ${value}")
    }
}

let callback = AmplitudeUpdateCallback()
let player = createAVPlayer()
player.on(AVPlayerCallbackType.AmplitudeUpdate, callback)
```

### func pause()

```cangjie
public func pause(): Unit
```

**功能：** 暂停播放音视频资源，只能在playing状态调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operation not allowed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

let player = createAVPlayer()
try {
    player.pause()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

### func play()

```cangjie
public func play(): Unit
```

**功能：** 开始播放音视频资源，只能在prepared/paused/completed状态调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operation not allowed.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

let player = createAVPlayer()
try {
    player.play()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```

### func prepare()

```cangjie
public func prepare(): Unit
```

**功能：** 准备播放音频/视频，需在[StateChange](#func-onavplayercallbacktype-onavplayerstatechangehandle)事件成功触发至initialized状态后，才能调用。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[Media错误码](../../errorcodes/cj-errorcode-multimedia-media.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |5400102|Operation not allowed.|
  |5400106|Unsupported format.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.MediaKit.*

let player = createAVPlayer()
try {
    player.prepare()
} catch (e: BusinessException) {
    AppLog.error(e.message)
}
```