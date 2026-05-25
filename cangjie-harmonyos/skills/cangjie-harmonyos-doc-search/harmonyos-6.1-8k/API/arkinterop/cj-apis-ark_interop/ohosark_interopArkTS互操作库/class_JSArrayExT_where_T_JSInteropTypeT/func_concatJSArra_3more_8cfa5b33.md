### func concat(JSArrayEx\<T>)

```cangjie
public func concat(other: JSArrayEx<T>): JSArrayEx<T>
```

**功能：** 该函数将创建一个新的 JSArrayEx，内容是当前 JSArrayEx 后面串联 other 指向的 JSArrayEx。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|other|[JSArrayEx](#class-jsarrayext-where-t--jsinteroptypet)\<T>|是|-|串联到末尾的 JSArrayEx。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSArrayEx](#class-jsarrayext-where-t--jsinteroptypet)\<T>|串联得到的新 JSArrayEx。|

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

func concatArrayEx(context: JSContext): JSValue {
    let array1: Array<Int64> = [1, 2, 3]
    let array2: Array<Int64> = [4, 5, 6]

    let jsArrayEx1 = JSArrayEx<Int64>(array1)
    let jsArrayEx2 = JSArrayEx<Int64>(array2)

    let concatenated = jsArrayEx1.concat(jsArrayEx2)
    Hilog.info(0, "test", "Concatenated array size: ${concatenated.size}")

    return concatenated.toJSValue(context)
}
```

### func get(Int64)

```cangjie
public func get(index: Int64): Option<T>
```

**功能：** 获取数组中下标 index 对应的元素。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|要获取的值的下标。|

**返回值：**

|类型|说明|
|:----|:----|
|Option\<T>|当前数组中下标 index 对应的值。|

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

func getElementFromArrayEx(context: JSContext, callInfo: JSCallInfo): JSValue {
    let array: Array<String> = ["apple", "banana", "cherry"]
    let jsArrayEx = JSArrayEx<String>(array)

    let element = jsArrayEx.get(1)  // 获取索引为1的元素
    if (element != None) {
        Hilog.info(0, "test", "Element at index 1: ${element}")
    }

    return jsArrayEx.toJSValue(context)
}
```

### func isEmpty()

```cangjie
public func isEmpty(): Bool
```

**功能：** 判断数组是否为空。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|Bool|如果数组为空，返回 true，否则，返回 false。|

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

func checkArrayExEmpty(context: JSContext): JSValue {
    let emptyArray: Array<Int64> = []
    let nonEmptyArray: Array<Int64> = [1, 2, 3]

    let emptyJSArrayEx = JSArrayEx<Int64>(emptyArray)
    let nonEmptyJSArrayEx = JSArrayEx<Int64>(nonEmptyArray)

    Hilog.info(0, "test", "Is empty array empty: ${emptyJSArrayEx.isEmpty()}")
    Hilog.info(0, "test", "Is non-empty array empty: ${nonEmptyJSArrayEx.isEmpty()}")

    return context.boolean(emptyJSArrayEx.isEmpty()).toJSValue()
}
```