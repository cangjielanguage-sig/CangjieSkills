## class Event0

```cangjie
public class Event0 <: EventBase {}
```

**功能：** 参数个数为0的事件中心。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**父类型：**

- [EventBase](#class-eventbase)

### func emit()

```cangjie
public func emit(): Unit
```

**功能：** 触发参数个数为0的指定事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F0 <: EventCallBack0 {
    public override func invoke() {
        println("F0 is invoked")
        return
    }
}

let eventhub = EventHub()
let foo0: EventCallBack0 = F0()
eventhub.obtainEvent0("click0").on(foo0)
eventhub.get0("click0").emit()
```

### func off(EventCallBack0)

```cangjie
public func off(callback: EventCallBack0): Unit
```

**功能：** 取消对指定事件callback的订阅，当该事件触发后，将不会回调该callback。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[EventCallBack0](#class-eventcallback0)|是|-|事件回调。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F0 <: EventCallBack0 {
    public override func invoke() {
        println("F0 is invoked")
        return
    }
}

let eventhub = EventHub()
let foo0: EventCallBack0 = F0()
eventhub.obtainEvent0("click0").on(foo0)
eventhub.obtainEvent0("click0").off(foo0)
```

### func off()

```cangjie
public func off(): Unit
```

**功能：** 取消订阅参数个数为0的所有指定事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F0 <: EventCallBack0 {
    public override func invoke() {
        println("F0 is invoked")
        return
    }
}

let eventhub = EventHub()
let foo0: EventCallBack0 = F0()
eventhub.obtainEvent0("click0").on(foo0)
eventhub.obtainEvent0("click0").off()
```

### func on(EventCallBack0)

```cangjie
public func on(callback: EventCallBack0): Unit
```

**功能：** 订阅指定事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|callback|[EventCallBack0](#class-eventcallback0)|是|-|事件回调，事件触发后调用。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F0 <: EventCallBack0 {
    public override func invoke() {
        println("F0 is invoked")
        return
    }
}
class F1 <: EventCallBack0 {
    public override func invoke() {
        println("F1 is invoked")
        return
    }
}

let eventhub = EventHub()
let foo0: EventCallBack0 = F0()
let foo1: EventCallBack0 = F1()
eventhub.obtainEvent0("click0").on(foo0)
eventhub.obtainEvent0("click0").on(foo1)
```