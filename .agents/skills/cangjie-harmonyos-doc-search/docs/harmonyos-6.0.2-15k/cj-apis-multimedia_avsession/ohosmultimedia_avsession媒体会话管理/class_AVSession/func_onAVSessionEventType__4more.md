### func on(AVSessionEventType, Callback1Argument\<KeyEvent>)

```cangjie
public func on(eventType: AVSessionEventType, callback: Callback1Argument<KeyEvent>): Unit
```

**功能：** 订阅会话监听事件，事件发生时触发回调函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionEventType](#enum-avsessioneventtype)|是|-|监听事件，支持HandleKeyEvent。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[KeyEvent](../InputKit/cj-apis-multimodalInput-keyEvent.md#class-keyevent)>|是|-|入参为[KeyEvent](../InputKit/cj-apis-multimodalInput-keyEvent.md#class-keyevent)的回调函数，事件与回调的关联详见[AVSessionEventType](#enum-avsessioneventtype)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func setAVCallState(AVCallState)

```cangjie
public func setAVCallState(state: AVCallState): Unit
```

**功能：** 设置通话状态。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|state|[AVCallState](#class-avcallstate)|是|-|通话状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func setAVMetadata(AVMetadata)

```cangjie
public func setAVMetadata(data: AVMetadata): Unit
```

**功能：** 设置会话元数据。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|[AVMetadata](#class-avmetadata)|是|-|会话元数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func setAVPlaybackState(AVPlaybackState)

```cangjie
public func setAVPlaybackState(state: AVPlaybackState): Unit
```

**功能：** 设置会话播放状态。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|state|[AVPlaybackState](#class-avplaybackstate)|是|-|会话播放状态，包括状态、倍数、循环模式等信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|