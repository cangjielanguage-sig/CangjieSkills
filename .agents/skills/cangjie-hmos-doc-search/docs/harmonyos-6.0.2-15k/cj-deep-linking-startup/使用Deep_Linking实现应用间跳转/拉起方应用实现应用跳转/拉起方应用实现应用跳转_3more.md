## 拉起方应用实现应用跳转

下面通过三个案例，分别介绍如何使用[openLink()](../../../cj-apis-ability/.overview.md)与[startAbility()](../../../cj-apis-ability/.overview.md)接口实现应用跳转，以及如何在[Web组件](../../../cj-web-web/.overview.md)中实现应用跳转。

### 使用openLink实现应用跳转

在[openLink](../../../cj-apis-ability/.overview.md)接口的link字段中传入目标应用的URL信息，并将options字段中的`appLinkingOnly`配置为`false`。示例中的context的获取方式请参见[获取UIAbility的上下文信息](cj-uiability-usage.md#获取uiability的上下文信息)。

示例代码如下：

```cangjie
import kit.AbilityKit.{UIAbilityContext, OpenLinkOptions}
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
                        let context = getContext()
                        let link = "link://www.example.com"
                        let openLinkOptions = OpenLinkOptions(appLinkingOnly: false)
                        try {
                            context.openLink(link, options: openLinkOptions)
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

### 使用startAbility实现应用跳转

[startAbility](../../../cj-apis-ability/.overview.md)接口是将应用链接放入want中，通过调用[隐式want匹配](cj-explicit-implicit-want-mappings.md#隐式want匹配原理)的方法触发应用跳转。通过[startAbility](../../../cj-apis-ability/.overview.md)接口启动时，还需要调用方传入待匹配的action和entity。示例中的context的获取方式请参见[获取UIAbility的上下文信息](cj-uiability-usage.md#获取uiability的上下文信息)。

示例代码如下：

```cangjie
import kit.AbilityKit.{UIAbilityContext, Want}
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
                        let context = getContext()
                        let want = Want(uri: "link://www.example.com")
                        try {
                            context.startAbility(want)
                            AppLog.info("start ability success.")
                        } catch (e: BusinessException) {
                            AppLog.error("Failed to start ability. Code is ${e.code}, message is ${e.message}")
                        }
                    }
                )
            }.width(100.percent)
        }.height(100.percent)
    }
}
```