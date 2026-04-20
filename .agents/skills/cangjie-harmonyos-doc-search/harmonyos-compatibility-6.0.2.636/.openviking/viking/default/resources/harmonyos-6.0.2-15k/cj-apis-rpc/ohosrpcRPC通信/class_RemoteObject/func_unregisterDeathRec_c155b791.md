### func unregisterDeathRecipient(DeathRecipient, Int32)

```cangjie
public func unregisterDeathRecipient(recipient: DeathRecipient, flags: Int32): Unit
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