## struct JSNumber

```cangjie
public struct JSNumber {}
```

**功能：** ArkTS number。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

### func toFloat64()

```cangjie
public func toFloat64(): Float64
```

**功能：** 转换为 Float64 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|Float64|仓颉浮点数。|

**示例：**

```cangjie
func doSth(context: JSContext, callInfo: JSCallInfo): JSValue {
    let jsNum = context.number(1.0)
    let value = jsNum.toFloat64()
    println("value is ${value}")
    return jsNum.toJSValue()
}
```

### func toJSValue()

```cangjie
public func toJSValue(): JSValue
```

**功能：** 转换为 JSValue 。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS 统一类型。|