### func getRealPlaybackPosition()

```cangjie
public func getRealPlaybackPosition(): Int64
```

**功能：** 获取当前播放位置。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Int64|时间节点，毫秒数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600103|The session controller does not exist.|

### func getValidCommands()

```cangjie
public func getValidCommands(): Array<AVControlCommandType>
```

**功能：** 获取会话支持的有效命令。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[AVControlCommandType](#enum-avcontrolcommandtype)>|返回有效命令的集合。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|

### func isActive()

```cangjie
public func isActive(): Bool
```

**功能：** 获取会话是否被激活。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|是否为激活状态，true表示被激活，false表示禁用。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|

### func off(AVSessionControllerEventType, ?CallbackObject)

```cangjie
public func off(eventType: AVSessionControllerEventType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅监听事件的注册函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionControllerEventType](#enum-avsessioncontrollereventtype)|是|-|监听事件。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 已注册的回调函数，未填则取消该事件下所有已注册的回调函数。|