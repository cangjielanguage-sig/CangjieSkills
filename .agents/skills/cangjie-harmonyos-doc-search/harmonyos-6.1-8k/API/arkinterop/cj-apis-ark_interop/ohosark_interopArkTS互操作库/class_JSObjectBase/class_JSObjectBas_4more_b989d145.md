## class JSObjectBase

```cangjie
abstract sealed class JSObjectBase <: JSHeapObject {}
```

**功能：** 一个 ArkTS 对象的安全引用的基类。可以操作 ArkTS 对象。

**起始版本：** 22

**父类型：**

- [JSHeapObject](#class-jsheapobject)

### func attachCJObject(JSExternal)

```cangjie
public func attachCJObject(target: JSExternal): Unit
```

**功能：** 为当前对象绑定一个仓颉对象在 ArkTS 的引用。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[JSExternal](#class-jsexternal)|是|-|ArkTS 对仓颉对象的引用。|

**示例：**

<!--compile-->
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

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标方法名。|
|args|Array\<[JSValue](#class-jsvalue)>|是|-|调用的参数列表。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|方法调用返回值。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.                |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let json = context.global["JSON"].asObject()
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

**功能：** 为当前对象定义 accessors。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|目标键。|
|getter|?[JSFunction](#class-jsfunction)|否|None| **命名参数。** getter 实现。|
|setter|?[JSFunction](#class-jsfunction)|否|None| **命名参数。** setter 实现。|
|isEnumerable|Bool|否|false| **命名参数。** 是否可枚举。|
|isConfigurable|Bool|否|false| **命名参数。** 是否可重新定义。|

**返回值：**

| 类型   | 说明    |
|:-----|:------|
| Bool | 是否成功。 |

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.                |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let obj = context.object()
    let getter = context.function { context, callInfo =>
        context.number(1.0).toJSValue()
    }
    obj.defineOwnAccessor("a", getter: getter, isConfigurable: false)
    return obj.toJSValue()
}
```