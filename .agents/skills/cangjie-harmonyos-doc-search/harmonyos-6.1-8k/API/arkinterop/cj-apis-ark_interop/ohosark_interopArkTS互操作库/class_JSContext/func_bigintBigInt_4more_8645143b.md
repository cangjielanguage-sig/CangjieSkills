### func bigint(BigInt)

```cangjie
public func bigint(value: BigInt): JSBigInt
```

**功能：** 通过仓颉 BigInt 创建一个等值的 ArkTS bigint。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|BigInt|是|-|仓颉BigInt。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSBigInt](#class-jsbigint)|ArkTS bigint 对象的引用。|

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
import std.math.numeric.BigInt

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.bigint(BigInt(100))
    return result.toJSValue()
}
```

### func boolean(Bool)

```cangjie
public func boolean(value: Bool): JSBoolean
```

**功能：** 创建一个 ArkTS boolean。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|Bool|是|-|仓颉布尔值。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSBoolean](#class-jsboolean)|ArkTS 布尔值。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.boolean(true)
    return result.toJSValue()
}
```

### func clazz(JSLambda, ?JSClass)

```cangjie
public func clazz(ctor: JSLambda, superClass!: ?JSClass = None): JSClass
```

**功能：** 创建一个 ArkTS 类。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|ctor|[JSLambda](#type-jslambda)|是|-|作为类构造的仓颉函数。|
|superClass|?[JSClass](#class-jsclass)|否|None| **命名参数。** ArkTS 类的父类。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSClass](#class-jsclass)|ArkTS 类的引用。|

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
func clsCtor(context: JSContext, callInfo: JSCallInfo): JSValue {
    callInfo.thisArg
}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.clazz(clsCtor)
    return result.toJSValue()
}
```

### func external(SharedObject)

```cangjie
public func external(data: SharedObject): JSExternal
```

**功能：** 创建一个 ArkTS 对仓颉对象的引用。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|data|[SharedObject](#class-sharedobject)|是|-|原始仓颉对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSExternal](#class-jsexternal)|ArkTS 对仓颉对象的引用。|

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
class Data <: SharedObject {}

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let data = Data()
    let result = context.external(data)
    return result.toJSValue()
}
```