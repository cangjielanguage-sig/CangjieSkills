## class EventCallBack4

```cangjie
public abstract class EventCallBack4<A1, A2, A3, A4> {}
```

**功能：** 参数个数为4的回调事件的抽象类，A1、A2、A3、A4为泛型类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### func invoke(A1, A2, A3, A4)

```cangjie
public open func invoke(arg1: A1, arg2: A2, arg3: A3, arg4: A4): Unit
```

**功能：** 触发回调事件。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg1|A1|是|-|事件触发时，传递给回调事件的参数。|
|arg2|A2|是|-|事件触发时，传递给回调事件的参数。|
|arg3|A3|是|-|事件触发时，传递给回调事件的参数。|
|arg4|A4|是|-|事件触发时，传递给回调事件的参数。|

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F4 <: EventCallBack4<Int64, Int64, Int64, Int64> {
    public func invoke(a: Int64, b: Int64, c: Int64, d: Int64) {
        println("F4 is invoked")
    }
}
```

## class EventCallBack5

```cangjie
public abstract class EventCallBack5<A1, A2, A3, A4, A5> {}
```

**功能：** 参数个数为5的回调事件的抽象类，A1、A2、A3、A4、A5为泛型类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### func invoke(A1, A2, A3, A4, A5)

```cangjie
public open func invoke(arg1: A1, arg2: A2, arg3: A3, arg4: A4, arg5: A5): Unit
```

**功能：** 触发回调事件。

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
class F5 <: EventCallBack5<Int64, Int64, Int64, Int64, Int64> {
    public func invoke(a: Int64, b: Int64, c: Int64, d: Int64, e: Int64) {
        println("F5 is invoked")
    }
}
```