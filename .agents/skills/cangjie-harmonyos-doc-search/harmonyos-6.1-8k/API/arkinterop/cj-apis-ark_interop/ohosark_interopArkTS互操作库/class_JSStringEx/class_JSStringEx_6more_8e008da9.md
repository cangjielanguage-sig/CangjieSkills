## class JSStringEx

```cangjie
public class JSStringEx <: JSInteropType<JSStringEx> & Equatable<JSStringEx> & ToString {
    public init(str: String)
}
```

**功能：** 对 [JSString](#class-jsstring) 的功能及性能扩展，可在声明式互操作宏中使用。

**起始版本：** 22

**父类型：**

- [JSInteropType\<JSStringEx>](#interface-jsinteroptypet)
- Equatable\<JSStringEx>
- ToString

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func createJSStringEx(context: JSContext): JSValue {
    // 创建一个 JSStringEx 对象
    let sourceString: String = "Hello, World!"
    let jsStringEx = JSStringEx(sourceString)

    Hilog.info(0, "test", "Created JSStringEx with content: ${jsStringEx.toString()}")

    return jsStringEx.toJSValue(context)
}
```

### init(String)

```cangjie
public init(str: String)
```

**功能：** 给定 String，构造对应的 JSStringEx 实例。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|str|String|是|-|初始字符串。|

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(context: JSContext, input: JSValue): JSStringEx
```

**功能：** 从 JSValue 转换为 JSStringEx。声明式互操作宏框架场景使用，开发者不需要使用此API。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|input|[JSValue](#class-jsvalue)|是|-|ArkTS 统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSStringEx](#class-jsstringex)|声明式互操作宏类型 JSStringEx。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |
| 34300005   | The ArkTS data types do not match.   |

### static func toArktsType()

```cangjie
public static func toArktsType(): String
```

**功能：** 获取仓颉类型对应的ArkTS类型名称。声明式互操作宏框架场景使用，开发者不需要使用此API。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后 ArkTS 类型名。|

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
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |

### func toString()

```cangjie
public func toString(): String
```

**功能：** 转换为 String。

**起始版本：** 22

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后的字符串。|

**异常：**

- BusinessException：对应错误码如下表，详见[互操作错误码](./cj-errorcode-ark_interop.md)

| 错误码ID | 错误信息                                 |
|:------|:-------------------------------------|
| 34300003   | Accessing reference is beyond reach. |
| 34300004   | Thread mismatch.                     |