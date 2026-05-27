## class EventCallBack0

```cangjie
public abstract class EventCallBack0 {}
```

**功能：** 参数个数为0的回调事件的抽象类。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### func invoke()

```cangjie
public open func invoke(): Unit
```

**功能：** 触发回调事件。

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
    }
}
```

## class EventCallBack1

```cangjie
public abstract class EventCallBack1<A> {}
```

**功能：** 参数个数为1的回调事件的抽象类，A为泛型类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### func invoke(A)

```cangjie
public open func invoke(arg: A): Unit
```

**功能：** 触发回调事件。

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
class F1 <: EventCallBack1<Int64> {
    public override func invoke(a: Int64) {
        println("F1 is invoked")
    }
}
```

## class EventCallBack2

```cangjie
public abstract class EventCallBack2<A1, A2> {}
```

**功能：** 参数个数为2的回调事件的抽象类，A1、A2为泛型类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### func invoke(A1, A2)

```cangjie
public open func invoke(arg1: A1, arg2: A2): Unit
```

**功能：** 触发回调事件。

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
class F2 <: EventCallBack2<Int64, Int64> {
    public func invoke(a: Int64, b: Int64) {
        println("F2 is invoked")
    }
}
```

## class EventCallBack3

```cangjie
public abstract class EventCallBack3<A1, A2, A3> {}
```

**功能：** 参数个数为3的回调事件的抽象类，A1、A2、A3为泛型类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 12

### func invoke(A1, A2, A3)

```cangjie
public open func invoke(arg1: A1, arg2: A2, arg3: A3): Unit
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

**示例：**

<!-- compile -->

```cangjie
// index.cj

import kit.AbilityKit.*

// 此处代码可添加在依赖项定义中
class F3 <: EventCallBack3<Int64, Int64, Int64> {
    public func invoke(a: Int64, b: Int64, c: Int64) {
        println("F3 is invoked")
    }
}
```