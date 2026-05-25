### func string(String)

```cangjie
public func string(value: String): JSString
```

**功能：** 创建一个 ArkTS string。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|String|是|-|仓颉字符串。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSString](#class-jsstring)|ArkTS 字符串引用。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.string("abc")
    return result.toJSValue()
}
```

### func string(Utf16String)

```cangjie
public func string(value: Utf16String): JSString
```

**功能：** 从 Utf16String 创建 JSString。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|value|[Utf16String](#class-utf16string)|是|-|源 Utf16String 对象。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSString](#class-jsstring)|根据源对象创建的 JSString。|

### func symbol(String)

```cangjie
public func symbol(description!: String = ""): JSSymbol
```

**功能：** 创建一个 ArkTS symbol 对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|description|String|否|""| **命名参数。** symbol的描述。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSSymbol](#class-jssymbol)|ArkTS symbol 对象的引用。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.symbol()
    let symbol1 = context.symbol(description: "Symbol1")
    return result.toJSValue()
}
```

### func undefined()

```cangjie
public func undefined(): JSUndefined
```

**功能：** 创建一个 ArkTS undefined。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSUndefined](#struct-jsundefined)|返回 ArkTS undefined。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let result = context.undefined()
    return result.toJSValue()
}
```