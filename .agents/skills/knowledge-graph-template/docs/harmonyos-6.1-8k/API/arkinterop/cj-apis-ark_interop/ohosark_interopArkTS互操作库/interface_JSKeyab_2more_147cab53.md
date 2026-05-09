## interface JSKeyable

```cangjie
sealed interface JSKeyable <: ToString & ToJSValue {
}
```

**功能：** 可用于作为 JSObject 键的接口。该接口为 String 类型实现了扩展方法。声明式互操作宏框架场景使用，开发者不需要使用此API。

**起始版本：** 22

**父类型：**

- ToString
- ToJSValue

**示例：**

<!--compile-->
```cangjie
import ohos.hilog.Hilog

func keyableUsage(context: JSContext): Unit {
    // 创建可作为 JSObject 键的数组
    let keys: Array<JSKeyable> = [
        "1",                 // String
        context.string("a"), // JSString
        context.symbol()     // JSSymbol
    ]
    let object = context.object()
    let value = context.boolean(true).toJSValue()
    for (key in keys) {
        object[key] = value
    }
    let isBool = object[keys[0]].isBoolean()
    Hilog.info(0, "test", "isBool: ${isBool}")
}
```

## interface ToJSValue

```cangjie
public interface ToJSValue {
    func toJSValue(context: JSContext): JSValue
}
```

**功能：** 可用于实现ToJSValue的接口

**起始版本：** 22

### func toJSValue(JSContext)

```cangjie
func toJSValue(context: JSContext): JSValue
```

**功能：** 将仓颉类型数据转换为JSValue。

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#class-jsvalue)|ArkTS 统一类型。|