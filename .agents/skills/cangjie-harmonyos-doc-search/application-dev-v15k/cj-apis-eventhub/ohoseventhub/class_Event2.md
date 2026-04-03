## class Event2

```cangjie
public class Event2<A1, A2> <: EventBase {}
```

**功能：** 参数个数为2的事件中心。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**父类型：**

- [EventBase](#class-eventbase)

### func emit(A1, A2)

```cangjie
public func emit(arg1: A1, arg2: A2): Unit
```

**功能：** 触发指定事件，A1、A2为泛型类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg1|A1|是|-|事件触发时，传递给回调事件的参数。|
|arg2|A2|是|-|事件触发时，传递给回调事件的参数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F4 <: EventCallBack2<Int64, Int64> {
    public override func invoke(a: Int64, b: Int64) {
        println("F4 is invoked")
    }
}

let eventhub = EventHub()
let foo4: EventCallBack2<Int64, Int64> = F4()
eventhub.obtainEvent2<Int64, Int64>("click2").on(foo4)
eventhub.get2<Int64, Int64>("click2").emit(2, 3)
```

### func off(EventCallBack2\<A1,A2>)

```cangjie
public func off(callback: EventCallBack2<A1, A2>): Unit
```

**功能：** 取消对指定事件callback的订阅，当该事件触发后，将不会回调该callback。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[EventCallBack2](#class-eventcallback2)\<A1,A2>|是|-|事件回调。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F4 <: EventCallBack2<Int64, Int64> {
    public override func invoke(a: Int64, b: Int64) {
        println("F4 is invoked")
    }
}

let eventhub = EventHub()
let foo4: EventCallBack2<Int64, Int64> = F4()
eventhub.obtainEvent2<Int64, Int64>("click2").on(foo4)
eventhub.obtainEvent2<Int64, Int64>("click2").off(foo4)
```

### func off()

```cangjie
public func off(): Unit
```

**功能：** 取消订阅参数个数为2的所有指定事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F4 <: EventCallBack2<Int64, Int64> {
    public override func invoke(a: Int64, b: Int64) {
        println("F4 is invoked")
    }
}

let eventhub = EventHub()
let foo4: EventCallBack2<Int64, Int64> = F4()
eventhub.obtainEvent2<Int64, Int64>("click2").on(foo4)
eventhub.obtainEvent2<Int64, Int64>("click2").off()
```

### func on(EventCallBack2\<A1,A2>)

```cangjie
public func on(callback: EventCallBack2<A1, A2>): Unit
```

**功能：** 订阅指定事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[EventCallBack2](#class-eventcallback2)\<A1,A2>|是|-|事件回调，事件触发后调用。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F4 <: EventCallBack2<Int64, Int64> {
    public override func invoke(a: Int64, b: Int64) {
        println("F4 is invoked")
    }
}
class F5 <: EventCallBack2<Int64, Int64> {
    public func invoke(a: Int64, b: Int64) {
        println("F5 is invoked")
    }
}

let eventhub = EventHub()
let foo4: EventCallBack2<Int64, Int64> = F4()
let foo5: EventCallBack2<Int64, Int64> = F5()
eventhub.obtainEvent2<Int64, Int64>("click2").on(foo4)
eventhub.obtainEvent2<Int64, Int64>("click2").on(foo5)
```