## class JSArray

```cangjie
public class JSArray <: JSHeapObject {}
```

**功能：** 一个ArkTS数组的安全引用。支持获取长度，读写元素功能。

**起始版本：** 22

**父类型：**

- [JSHeapObject](#class-jsheapobject)

### prop size

```cangjie
public prop size: Int64
```

**功能：** 获取元素数量。

**起始版本：** 22

**类型：** Int64

**读写能力：** 只读

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息 |
|:------| :--- |
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch. |

### operator func \[](Int64)

```cangjie
public operator func [](index: Int64): JSValue
```

**功能：** 往 ArkTS 数组写入一个元素。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|入参索引，安全范围：[0, 入参数量)。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS 统一类型。|

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
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsArr = callInfo[0].asArray()
    let firstElement = jsArr[0]
    return firstElement
}
```

### operator func \[](Int64, JSValue)

```cangjie
public operator func [](index: Int64, value!: JSValue): Unit
```

**功能：** 往 ArkTS 数组写入一个元素。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|写入索引。|
|value|[JSValue](#class-jsvalue)|是|-| **命名参数。** 写入值。|

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
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsArr = callInfo[0].asArray()
    let setValue = context.number(1.0).toJSValue()
    jsArr[0] = setValue
    return setValue
}
```

### operator func \[](Int64, JSHeapObject)

```cangjie
public operator func [](index: Int64, value!: JSHeapObject): Unit
```

**功能：** 往 ArkTS 数组写入一个元素。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|写入索引。|
|value|[JSHeapObject](#class-jsheapobject)|是|-| **命名参数。** 写入值。|

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
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsArr = callInfo[0].asArray()
    let setValue = context.string("abc")
    jsArr[0] = setValue
    return setValue.toJSValue()
}
```