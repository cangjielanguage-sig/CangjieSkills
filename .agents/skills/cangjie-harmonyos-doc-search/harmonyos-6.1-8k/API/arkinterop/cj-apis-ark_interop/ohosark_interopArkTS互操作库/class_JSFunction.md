## class JSFunction

```cangjie
public class JSFunction <: JSHeapObject {}
```

**功能：** 一个 ArkTS 函数的安全引用。

**起始版本：** 22

**父类型：**

- [JSHeapObject](#class-jsheapobject)

### func call(JSValue)

```cangjie
public func call(thisArg!: JSValue = context.undefined().toJSValue()): JSValue
```

**功能：** 进行一次 ArkTS 函数调用（多个参数）。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|thisArg|[JSValue](#class-jsvalue)|否|context.undefined().toJSValue()| **命名参数。** this 指针。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|函数调用返回值。|

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
    let callback = callInfo[0].asFunction()
    return callback.call()
}
```

### func call(JSValue, JSValue)

```cangjie
public func call(arg: JSValue, thisArg!: JSValue = context.undefined().toJSValue()): JSValue
```

**功能：** 进行一次 ArkTS 函数调用（多个参数）。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg|[JSValue](#class-jsvalue)|是|-|ArkTS 函数调用入参。|
|thisArg|[JSValue](#class-jsvalue)|否|context.undefined().toJSValue()| **命名参数。** ArkTS函数调用 this 指针。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|函数调用返回值。|

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
    let callback = callInfo[0].asFunction()
    let arg0 = context.number(1.0).toJSValue()
    return callback.call(arg0)
}
```

### func call(Array\<JSValue>, JSValue)

```cangjie
public func call(args: Array<JSValue>, thisArg!: JSValue = context.undefined().toJSValue()): JSValue
```

**功能：** 进行一次 ArkTS 函数调用（多个参数）。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|args|Array\<[JSValue](#class-jsvalue)>|是|-|参数列表。|
|thisArg|[JSValue](#class-jsvalue)|否|context.undefined().toJSValue()| **命名参数。** this 指针。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|函数调用返回值。|

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
    let callback = callInfo[0].asFunction()
    let arg0 = context.number(1.0).toJSValue()
    let arg1 = context.boolean(false).toJSValue()
    return callback.call([arg0, arg1])
}
```