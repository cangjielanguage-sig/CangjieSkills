### func isNumber()

```cangjie
public func isNumber(): Bool
```

**功能：** 判断一个 JSValue 是否是 number 类型 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 number。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 number
    let result = arg0.isNumber()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isObject()

```cangjie
public func isObject(): Bool
```

**功能：** 判断一个 JSValue 是否是 object 类型 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 object|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 object
    let result = arg0.isObject()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isPromise()

```cangjie
public func isPromise(): Bool
```

**功能：** 判断一个 JSValue 是否是 Promise 类型 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 Promise。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 Promise
    let result = arg0.isPromise()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isString()

```cangjie
public func isString(): Bool
```

**功能：** 判断一个 JSValue 是否是 string 类型 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 string。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 string
    let result = arg0.isString()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isSymbol()

```cangjie
public func isSymbol(): Bool
```

**功能：** 判断一个 JSValue 是否是 Symbol 类型 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 Symbol。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 Symbol
    let result = arg0.isSymbol()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isUndefined()

```cangjie
public func isUndefined(): Bool
```

**功能：** 判断一个 JSValue 是否是 undefined 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 undefined。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 undefined
    let result = arg0.isUndefined()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func setElement(Int64, JSValue)

```cangjie
public func setElement(index: Int64, value: JSValue): Unit
```

**功能：** 从 ArkTS 数组写入元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|数组写入索引。|
|value|[JSValue](#struct-jsvalue)|是|-|写入数组的值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsArr = callInfo[0]
    let setValue = context.number(1.0)
    let element = jsArr.setElement(0, setValue.toJSValue())
    return element
}
```