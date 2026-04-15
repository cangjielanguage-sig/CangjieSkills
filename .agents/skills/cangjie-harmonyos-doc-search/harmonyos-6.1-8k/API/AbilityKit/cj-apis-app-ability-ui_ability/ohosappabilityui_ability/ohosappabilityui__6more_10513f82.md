# ohos.app.ability.ui_ability

<!--Del-->
> **说明：**
>
> 当前为Beta阶段。
<!--DelEnd-->

ui_ability模块提供UIAbility应用组件的核心API，包括UIAbility生命周期管理、上下文（Context）体系、Ability启动与销毁、以及与ArkTS的互操作能力。通过本模块，开发者可以创建和管理包含UI界面的应用组件，实现组件的创建、销毁、前后台切换等生命周期回调，并通过Context实现获取应用资源、启动其他Ability等能力。

## 导入模块

```cangjie
import kit.AbilityKit.*
```

## 权限列表

ohos.permission.DISTRIBUTED_DATASYNC

ohos.permission.PREPARE_APP_TERMINATE

ohos.permission.PRIVACY_WINDOW

## 使用说明

API示例代码使用说明：

- 若示例代码首行有“// index.cj”注释，表示该示例可在仓颉模板工程的“index.cj”文件中编译运行。
- 若示例需获取[Context](./cj-apis-app-ability-ui_ability.md#class-context)应用上下文，需在仓颉模板工程中的“main_ability.cj”文件中进行配置。

上述示例工程及配置模板详见[仓颉示例代码说明](../cj-development-intro.md#仓颉示例代码说明)。

## func createAbilityStageContextFromJSValue(JSContext, JSValue)

```cangjie
public func createAbilityStageContextFromJSValue(context: JSContext, input: JSValue): AbilityStageContext
```

**功能：** 从JSValue转换为AbilityStageContext类型。该转换仅可在函数传递中使用。

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
|[AbilityStageContext](#class-abilitystagecontext)|返回AbilityStageContext类型实例。|

**示例：**

<!-- compile -->
```cangjie
import ohos.ark_interop.*
import kit.AbilityKit.*

class MyAbilityStage1 <: AbilityStage {
    public override func onCreate(): Unit {
        let jsContext = jsRuntime.getOrThrow().mainContext
        let input = this.context.toJSValue(jsContext)
        let ctx = createAbilityStageContextFromJSValue(jsContext, input)
    }
}
```

## func createApplicationContextFromJSValue(JSContext, JSValue)

```cangjie
public func createApplicationContextFromJSValue(context: JSContext, input: JSValue): ApplicationContext
```

**功能：** 从[JSValue](../arkinterop/cj-apis-ark_interop.md#class-jsvalue)转换为[ApplicationContext](#class-applicationcontext)类型。该转换仅可在函数传递中使用。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 22

**参数：**

|参数名|类型|必填|默认值|说明|
|:---|:---|:---|:---|:---|
|context|[JSContext](../arkinterop/cj-apis-ark_interop.md#class-jscontext)|是|-| ArkTS互操作上下文。|
|input|[JSValue](../arkinterop/cj-apis-ark_interop.md#class-jsvalue)|是|-|ArkTS统一类型。|

**返回值：**

|类型|说明|
|:----|:----|
|[ApplicationContext](#class-applicationcontext)|返回 ApplicationContext 类型实例。|

**示例：**

<!-- compile -->
```cangjie
import ohos.ark_interop.*
import kit.AbilityKit.*
import kit.TestKit.*

class MyAbilityStage2 <: AbilityStage {
    public override func onCreate(): Unit {
        let jsContext = jsRuntime.getOrThrow().mainContext
        let input = AbilityDelegatorRegistry.getAbilityDelegator().getAppContext().toJSValue(jsContext)
        let ctx = createApplicationContextFromJSValue(jsContext, input)
    }
}
```