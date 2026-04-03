## class Event3

```cangjie
public class Event3<A1, A2, A3> <: EventBase {}
```

**功能：** 参数个数为3的事件中心。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**父类型：**

- [EventBase](#class-eventbase)

### func emit(A1, A2, A3)

```cangjie
public func emit(arg1: A1, arg2: A2, arg3: A3): Unit
```

**功能：** 触发参数个数为3的指定事件，A1、A2、A3为泛型类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg1|A1|是|-|事件触发时，传递给回调事件的参数。|
|arg2|A2|是|-|事件触发时，传递给回调事件的参数。|
|arg3|A3|是|-|事件触发时，传递给回调事件的参数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F6 <: EventCallBack3<Int64, Int64, Int64> {
       public func invoke(a: Int64, b: Int64, c: Int64) {
           println("F6 is invoked")
       }
}

let eventhub = EventHub()
let foo6: EventCallBack3<Int64, Int64, Int64> = F6()
eventhub.obtainEvent3<Int64, Int64, Int64>("click3").on(foo6)
eventhub.get3<Int64, Int64, Int64>("click3").emit(3, 3, 3)
```

### func off(EventCallBack3\<A1,A2,A3>)

```cangjie
public func off(callback: EventCallBack3<A1, A2, A3>): Unit
```

**功能：** 取取消对指定事件callback的订阅，当该事件触发后，将不会回调该callback。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[EventCallBack3](#class-eventcallback3)\<A1,A2,A3>|是|-|事件回调。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F6 <: EventCallBack3<Int64, Int64, Int64> {
       public func invoke(a: Int64, b: Int64, c: Int64) {
           println("F6 is invoked")
       }
}

let eventhub = EventHub()
let foo6: EventCallBack3<Int64, Int64, Int64> = F6()
eventhub.obtainEvent3<Int64, Int64, Int64>("click3").on(foo6)
eventhub.obtainEvent3<Int64, Int64, Int64>("click3").off(foo6)
```

### func off()

```cangjie
public func off(): Unit
```

**功能：** 取消订阅参数个数为3的所有指定事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F6 <: EventCallBack3<Int64, Int64, Int64> {
       public func invoke(a: Int64, b: Int64, c: Int64) {
           println("F6 is invoked")
       }
}

let eventhub = EventHub()
let foo6: EventCallBack3<Int64, Int64, Int64> = F6()
eventhub.obtainEvent3<Int64, Int64, Int64>("click3").on(foo6)
eventhub.obtainEvent3<Int64, Int64, Int64>("click3").off()
```

### func on(EventCallBack3\<A1,A2,A3>)

```cangjie
public func on(callback: EventCallBack3<A1, A2, A3>): Unit
```

**功能：** 订阅指定事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[EventCallBack3](#class-eventcallback3)\<A1,A2,A3>|是|-|事件回调，事件触发后调用。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F6 <: EventCallBack3<Int64, Int64, Int64> {
       public func invoke(a: Int64, b: Int64, c: Int64) {
           println("F6 is invoked")
       }
}
class F7 <: EventCallBack3<Int64, Int64, Int64> {
    public func invoke(a: Int64, b: Int64, c: Int64) {
        println("F7 is invoked")
   }
}

let eventhub = EventHub()
let foo6: EventCallBack3<Int64, Int64, Int64> = F6()
let foo7: EventCallBack3<Int64, Int64, Int64> = F7()
eventhub.obtainEvent3<Int64, Int64, Int64>("click3").on(foo6)
eventhub.obtainEvent3<Int64, Int64, Int64>("click3").on(foo7)
```