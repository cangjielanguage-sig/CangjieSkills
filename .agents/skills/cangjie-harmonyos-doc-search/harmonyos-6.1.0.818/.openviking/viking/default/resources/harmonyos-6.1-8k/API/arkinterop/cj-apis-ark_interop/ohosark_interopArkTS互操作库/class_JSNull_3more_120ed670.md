## class JSNull

```cangjie
public class JSNull {}
```

**功能：** ArkTS null。

**起始版本：** 22

### func toJSValue()

```cangjie
public func toJSValue(): JSValue
```

**功能：** 转换为 ArkTS 统一类型。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS 统一类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

## class JSNumber

```cangjie
public class JSNumber {}
```

**功能：** ArkTS number。

**起始版本：** 22

### func toFloat64()

```cangjie
public func toFloat64(): Float64
```

**功能：** 转换为 Float64。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Float64|仓颉浮点数。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsNum = context.number(1.0)
    let value = jsNum.toFloat64()
    Hilog.info(0, "test", "value is ${value}")
    return jsNum.toJSValue()
}
```

### func toJSValue()

```cangjie
public func toJSValue(): JSValue
```

**功能：** 转换为 JSValue。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS 统一类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

## class JSObject

```cangjie
public class JSObject <: JSObjectBase {}
```

**功能：** 一个ArkTS对象的安全引用。

**起始版本：** 22

**父类型：**

- [JSObjectBase](#class-jsobjectbase)

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func setObjectProperties(context: JSContext): JSValue {
    let jsObject = context.object()

    // 设置不同类型的属性
    jsObject.setProperty("name", context.string("John").toJSValue())
    jsObject.setProperty("age", context.number(30).toJSValue())
    jsObject.setProperty("isActive", context.boolean(true).toJSValue())

    // 设置嵌套对象
    let address = context.object()
    address.setProperty("city", context.string("Beijing").toJSValue())
    address.setProperty("country", context.string("China").toJSValue())
    jsObject.setProperty("address", address.toJSValue())

    Hilog.info(0, "test", "Set object properties")

    return jsObject.toJSValue()
}
```