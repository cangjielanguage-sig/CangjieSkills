# 显式Want跳转切换应用链接跳转适配指导

从API 18开始，已不再推荐三方应用使用指定Ability方式（即显式Want）拉起其他应用，推荐通过指定[应用链接](cj-app-startup-overview.md#应用链接)的方式来实现。

本章介绍如何从显式Want跳转切换到应用链接跳转。

## 启动其他应用的UIAbility

1. 将待跳转的应用安装到设备，在其对应UIAbility的[module.json5配置文件](../cj-start/basic-knowledge/module-configuration-file.md)中配置skills标签的entities字段、actions字段和uri字段：
    - "actions"列表中包含"ohos.want.action.viewData"。
    - "entities"列表中包含"entity.system.browsable"。
    - "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。uri的匹配规则请参见[uri匹配](cj-explicit-implicit-want-mappings.md#uri匹配规则), domainVerify为true代表开启域名检查，通过applinking匹配该应用时需经过配置的域名校验后才能匹配到。applinking域名配置请参见[AppLinking](cj-app-linking-startup.md)。

    ```json
    {
      "module": {
        // ...
        "abilities": [
          {
            // ...
            "skills": [
              {
                "entities": [
                  "entity.system.browsable"
                ],
                "actions": [
                  "ohos.want.action.viewData"
                ],
                "uris": [
                  {
                    "scheme": "https",
                    "host": "www.example.com",
                  }
                ],
              "domainVerify": true
              }
            ]
          }
        ]
      }
    }
    ```

2. 调用方通过[openLink](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#func-openlinkstring-openlinkoptions-asynccallbackabilityresult)接口执行跳转，在接口入参需要传入转换后的link和配置[options](../../API_Reference/source_zh_cn/apis/AbilityKit/cj-apis-ability.md#class-openlinkoptions), 不再传入bundleName、moduleName和abilityName。系统会根据传入的link匹配到符合skill配置的应用。
    - 当options中的appLinkingOnly为true时，匹配到的应用会经过应用市场域名检查（需联网）返回域名校验检查的唯一匹配项或未匹配结果。
    - 当options中的appLinkingOnly为false时，会优先尝试以AppLinking的方式拉起，如果没有匹配的应用则改为使用DeepLinking的方式拉起目标应用。

    ```cangjie
    import std.collection.HashMap
    import kit.AbilityKit.{UIAbilityContext, Want, OpenLinkOptions}
    import kit.UIKit.{AppLog, Button, BusinessException}

    // 见获取UIAbility的上下文信息章节
    func getContext(): UIAbilityContext {
        return globalContext.getOrThrow()
    }

    @Entry
    @Component
    class EntryView {
        @State
        var message: String = "Hello World"

        func build() {
            Row {
                Column {
                    Button("start link").onClick(
                        {
                            evt =>
                            let uri = "link://www.example.com"
                            // 仅以App Linking的方式打开应用
                            let context = getContext()
                            // 通过startAbility接口显式启动其他Ability，推荐使用openLink接口。
                            // let want = Want(
                            //   bundleName: "com.test.example",
                            //   moduleName: "entry",
                            //   abilityName: "EntryAbility"
                            // )
                            // try {
                            //   context.startAbility(want).get()
                            // } catch (e: BusinessException) {
                            //   AppLog.error("Failed to startAbility. Code is ${e.code}, message is ${e.message}")
                            // }
                            let openLinkOptions = OpenLinkOptions(
                                // 匹配的abilities选项是否需要通过AppLinking域名校验，匹配到唯一配置过的应用ability
                                appLinkingOnly: true,
                                // 同want中的parameter，用于传递的参数
                                parameters: "{\"demo_key\":\"demo_value\"}"
                            )
                            try {
                                context.openLink(uri, options: openLinkOptions)
                                AppLog.info("open link success.")
                            } catch (e: BusinessException) {
                                AppLog.error("Failed to start link. Code is ${e.code}, message is ${e.message}")
                            }
                        }
                    )
                }.width(100.percent)
            }.height(100.percent)
        }
    }
    ```