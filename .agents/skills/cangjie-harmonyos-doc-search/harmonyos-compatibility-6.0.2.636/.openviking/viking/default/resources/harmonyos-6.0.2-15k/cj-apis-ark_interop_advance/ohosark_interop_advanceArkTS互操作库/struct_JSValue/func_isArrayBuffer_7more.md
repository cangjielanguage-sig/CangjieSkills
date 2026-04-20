### func isArrayBuffer()

```cangjie
public func isArrayBuffer(): Bool
```

**功能：** 判断一个 JSValue 是否是 ArrayBuffer 类型 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 ArrayBuffer。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 ArrayBuffer
    let result = arg0.isArrayBuffer()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isBigInt()

```cangjie
public func isBigInt(): Bool
```

**功能：** 判断一个 JSValue 是否是 bigint 类型 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 bigint。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 bigint
    let result = arg0.isBigInt()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isBoolean()

```cangjie
public func isBoolean(): Bool
```

**功能：** 判断一个 JSValue 是否是 boolean 类型 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 boolean。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 boolean
    let result = arg0.isBoolean()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isClass()

```cangjie
public func isClass(): Bool
```

**功能：** 判断一个 JSValue 是否是一个 ArkTS 类（构造函数） 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 ArkTS 类（构造函数）|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 ArkTS 类（构造函数）
    let result = arg0.isClass()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isExternal()

```cangjie
public func isExternal(): Bool
```

**功能：** 判断一个 JSValue 是否是一个外部对象（仓颉对象的 ArkTS 引用） 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为外部对象（仓颉对象的 ArkTS 引用）。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是外部对象（仓颉对象的 ArkTS 引用）
    let result = arg0.isExternal()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isFunction()

```cangjie
public func isFunction(): Bool
```

**功能：** 判断一个 JSValue 是否是 function 类型 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 function。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 function
    let result = arg0.isFunction()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```

### func isNull()

```cangjie
public func isNull(): Bool
```

**功能：** 判断一个 JSValue 是否是 null 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 null。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 null
    let result = arg0.isNull()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```