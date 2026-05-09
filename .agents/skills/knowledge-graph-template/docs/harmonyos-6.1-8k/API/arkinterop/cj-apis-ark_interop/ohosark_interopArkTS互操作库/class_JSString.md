## class JSString

```cangjie
public class JSString <: JSHeapObject & ToString & JSKeyable {}
```

**功能：** 一个ArkTS字符串的安全引用。可以转换为String。

**起始版本：** 22

**父类型：**

- [JSHeapObject](#class-jsheapobject)
- ToString
- [JSKeyable](#interface-jskeyable)

### func toJSValue(JSContext)

```cangjie
public func toJSValue(_: JSContext): JSValue
```

**功能：** 转换为 JSValue。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

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

### func toString()

```cangjie
public func toString(): String
```

**功能：** 转换为仓颉字符串。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|仓颉字符串。|

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
    let jsStr = context.string("abc")
    let value = jsStr.toString()
    Hilog.info(0, "test", "value is ${value}")
    return jsStr.toJSValue()
}
```

### func toUtf16String()

```cangjie
public func toUtf16String(): Utf16String
```

**功能：** 从 JSString 转换为 Utf16String。

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

### extend JSString <: JSInteropType\<JSString>

**功能：** 为类型JSString实现扩展方法。

**起始版本：** 22

**父类型：**

- [JSInteropType\<JSString>](#interface-jsinteroptypet)

#### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(_: JSContext, input: JSValue): JSString
```

**功能：** 将JSValue类型转换为相应的JSString类型。

**起始版本：** 22

**参数：**

| 参数名 | 类型                          | 必填 | 默认值 | 说明                |
| :----- | :---------------------------- | :--- | :----- | :------------------ |
| _      | [JSContext](#class-jscontext) | 是   | -      | ArkTS互操作上下文。 |
| input  | [JSValue](#class-jsvalue)     | 是   | -      | ArkTS统一类型。     |

**返回值：**

| 类型                        | 说明                              |
| :-------------------------- | :-------------------------------- |
| [JSString](#class-jsstring) | JSValue类型转换后的JSString类型。 |

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                             |
| :------- | :----------------------------------- |
| 34300002 | Outside error occurred.              |
| 34300003 | Accessing reference is beyond reach. |
| 34300004 | Thread mismatch.                     |
| 34300005 | The ArkTS data types do not match.   |

#### static func toArktsType()

```cangjie
public static func toArktsType(): String
```

**功能：** 获取JSString类型对应的ArkTS类型的名称。

**起始版本：** 22

**返回值：**

| 类型   | 说明                |
| :----- | :------------------ |
| String | 对应的ArkTS类型的名称，即"string"。 |