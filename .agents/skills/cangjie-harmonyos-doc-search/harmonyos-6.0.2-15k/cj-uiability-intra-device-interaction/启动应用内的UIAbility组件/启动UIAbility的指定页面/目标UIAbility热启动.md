### 目标UIAbility热启动

在应用开发中，会遇到目标[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)实例之前已经启动过的场景，这时再次启动目标Ability时，不会重新走初始化逻辑，只会直接触发[onNewWant()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onnewwantwant-launchparam)生命周期方法。为了实现跳转到指定页面，需要在onNewWant()中解析参数进行处理。

例如短信应用和联系人应用配合使用的场景。

1. 用户先打开短信应用，短信应用的UIAbility实例启动，显示短信应用的主页。
2. 用户将设备回到桌面界面，短信应用进入后台运行状态。
3. 用户打开联系人应用，找到联系人张三。
4. 用户点击联系人张三的短信按钮，会重新启动短信应用的UIAbility实例。
5. 由于短信应用的UIAbility实例已经启动过了，此时会触发该UIAbility的onNewWant()回调，而不会再执行[onCreate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-oncreatewant-launchparam)和[onWindowStageCreate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onwindowstagecreatewindowstage)等初始化逻辑。

**图1** 目标UIAbility热启动

![目标UIAbility热启动](figures/uiability-hot-start.png)

开发步骤如下所示。

1. 冷启动短信应用的UIAbility实例。

    ```cangjie
    import std.collection.HashMap
    import ohos.base.{AppLog, BusinessException}
    import kit.AbilityKit.{UIAbility, LaunchParam, Want}

    class FuncAbilityA <: UIAbility {
        var url = "Index"
        public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
            // 接收调用方Ability传过来的参数
            let funcAbilityWant = want
            let info = "XXX"
            // want.parameters是一个json格式的字符串，用户可通过三方json库解析出router字段的值，赋给info
            if (info == "FuncA") {
                url = "PageColdStartUp"
            }
        }

        public override func onWindowStageCreate(windowStage: WindowStage): Unit {
            AppLog.info("FuncAbilityA onWindowStageCreate.")
            globalFuncAbilityAContext = this.context
            windowStage.loadContent(url)
        }
    }
    ```

2. 在短信应用UIAbility的[onNewWant()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onnewwantwant-launchparam)回调中解析调用方传递过来的[Want](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)参数，通过[Router](../../API_Reference/source_zh_cn/arkui-cj/cj-apis-router.md#class-router)对象，并进行指定页面的跳转。此时再次启动该短信应用的UIAbility实例时，即可跳转到该短信应用的UIAbility实例的指定页面。

    ```cangjie
    import std.collection.HashMap
    import ohos.base.{AppLog, BusinessException}
    import kit.AbilityKit.{UIAbility, LaunchParam, Want}
    import kit.UIKit.{launch, Router}

    class FuncAbilityA <: UIAbility {
        //...
        public override func onNewWant(want: Want, launchParam: LaunchParam): Unit {
            // 接收调用方Ability传过来的参数
            let funcAbilityWant = want
            let info = "XXX"
            // want.parameters是一个json格式的字符串，用户可通过三方json库解析出router字段的值，赋给info
            if (info == "FuncA") {
                url = "PageHotStartUp"
            }
            launch {
                Router.pushUrl(url: "PageHotStartUp",
                    callback: {code => AppLog.error("Failed to push url. Code is ${code}")})
            }
        }
    }
    ```

> **说明：**
>
> 当被调用方[UIAbility组件启动模式](cj-uiability-launch-type.md)设置为multiton启动模式时，每次启动都会创建一个新的实例，那么onNewWant()回调就不会被用到。