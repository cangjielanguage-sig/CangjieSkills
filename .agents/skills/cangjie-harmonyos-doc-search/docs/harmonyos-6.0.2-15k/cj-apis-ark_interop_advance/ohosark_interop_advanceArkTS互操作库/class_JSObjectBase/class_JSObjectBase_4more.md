## class JSObjectBase

```cangjie
abstract sealed class JSObjectBase <: JSProxyWithSubRef {}
```

**功能：** 一个 ArkTS 对象的安全引用的基类。可以操作 ArkTS 对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**父类型：**

* [JSProxyWithSubRef](#class-jsproxywithsubref)

### func attachCJObject(JSExternal)

```cangjie
public func attachCJObject(target: JSExternal): Unit
```

**功能：** 为当前对象绑定一个仓颉对象在 ArkTS 的引用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[JSExternal](#class-jsexternal)|是|-|ArkTS 对仓颉对象的引用。|

**示例：**

```cangjie
class Data <: SharedObject {}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = context.object()
    let data = Data()
    let ext = context.external(data)
    obj.attachCJObject(ext)
    return obj.toJSValue()
}
```

### func callMethod(JSKeyable, Array\<JSValue>)

```cangjie
public func callMethod(key: JSKeyable, args: Array<JSValue>): JSValue
```

**功能：** 调用当前对象下的方法。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标方法名。|
|args|Array\<[JSValue](#struct-jsvalue)>|是|-|调用的参数列表。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|方法调用返回值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let json = context.global["JSON"].asObject(context)
    json.callMethod("parse", [context.string("{a: 1, b: 2}").toJSValue()])
}
```

### func defineOwnAccessor(JSKeyable, ?JSFunction, ?JSFunction, Bool, Bool)

```cangjie
public func defineOwnAccessor(key: JSKeyable, getter!:? JSFunction = None, setter!: ?JSFunction = None,
    isEnumerable!: Bool = false,
    isConfigurable!: Bool = false
): Bool
```

**功能：** 为当前对象定义 accessors 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标键。|
|getter|?[JSFunction](#class-jsfunction)|否|None| **命名参数。** getter 实现。|
|setter|?[JSFunction](#class-jsfunction)|否|None| **命名参数。** setter 实现。|
|isEnumerable|Bool|否|false| **命名参数。** 是否可枚举。|
|isConfigurable|Bool|否|false| **命名参数。** 是否可重新定义。|

**返回值：**

|类型|说明|
|:---|:---|
|Bool|是否成功。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = context.object()
    let getter = context.function {
        context, callInfo => context.number(1.0).toJSValue()
    }
    obj.defineOwnAccessor("a", getter: getter, isConfigurable: false)
    return obj.toJSValue()
}
```