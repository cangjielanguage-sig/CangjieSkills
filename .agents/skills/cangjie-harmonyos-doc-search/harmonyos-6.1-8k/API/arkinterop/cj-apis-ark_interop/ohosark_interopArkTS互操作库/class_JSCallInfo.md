## class JSCallInfo

```cangjie
public class JSCallInfo {}
```

**功能：** 一次ArkTS函数调用的相关信息。可以获取this指针、获取参数数量、按索引读取参数。

每次ArkTS函数调用会在ArkTS栈上保存参数列表和其他相关信息，JSCallInfo是一个指向这些信息的指针。

生命周期：本次ArkTS函数调用结束这个JSCallInfo就会失效。

**起始版本：** 22

### prop count

```cangjie
public prop count: Int64
```

**功能：** 入参数量。

**起始版本：** 22

**类型：** Int64

**读写能力：** 只读

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### prop thisArg

```cangjie
public prop thisArg: JSValue
```

**功能：** this 指针。

**起始版本：** 22

**类型：** [JSValue](#class-jsvalue)

**读写能力：** 只读

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### operator func \[](Int64)

```cangjie
public operator func [](index: Int64): JSValue
```

**功能：** 通过索引获取对应的参数。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|入参索引，安全范围：[0, 入参数量)。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|入参的值。|

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
    if (callInfo.count > 0) {
        let firstArg = callInfo[0]
        return firstArg
    }
    return context.undefined().toJSValue()
}
```