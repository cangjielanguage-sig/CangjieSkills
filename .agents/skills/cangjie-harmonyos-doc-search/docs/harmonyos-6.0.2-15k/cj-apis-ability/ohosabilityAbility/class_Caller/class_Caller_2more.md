## class Caller

```cangjie
public class Caller {}
```

**功能：** 通用组件Caller通信客户端调用接口, 用来向通用组件服务端发送约定数据。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

### func call(String, Parcelable, Callback0Argument)

```cangjie
public func call(method: String, data: Parcelable, callback: Callback0Argument): Unit
```

**功能：** 向通用组件服务端发送约定序列化数据。

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

**起始版本：** 19

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|method|String|是|-|约定的服务端注册事件字符串。|
|data|[Parcelable](../IPCKit/cj-apis-rpc.md#interface-parcelable)|是|-|由开发者实现的Parcelable可序列化数据。|
|callback|[Callback0Argument](../BasicServicesKit/cj-apis-base.md#class-callback0argument)|是|-|开发者传入的回调函数类，用来处理函数调用结果。|

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

class Cb <: Callback0Argument {
    public func invoke(): Unit {
        AppLog.info("message callback done")
    }
}

let uiAbilityContext = Global.getAbilityContext() // 需获取Context应用上下文，详见本文使用说明
let want = Want(bundleName: "com.example.myservice", moduleName: 'entry',
    abilityName: "EntryAbility", parameters: ##"{"ohos.aafwk.param.callAbilityToForeground":true}"##) // parameters是一个json格式的字符串
let caller = uiAbilityContext.startAbilityByCall(want)
caller.call("call_Function", MyMessageAble("test", "cangjie"), Cb())
```