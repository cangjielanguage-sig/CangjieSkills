## class JSSymbol

```cangjie
public class JSSymbol <: JSHeapObject & JSKeyable {}
```

**功能：** 一个js symbol的安全引用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**父类型：**

* [JSHeapObject](#class-jsheapobject)
* [JSKeyable](#interface-jskeyable)

### prop description

```cangjie
public prop description: String
```

**功能：** symbol的描述。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**类型：** String

**读写能力：** 只读

### func toJSValue(JSContext)

```cangjie
public func toJSValue(_: JSContext): JSValue
```

**功能：** 转换为 JSValue。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS 统一类型。|

### func toString()

```cangjie
public func toString(): String
```

**功能：** 转换为 String。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后的字符串。|

## class JSThreadMisMatch

```cangjie
public class JSThreadMisMatch <: JSInteropException {
    public init(bindTid: UInt64, curTid: UInt64, message!: String = "js thread mismatch")
}
```

**功能：** 执行 ArkTS 接口的线程不匹配异常。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**父类型：**

* [JSInteropException](#class-jsinteropexception)

### init(UInt64, UInt64, String)

```cangjie
public init(bindTid: UInt64, curTid: UInt64, message!: String = "js thread mismatch")
```

**功能：** 构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|bindTid|UInt64|是|-|ArkTS绑定的系统线程的id。|
|curTid|UInt64|是|-|当前系统线程的id。|
|message|String|否|"js thread mismatch"| **命名参数。** 异常消息。|

## class JSTypeMisMatch

```cangjie
public class JSTypeMisMatch <: JSInteropException {
    public init(acquireType: String, givenType: JSType, message!: String = "js type mismatch")
    public init(acquireType: JSType, givenType: JSType, message!: String = "js type mismatch")
}
```

**功能：** ArkTS 操作和实际类型不匹配异常。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**父类型：**

* [JSInteropException](#class-jsinteropexception)

### init(String, JSType, String)

```cangjie
public init(acquireType: String, givenType: JSType, message!: String = "js type mismatch")
```

**功能：** 构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|acquireType|String|是|-|接口要求的类型。|
|givenType|[JSType](#struct-jstype)|是|-|当前的ArkTS类型。|
|message|String|否|"js type mismatch"| **命名参数。** 异常消息。|

### init(JSType, JSType, String)

```cangjie
public init(acquireType: JSType, givenType: JSType, message!: String = "js type mismatch")
```

**功能：** 构造函数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|acquireType|[JSType](#struct-jstype)|是|-|接口要求的类型。|
|givenType|[JSType](#struct-jstype)|是|-|当前的ArkTS类型。|
|message|String|否|"js type mismatch"| **命名参数。** 异常消息。|