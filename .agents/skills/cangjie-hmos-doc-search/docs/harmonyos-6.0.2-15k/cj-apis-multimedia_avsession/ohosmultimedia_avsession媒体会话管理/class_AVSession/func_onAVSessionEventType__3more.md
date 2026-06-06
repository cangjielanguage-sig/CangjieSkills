### func on(AVSessionEventType, Callback1Argument\<LoopMode>)

```cangjie
public func on(eventType: AVSessionEventType, callback: Callback1Argument<LoopMode>): Unit
```

**功能：** 订阅会话监听事件，事件发生时触发回调函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionEventType](#enum-avsessioneventtype)|是|-|监听事件，支持SetLoopMode。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[LoopMode](#enum-loopmode)>|是|-|入参为[LoopMode](#enum-loopmode)的回调函数，事件与回调的关联详见[AVSessionEventType](#enum-avsessioneventtype)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func on(AVSessionEventType, Callback2Argument\<ConnectionState, OutputDeviceInfo>)

```cangjie
public func on(eventType: AVSessionEventType, callback: Callback2Argument<ConnectionState, OutputDeviceInfo>): Unit
```

**功能：** 订阅会话监听事件，事件发生时触发回调函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionEventType](#enum-avsessioneventtype)|是|-|监听事件，支持OutputDeviceChange。|
|callback|[Callback2Argument](../BasicServicesKit/cj-apis-base.md#class-callback2argument)\<[ConnectionState](#enum-connectionstate), [OutputDeviceInfo](#class-outputdeviceinfo)>|是|-|入参为[ConnectionState](#enum-connectionstate)和[OutputDeviceInfo](#class-outputdeviceinfo)的回调函数，事件与回调的关联详见[AVSessionEventType](#enum-avsessioneventtype)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|

### func on(AVSessionEventType, Callback2Argument\<String, HashMap\<String, ValueType>>)

```cangjie
public func on(eventType: AVSessionEventType, callback: Callback2Argument<String, HashMap<String, ValueType>>): Unit
```

**功能：** 订阅会话监听事件，事件发生时触发回调函数。

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|eventType|[AVSessionEventType](#enum-avsessioneventtype)|是|-|监听事件，支持CommonCommand。|
|callback|[Callback2Argument](../BasicServicesKit/cj-apis-base.md#class-callback2argument)\<String, HashMap\<String, [ValueType](#enum-valuetype)>>|是|-|入参为String和HashMap\<String, [ValueType](#enum-valuetype)>的回调函数，事件与回调的关联详见[AVSessionEventType](#enum-avsessioneventtype)。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[媒体会话管理错误码](../../errorcodes/cj-errorcode-multimedia-avsession.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |6600101|Session service exception.|
  |6600102|The session does not exist.|