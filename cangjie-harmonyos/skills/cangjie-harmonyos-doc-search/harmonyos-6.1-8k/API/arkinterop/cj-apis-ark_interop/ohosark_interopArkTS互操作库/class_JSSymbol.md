## class JSSymbol

```cangjie
public class JSSymbol <: JSHeapObject & JSKeyable {}
```

**功能：** 一个js symbol的安全引用。

**起始版本：** 22

**父类型：**

- [JSHeapObject](#class-jsheapobject)
- [JSKeyable](#interface-jskeyable)

**示例：**

<!--compile-->
```cangjie
func createSymbol(context: JSContext): JSValue {
    // 创建一个 JSSymbol 对象
    let symbol = context.symbol(description: "mySymbol")
    // 创建一个 JSObject 对象
    let object = context.object()
    // 使用symbol作为键保存一个隐藏属性
    object[symbol] = context.string("123").toJSValue()
    // 创建一个对外可见函数，在这个函数中，通过symbol访问对象属性
    object["name"] = context.function { context, callInfo =>
        return object[symbol]
    }.toJSValue()
    return object.toJSValue()
}
```

### prop description

```cangjie
public prop description: String
```

**功能：** symbol的描述。

**起始版本：** 22

**类型：** String

**读写能力：** 只读

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### func toJSValue(JSContext)

```cangjie
public func toJSValue(_: JSContext): JSValue
```

**功能：** 转换为 JSValue。声明式互操作宏框架场景使用，开发者不需要使用此API。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS 统一类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### func toString()

```cangjie
public func toString(): String
```

**功能：** 转换为 String。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后的字符串。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |