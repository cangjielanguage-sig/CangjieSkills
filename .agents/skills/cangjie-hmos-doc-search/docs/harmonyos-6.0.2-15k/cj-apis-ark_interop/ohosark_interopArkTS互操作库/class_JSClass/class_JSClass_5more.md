## class JSClass

```cangjie
public class JSClass <: JSHeapObject {}
```

**功能：** 一个ArkTS类（构造函数）的安全引用。可以为该类添加方法和accessor、创建该类的实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**父类型：**

* [JSHeapObject](#class-jsheapobject)

### prop prototype

```cangjie
public prop prototype: JSObject
```

**功能：** 类的原型对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**类型：** [JSObject](#class-jsobject)

**读写能力：** 只读

### func addAccessor(JSKeyable, ?JSFunction, ?JSFunction)

```cangjie
public func addAccessor(key: JSKeyable, getter!: ?JSFunction = None, setter!: ?JSFunction = None): Unit
```

**功能：** 为当前 ArkTS 类定义一对 getter 和 setter。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性键。|
|getter|?[JSFunction](#class-jsfunction)|否|None| **命名参数。** getter 实现。|
|setter|?[JSFunction](#class-jsfunction)|否|None| **命名参数。** setter 实现。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let ctor: JSLambda = {
        _, callInfo => return callInfo.thisArg
    }
    let clazz = context.clazz(ctor)
    let getClassKind: JSLambda = {
        context, _ => context.string("aaa").toJSValue()
    }
    clazz.addAccessor("classKind", getter: context.function(getClassKind))
    let obj = clazz.new()
    let classKind = obj.getProperty(context, "classKind").toString(context)
    println("class kind is ${classKind}")
    return obj
}
```

### func addAccessor(JSKeyable, ?JSLambda, ?JSLambda)

```cangjie
public func addAccessor(key: JSKeyable, getter!: ?JSLambda = None, setter!: ?JSLambda = None): Unit
```

**功能：** 为当前 ArkTS 类定义一对 getter 和 setter。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性键。|
|getter|?[JSLambda](#type-jslambda)|否|None| **命名参数。** getter 实现。|
|setter|?[JSLambda](#type-jslambda)|否|None| **命名参数。** setter 实现。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let ctor: JSLambda = {
        _, callInfo => return callInfo.thisArg
    }
    let clazz = context.clazz(ctor)
    let getClassKind: JSLambda = {
        context, _ => context.string("aaa").toJSValue()
    }
    clazz.addAccessor("classKind", getter: getClassKind)
    let obj = clazz.new()
    let classKind = obj.getProperty(context, "classKind").toString(context)
    println("class kind is ${classKind}")
    return obj
}
```

### func addMethod(JSKeyable, JSFunction)

```cangjie
public func addMethod(key: JSKeyable, method: JSFunction): Unit
```

**功能：** 为当前 ArkTS 类定义一个方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性键。|
|method|[JSFunction](#class-jsfunction)|是|-|方法实现。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let ctor: JSLambda = {
        _, callInfo => return callInfo.thisArg
    }
    let clazz = context.clazz(ctor)
    let getClassKind: JSLambda = {
        context, _ => context.string("aaa").toJSValue()
    }
    clazz.addMethod("getClassKind", context.function(getClassKind))
    let obj = clazz.new()
    let classKind = obj.getProperty(context, "classKind").toString(context)
    println("class kind is ${classKind}")
    return obj
}
```