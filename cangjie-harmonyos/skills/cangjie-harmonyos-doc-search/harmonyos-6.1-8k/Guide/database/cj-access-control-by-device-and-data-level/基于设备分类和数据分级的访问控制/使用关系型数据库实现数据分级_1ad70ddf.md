## 使用关系型数据库实现数据分级

关系型数据库通过securityLevel参数设置数据库的安全等级。此处以创建安全等级为S1的数据库为例。

具体接口及功能，请参见[关系型数据库](../reference/ArkData/cj-apis-relational_store.md)。

1. 获取context。

    <!-- compile -->

    ```cangjie
    // main_ability.cj
    import kit.PerformanceAnalysisKit.Hilog
    import kit.AbilityKit.{UIAbility, Want, LaunchParam, LaunchReason, UIAbilityContext}

    var globalAbilityContext: Option<UIAbilityContext> = Option<UIAbilityContext>.None

    class MainAbility <: UIAbility {
        public init() {
            super()
            registerSelf()
        }

        public override func onCreate(want: Want, launchParam: LaunchParam): Unit {
            // 获取context
            globalAbilityContext = this.context

            match (launchParam.launchReason) {
                case LaunchReason.StartAbility => Hilog.info(0, "cangjie", "START_ABILITY")
                case _ => ()
            }
        } 
        // ...
    }
    ```

2. 创建安全等级为S1的关系型数据库。

    为实现创建数据库功能，需要导入如下包：

    <!-- compile -->

    ```cangjie
    // xxx.cj
    import kit.ArkData.*
    import kit.PerformanceAnalysisKit.Hilog
    import ohos.business_exception.BusinessException
    ```

    实现创建数据库功能的核心代码是：

    <!-- compile -->

    ```cangjie
    try {
        let context = globalAbilityContext.getOrThrow()
        let storeConfig = StoreConfig(
            RelationalStoreSecurityLevel.S1, // 设置安全等级为S1
            name: "RdbTest.db",
        )
        let rdbStore = getRdbStore(context, storeConfig)
        Hilog.info(0, "cangjie", "getRdbStore success")
    } catch (e: BusinessException) {
        Hilog.error(0, "ErrorCode: ${e.code}", e.message)
    }
    // 进行其它数据库相关的操作
    // ...
    ```