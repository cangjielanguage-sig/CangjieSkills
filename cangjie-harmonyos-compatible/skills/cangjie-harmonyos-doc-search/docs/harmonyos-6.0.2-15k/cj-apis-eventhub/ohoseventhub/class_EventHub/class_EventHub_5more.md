## class EventHub

```cangjie
public class EventHub {}
```

**功能：** 事件管理中心抽象类，A、A1、A2、A3、A4、A5均为泛型类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### func get(String)

```cangjie
public func get(s: String): EventBase
```

**功能：** 取出回调事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|s|String|是|-|取出指定事件中心s。|

**返回值：**

|类型|说明|
|:----|:----|
|[EventBase](#class-eventbase)|取出的回调事件。|

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
eventhub.get("click5").as5<Int64, Int64, Int64, Int64, Int64>().emit(5, 5, 5, 5, 5)
```

### func get0(String)

```cangjie
public func get0(s: String): Event0
```

**功能：** 取出回调事件，并校验参数（参数个数为0）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|s|String|是|-|取出指定事件中心s。|

**返回值：**

|类型|说明|
|:----|:----|
|[Event0](#class-event0)|校验后的回调事件中心。|

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

### func get1\<A>(String)

```cangjie
public func get1<A>(s: String): Event1<A>
```

**功能：** 取出回调事件，并校验参数（参数个数为1）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|s|String|是|-|取出指定事件中心s。|

**返回值：**

|类型|说明|
|:----|:----|
|[Event1](#class-event1)\<A>|校验后的回调事件中心。|

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

### func get2\<A1, A2>(String)

```cangjie
public func get2<A1, A2>(s: String): Event2<A1, A2>
```

**功能：** 取出回调事件，并校验参数（参数个数为2）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|s|String|是|-|取出指定事件中心s。|

**返回值：**

|类型|说明|
|:----|:----|
|[Event2](#class-event2)\<A1,A2>|校验后的回调事件中心。|

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