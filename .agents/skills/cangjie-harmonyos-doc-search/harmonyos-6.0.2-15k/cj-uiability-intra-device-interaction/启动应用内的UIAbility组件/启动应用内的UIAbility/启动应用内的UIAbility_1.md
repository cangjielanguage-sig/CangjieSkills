## 启动应用内的UIAbility

当一个应用内包含多个[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)时，存在应用内启动Ability的场景。例如在支付应用中从入口Ability启动收付款Ability。

假设应用中有两个Ability：EntryAbility和FuncAbility（可以在同一个Module中，也可以在不同的Module中），需要从EntryAbility的页面中启动FuncAbility。

1. 在EntryAbility中，通过调用[startAbility()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-startabilitywant)方法启动Ability，[Want](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)为Ability实例启动的入口参数，其中bundleName为待启动应用的Bundle名称，abilityName为待启动的Ability名称，moduleName在待启动的Ability属于不同的Module时添加，parameters为自定义信息参数。示例中的context的获取方式请参见[获取UIAbility的上下文信息](cj-uiability-usage.md#获取uiability的上下文信息)。

    ```cangjie
    import kit.UIKit.Button
    import ohos.base.{BusinessException, AppLog}
    import kit.AbilityKit.{Want, UIAbilityContext}
    import std.collection.HashMap
    import encoding.json.{JsonValue, JsonObject, JsonString}

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
                    Button().onClick {
                        evt =>
                        // context为调用方Ability的AbilityContext
                        let context = getContext()
                        let parametersMap = HashMap<String, JsonValue>()
                        parametersMap.add("info", JsonString("来自EntryAbility PageAbilityComponentsInteractive页面"))
                        let want = Want(
                            deviceId: "", // deviceId为空表示本设备
                            bundleName: "com.samples.stagemodelabilitydevelop",
                            abilityName: "FuncAbilityA",
                            moduleName: "entry", // moduleName非必选
                            // 自定义信息
                            parameters: JsonObject(parametersMap).toString()
                        )
                        try {
                            context.startAbility(want).get()
                        } catch (e: BusinessException) {
                            AppLog.error("Failed to start FuncAbility. Code is ${e.code}, message is ${e.message}")
                        }
                    }
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

2. 在FuncAbility的[onCreate()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-oncreatewant-launchparam)或者[onNewWant()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onnewwantwant-launchparam)生命周期回调文件中接收EntryAbility传递过来的参数。

    ```cangjie
    import ohos.base.AppLog
    import kit.AbilityKit.{UIAbility, UIAbilityContext, LaunchParam, Want}

    var globalFuncAbilityAContext: ?UIAbilityContext = None

    class FuncAbilityA <: UIAbility {
        public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
            globalFuncAbilityAContext = this.context
            // 接收调用方Ability传过来的参数
            let funcAbilityWant = want
            // want.parameters是一个json格式的字符串，用户可通过三方json库解析出info字段的值
        }
        // ...
    }
    ```

    > **说明：**
    >
    > 在被拉起的FuncAbility中，可以通过获取传递过来的[Want](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-want)参数的`parameters`来获取拉起方[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)的PID、Bundle Name等信息。