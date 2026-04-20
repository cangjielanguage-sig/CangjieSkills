### 概述

一个[UIAbility](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)可以对应多个页面，在不同的场景下启动该UIAbility时需要展示不同的页面，例如从一个UIAbility的页面中跳转到另外一个UIAbility时，希望启动目标UIAbility的指定页面。

UIAbility的启动分为两种情况：UIAbility冷启动和UIAbility热启动。

- UIAbility冷启动：指的是UIAbility实例处于完全关闭状态下被启动，这需要完整地加载和初始化UIAbility实例的代码、资源等。
- UIAbility热启动：指的是UIAbility实例已经启动并在前台运行过，由于某些原因切换到后台，再次启动该UIAbility实例，这种情况下可以快速恢复UIAbility实例的状态。

本章主要讲解[目标UIAbility冷启动](#目标uiability冷启动)和[目标UIAbility热启动](#目标uiability热启动)两种启动指定页面的场景，以及调用方如何指定启动页面。

### 调用方UIAbility指定启动页面

调用方[UIAbility](../reference/AbilityKit/cj-apis-app-ability-ui_ability.md#class-uiability)启动另外一个UIAbility时，通常需要跳转到指定的页面。例如FuncAbility包含两个页面（Index对应首页，FuncA对应功能A页面），此时需要在传入的[Want](../reference/AbilityKit/cj-apis-app-ability-want.md#class-want)参数中配置指定的页面信息，可以通过want中的parameters参数增加一个自定义参数传递页面跳转信息。示例中的context的获取方式请参见[获取UIAbility的上下文信息](cj-uiability-usage.md#获取uiability的上下文信息)。

<!-- compile -->

```cangjie
import kit.ArkUI.Button
import ohos.business_exception.*
import kit.AbilityKit.{Want, UIAbilityContext, AbilityResult, WantValueType}
import std.collection.HashMap
import kit.PerformanceAnalysisKit.Hilog

// 见获取UIAbility的上下文信息章节
func getContext(): UIAbilityContext {
    return globalContext.getOrThrow()
}

@Entry
@Component
class PageAbilityComponentsInteractive {
    func build() {
        Row {
            Column {
                Button().onClick ({
                    evt =>
                    // context为调用方Ability的AbilityContext
                    let context = getContext()
                    let parametersMap = HashMap<String, WantValueType>()
                    parametersMap.add("router", StringValue("FuncA"))
                    let want = Want(
                        deviceId: "", // deviceId为空表示本设备
                        bundleName: "com.samples.stagemodelabilitydevelop",
                        abilityName: "FuncAbilityA",
                        moduleName: "entry", // moduleName非必选
                        // 自定义信息
                        parameters: parametersMap
                    )
                    try {
                        context.startAbility(want)
                    } catch (e: BusinessException) {
                        Hilog.info(0, "device_interaction", "Failed to start FuncAbility. Code is ${e.code}, message is ${e.message}")
                    }
                })
            }.width(100.percent)
        }.height(100.percent)
    }
}
```