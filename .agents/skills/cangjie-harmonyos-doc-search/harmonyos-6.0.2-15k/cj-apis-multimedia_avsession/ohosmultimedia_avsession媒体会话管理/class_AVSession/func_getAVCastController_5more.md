### func getAVCastController()

```cangjie
public func getAVCastController(): AVCastController
```

**功能：** 设备建立连接后，获取投播控制器。如果avsession未处于投播状态，则控制器将抛出异常。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVCastController](#class-avcastcontroller)|返回投播控制器实例。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600102|The session does not exist.|
  |6600109|The remote connection is not established.|

### func getAllCastDisplays()

```cangjie
public func getAllCastDisplays(): Array<CastDisplayInfo>
```

**功能：** 获取当前系统中所有支持扩展屏投播的显示设备。

**系统能力：** SystemCapability.Multimedia.AVSession.ExtendedDisplayCast

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Array\<[CastDisplayInfo](#class-castdisplayinfo)>|返回当前系统中所有支持扩展屏投播的显示设备。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func getController()

```cangjie
public func getController(): AVSessionController
```

**功能：** 获取本会话对应的控制器。需要系统权限ohos.permission.MANAGE_MEDIA_RESOURCES，否则会抛出错误码为6600101的异常。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[AVSessionController](#class-avsessioncontroller)|返回会话控制器。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func getOutputDevice()

```cangjie
public func getOutputDevice(): OutputDeviceInfo
```

**功能：** 通过会话获取播放设备信息。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|[OutputDeviceInfo](#class-outputdeviceinfo)|返回播放设备信息。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func off(AVSessionEventType, ?CallbackObject)

```cangjie
public func off(eventType: AVSessionEventType, callback!: ?CallbackObject = None): Unit
```

**功能：** 取消订阅监听事件的注册函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionEventType](#enum-avsessioneventtype)|是|-|监听事件。|
|callback|?[CallbackObject](../BasicServicesKit/cj-apis-base.md#class-callbackobject)|否|None| **命名参数。** 已注册的回调函数，未填则取消该事件下所有已注册的回调函数。|