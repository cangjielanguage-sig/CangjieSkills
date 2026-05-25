# ohos.ark_interop_advance（ArkTS互操作库）

ArkTS 应用的开发语言包括 ArkTS、typescript、javascript，ArkTS 互操作库是为仓颉语言提供与 ArkTS 语言互操作能力。

本库新增了对跨堆环形引用释放的支持，下面通过一个案例来说明跨堆环形引用：

```cangjie
func createObject(context: JSContext, callInfo: JSCallInfo): JSValue {
    let object: JSObject = context.object()
    let lambda: JSLambda = {
        _, _ => return object["a"]
    }
    object["a"] = callInfo[0]
    object["b"] = context.function(lambda).toJSValue()
    return object.toJSValue()
}
```

![image](../figures/image-cross-heap-cycle.png)

上述的跨堆环形引用在[原互操作库](./cj-apis-ark_interop.md)中，所有涉及的堆对象无法被 GC 释放，从而导致内存泄漏；而本库则能有效的释放这种场景里的对象。

从API Level 20开始，推荐使用本库来替换原 ohos.ark_interop 库。

> **注意：**
>
> ohos.ark_interop_advance 和 ohos.ark_interop 不可在一个应用里混用，否则从 ArkTS 导入仓颉模块可能失败。

## 导入模块

```cangjie
import ohos.ark_interop_advance.*
```

## interface JSInteropByte

```cangjie
sealed interface JSInteropByte {}
```

**功能：** 该接口用于为可用于声明式互操作宏的Array的泛型约束实现。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

## interface JSInteropType

```cangjie
public interface JSInteropType<T> {
    static func fromJSValue(context: JSContext, input: JSValue): T
    func toJSValue(context: JSContext): JSValue
    static func toArkTsType(): String
}
```

**功能：** 该接口用于为可用于声明式互操作宏的类型实现扩展方法。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

如下类型扩展了此接口：

* 被`@Interop[ArkTS]`修饰的用户自定义class

* 被`@Interop[ArkTS]`修饰的用户自定义interface

### static func fromJSValue(JSContext, JSValue)

```cangjie
static func fromJSValue(context: JSContext, input: JSValue): T
```

**功能：** 将 JSValue 类型数据转换为相应的仓颉类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|
|input|[JSValue](#struct-jsvalue)|是|-|ArkTS 统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|T|仓颉类型。|

### static func toArkTsType()

```cangjie
static func toArkTsType(): String
```

**功能：** 获取仓颉类型对应的ArkTS类型名称。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**返回值：**

|类型|说明|
|:----|:----|
|String|转换后 ArkTS 类型名。|

### func toJSValue(JSContext)

```cangjie
func toJSValue(context: JSContext): JSValue
```

**功能：** 将仓颉类型数据转换为JSValue。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 15

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS 统一类型。|

## interface JSKeyable

```cangjie
sealed interface JSKeyable <: ToString & ToJSValue {
}
```

**功能：** 可用于作为 JSObject 键的接口。该接口为 String 类型实现了扩展方法。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 13

**父类型：**

* ToString
* ToJSValue