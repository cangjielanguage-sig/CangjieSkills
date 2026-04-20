# 拉起快递类应用（startAbilityByType）

本章介绍如何拉起快递类应用扩展面板。

例如，在消息类App中，用户收到快递单号，应用能够识别快递单号信息并提供快递查询的链接。用户点击链接后，应用将通过调用[UIAbilityContext.startAbilityByType](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-startabilitybytypestring-string-abilitystartcallback)或[UIExtensionContentSession.startAbilityByType](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-startabilitybytypestring-string-abilitystartcallback-1)接口，拉起快递类应用的扩展面板。面板上将展示设备上所有支持快递查询的应用，供用户选择并跳转至所需应用。

## 快递类应用扩展面板参数说明

startAbilityByType接口中type字段为express，支持查询快递意图，对应的wantParam参数如下：

| 参数名    | 类型   | 必填 | 说明                                   |
| --------- | ------ | ---- | -------------------------------------- |
| sceneType | Int64 | 否   | 意图场景，表明本次请求对应的操作意图。默认为1，查询快递填场景填1或不填。 |
| expressNo | String | 是   | 快递单号。                               |

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
                            let jsonString = ##"{"sceneType":1,"expressNo":"SF123456"}"##
                            try {
                                context.startAbilityByType("express", jsonString, callBack)
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

    ![效果示例图](./figures/start-express-panel.png)