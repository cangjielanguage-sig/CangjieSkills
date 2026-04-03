## class AVSessionController

```cangjie
public class AVSessionController {}
```

**功能：** [AVSessionController](#class-avsessioncontroller)控制器可查看会话ID，并可完成对会话发送命令及事件，获取会话元数据，播放状态信息等操作。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

### prop sessionId

```cangjie
public prop sessionId: String
```

**功能：** [AVSessionController](#class-avsessioncontroller)对象唯一的会话标识。

**类型：** String

**读写能力：** 只读

**起始版本：** 19

### func destroy()

```cangjie
public func destroy(): Unit
```

**功能：** 销毁当前控制器，销毁后当前控制器不可再用。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600103|The session controller does not exist.|

### func getAVCallState()

```cangjie
public func getAVCallState(): AVCallState
```

**功能：** 获取通话状态数据。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVCallState](#class-avcallstate)|通话状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|

### func getAVMetadata()

```cangjie
public func getAVMetadata(): AVMetadata
```

**功能：** 获取会话元数据。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVMetadata](#class-avmetadata)|会话元数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|

### func getAVPlaybackState()

```cangjie
public func getAVPlaybackState(): AVPlaybackState
```

**功能：** 获取当前会话的播放状态。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVPlaybackState](#class-avplaybackstate)|当前会话的播放状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|

### func getAVQueueItems()

```cangjie
public func getAVQueueItems(): Array<AVQueueItem>
```

**功能：** 获取当前会话播放列表相关信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[AVQueueItem](#class-avqueueitem)>|当前会话播放列表队列。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|