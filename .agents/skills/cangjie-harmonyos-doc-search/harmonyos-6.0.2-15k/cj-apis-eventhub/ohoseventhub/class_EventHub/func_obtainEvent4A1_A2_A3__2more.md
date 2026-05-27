### func obtainEvent4\<A1, A2, A3, A4>(String)

```cangjie
public func obtainEvent4<A1, A2, A3, A4>(name: String): Event4<A1, A2, A3, A4>
```

**功能：** 创建或取出的事件（参数个数为4）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|创建或取出名为name的指定事件中心。|

**返回值：**

|类型|说明|
|:----|:----|
|[Event4](#class-event4)\<A1,A2,A3,A4>|创建或取出的事件中心。|

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

let eventhub = EventHub()
let foo8: EventCallBack4<Int64, Int64, Int64, Int64> = F8()
eventhub.obtainEvent4<Int64, Int64, Int64, Int64>("click4").on(foo8)
```

### func obtainEvent5\<A1, A2, A3, A4, A5>(String)

```cangjie
public func obtainEvent5<A1, A2, A3, A4, A5>(name: String): Event5<A1, A2, A3, A4, A5>
```

**功能：** 创建或取出指定事件中心（参数个数为5）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|name|String|是|-|创建或取出名为name的指定事件中心。|

**返回值：**

|类型|说明|
|:----|:----|
|[Event5](#class-event5)\<A1,A2,A3,A4,A5>|创建或取出的事件中心。|

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
```