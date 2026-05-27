## class JSStringEx

```cangjie
public class JSStringEx <: JSInteropType<JSStringEx> & Equatable<JSStringEx> & ToString {
    public init(str: String)
}
```

**功能：** 对 [JSString](#class-jsstring) 的功能及性能扩展，可在声明式互操作宏中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**父类型：**

* [JSInteropType\<JSStringEx>](#interface-jsinteroptype)
* Equatable\<JSStringEx>
* ToString

### prop size

```cangjie
public prop size: Int64
```

**功能：** 获取字符串 UTF-8 编码后的字节长度。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

类型：Int64

**类型：** Int64

**读写能力：** 只读

### init(String)

```cangjie
public init(str: String)
```

**功能：** 给定 String，构造对应的 JSStringEx 实例。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|str|String|是|-|初始字符串。|

### static func fromJSValue(JSContext, JSValue)

```cangjie
public static func fromJSValue(context: JSContext, input: JSValue): JSStringEx
```

**功能：** 从 JSValue 转换为 JSStringEx。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|input|[JSValue](#struct-jsvalue)|是|-|ArkTS 统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSStringEx](#class-jsstringex)|声明式互操作宏类型 JSStringEx。|

### static func toArkTsType()

```cangjie
public static func toArkTsType(): String
```

**功能：** 获取仓颉类型对应的ArkTS类型名称。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后 ArkTS 类型名。|

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

### func !=(JSStringEx)

```cangjie
public operator func !=(str: JSStringEx): Bool
```

**功能：** 判断两个 JSStringEx 是否不相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|str|[JSStringEx](#class-jsstringex)|是|-|待比较的字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|不相等返回 true，相等返回 false。|

### func ==(JSStringEx)

```cangjie
public operator func ==(str: JSStringEx): Bool
```

**功能：** 功能：判断两个 JSStringEx 是否相等。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|str|[JSStringEx](#class-jsstringex)|是|-|待比较的字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|相等返回 true，不相等返回 false。|