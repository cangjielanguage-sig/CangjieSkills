# ohos.ark_interop（ArkTS互操作库）

ArkTS 应用的开发语言包括 ArkTS、typescript、javascript，ArkTS 互操作库是为仓颉语言提供与 ArkTS 语言互操作能力。

> **注意：**
>
> 适用于需要前向兼容（API Level 12~19）的应用。从 API Level 20 开始，推荐使用 [ohos.ark_interop_advance](./cj-apis-ark_interop_advance.md)。

## 导入模块

```cangjie
import ohos.ark_interop.*
```

## interface JSInteropByte

```cangjie
sealed interface JSInteropByte {}
```

**功能：** 该接口用于为可用于声明式互操作宏的Array的泛型约束实现。声明式互操作宏框架场景使用，开发者不需要使用此API。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

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

**起始版本：** 12

如下类型扩展了此接口：

* 被`@Interop[ArkTS]`修饰的用户自定义class

* 被`@Interop[ArkTS]`修饰的用户自定义interface

### static func fromJSValue(JSContext, JSValue)

```cangjie
static func fromJSValue(context: JSContext, input: JSValue): T
```

**功能：** 将 JSValue 类型数据转换为相应的仓颉类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

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

**起始版本：** 12

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

**起始版本：** 12

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

**起始版本：** 12

**父类型：**

* ToString
* ToJSValue

## interface ToJSValue

```cangjie
interface ToJSValue {
    func toJSValue(context: JSContext): JSValue
}
```

**功能：** 可用于实现ToJSValue的接口。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

### func toJSValue(JSContext)

```cangjie
func toJSValue(context: JSContext): JSValue
```

**功能：** 将仓颉类型数据转换为JSValue。

**系统能力：** SystemCapability.ArkUI.ArkUI.Napi

**起始版本：** 12

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](#class-jscontext)|是|-|ArkTS 互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](#struct-jsvalue)|ArkTS 统一类型。|