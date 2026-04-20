## func createContextFromJSValue(JSContext, JSValue)

```cangjie
public func createContextFromJSValue(context: JSContext, input: JSValue): Context
```

**功能：** 从[JSValue](../arkinterop/cj-apis-ark_interop.md#class-jsvalue)转换为[Context](./cj-apis-app-ability-ui_ability.md#class-context)类型。该转换仅可在函数传递中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是|-| ArkTS互操作上下文。|
|input|[JSValue](../arkinterop/cj-apis-ark_interop.md#class-jsvalue)|是|-| ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[Context](./cj-apis-app-ability-ui_ability.md#class-context)|返回Context类型实例。|

**示例：**

<!-- compile -->
```cangjie
import ohos.ark_interop.*
import kit.AbilityKit.*

class MyAbilityStage3 <: AbilityStage {
    public override func onCreate(): Unit {
        let jsContext = jsRuntime.getOrThrow().mainContext
        let input = this.context.toJSValue(jsContext)
        let ctx = createContextFromJSValue(jsContext, input)
    }
}
```

## func createUIAbilityContextFromJSValue(JSContext, JSValue)

```cangjie
public func createUIAbilityContextFromJSValue(context: JSContext, input: JSValue): UIAbilityContext
```

**功能：** 从[JSValue](../arkinterop/cj-apis-ark_interop.md#class-jsvalue)转换为[UIAbilityContext](#class-uiabilitycontext)类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是|-|ArkTS互操作上下文。|
|input|[JSValue](../arkinterop/cj-apis-ark_interop.md#class-jsvalue)|是|-|ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[UIAbilityContext](#class-uiabilitycontext)|返回UIAbilityContext类型实例。|

**示例：**

<!-- compile -->
```cangjie
import ohos.ark_interop.*
import kit.AbilityKit.*

class MyUIAbility1 <: UIAbility {
    public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
        let jsContext = jsRuntime.getOrThrow().mainContext
        let input = this.context.toJSValue(jsContext)
        let ctx = createContextFromJSValue(jsContext, input)
    }
}
```

## interface SystemObjectInteropTypeToJS

```cangjie
public interface SystemObjectInteropTypeToJS {
    func toJSValue(context: JSContext): JSValue
}
```

**功能：** 系统对象专用的拓展接口，以实现与[JSValue](../arkinterop/cj-apis-ark_interop.md#class-jsvalue)的互转。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

### func toJSValue(JSContext)

```cangjie
func toJSValue(context: JSContext): JSValue
```

**功能：** 将仓颉对象转换成[JSValue](../arkinterop/cj-apis-ark_interop.md#class-jsvalue)。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是|-|ArkTS互操作上下文。|

**返回值：**

|类型|说明|
|:----|:----|
|[JSValue](../arkinterop/cj-apis-ark_interop.md#class-jsvalue)|ArkTS统一类型。|

**示例：**

<!-- compile -->
```cangjie
import ohos.ark_interop.*
import kit.AbilityKit.*

class MyAbilityStage4 <: AbilityStage {
    public override func onCreate(): Unit {
        let jsContext = jsRuntime.getOrThrow().mainContext
        let input = this.context.toJSValue(jsContext)
        let ctx = createContextFromJSValue(jsContext, input)
    }
}
```