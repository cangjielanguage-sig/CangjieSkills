### func toNumber()

```cangjie
public func toNumber(): Float64
```

**功能：** 把一个 JSValue 转换为 Float64。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Float64|仓颉 Float64 的值。|

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
    let value = callInfo[0].toNumber()
    Hilog.info(0, "test", "value is ${value}")
    return context.undefined().toJSValue()
}
```

### func toString()

```cangjie
public func toString(): String
```

**功能：** 把一个 JSValue 转换为 String。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|仓颉字符串。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.　             |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

**示例：**

<!--compile-->
```cangjie
// 判断首个参数是否是数字，如果是返回true，如果否返回数据类型的字符串
func checkIsNumber(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取参数
    let value: JSValue = callInfo[0]
    // 获取参数类型
    let valueType: JSType = value.typeof()
    // 类型判断
    if (valueType == JSType.NUMBER) {
        // 返回 true
        return context.boolean(true).toJSValue()
    }
    // 返回类型字符串
    return context.string(valueType.toString()).toJSValue()
}
```

### func toUtf16String()

```cangjie
public func toUtf16String(): Utf16String
```

**功能：** 从 JSValue 转换为 Utf16String。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[Utf16String](#class-utf16string)|转换后的 Utf16String 对象。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func typeof()

```cangjie
public func typeof(): JSType
```

**功能：** 获取一个 JSValue 的类型，和 ArkTS 的 typeof 语法枚举出的类型基本一致。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSType](#struct-jstype)|ArkTS 类型|

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
    // 获取首个参数
    let arg0 = callInfo[0]
    // 获取参数类型
    let valueType = arg0.typeof()
    // 打印参数类型
    Hilog.info(0, "test", "arg type is ${valueType.toString()}")
    arg0
}
```