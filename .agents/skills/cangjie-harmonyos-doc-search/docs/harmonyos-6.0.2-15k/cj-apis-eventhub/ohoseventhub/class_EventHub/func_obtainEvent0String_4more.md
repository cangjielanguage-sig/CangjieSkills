### func obtainEvent0(String)

```cangjie
public func obtainEvent0(name: String): Event0
```

**功能：** 创建或取出的事件（参数个数为0）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|创建或取出名为name的指定事件中心。|

**返回值：**

|类型|说明|
|:----|:----|
|[Event0](#class-event0)|创建或取出的事件中心。|

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
```

### func obtainEvent1\<A>(String)

```cangjie
public func obtainEvent1<A>(name: String): Event1<A>
```

**功能：** 创建或取出的事件（参数个数为1）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|创建或取出名为name的指定事件中心。|

**返回值：**

|类型|说明|
|:----|:----|
|[Event1](#class-event1)\<A>|创建或取出的事件中心。|

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
```

### func obtainEvent2\<A1, A2>(String)

```cangjie
public func obtainEvent2<A1, A2>(name: String): Event2<A1, A2>
```

**功能：** 创建或取出的事件（参数个数为2）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|创建或取出名为name的指定事件中心。|

**返回值：**

|类型|说明|
|:----|:----|
|[Event2](#class-event2)\<A1,A2>|创建或取出的事件中心。|

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
```

### func obtainEvent3\<A1, A2, A3>(String)

```cangjie
public func obtainEvent3<A1, A2, A3>(name: String): Event3<A1, A2, A3>
```

**功能：** 创建或取出的事件（参数个数为3）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|创建或取出名为name的指定事件中心。|

**返回值：**

|类型|说明|
|:----|:----|
|[Event3](#class-event3)\<A1,A2,A3>|创建或取出的事件中心。|

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
```