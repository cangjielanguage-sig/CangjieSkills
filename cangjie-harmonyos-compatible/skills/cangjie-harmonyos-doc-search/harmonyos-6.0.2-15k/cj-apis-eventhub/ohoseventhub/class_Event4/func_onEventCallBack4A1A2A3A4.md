### func on(EventCallBack4\<A1,A2,A3,A4>)

```cangjie
public func on(callback: EventCallBack4<A1, A2, A3, A4>): Unit
```

**功能：** 订阅指定事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[EventCallBack4](#class-eventcallback4)\<A1,A2,A3,A4>|是|-|事件回调，事件触发后调用。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F8 <: EventCallBack4<Int64, Int64, Int64, Int64> {
       public func invoke(a: Int64, b: Int64, c: Int64, d: Int64) {
           println("F8 is invoked")
       }
}
class F9 <: EventCallBack4<Int64, Int64, Int64, Int64> {
       public func invoke(a: Int64, b: Int64, c: Int64, d: Int64) {
           println("F9 is invoked")
       }
}

let eventhub = EventHub()
let foo8: EventCallBack4<Int64, Int64, Int64, Int64> = F8()
let foo9: EventCallBack4<Int64, Int64, Int64, Int64> = F9()
eventhub.obtainEvent4<Int64, Int64, Int64, Int64>("click4").on(foo8)
eventhub.obtainEvent4<Int64, Int64, Int64, Int64>("click4").on(foo9)
```