### func toBoolean()

```cangjie
public func toBoolean(): Bool
```

**功能：** 把一个 JSValue 转换为 Bool 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|仓颉 Bool 值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let value = callInfo[0].toBoolean()
    println("value is ${value}")
    return context.undefined().toJSValue()
}
```

### func toNumber()

```cangjie
public func toNumber(): Float64
```

**功能：** 把一个 JSValue 转换为 Float64 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Float64|仓颉 Float64 的值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let value = callInfo[0].toNumber()
    println("value is ${value}")
    return context.undefined().toJSValue()
}
```

### func toString()

```cangjie
public func toString(): String
```

**功能：** 把一个 JSValue 转换为 String 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|String|仓颉字符串。|

**示例：**

```cangjie
// 判断首个参数是否是数字，如果是返回true，如果否返回数据类型的字符串
func checkIsNumber(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取参数
    let value: JSValue = callInfo[0]
    // 获取参数类型
    let valueType: JSType = value.typeof()
    // 类型判断
    if (valueType == JSType.NUMBER) {
        // 返回 true
        return context.boolean(true).toJSValue()
    }
    // 返回类型字符串
    return context.string(valueType.toString()).toJSValue()
}
```

### func toString(JSContext) <sub>(deprecated)</sub>

```cangjie
public func toString(_: JSContext): String
```

**功能：** 把一个 JSValue 转换为 String 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|String|仓颉字符串。|

### func toUtf16String()

```cangjie
public func toUtf16String(): Utf16String
```

**功能：** 从 JSValue 转换为 Utf16String。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 20

**返回值：**

|类型|说明|
|:----|:----|
|[Utf16String](#class-utf16string)|转换后的 Utf16String 对象。|

### func typeof()

```cangjie
public func typeof(): JSType
```

**功能：** 获取一个 JSValue 的类型，和 ArkTS 的 typeof 语法枚举出的类型基本一致。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[JSType](#struct-jstype)|ArkTS 类型|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取首个参数
    let arg0 = callInfo[0]
    // 获取参数类型
    let valueType = arg0.typeof()
    // 打印参数类型
    println("arg type is ${valueType.toString()}")
    arg0
}
```