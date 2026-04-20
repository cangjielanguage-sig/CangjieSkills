## class Event1

```cangjie
public class Event1<A> <: EventBase {}
```

**功能：** 参数个数为1的事件中心。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**父类型：**

- [EventBase](#class-eventbase)

### func emit(A)

```cangjie
public func emit(arg: A): Unit
```

**功能：** 触发参数个数为1的指定事件，A为泛型类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg|A|是|-|事件触发时，传递给回调事件的参数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F2 <: EventCallBack1<Int64> {
    public override func invoke(a: Int64) {
        println("F2 is invoked")
    }
}

let eventhub = EventHub()
let foo2: EventCallBack1<Int64> = F2()
eventhub.obtainEvent1<Int64>("click1").on(foo2)
eventhub.get1<Int64>("click1").emit(1)
```

### func off(EventCallBack1\<A>)

```cangjie
public func off(callback: EventCallBack1<A>): Unit
```

**功能：** 取消对指定事件callback的订阅，当该事件触发后，将不会回调该callback。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[EventCallBack1](#class-eventcallback1)\<A>|是|-|事件回调。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F2 <: EventCallBack1<Int64> {
    public override func invoke(a: Int64) {
        println("F2 is invoked")
    }
}

let eventhub = EventHub()
let foo2: EventCallBack1<Int64> = F2()
eventhub.obtainEvent1<Int64>("click1").on(foo2)
eventhub.obtainEvent1<Int64>("click1").off(foo2)
```

### func off()

```cangjie
public func off(): Unit
```

**功能：** 取消订阅参数个数为1的所有指定事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F2 <: EventCallBack1<Int64> {
    public override func invoke(a: Int64) {
        println("F2 is invoked")
    }
}

let eventhub = EventHub()
let foo2: EventCallBack1<Int64> = F2()
eventhub.obtainEvent1<Int64>("click1").on(foo2)
eventhub.obtainEvent1<Int64>("click1").off()
```

### func on(EventCallBack1\<A>)

```cangjie
public func on(callback: EventCallBack1<A>): Unit
```

**功能：** 订阅指定事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[EventCallBack1](#class-eventcallback1)\<A>|是|-|事件回调，事件触发后调用。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F2 <: EventCallBack1<Int64> {
    public override func invoke(a: Int64) {
        println("F2 is invoked")
    }
}
class F3 <: EventCallBack1<Int64> {
    public override func invoke(a: Int64) {
        println("F3 is invoked")
    }
}

let eventhub = EventHub()
let foo2: EventCallBack1<Int64> = F2()
let foo3: EventCallBack1<Int64> = F3()
eventhub.obtainEvent1<Int64>("click1").on(foo2)
eventhub.obtainEvent1<Int64>("click1").on(foo3)
```