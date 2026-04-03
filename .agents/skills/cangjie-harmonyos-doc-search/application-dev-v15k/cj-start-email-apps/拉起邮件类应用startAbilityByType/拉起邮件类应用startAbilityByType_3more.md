# 拉起邮件类应用（startAbilityByType）

本章介绍如何拉起邮件类应用扩展面板。

## 邮件类应用扩展面板参数说明

startAbilityByType接口中type字段为mail，对应的wantParam参数：

| 参数名 | 类型 | 必填 | 说明 |
| ---- | ---- | ---- | ---- |
| email | Array\<String> | 否 | 收件人邮箱地址（支持多个且以逗号分隔）。 |
| cc | Array\<String> | 否 | 抄收人邮箱地址（支持多个且以逗号分隔）。 |
| bcc | Array\<String> | 否 | 密送人邮箱地址（支持多个且以逗号分隔）。 |
| subject | String | 否 | 邮件主题。 |
| body | String | 否 | 邮件内容。 |
| ability.params.stream | Array\<String> | 否 | 邮件附件（附件的uri地址列表）。 |
| ability.want.params.uriPermissionFlag | Int64 | 否 | 给邮件附件赋予至少读权限。[Flags](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#enum-flags)。邮件附件参数存在时，该参数也必须要传 |
| sceneType | Int64 | 否 | 意图场景，表明本次请求对应的操作意图。1：发邮件。默认为1。 |

> **说明：**
>
> * 邮件类应用扩展面板中的类型为String的参数，都要经过url编码。
> * 邮件类应用扩展面板中的类型为Array\<String>的参数，数组中的元素都要经过url编码。

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
                            // email，收件人邮箱地址，多值以逗号分隔，对数组内容进行url编码
                            // cc，抄收人邮箱地址，多值以逗号分隔，对数组内容进行url编码
                            // bcc，密送人邮箱地址，多值以逗号分隔，对数组内容进行url编码
                            // subject，邮件主题，对内容进行url编码
                            // body，邮件正文，对内容进行url编码
                            // 附件uri，多值以逗号分隔，对数组内容进行url编码
                            let jsonString = ##"{"sceneType":1,"email":["xxx@example.com","xxx@example.com"],"cc":["xxx@example.com","xxx@example.com"],"bcc":["xxx@example.com","xxx@example.com"],"subject":"邮件主题","body":"邮件正文","ability.params.stream":["附件uri1","附件uri2"],"ability.want.params.uriPermissionFlag":1}"##

                            try {
                                context.startAbilityByType("mail", jsonString, callBack)
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

    ![效果示例图](./figures/start-mail-panel.png)