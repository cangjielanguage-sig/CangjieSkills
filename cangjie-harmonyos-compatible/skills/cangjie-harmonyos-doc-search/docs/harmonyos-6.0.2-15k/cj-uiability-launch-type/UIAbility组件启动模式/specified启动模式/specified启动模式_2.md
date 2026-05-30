@Entry
    @Component
    class EntryView {
        @State
        var keyNew = "KEY"
        func build() {
            Row {
                Column {
                    Button().onClick {
                        evt =>
                        // context为调用方Ability的AbilityContext;
                        let context = getContext()
                        let want = Want(
                            deviceId: "", // deviceId为空表示本设备
                            bundleName: "com.samples.stagemodelabilitydevelop",
                            abilityName: "SpecifiedFirstAbility",
                            moduleName: "entry", // moduleName非必选
                            // 自定义信息
                            parameters: "{\"instanceKey\":\"${keyNew}\"}"
                        )
                        try {
                            context.startAbility(want).get()
                        } catch (e: BusinessException) {
                            AppLog.error("Failed to start SpecifiedAbility. Code is ${e.code}, message is ${e.message}")
                        }
                        keyNew = keyNew + "a"
                    }
                    Button().onClick {
                        evt =>
                        // context为调用方Ability的AbilityContext;
                        let context = getContext()
                        let want = Want(
                            deviceId: "", // deviceId为空表示本设备
                            bundleName: "com.samples.stagemodelabilitydevelop",
                            abilityName: "SpecifiedSecondAbility",
                            moduleName: "entry", // moduleName非必选
                            // 自定义信息
                            parameters: "{\"instanceKey\":\"${getInstance()}\"}"
                        )
                        try {
                            context.startAbility(want).get()
                        } catch (e: BusinessException) {
                            AppLog.error("Failed to start SpecifiedAbility. Code is ${e.code}, message is ${e.message}")
                        }
                    }
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

3. 开发者根据业务在SpecifiedAbility的[onAcceptWant()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onacceptwantwant)生命周期回调设置该UIAbility的标识。示例中标识设置为`SpecifiedAbilityInstance_KEY`。

    ```cangjie
    import kit.AbilityKit.{AbilityStage, Want}

    class MyAbilityStage <: AbilityStage {
        public override func onCreate(): Unit {
            AppLog.info("MyAbilityStage onCreated.")
        }

        public override func onAcceptWant(want: Want): String {
            // 在被调用方的AbilityStage中，针对启动模式为specified的Ability返回一个Ability实例对应的一个Key值
            // 当前示例指的是module1 Module的SpecifiedAbility
            if (want.abilityName == 'SpecifiedFirstAbility' || want.abilityName == 'SpecifiedSecondAbility') {
                // 返回的字符串KEY标识为自定义拼接的字符串内容
                if (want.parameters != "") {
                    // parameters是一个json格式的字符串，用户可通过三方json库解析出instanceKey字段的值
                    let instanceKey = "XXX"
                    return "SpecifiedAbilityInstance_${instanceKey}"
                }
            }
            // ...
            return "MyAbilityStage"
        }
    }
    ```

    > **说明：**
    >
    > - 当应用的UIAbility实例已经被创建，并且配置为指定实例模式时，如果再次调用[startAbility()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-startabilitywant)方法启动该UIAbility实例，且[AbilityStage](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-abilitystage)的[onAcceptWant()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onacceptwantwant)回调匹配到一个已创建的UIAbility实例，则系统会启动原来的UIAbility实例，并且不会重新创建一个新的UIAbility实例。此时，该UIAbility实例的onNewWant()回调会被触发，而不会触发onCreate()和onWindowStageCreate()生命周期回调。
    > - AbilityStage文件的创建请参见[AbilityStage组件容器](cj-abilitystage.md)。