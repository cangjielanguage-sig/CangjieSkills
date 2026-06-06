### func off(AVCastControllerEventType, ?Callback1Argument\<Array\<AVCastControlCommandType>>)

```cangjie
public func off(`type`: AVCastControllerEventType, callback!: ?Callback1Argument<Array<AVCastControlCommandType>> = None): Unit
```

**功能：** 取消订阅监听事件的注册函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVCastControllerEventType](#enum-avcastcontrollereventtype)|是|-|监听事件，支持CAST_CONTROLLER_VALID_COMMAND_CHANGE。|
|callback|?[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<[AVCastControlCommandType](#enum-avcastcontrolcommandtype)>>|否|None| **命名参数。** 已注册的回调函数，未填则取消该事件下所有已注册的回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|

### func off(AVCastControllerEventType, ?Callback1Argument\<BusinessException>)

```cangjie
public func off(`type`: AVCastControllerEventType, callback!: ?Callback1Argument<BusinessException> = None): Unit
```

**功能：** 取消订阅监听事件的注册函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVCastControllerEventType](#enum-avcastcontrollereventtype)|是|-|监听事件，支持CAST_CONTROLLER_ERROR。|
|callback|?[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)>|否|None| **命名参数。** 已注册的回调函数，未填则取消该事件下所有已注册的回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|

### func off(AVCastControllerEventType, ?Callback2Argument\<String, Array\<UInt8>>)

```cangjie
public func off(`type`: AVCastControllerEventType, callback!: ?Callback2Argument<String, Array<UInt8>> = None): Unit
```

**功能：** 取消订阅监听事件的注册函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVCastControllerEventType](#enum-avcastcontrollereventtype)|是|-|监听事件，支持CAST_CONTROLLER_KEY_REQUEST。|
|callback|?[Callback2Argument](../BasicServicesKit/cj-apis-base.md#class-callback2argument)\<String, Array\<UInt8>>|否|None| **命名参数。** 已注册的回调函数，未填则取消该事件下所有已注册的回调函数。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|