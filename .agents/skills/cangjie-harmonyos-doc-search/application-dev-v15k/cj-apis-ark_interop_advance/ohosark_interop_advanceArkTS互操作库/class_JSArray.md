## class JSArray

```cangjie
public class JSArray <: JSProxyWithSubRef {}
```

**功能：** 一个ArkTS数组的安全引用。支持获取长度，读写元素功能。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**父类型：**

* [JSProxyWithSubRef](#class-jsproxywithsubref)

### prop size

```cangjie
public prop size: Int64
```

**功能：** 获取元素数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**类型：** Int64

**读写能力：** 只读

### func \[](Int64)

```cangjie
public operator func[](index: Int64): JSValue
```

**功能：** 往 ArkTS 数组写入一个元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|入参索引，安全范围：[0, 入参数量)。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS 统一类型。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsArr = callInfo[0].asArray(context)
    let firstElement = jsArr[0]
    return firstElement
}
```

### func \[](Int64, JSValue)

```cangjie
public operator func[](index: Int64, value!: JSValue): Unit
```

**功能：** 往 ArkTS 数组写入一个元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|写入索引。|
|value|[JSValue](#struct-jsvalue)|是|-| **命名参数。** 写入值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsArr = callInfo[0].asArray(context)
    let setValue = context.number(1.0).toJSValue()
    jsArr[0] = setValue
    return setValue
}
```

### func \[](Int64, JSHeapObject)

```cangjie
public operator func[](index: Int64, value!: JSHeapObject): Unit
```

**功能：** 往 ArkTS 数组写入一个元素。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|写入索引。|
|value|[JSHeapObject](#class-jsheapobject)|是|-| **命名参数。** 写入值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsArr = callInfo[0].asArray(context)
    let setValue = context.string("abc")
    jsArr[0] = setValue
    return setValue.toJSValue()
}
```