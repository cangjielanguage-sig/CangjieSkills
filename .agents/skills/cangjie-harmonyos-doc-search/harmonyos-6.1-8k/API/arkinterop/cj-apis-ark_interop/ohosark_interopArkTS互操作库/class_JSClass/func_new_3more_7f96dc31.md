### func new()

```cangjie
public func new(): JSValue
```

**功能：** 通过 ArkTS 类实例化一个新对象。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|new 出来的实例。|

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
    let ctor: JSLambda = { _, callInfo =>
        return callInfo.thisArg
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

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|arg|[JSValue](#class-jsvalue)|是|-|new 的入参。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|实例化出来的新对象。|

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
    let ctor: JSLambda = { context, callInfo =>
        let firstArg = callInfo[0]
        let thisArg = callInfo.thisArg
        thisArg.setProperty("id", firstArg)
        return thisArg
    }
    let clazz = context.clazz(ctor)
    let id = context.number(1.0)
    let obj = clazz.new(id.toJSValue())
    return obj
}
```

### func new(Array\<JSValue>)

```cangjie
public func new(args: Array<JSValue>): JSValue
```

**功能：** 通过 ArkTS 类实例化一个新对象。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|args|Array\<[JSValue](#class-jsvalue)>|是|-|new 的参数列表。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|实例化出来的新对象。|

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
    let ctor: JSLambda = { context, callInfo =>
        let id = callInfo[0]
        let name = callInfo[1]
        let thisArg = callInfo.thisArg
        thisArg.setProperty("id", id)
        thisArg.setProperty("name", name)
        return thisArg
    }
    let clazz = context.clazz(ctor)
    let id = context.number(1.0)
    let name = context.string("aaa")
    let obj = clazz.new([id.toJSValue(), name.toJSValue()])
    return obj
}
```