### func addMethod(JSKeyable, JSLambda)

```cangjie
public func addMethod(key: JSKeyable, method: JSLambda): Unit
```

**功能：** 为当前 ArkTS 类定义一个方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性键。|
|method|[JSLambda](#type-jslambda)|是|-|方法实现。|

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
    clazz.addMethod("getClassKind", getClassKind)
    let obj = clazz.new()
    let classKind = obj.getProperty(context, "classKind").toString(context)
    println("class kind is ${classKind}")
    return obj
}
```

### func addProperty(JSKeyable, JSValue)

```cangjie
public func addProperty(key: JSKeyable, value: JSValue): Unit
```

**功能：** 为目标 ArkTS 类新增一个数据成员，一般用于定义不可变属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性键。|
|value|[JSValue](#struct-jsvalue)|是|-|属性值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let ctor: JSLambda = {
        _, callInfo => return callInfo.thisArg
    }
    let clazz = context.clazz(ctor)
    clazz.addProperty("classKind", context.string("CustomClass").toJSValue())
    let obj = clazz.new()
    let classKind = obj.getProperty(context, "classKind").toString(context)
    println("class kind is ${classKind}")
    return obj
}
```

### func new()

```cangjie
public func new(): JSValue
```

**功能：** 通过 ArkTS 类实例化一个新对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|new 出来的实例。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let ctor: JSLambda = {
        _, callInfo => return callInfo.thisArg
    }
    let clazz = context.clazz(ctor)
    let obj = clazz.new()
    return obj
}
```

### func new(JSValue)

```cangjie
public func new(arg: JSValue): JSValue
```

**功能：** 通过 ArkTS 类实例化一个新对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg|[JSValue](#struct-jsvalue)|是|-|new 的入参。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|实例化出来的新对象。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let ctor: JSLambda = {
        context, callInfo =>
        let firstArg = callInfo[0]
        let thisArg = callInfo.thisArg
        thisArg.setProperty(context, "id", firstArg)
        return thisArg
    }
    let clazz = context.clazz(ctor)
    let id = context.number(1.0)
    let obj = clazz.new(id.toJSValue())
    return obj
}
```