### func on(EventCallBack5\<A1,A2,A3,A4,A5>)

```cangjie
public func on(callback: EventCallBack5<A1, A2, A3, A4, A5>): Unit
```

**功能：** 订阅指定事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[EventCallBack5](#class-eventcallback5)\<A1,A2,A3,A4,A5>|是|-|事件回调，事件触发后调用。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F10 <: EventCallBack5<Int64, Int64, Int64, Int64, Int64> {
    public override func invoke(a: Int64, b: Int64, c: Int64, d: Int64, e: Int64) {
        println("F10 is invoked")
    }
}
class F11 <: EventCallBack5<Int64, Int64, Int64, Int64, Int64> {
    public func invoke(a: Int64, b: Int64, c: Int64, d: Int64, e: Int64) {
        println("F11 is invoked")
    }
}

let eventhub = EventHub()
let foo10: EventCallBack5<Int64, Int64, Int64, Int64, Int64> = F10()
let foo11: EventCallBack5<Int64, Int64, Int64, Int64, Int64> = F11()
eventhub.obtainEvent5<Int64, Int64, Int64, Int64, Int64>("click5").on(foo10)
eventhub.obtainEvent5<Int64, Int64, Int64, Int64, Int64>("click5").on(foo11)
```