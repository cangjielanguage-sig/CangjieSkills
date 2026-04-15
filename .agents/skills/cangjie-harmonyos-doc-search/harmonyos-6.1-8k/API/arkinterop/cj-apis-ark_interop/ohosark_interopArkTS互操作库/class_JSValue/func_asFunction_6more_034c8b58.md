### func asFunction()

```cangjie
public func asFunction(): JSFunction
```

**功能：** 把一个 JSValue 转换为 JSFunction。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSFunction](#class-jsfunction)|一个 ArkTS 函数的引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func asNull()

```cangjie
public func asNull(): JSNull
```

**功能：** 把一个 JSValue 转换为 JSNull。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSNull](#class-jsnull)|一个 ArkTS null|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func asNumber()

```cangjie
public func asNumber(): JSNumber
```

**功能：** 把一个 JSValue 转换为 JSNumber。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSNumber](#class-jsnumber)|一个 ArkTS number。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func asObject()

```cangjie
public func asObject(): JSObject
```

**功能：** 把一个 JSValue 转换为 JSObject。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSObject](#class-jsobject)|一个 ArkTS object 引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func asPromise()

```cangjie
public func asPromise(): JSPromise
```

**功能：** 把一个 JSValue 转换为 JSPromise。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSPromise](#class-jspromise)|ArkTS promise的引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### func asString()

```cangjie
public func asString(): JSString
```

**功能：** 把一个 JSValue 转换为 JSString。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|[JSString](#class-jsstring)|一个 ArkTS string的引用。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |