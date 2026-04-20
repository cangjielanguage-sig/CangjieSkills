### func set(Int64, T)

```cangjie
public func set(index: Int64, element: T): Unit
```

**功能：** 修改数组中下标 index 对应的值。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|需要修改的值的下标，取值范围为 [0..this.size]。|
|element|T|是|-|修改的目标值。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                     |
|:------|:-----------------------------------------|
| 1     | The accessing index is out of range.     |
| 34300003   | Accessing reference is beyond reach.     |
| 34300004   | Thread mismatch.                         |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func setElementInArrayEx(context: JSContext): JSValue {
    let array: Array<Int64> = [1, 2, 3, 4, 5]
    let jsArrayEx = JSArrayEx<Int64>(array)

    // 修改索引为2的元素
    jsArrayEx.set(2, 10)
    Hilog.info(0, "test", "Modified element at index 2 to 10")

    return jsArrayEx.toJSValue(context)
}
```

### func toArray()

```cangjie
public func toArray(): Array<T>
```

**功能：** 转换为 Array。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Array\<T>|转换后的仓颉数组。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                     |
|:------|:-----------------------------------------|
| 34300003   | Accessing reference is beyond reach.     |
| 34300004   | Thread mismatch.                         |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func convertArrayExToArray(context: JSContext): JSValue {
    let array: Array<String> = ["hello", "world", "cangjie"]
    let jsArrayEx = JSArrayEx<String>(array)

    let convertedArray = jsArrayEx.toArray()
    Hilog.info(0, "test", "Converted array size: ${convertedArray.size}")

    return jsArrayEx.toJSValue(context)
}
```

### func toJSValue(JSContext)

```cangjie
public func toJSValue(context: JSContext): JSValue
```

**功能：** 转换为 JSValue。声明式互操作宏框架场景使用，开发者不需要使用此API。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS 统一类型。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300002   | Outside error occurred.                |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### operator func \[](Int64)

```cangjie
public operator func [](index: Int64): T
```

**功能：** 获取数组下标 index 对应的值。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|要获取的值的下标。|

**返回值：**

|类型|说明|
|:----|:----|
|T|当前数组中下标 index 对应的值。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                  |
|:------|:--------------------------------------|
| 1     | The accessing index is out of range.  |
| 34300003   | Accessing reference is beyond reach.  |
| 34300004   | Thread mismatch.                      |

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func getIndexOperator(context: JSContext): JSValue {
    let array: Array<Int64> = [10, 20, 30, 40]
    let jsArrayEx = JSArrayEx<Int64>(array)

    let value = jsArrayEx[2]  // 获取索引为2的元素
    Hilog.info(0, "test", "Value at index 2: ${value}")

    return context.number(Float64(value)).toJSValue()
}
```