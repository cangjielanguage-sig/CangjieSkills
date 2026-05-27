## interface IRemoteObject

```cangjie
public interface IRemoteObject {
    func getLocalInterface(descriptor: String): IRemoteBroker
    func sendMessageRequest(code: UInt32, data: MessageSequence, reply: MessageSequence, options: MessageOption,
        callback: Callback1Argument<RequestResult>): Unit
    func registerDeathRecipient(recipient: DeathRecipient, flags: Int32): Unit
    func unregisterDeathRecipient(recipient: DeathRecipient, flags: Int32): Unit
    func getDescriptor(): String
    func isObjectDead(): Bool
}
```

**功能：** 该接口可用于查询或获取接口描述符、添加或删除死亡通知、转储对象状态到特定文件、发送消息。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

### func getDescriptor()

```cangjie
func getDescriptor(): String
```

**功能：** 获取对象的接口描述符，接口描述符为字符串。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|String|返回接口描述符。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |1900008|The proxy or remote object is invalid.|

### func getLocalInterface(String)

```cangjie
func getLocalInterface(descriptor: String): IRemoteBroker
```

**功能：** 查询接口描述符的字符串。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|descriptor|String|是|-|接口描述符的字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|[IRemoteBroker](#interface-iremotebroker)|返回绑定到指定接口描述符的IRemoteBroker对象。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: <br/> 1.The number of parameters is incorrect; <br/> 2.The parameter type does not match; <br/> 3.The string length exceeds 40960 bytes; <br/> 4.The number of bytes copied to the buffer is different from the length of the obtained string.|

### func isObjectDead()

```cangjie
func isObjectDead(): Bool
```

**功能：** 检查当前对象是否死亡。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**返回值：**

|类型|说明|
|:----|:----|
|Bool|true：对象死亡，false：对象未死亡。|

### func registerDeathRecipient(DeathRecipient, Int32)

```cangjie
func registerDeathRecipient(recipient: DeathRecipient, flags: Int32): Unit
```

**功能：** 注册用于接收远程对象死亡通知的回调。如果与RemoteProxy对象匹配的远程对象进程死亡，则调用此方法。

**系统能力：** SystemCapability.Communication.IPC.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|recipient|[DeathRecipient](#class-deathrecipient)|是|-|要注册的回调。|
|flags|Int32|是|-|死亡通知标志。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[RPC错误码](../../errorcodes/cj-errorcode-rpc.md)和[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error. Possible causes: <br/> 1.The number of parameters is incorrect; <br/> 2.The parameter type does not match; <br/> 3.The callback used to receive remote object death notifications is empty.|
  |1900008|The proxy or remote object is invalid.|