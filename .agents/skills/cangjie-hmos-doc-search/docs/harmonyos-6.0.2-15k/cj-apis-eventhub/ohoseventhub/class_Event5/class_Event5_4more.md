## class Event5

```cangjie
public class Event5<A1, A2, A3, A4, A5> <: EventBase {}
```

**功能：** 参数个数为5的事件中心。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**父类型：**

- [EventBase](#class-eventbase)

### func emit(A1, A2, A3, A4, A5)

```cangjie
public func emit(arg1: A1, arg2: A2, arg3: A3, arg4: A4, arg5: A5): Unit
```

**功能：** 触发参数个数为5的指定事件，A1、A2、A3、A4、A5为泛型类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg1|A1|是|-|事件触发时，传递给回调事件的参数。|
|arg2|A2|是|-|事件触发时，传递给回调事件的参数。|
|arg3|A3|是|-|事件触发时，传递给回调事件的参数。|
|arg4|A4|是|-|事件触发时，传递给回调事件的参数。|
|arg5|A5|是|-|事件触发时，传递给回调事件的参数。|

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

let eventhub = EventHub()
let foo10: EventCallBack5<Int64, Int64, Int64, Int64, Int64> = F10()
eventhub.obtainEvent5<Int64, Int64, Int64, Int64, Int64>("click5").on(foo10)
eventhub.get5<Int64, Int64, Int64, Int64, Int64>("click5").emit(5, 5, 5, 5, 5)
```

### func off(EventCallBack5\<A1,A2,A3,A4,A5>)

```cangjie
public func off(callback: EventCallBack5<A1, A2, A3, A4, A5>): Unit
```

**功能：** 取消对指定事件callback的订阅，当该事件触发后，将不会回调该callback。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[EventCallBack5](#class-eventcallback5)\<A1,A2,A3,A4,A5>|是|-|事件回调。|

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

let eventhub = EventHub()
let foo10: EventCallBack5<Int64, Int64, Int64, Int64, Int64> = F10()
eventhub.obtainEvent5<Int64, Int64, Int64, Int64, Int64>("click5").on(foo10)
eventhub.obtainEvent5<Int64, Int64, Int64, Int64, Int64>("click5").off(food10)
```

### func off()

```cangjie
public func off(): Unit
```

**功能：** 取消订阅参数个数为5的所有指定事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

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

let eventhub = EventHub()
let foo10: EventCallBack5<Int64, Int64, Int64, Int64, Int64> = F10()
eventhub.obtainEvent5<Int64, Int64, Int64, Int64, Int64>("click5").on(foo10)
eventhub.obtainEvent5<Int64, Int64, Int64, Int64, Int64>("click5").off()
```