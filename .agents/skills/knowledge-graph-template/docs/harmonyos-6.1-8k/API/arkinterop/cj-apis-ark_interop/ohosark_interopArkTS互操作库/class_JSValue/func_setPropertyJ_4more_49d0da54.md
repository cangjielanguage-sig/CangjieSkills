### func setProperty(JSKeyable, JSValue)

```cangjie
public func setProperty(key: JSKeyable, setValue: JSValue): Unit
```

**功能：** 往 ArkTS 对象写入属性。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性的键。|
|setValue|[JSValue](#class-jsvalue)|是|-|属性的值。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.                |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

**示例：**

<!--compile-->
```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsObJ = context.object()
    let setValue = context.number(1.0)
    jsObJ.setProperty("a", setValue.toJSValue())
    return jsObJ.toJSValue()
}
```

### func strictEqual(JSValue)

```cangjie
public func strictEqual(target: JSValue): Bool
```

**功能：** 对两个 JSValue 做严格判等（类型一致 + 值相等）。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[JSValue](#class-jsvalue)|是|-|比较的目标值|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表两个值相同|

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
    // 获取两个入参
    let arg0 = callInfo[0]
    let arg1 = callInfo[1]
    // 对两个入参做严格判等
    let isStrictEqual = arg0.strictEqual(arg1)
    // 返回严格判等的值
    return context.boolean(isStrictEqual).toJSValue()
}
```

### func toBigInt()

```cangjie
public func toBigInt(): BigInt
```

**功能：** 把一个 JSValue 转换为 BigInt。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|BigInt|仓颉 BigInt。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let value = callInfo[0].toBigInt()
    Hilog.info(0, "test", "value is ${value}")
    return context.undefined().toJSValue()
}
```

### func toBoolean()

```cangjie
public func toBoolean(): Bool
```

**功能：** 把一个 JSValue 转换为 Bool。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|仓颉 Bool 值。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let value = callInfo[0].toBoolean()
    Hilog.info(0, "test", "value is ${value}")
    return context.undefined().toJSValue()
}
```