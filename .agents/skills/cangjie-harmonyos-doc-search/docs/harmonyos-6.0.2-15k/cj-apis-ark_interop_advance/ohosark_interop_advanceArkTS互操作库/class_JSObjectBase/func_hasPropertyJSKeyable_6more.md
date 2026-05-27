### func hasProperty(JSKeyable)

```cangjie
public func hasProperty(key: JSKeyable): Bool
```

**功能：** 判断当前对象是否存在目标属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标键。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表当前对象存在目标属性。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = callInfo[0].asObject(context)
    let hasA = obj.hasProperty("a")
    println("obj has property of a: ${hasA}")
    obj.toJSValue()
}
```

### func instanceOf(JSClass)

```cangjie
public func instanceOf(clazz: JSClass): Bool
```

**功能：** 判断当前的对象是否是目标 ArkTS 类的实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|clazz|[JSClass](#class-jsclass)|是|-|目标 ArkTS 类。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表该对象是目标 ArkTS 类的实例。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let ctor: JSLambda = {
        context, callInfo => callInfo.thisArg
    }
    let classA = context.clazz(ctor)
    let obj = classA.new().asObject(context)
    let isClassA = obj.instanceOf(classA)
    println("obj is classA: ${isClassA}")
    return obj.toJSValue()
}
```

### func keys()

```cangjie
public func keys(): Array<String>
```

**功能：** 枚举出当前对象所有可枚举的属性名。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Array\<String>|键列表。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let keys = context.global.keys()
    println("global keys: ${keys}")
    context.undefined().toJSValue()
}
```

### func setProperty(JSKeyable, JSValue)

```cangjie
public func setProperty(key: JSKeyable, setValue: JSValue): Unit
```

**功能：** 对当前对象赋值一个属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标键。|
|setValue|[JSValue](#struct-jsvalue)|是|-|目标值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = context.object()
    obj.setProperty("a", context.number(1.0).toJSValue())
    return obj.toJSValue()
}
```

### func \[](JSKeyable)

```cangjie
public operator func [](key: JSKeyable): JSValue
```

**功能：** 对当前对象赋值一个属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标键。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|取到的值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = callInfo[0].asObject(context)
    let result = obj["a"]
    return result
}
```

### func \[](JSKeyable, JSValue)

```cangjie
public operator func [](key: JSKeyable, value!: JSValue): Unit
```

**功能：** 对当前对象赋值一个属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标键。|
|value|[JSValue](#struct-jsvalue)|是|-| **命名参数。** 目标值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = context.object()
    obj["a"] = context.number(1.0).toJSValue()
    return obj.toJSValue()
}
```