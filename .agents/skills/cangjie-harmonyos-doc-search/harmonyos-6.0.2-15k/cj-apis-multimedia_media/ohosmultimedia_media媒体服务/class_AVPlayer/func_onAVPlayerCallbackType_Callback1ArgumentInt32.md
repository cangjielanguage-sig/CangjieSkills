### func on(AVPlayerCallbackType, Callback1Argument\<Int32>)

```cangjie
public func on(`type`: AVPlayerCallbackType, callback: Callback1Argument<Int32>): Unit
```

**功能：** 订阅[SeekDone](#seekdone)，[SpeedDone](#speeddone)，[BitrateDone](#bitratedone)，[TimeUpdate](#timeupdate)，[DurationUpdate](#durationupdate)事件的回调函数。

**系统能力：** SystemCapability.Multimedia.Media.AVPlayer

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVPlayerCallbackType](#enum-avplayercallbacktype)|是|-|事件：[SeekDone](#seekdone)。[seek](#func-seekint32-seekmode)生效的事件回调类型，每次调用[seek](#func-seekint32-seekmode)后都会回调此事件。<br/>事件：[SpeedDone](#speeddone)。[setSpeed](#func-setspeedplaybackspeed)生效的事件回调类型，每次调用[setSpeed](#func-setspeedplaybackspeed)后都会回调此事件。<br/>事件：[BitrateDone](#bitratedone)。[setBitrate](#func-setbitrateint32)生效的事件回调类型，每次调用[setBitrate](#func-setbitrateint32)后都会回调此事件。<br/>事件：[TimeUpdate](#timeupdate)。时间更新的回调类型，监听资源播放当前时间，单位为毫秒（ms），用于刷新进度条当前位置，默认间隔100ms时间上报，因用户操作(seek)产生的时间变化会立刻上报。**直播场景不支持timeUpdate上报**。<br/>事件：[DurationUpdate](#durationupdate)。时长更新的回调类型，监听资源播放资源的时长，单位为毫秒（ms），用于刷新进度条长度，默认只在prepared上报一次，同时允许一些特殊码流刷新多次时长。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Int32>|是|-|回调函数。seek生效的事件回调方法，只会上报用户请求的time位置。<br/>**视频播放：**[SeekMode](#enum-seekmode)会造成实际跳转位置与用户设置产生偏差，精准位置需要通过currentTime获取，事件回调的time仅代表完成用户某一次请求。|

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
class SeekDoneCb <: Callback1Argument<Int32> {
    public init() {}
    public open func invoke(e: Int32): Unit {
        AppLog.error("SeekDoneCb: ${e}")
    }
}

let callback = SeekDoneCb()
let player = createAVPlayer()
player.on(AVPlayerCallbackType.SeekDone, callback)
```