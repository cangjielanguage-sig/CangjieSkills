## class JSFunction

```cangjie
public class JSFunction <: JSProxyWithSubRef {}
```

**功能：** 一个 ArkTS 函数的安全引用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**父类型：**

* [JSProxyWithSubRef](#class-jsproxywithsubref)

### func call(JSValue)

```cangjie
public func call(thisArg!: JSValue = context.undefined().toJSValue()): JSValue
```

**功能：** 进行一次 ArkTS 函数调用（多个参数）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|thisArg|[JSValue](#struct-jsvalue)|否|context.undefined().toJSValue()| **命名参数。** this 指针。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|函数调用返回值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let callback = callInfo[0].asFunction(context)
    return callback.call()
}
```

### func call(JSValue, JSValue)

```cangjie
public func call(arg: JSValue, thisArg!: JSValue = context.undefined().toJSValue()): JSValue
```

**功能：** 进行一次 ArkTS 函数调用（多个参数）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg|[JSValue](#struct-jsvalue)|是|-|ArkTS 函数调用入参。|
|thisArg|[JSValue](#struct-jsvalue)|否|context.undefined().toJSValue()| **命名参数。** ArkTS函数调用 this 指针。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|函数调用返回值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let callback = callInfo[0].asFunction(context)
    let arg0 = context.number(1.0).toJSValue()
    return callback.call(arg0)
}
```

### func call(Array\<JSValue>, JSValue)

```cangjie
public func call(args: Array<JSValue>, thisArg!: JSValue = context.undefined().toJSValue()): JSValue
```

**功能：** 进行一次 ArkTS 函数调用（多个参数）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|args|Array\<[JSValue](#struct-jsvalue)>|是|-|参数列表。|
|thisArg|[JSValue](#struct-jsvalue)|否|context.undefined().toJSValue()| **命名参数。** this 指针。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|函数调用返回值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let callback = callInfo[0].asFunction(context)
    let arg0 = context.number(1.0).toJSValue()
    let arg1 = context.boolean(false).toJSValue()
    return callback.call([arg0, arg1])
}
```