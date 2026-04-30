### func sendMessageRequest(UInt32, MessageSequence, MessageSequence, MessageOption, Callback1Argument\<RequestResult>)

```cangjie
func sendMessageRequest(code: UInt32, data: MessageSequence, reply: MessageSequence, options: MessageOption,
    callback: Callback1Argument<RequestResult>): Unit
```

**功能：** 以同步或异步方式向对端进程发送MessageSequence消息。如果为选项设置了异步模式，则立即收到回调，reply报文里没有内容，具体回复需要在业务侧的回调中获取。如果为选项设置了同步模式，则将在sendRequest返回时收到回调，回复内容在reply报文里。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|code|UInt32|是|-|本次请求调用的消息码（1-16777215），由通信双方确定。如果接口由IDL工具生成，则消息代码由IDL自动生成。|
|data|[MessageSequence](#class-messagesequence)|是|-|保存待发送数据的MessageSequence对象。|
|reply|[MessageSequence](#class-messagesequence)|是|-|接收应答数据的MessageSequence对象。|
|options|[MessageOption](#class-messageoption)|是|-|本次请求的同异步模式，默认同步调用。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[RequestResult](#struct-requestresult)>|是|-|接收发送结果的回调。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: <br/> 1.The number of parameters is incorrect; <br/> 2.The parameter type does not match; <br/> 3.Failed to obtain the passed object instance.|

### func unregisterDeathRecipient(DeathRecipient, Int32)

```cangjie
func unregisterDeathRecipient(recipient: DeathRecipient, flags: Int32): Unit
```

**功能：** 注销用于接收远程对象死亡通知的回调。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|recipient|[DeathRecipient](#class-deathrecipient)|是|-|要注销的回调。|
|flags|Int32|是|-|死亡通知标志。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: <br/> 1.The number of parameters is incorrect; <br/> 2.The parameter type does not match; <br/> 3.The callback used to receive remote object death notifications is empty.|
  |1900008|The proxy or remote object is invalid.|