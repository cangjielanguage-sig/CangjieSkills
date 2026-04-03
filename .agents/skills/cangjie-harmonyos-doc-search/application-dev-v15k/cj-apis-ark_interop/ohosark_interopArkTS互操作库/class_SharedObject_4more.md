## class SharedObject

```cangjie
public open class SharedObject {
    public init()
}
```

**功能：** 可以被 ArkTS 引用的仓颉对象的基类。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

### prop nativeId

```cangjie
public prop nativeId: Int64
```

**功能：** 对象唯一标识。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**类型：** Int64

**读写能力：** 只读

### init()

```cangjie
public init()
```

**功能：** 创建一个 SharedObject 对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

## struct JSBoolean

```cangjie
public struct JSBoolean {}
```

**功能：** ArkTS boolean。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

### func toBool()

```cangjie
public func toBool(): Bool
```

**功能：** 转换为仓颉 Bool。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|Bool|仓颉Bool值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsBool = context.boolean(true)
    let value = jsBool.toBool()
    println("value is ${value}")
    return jsBool.toJSValue()
}
```

### func toJSValue()

```cangjie
public func toJSValue(): JSValue
```

**功能：** 转换为 JSValue 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS 统一类型。|

## struct JSCallInfo

```cangjie
public struct JSCallInfo {}
```

**功能：** 一次ArkTS函数调用的相关信息。可以获取this指针、获取参数数量、按索引读取参数。

每次ArkTS函数调用会在ArkTS栈上保存参数列表和其他相关信息，JSCallInfo是一个指向这些信息的指针。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

生命周期：本次ArkTS函数调用结束这个JSCallInfo就会失效。

### prop count

```cangjie
public prop count: Int64
```

**功能：** 入参数量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**类型：** Int64

**读写能力：** 只读

### prop thisArg

```cangjie
public prop thisArg: JSValue
```

**功能：** this 指针。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**类型：** [JSValue](#struct-jsvalue)

**读写能力：** 只读

### func \[](Int64)

```cangjie
public operator func[](index: Int64): JSValue
```

**功能：** 通过索引获取对应的参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|index|Int64|是|-|入参索引，安全范围：[0, 入参数量)。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|入参的值。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    if (callInfo.count > 0) {
        let firstArg = callInfo[0]
        return firstArg
    }
    return context.undefined().toJSValue()
}
```

## struct JSNull

```cangjie
public struct JSNull {}
```

**功能：** ArkTS null。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

### func toJSValue()

```cangjie
public func toJSValue(): JSValue
```

**功能：** 转为为 ArkTS 统一类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS 统一类型。|