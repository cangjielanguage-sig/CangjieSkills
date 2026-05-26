### func sendAVKeyEvent(KeyEvent)

```cangjie
public func sendAVKeyEvent(event: KeyEvent): Unit
```

**功能：** 发送按键事件到控制器对应的会话。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|event|[KeyEvent](../InputKit/cj-apis-multimodalInput-keyEvent.md#class-keyevent)|是|-|按键事件。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|
  |6600105|Invalid session command.|
  |6600106|The session is not activated.|

### func sendCommonCommand(String, HashMap\<String, ValueType>)

```cangjie
public func sendCommonCommand(command: String, args: HashMap<String, ValueType>): Unit
```

**功能：** 发送自定义控制命令到其对应的会话。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|command|String|是|-|需要设置的自定义控制命令的名称。|
|args|HashMap\<String, [ValueType](#enum-valuetype)>|是|-|需要传递的控制命令键值对。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|
  |6600105|Invalid session command.|
  |6600106|The session is not activated.|
  |6600107|Too many commands or events.|

### func sendControlCommand(AVControlCommand)

```cangjie
public func sendControlCommand(command: AVControlCommand): Unit
```

**功能：** 通过会话控制器发送自定义命令到其对应的会话。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|command|[AVControlCommand](#class-avcontrolcommand)|是|-|会话的相关命令和命令相关参数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|
  |6600105|Invalid session command.|
  |6600106|The session is not activated.|
  |6600107|Too many commands or events.|

### func skipToQueueItem(Int32)

```cangjie
public func skipToQueueItem(itemId: Int32): Unit
```

**功能：** 设置指定播放列表单项的ID，发送给session端处理，session端可以选择对这个单项歌曲进行播放。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|itemId|Int32|是|-|播放列表单项的ID值，用以表示选中的播放列表单项。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|
  |6600103|The session controller does not exist.|