## class JSBigInt

```cangjie
public class JSBigInt <: JSHeapObject {}
```

**起始版本：** 22

**功能：** JSBigInt 对象用来表示 JS bigint 类型的安全引用。通过创建 JS bigint 对象，可以转换为仓颉 Int64，转换为仓颉 BigInt。

**父类型：**

- [JSHeapObject](#class-jsheapobject)

### func toBigInt()

```cangjie
public func toBigInt(): BigInt
```

**功能：** 转换为仓颉 BigInt。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|BigInt|仓颉 BigInt。|

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

func convertToBigInt(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsBigInt = callInfo[0].asBigInt()
    let bigIntValue = jsBigInt.toBigInt()

    Hilog.info(0, "test", "Converted BigInt value: ${bigIntValue}")

    return context.string(bigIntValue.toString()).toJSValue()
}
```

## class JSBoolean

```cangjie
public class JSBoolean {}
```

**功能：** ArkTS boolean。

**起始版本：** 22

### func toBool()

```cangjie
public func toBool(): Bool
```

**功能：** 转换为仓颉 Bool。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|仓颉Bool值。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsBool = context.boolean(true)
    let value = jsBool.toBool()
    Hilog.info(0, "test", "value is ${value}")
    return jsBool.toJSValue()
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

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |