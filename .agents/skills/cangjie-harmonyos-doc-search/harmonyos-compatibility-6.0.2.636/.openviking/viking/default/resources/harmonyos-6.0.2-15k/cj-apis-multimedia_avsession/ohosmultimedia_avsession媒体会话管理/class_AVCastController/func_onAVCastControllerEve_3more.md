### func on(AVCastControllerEventType, Callback1Argument\<Int32>)

```cangjie
public func on(`type`: AVCastControllerEventType, callback: Callback1Argument<Int32>): Unit
```

**功能：** 订阅投播控制器的监听事件，事件发生时触发回调函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVCastControllerEventType](#enum-avcastcontrollereventtype)|是|-|监听事件，支持CAST_CONTROLLER_SEEK_DONE。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Int32>|是|-|入参为Int32的回调函数，事件与回调的关联详见[AVCastControllerEventType](#enum-avcastcontrollereventtype)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|

### func on(AVCastControllerEventType, Callback1Argument\<Array\<AVCastControlCommandType>>)

```cangjie
public func on(`type`: AVCastControllerEventType, callback: Callback1Argument<Array<AVCastControlCommandType>>): Unit
```

**功能：** 订阅投播控制器的监听事件，事件发生时触发回调函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVCastControllerEventType](#enum-avcastcontrollereventtype)|是|-|监听事件，支持CAST_CONTROLLER_VALID_COMMAND_CHANGE。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<Array\<[AVCastControlCommandType](#enum-avcastcontrolcommandtype)>>|是|-|入参为[AVCastControlCommandType](#enum-avcastcontrolcommandtype)的回调函数，事件与回调的关联详见[AVCastControllerEventType](#enum-avcastcontrollereventtype)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|

### func on(AVCastControllerEventType, Callback1Argument\<BusinessException>)

```cangjie
public func on(`type`: AVCastControllerEventType, callback: Callback1Argument<BusinessException>): Unit
```

**功能：** 订阅投播控制器的监听事件，事件发生时触发回调函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|\`type\`|[AVCastControllerEventType](#enum-avcastcontrollereventtype)|是|-|监听事件，支持CAST_CONTROLLER_ERROR。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)>|是|-|入参为[BusinessException](../BasicServicesKit/cj-apis-base.md#class-businessexception)的回调函数，事件与回调的关联详见[AVCastControllerEventType](#enum-avcastcontrollereventtype)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|