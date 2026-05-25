### func on(AVCastControllerEventType, Callback2Argument\<String, Array\<UInt8>>)

```cangjie
public func on(`type`: AVCastControllerEventType, callback: Callback2Argument<String, Array<UInt8>>): Unit
```

**功能：** 订阅投播控制器的监听事件，事件发生时触发回调函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVCastControllerEventType](#enum-avcastcontrollereventtype)|是|-|监听事件，支持CAST_CONTROLLER_KEY_REQUEST。|
|callback|[Callback2Argument](../BasicServicesKit/cj-apis-base.md#class-callback2argument)\<String, Array\<UInt8>>|是|-|入参为String,Array\<UInt8>>的回调函数，事件与回调的关联详见[AVCastControllerEventType](#enum-avcastcontrollereventtype)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|

### func prepare(AVQueueItem)

```cangjie
public func prepare(item: AVQueueItem): Unit
```

**功能：** 准备播放媒体资源，即进行播放资源的加载和缓冲。

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

### func processMediaKeyResponse(String, Array\<UInt8>)

```cangjie
public func processMediaKeyResponse(assetId: String, response: Array<UInt8>): Unit
```

**功能：** 在线DRM资源投播时，处理许可证响应。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|assetId|String|是|-|媒体ID。|
|response|Array\<UInt8>|是|-|许可证响应。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|

### func release()

```cangjie
public func release(): Unit
```

**功能：** 销毁当前controller。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|