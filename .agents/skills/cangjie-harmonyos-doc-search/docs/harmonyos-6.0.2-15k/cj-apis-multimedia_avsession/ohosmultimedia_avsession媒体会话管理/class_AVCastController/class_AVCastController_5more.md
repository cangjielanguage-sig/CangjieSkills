## class AVCastController

```cangjie
public class AVCastController {}
```

**功能：** 在投播建立后，调用[getAVCastController](#func-getavcastcontroller)后，返回会话控制器实例。控制器可查看会话ID，并可完成对会话发送命令及事件，获取会话元数据，播放状态信息等操作。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

### func getAVPlaybackState()

```cangjie
public func getAVPlaybackState(): AVPlaybackState
```

**功能：** 获取当前的远端播放状态。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVPlaybackState](#class-avplaybackstate)|返回远端播放状态。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|

### func getCurrentItem()

```cangjie
public func getCurrentItem(): AVQueueItem
```

**功能：** 获取当前投播的资源信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVQueueItem](#class-avqueueitem)|播放列表中单项的相关属性。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600109|The remote connection is not established.|

### func getValidCommands()

```cangjie
public func getValidCommands(): Array<AVCastControlCommandType>
```

**功能：** 获取当前支持的命令。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[AVCastControlCommandType](#enum-avcastcontrolcommandtype)>|返回当前支持的命令。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|

### func off(AVCastControllerEventType, ?Callback1Argument\<AVPlaybackState>)

```cangjie
public func off(`type`: AVCastControllerEventType, callback!: ?Callback1Argument<AVPlaybackState> = None): Unit
```

**功能：** 取消订阅监听事件的注册函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVCastControllerEventType](#enum-avcastcontrollereventtype)|是|-|监听事件，支持CAST_CONTROLLER_PLAYBACK_STATE_CHANGE。|
|callback|?[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[AVPlaybackState](#class-avplaybackstate)>|否|None| **命名参数。** 已注册的回调函数，未填则取消该事件下所有已注册的回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|