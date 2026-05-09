```cangjie
    import ohos.business_exception.*
    import kit.AbilityKit.UIAbilityContext
    import kit.PerformanceAnalysisKit.Hilog

    var globalFuncAbilityAContext: ?UIAbilityContext = None
    // 见获取UIAbility的上下文信息章节
    func getFuncAbilityAContext(): UIAbilityContext {
        return globalFuncAbilityAContext.getOrThrow()
    }

    @Entry
    @Component
    class PageFromStageModel {
        func build() {
            Row {
                Column {
                    Button("FuncAbility").onClick ({
                        evt =>
                        let context = getFuncAbilityAContext()
                        try {
                            context.terminateSelf()
                        } catch (e: BusinessException) {
                            Hilog.info(0, "device_interaction", "Failed to start terminate self. Code is ${e.code}, message is ${e.message}")
                        }
                    })
                    // ...
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

    > **说明：**
    >
    > 调用terminateSelf()方法停止当前Ability实例时，默认会保留该实例的快照（Snapshot），即在最近任务列表中仍然能查看到该实例对应的任务。如不需要保留该实例的快照，可以在其对应Ability的[module.json5配置文件](../cj-start/basic-knowledge/cj-module-configuration-file.md)中，将[abilities标签](../cj-start/basic-knowledge/cj-module-configuration-file.md#abilities标签)的removeMissionAfterTerminate字段配置为true。