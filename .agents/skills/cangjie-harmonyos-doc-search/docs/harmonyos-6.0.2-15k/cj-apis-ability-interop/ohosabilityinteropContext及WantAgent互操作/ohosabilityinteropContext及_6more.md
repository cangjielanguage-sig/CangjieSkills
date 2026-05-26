# ohos.ability.interop（Context及WantAgent互操作）

本模块提供[Context](./cj-apis-ability.md#class-context)及其相关子类和[WantAgent](./cj-apis-ability.md#class-wantagent)进行互操作的能力。

## 导入模块

```cangjie
import kit.AbilityKit.*
```

## func createAbilityContextFromJSValue(JSContext, JSValue)

```cangjie
public func createAbilityContextFromJSValue(context: JSContext, input: JSValue): UIAbilityContext
```

**功能：** 从JSValue转换为AbilityContext类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是| ArkTS互操作上下文。|
|input|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)|是| ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[UIAbilityContext](./cj-apis-ability.md#class-uiabilitycontext)| 返回AbilityContext类型实例。|

## func createAbilityStageContextFromJSValue(JSContext, JSValue)

```cangjie
public func createAbilityStageContextFromJSValue(context: JSContext, input: JSValue): AbilityStageContext
```

**功能：** 从[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为[AbilityStageContext](./cj-apis-ability.md#class-abilitystagecontext)类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是| ArkTS互操作上下文。|
|input|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)|是| ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[AbilityStageContext](./cj-apis-ability.md#class-abilitystagecontext)| 返回AbilityStageContext类型实例。 |

## func createApplicationContextFromJSValue(JSContext, JSValue)

```cangjie
public func createApplicationContextFromJSValue(context: JSContext, input: JSValue): ApplicationContext
```

**功能：** 从[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为[ApplicationContext](./cj-apis-ability.md#class-applicationcontext)类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是| ArkTS互操作上下文。|
|input|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)|是| ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[ApplicationContext](./cj-apis-ability.md#class-applicationcontext)| 返回 ApplicationContext 类型实例。 |

## func createContextFromJSValue(JSContext, JSValue)

```cangjie
public func createContextFromJSValue(context: JSContext, input: JSValue): Context
```

**功能：** 从[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)转换为[Context](./cj-apis-ability.md#class-context)类型。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 19

**参数：**

|参数名|类型|必填|说明|
|:---|:---|:---|:---|
|context|[JSContext](../../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是| ArkTS互操作上下文。|
|input|[JSValue](../../arkinterop/cj-apis-ark_interop.md#struct-jsvalue)|是| ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[Context](./cj-apis-ability.md#class-context)| 返回Context类型实例。|