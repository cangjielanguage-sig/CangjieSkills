### func setElement(JSContext, Int64, JSValue) <sub>(deprecated)</sub>

```cangjie
public func setElement(_: JSContext, index: Int64, value: JSValue): Unit
```

**功能：** 从 ArkTS 数组写入元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|index|Int64|是|-|数组写入索引。|
|value|[JSValue](#struct-jsvalue)|是|-|写入数组的值。|

### func setProperty(JSKeyable, JSValue)

```cangjie
public func setProperty(key: JSKeyable, setValue: JSValue): Unit
```

**功能：** 往 ArkTS 对象写入属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性的键。|
|setValue|[JSValue](#struct-jsvalue)|是|-|属性的值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsObJ = context.object()
    let setValue = context.number(1.0)
    jsObJ.setProperty("a", setValue.toJSValue())
    return jsObJ.toJSValue()
}
```

### func setProperty(JSContext, JSKeyable, JSValue) <sub>(deprecated)</sub>

```cangjie
public func setProperty(_: JSContext, key: JSKeyable, setValue: JSValue): Unit
```

**功能：** 往 ArkTS 对象写入属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性的键。|
|setValue|[JSValue](#struct-jsvalue)|是|-|属性的值。|

### func strictEqual(JSValue)

```cangjie
public func strictEqual(target: JSValue): Bool
```

**功能：** 对两个 JSValue 做严格判等（类型一致 + 值相等）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|target|[JSValue](#struct-jsvalue)|是|-|比较的目标值|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表两个值相同|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取两个入参
    let arg0 = callInfo[0]
    let arg1 = callInfo[1]
    // 对两个入参做严格判等
    let isStrictEqual = arg0.strictEqual(arg1)
    // 返回严格判等的值
    return context.boolean(isStrictEqual).toJSValue()
}
```

### func strictEqual(JSContext, JSValue) <sub>(deprecated)</sub>

```cangjie
public func strictEqual(_: JSContext, target: JSValue): Bool
```

**功能：** 对两个 JSValue 做严格判等（类型一致 + 值相等）。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|target|[JSValue](#struct-jsvalue)|是|-|比较的目标值|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表两个值相同|

### func toBigInt()

```cangjie
public func toBigInt(): BigInt
```

**功能：** 把一个 JSValue 转换为 BigInt 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|BigInt|仓颉 BigInt。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let value = callInfo[0].toBigInt()
    println("value is ${value}")
    return context.undefined().toJSValue()
}
```