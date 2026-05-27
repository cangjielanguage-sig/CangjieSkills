## 使用ApplicationContext订阅回调

[ApplicationContext](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-applicationcontext)提供了注册回调函数以订阅系统环境变量的变化，并且可以通过调用相应的方法来撤销该回调。这有助于在资源不再需要时释放相关资源，从而提高系统的可靠性和性能。

1. 使用[on](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-onapplicationcontexttype-environmentcallback)方法，应用程序可以通过在非应用组件模块中订阅系统环境变量的变化来动态响应这些变化。例如，使用该方法在页面中监测系统语言的变化。示例中的context的获取方式请参见[获取UIAbility的上下文信息](cj-uiability-usage.md#获取uiability的上下文信息)。

    ```cangjie
    import kit.UIKit.{AppLog, BusinessException}
    import kit.AbilityKit.{UIAbilityContext, ApplicationContext, EnvironmentCallback, ApplicationContextType}

    var callbackId: Int32 = 0 // 注册订阅系统环境变化的ID

    // 见获取UIAbility的上下文信息章节
    func getContext(): UIAbilityContext {
        return globalContext.getOrThrow()
    }

    func subscribeConfigurationUpdate(): Unit {
        let context = getContext()
        let systemLanguage = Box<String>(context.config.language) // 获取系统当前语言

        // 1.获取ApplicationContext
        let applicationContext = context.getApplicationContext()

        // 2.通过applicationContext订阅环境变量变化
        let environmentCallback = EnvironmentCallback(
            onConfigurationUpdated: {
                newConfig =>
                AppLog.info("onConfigurationUpdated systemLanguage is ${systemLanguage}")
                if (systemLanguage.value != newConfig.language) {
                    AppLog.info("systemLanguage from ${systemLanguage} changed to ${newConfig.language}")
                    systemLanguage.value = newConfig.language // 将变化之后的系统语言保存，作为下一次变化前的系统语言
                }
            },
            onMemoryLevel: {
                level => AppLog.info("onMemoryLevel level: ${level}")
            }
        )
        try {
            callbackId = applicationContext.on(ApplicationContextType.ENVIRONMENT, environmentCallback)
        } catch (e: BusinessException) {
            AppLog.error("Failed to register applicationContext. Code is ${e.code}, message is ${e.message}");
        }
    }

    @Entry
    @Component
    class EntryView {
        @State
        var message: String = "Hello World"

        func build() {
            Row {
                Column {
                    Text("subscribe configuration update").fontSize(50).fontWeight(FontWeight.Bold).onClick {
                        evt => subscribeConfigurationUpdate()
                    }
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

2. 在资源使用完成之后，可以通过调用[off](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-offapplicationcontexttype-applicationstatechangecallback)方法释放相关资源。

    ```cangjie
    import kit.UIKit.{AppLog, BusinessException}
    import kit.AbilityKit.{UIAbilityContext, ApplicationContext, EnvironmentCallback, ApplicationContextType}

    var callbackId: Int32 = 0 // 注册订阅系统环境变化的ID

    // 见获取UIAbility的上下文信息章节
    func getContext(): UIAbilityContext {
        return globalContext.getOrThrow()
    }

    func unsubscribeConfigurationUpdate(): Unit {
        let context = getContext()
        // 1.获取ApplicationContext
        let applicationContext = context.getApplicationContext()
        try {
            applicationContext.off(ApplicationContextType.ENVIRONMENT, callbackId);
        } catch (e: BusinessException) {
            AppLog.error("Failed to unregister applicationContext. Code is ${e.code}, message is ${e.message}");
        }
    }

    @Entry
    @Component
    class EntryView {
        @State
        var message: String = "Hello World"

        func build() {
            Row {
                Column {
                    Text("unsubscribe configuration update").fontSize(50).fontWeight(FontWeight.Bold).onClick {
                        evt => unsubscribeConfigurationUpdate()
                    }
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```