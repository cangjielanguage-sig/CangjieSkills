### func getElement(Int64)

```cangjie
public func getElement(index: Int64): JSValue
```

**功能：** 从 ArkTS 数组读取元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|数组元素索引。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|一个 ArkTS 值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsArr = callInfo[0]
    let element = jsArr.getElement(0)
    return element
}
```

### func getElement(JSContext, Int64) <sub>(deprecated)</sub>

```cangjie
public func getElement(_: JSContext, index: Int64): JSValue
```

**功能：** 从 ArkTS 数组读取元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|index|Int64|是|-|数组元素索引。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|一个 ArkTS 值。|

### func getProperty(JSKeyable)

```cangjie
public func getProperty(key: JSKeyable): JSValue
```

**功能：** 从 ArkTS 对象读取属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性的键，可以是 String 、 JSString 或 JSSymbol。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|取到的值|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsObJ = callInfo[0]
    let element = jsObJ.getProperty(context, "a")
    let element1 = jsObJ.getProperty(context, context.string("a"))
    let element2 = jsObJ.getProperty(context, context.symbol())
    return element
}
```

>

### func getProperty(JSContext, JSKeyable) <sub>(deprecated)</sub>

```cangjie
public func getProperty(_: JSContext, key: JSKeyable): JSValue
```

**功能：** 从 ArkTS 对象读取属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|key|[JSKeyable](#interface-jskeyable)|是|-|属性的键，可以是 String 、 JSString 或 JSSymbol。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|取到的值|

### func isArray(JSContext) <sub>(deprecated)</sub>

```cangjie
public func isArray(_: JSContext): Bool
```

**功能：** 判断一个 JSValue 是否是 Array 类型 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|_|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 Array。|

### func isArray()

```cangjie
public func isArray(): Bool
```

**功能：** 判断一个 JSValue 是否是 Array 类型 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|为 true 时代表类型为 Array。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    // 获取入参
    let arg0 = callInfo[0]
    // 判断是否是 object
    let result = arg0.isArray()
    // 返回结果
    return context.boolean(result).toJSValue()
}
```