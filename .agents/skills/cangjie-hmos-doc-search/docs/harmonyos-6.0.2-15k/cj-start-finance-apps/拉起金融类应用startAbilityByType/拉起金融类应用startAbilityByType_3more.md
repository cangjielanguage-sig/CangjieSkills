# 拉起金融类应用（startAbilityByType）

本章介绍如何拉起金融类应用扩展面板。

## 金融类应用扩展面板参数说明

startAbilityByType接口中type字段为finance，对应的wantParam参数：

| 参数名 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| sceneType | Int64 | 否 | 意图场景，表明本次请求对应的操作意图。1：转账汇款 2：信用卡还款。默认为1。 |
| bankCardNo | String | 否  | 银行卡卡号。 |

## 拉起方开发步骤

1. 导入相关模块。

    ```cangjie
    import kit.AbilityKit.*
    ```

2. 构造接口参数并调用startAbilityByType接口。示例中的context的获取方式请参见[获取UIAbility的上下文信息](cj-uiability-usage.md#获取uiability的上下文信息)。

    ```cangjie
    import std.collection.HashMap
    import kit.AbilityKit.{UIAbilityContext, Want, AbilityStartCallback, Flags}
    import kit.UIKit.{AsyncError, AppLog, Button, BusinessException}

    // 见获取UIAbility的上下文信息章节
    func getContext(): UIAbilityContext {
        return globalContext.getOrThrow()
    }

    let callBack = AbilityStartCallback(
        {
            code, name, message => AppLog.info("onError code ${code} name: ${name} message: ${message}")
        },
        onResult: {
            result => AppLog.info("onResult resultCode: ${result.resultCode}")
        }
    )

    @Entry
    @Component
    class EntryView {
        func build() {
            Row {
                Column {
                    Button("start type").onClick(
                        {
                            evt =>
                            let context = getContext()
                            let jsonString = ##"{"sceneType":1,"bankCardNo":"123456789"}"##
                            try {
                                context.startAbilityByType("finance", jsonString, callBack)
                            } catch (e: BusinessException) {
                                AppLog.error("startAbilityByType fail, err: ${e.message}")
                            }
                        }
                    )
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```

    效果示例图：

    ![效果示例图](./figures/start-finance-panel.png)