3. 在FuncAbility业务完成之后，如需要停止当前[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)实例，在FuncAbility中通过调用[terminateSelf()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-terminateself)方法实现。示例中的context的获取方式请参见[获取UIAbility的上下文信息](cj-uiability-usage.md#获取uiability的上下文信息)。

    ```cangjie
    import ohos.base.{BusinessException, AppLog}
    import kit.AbilityKit.UIAbilityContext

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
                    Button("FuncAbility").onClick {
                        evt =>
                        let context = getFuncAbilityAContext()
                        try {
                            context.terminateSelf().get()
                        } catch (e: BusinessException) {
                            AppLog.error("Failed to start terminate self. Code is ${e.code}, message is ${e.message}")
                        }
                    }
                // ...
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

    > **说明：**
    >
    > 调用terminateSelf()方法停止当前Ability实例时，默认会保留该实例的快照（Snapshot），即在最近任务列表中仍然能查看到该实例对应的任务。如不需要保留该实例的快照，可以在其对应Ability的[module.json5配置文件](../cj-start/basic-knowledge/module-configuration-file.md)中，将[abilities标签](../cj-start/basic-knowledge/module-configuration-file.md#abilities标签)的removeMissionAfterTerminate字段配置为true。

4. 如需要关闭应用所有的[UIAbility](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-uiability)实例，可以调用[ApplicationContext](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-applicationcontext)的[killAllProcesses()](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-killallprocessesbool)方法实现关闭应用所有的进程。