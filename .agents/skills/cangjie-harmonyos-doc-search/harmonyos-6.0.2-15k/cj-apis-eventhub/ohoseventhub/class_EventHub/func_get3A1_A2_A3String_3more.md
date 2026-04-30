### func get3\<A1, A2, A3>(String)

```cangjie
public func get3<A1, A2, A3>(s: String): Event3<A1, A2, A3>
```

**功能：** 取出回调事件，并校验参数（参数个数为3）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|s|String|是|-| 取出指定事件中心s。|

**返回值：**

|类型|说明|
|:----|:----|
|[Event3](#class-event3)\<A1,A2,A3>|校验后的回调事件中心。|

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

### func get4\<A1, A2, A3, A4>(String)

```cangjie
public func get4<A1, A2, A3, A4>(s: String): Event4<A1, A2, A3, A4>
```

**功能：** 取出回调事件，并校验参数（参数个数为4）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|s|String|是|-|取出指定事件中心s。|

**返回值：**

|类型|说明|
|:----|:----|
|[Event4](#class-event4)\<A1,A2,A3,A4>|校验后的回调事件中心。|

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
eventhub.get4<Int64, Int64, Int64, Int64>("click4").emit(4, 4, 4, 4)
```

### func get5\<A1, A2, A3, A4, A5>(String)

```cangjie
public func get5<A1, A2, A3, A4, A5>(s: String): Event5<A1, A2, A3, A4, A5>
```

**功能：** 取出回调事件，并校验参数（参数个数为5）。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|s|String|是|-|取出指定事件中心s。|

**返回值：**

|类型|说明|
|:----|:----|
|[Event5](#class-event5)\<A1,A2,A3,A4,A5>|校验后的回调事件中心。|

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

**异常：**

- BusinessException：对应错误码的详细介绍请参见[通用错误码](../../errorcodes/cj-errorcode-universal.md)。

  |错误码|错误信息|
  |:------|:------------------|
  |401|Invalid parameter.|