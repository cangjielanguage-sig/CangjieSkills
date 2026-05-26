### func sendControlCommand(AVCastControlCommand)

```cangjie
public func sendControlCommand(command: AVCastControlCommand): Unit
```

**功能：** 通过控制器发送命令到其对应的会话。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|command|[AVCastControlCommand](#class-avcastcontrolcommand)|是|-|通过控制器发送命令到其对应的会话。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|parameter check failed. 1.Mandatory parameters are left unspecified. 2.Parameter verification failed.|
  |6600101|Session service exception.|
  |6600105|Invalid session command.|
  |6600109|The remote connection is not established.|

### func start(AVQueueItem)

```cangjie
public func start(item: AVQueueItem): Unit
```

**功能：** 启动播放某个媒体资源。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|item|[AVQueueItem](#class-avqueueitem)|是|-|播放列表中单项的相关属性。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600109|The remote connection is not established.|