### func callWithResult(String, Parcelable, Callback1Argument\<MessageSequence>)

```cangjie
public func callWithResult(method: String, data: Parcelable, callback: Callback1Argument<MessageSequence>): Unit
```

**功能：** 向通用组件服务端发送约定序列化数据, 并将服务端返回的约定序列化数据带回。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|method|String|是|-|约定的服务端注册事件字符串。|
|data|[Parcelable](../IPCKit/cj-apis-rpc.md#interface-parcelable)|是|-|约定的服务端注册事件字符串。|
|callback|[Callback1Argument](../BasicServicesKit/cj-apis-base.md#class-callback1argument)\<[MessageSequence](../IPCKit/cj-apis-rpc.md#class-messagesequence)>|是|-|开发者传入的回调函数类，用于处理返回通用组件服务端应答数据。|

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)和[元能力子系统错误码](../../errorcodes/cj-errorcode-ability.md)。

  |错误码ID|错误信息|
  |:---|:---|
  |401|Parameter error.|
  |16200001|The caller has been released.|
  |16200002|The callee does not exist.|
  |16000050|Internal error.|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import ohos.base.*
import kit.AbilityKit.*
import kit.IPCKit.*

public class MyMessageAble <: Parcelable { // 自定义的Parcelable数据结构
    var num: Int32 = 1
    MyMessageAble(var name: String, var str: String) {
    }
    public override func marshalling(messageSequence: MessageSequence): Bool {
        messageSequence.writeInt(this.num)
        messageSequence.writeString(this.str)
        AppLog.info("MyMessageAble marshalling num[${this.num}] str[${this.str}]")
        return true
    }
    public override func unmarshalling(messageSequence: MessageSequence): Bool {
        this.num = messageSequence.readInt()
        this.str = messageSequence.readString()
        AppLog.info("MyMessageAble unmarshalling num[${this.num}] str[${this.str}]")
        return true
    }
}

class MessageCb <: Callback1Argument<MessageSequence> {
    public func invoke(arg: MessageSequence): Unit {
        AppLog.info("message callback done")
        let retmsg = MyMessageAble('msg', '')
        arg.readParcelable(retmsg)
    }
}

let uiAbilityContext = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let want = Want(bundleName: "com.example.myservice", moduleName: 'entry',
    abilityName: "EntryAbility", parameters: ##"{"ohos.aafwk.param.callAbilityToForeground":true}"##) // parameters是一个json格式的字符串
let caller = uiAbilityContext.startAbilityByCall(want)
caller.callWithResult("call_Function", MyMessageAble("test", "cangjie"), MessageCb())
```