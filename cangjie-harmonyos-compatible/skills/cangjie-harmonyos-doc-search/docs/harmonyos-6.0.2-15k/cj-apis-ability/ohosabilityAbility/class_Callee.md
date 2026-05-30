## class Callee

```cangjie
public class Callee {}
```

**功能：** 通用组件服务端注册和解除客户端caller通知送信的callback接口。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

### func off(String)

```cangjie
public func off(method: String): Unit
```

**功能：** 解除通用组件服务端注册消息通知callback。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|method|String|是|-|已注册的通知事件字符串。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16200005|The method has not been registered.|
  |16000050|Internal error.|

### func on(String, CalleeCallback)

```cangjie
public func on(method: String, callback: CalleeCallback): Unit
```

**功能：** 通用组件服务端注册消息通知callback。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|method|String|是|-|与客户端约定的通知消息字符串。|
|callback|[CalleeCallback](#class-calleecallback)|是|-|一个[MessageSequence](../IPCKit/cj-apis-rpc.md#class-messagesequence)类型入参的通知同步回调函数, 回调函数至少要返回一个空的[Parcelable](../IPCKit/cj-apis-rpc.md#interface-parcelable)数据对象, 其他视为函数执行错误。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16200005|The method has not been registered.|
  |16000050|Internal error.|